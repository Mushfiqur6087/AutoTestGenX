# Architecture — Test Generation

## Overview

Test Generation is a **multi-agent pipeline** built on [LangGraph](https://github.com/langchain-ai/langgraph) and [LiteLLM](https://github.com/BerriAI/litellm). It takes a markdown spec and produces structured JSON test cases.

---

## Package Structure

```
test_generation/
├── cli.py                          # argparse entry point; dispatches to pipelines
├── __main__.py                     # enables `python -m test_generation`
├── framework/
│   ├── agents/
│   │   ├── base.py                 # BaseAgent — LiteLLM wrapper, semaphore, debug logging
│   │   ├── utils.py                # Shared build_test_prompt() utility (Stage 3)
│   │   ├── structural_model_generator.py   # Stage 1 generator
│   │   ├── structural_model_validator.py   # Stage 1 critic
│   │   ├── workflow_extractor.py           # Stage 2 extractor
│   │   ├── workflow_validator.py           # Stage 2 critic
│   │   ├── positive_test_case_generator.py # Stage 3 positive
│   │   ├── negative_test_case_generator.py # Stage 3 negative
│   │   └── edge_test_case_generator.py     # Stage 3 edge/boundary
│   └── orchestrator/
│       ├── generator.py            # TestGenerationPipeline — drives the LangGraph
│       ├── graph.py                # LangGraph node wiring
│       ├── nodes.py                # Node implementations (async, per-module fan-out)
│       ├── state.py                # PipelineState TypedDict (LangGraph state schema)
│       ├── reporters.py            # Markdown report renderers
│       └── runs.py                 # Run-ID generation, sidecar metadata, checkpoint helpers
└── prompts/
    ├── structural_model_generator.md
    ├── structural_model_validator.md
    ├── workflow_extractor.md
    ├── workflow_validator.md
    ├── positive_test_case_generator.md
    ├── negative_test_case_generator.md
    ├── edge_test_case_generator.md
```

---

## Test Generation Pipeline

### LangGraph Node Graph

```
generate_and_critique ──► extract_workflows ──► generate_tests ──► finalize ──► END
```

Each node is an `async` function that reads `PipelineState` and returns a dict of state updates. All modules are processed **concurrently** within each node using `asyncio.gather`.

---

### Node: `generate_and_critique`

- **Purpose:** Stage 1 — produce a Structural Model JSON for every module.
- **Per-module loop (max 3 attempts):**
  1. `StructuralModelGeneratorAgent` reads the module description (+ structured `fixes[]` block from the previous validator, injected into the system prompt) and emits a JSON AST of all interactive UI components.
  2. `StructuralModelValidatorAgent` audits the AST against the description, returning `verdict` and severity-tagged `missing[]`/`phantoms[]` arrays.
  3. **Verdict handling:**
     - `yes` → done; AST ships.
     - `retry` → `fixes[]` injected into the generator's system prompt for the next attempt.
     - `needs_clarification` → loop stops immediately; clarifications are surfaced and the module is flagged. Retrying against a broken description wastes budget.
  4. After 3 attempts without `yes`, the orchestrator **escalates**: it prints a severity-broken report (critical missing, critical phantoms, structural errors) and records `forced_ship=True`. It does **not** silently ship the last AST as if it passed.
- **Attempt context:** Both generator and validator receive `attempt_number` and `max_attempts` via their rendered system prompts. On the final attempt the validator receives an additional `WARNING` injection.
- **Output state keys:** `structural_model_results`, `structural_model_critique_results`

---

### Node: `extract_workflows`

- **Purpose:** Stage 2 — enumerate every distinct executable path through each module.
- **Per-module loop (max 3 attempts):**
  1. `WorkflowExtractorAgent` reads the AST + description and emits a list of `Workflow` objects. The agent runs a 9-item self-check before outputting (coverage of all submit_actions, state × action pairs, sequential wf_id numbering, etc.).
  2. `WorkflowValidatorAgent` audits for missing paths, phantom workflows, wrong terminal actions, and generic `on_success` strings — returning severity-tagged `missing[]`/`phantoms[]`.
  3. Same verdict handling as Stage 1: `yes`, `retry`, `needs_clarification`, and escalate on exhaustion.
- **Attempt context:** Both agents receive `attempt_number` and `max_attempts` via rendered system prompts. Fixes are injected into the extractor's system prompt on retry (not the user prompt).
- **Output state keys:** `workflow_results`, `workflow_critique_results`

---

### Node: `generate_tests`

- **Purpose:** Stage 3 — generate comprehensive test cases for every module.
- **Per-module:** Three agents run in **parallel** (`asyncio.gather`):
  - `PositiveTestCaseGeneratorAgent` — must cover every `wf_id`; at least one TC per workflow.
  - `NegativeTestCaseGeneratorAgent` — one blocking failure per workflow with form interaction.
  - `EdgeTestCaseGeneratorAgent` — boundary conditions for workflows with numeric/date fields.
- All three receive the approved workflow list as a `<workflows>` context block, assembled by the shared `build_test_prompt()` utility in `agents/utils.py`.
- Results are merged and TC IDs are renumbered sequentially per module.
- **Output state key:** `test_results`

---

### Node: `finalize`

- Serialises all state into output JSON and markdown files.
- Writes: `structural-model.json`, `structural-model-critique.json`, `workflows.json`, `workflow-validator-critique.json`, `test-cases.json`, and `.md` reports.

---

## Prompt Template Rendering

All Stage 1 and Stage 2 generator/validator agents use **dynamic system prompt rendering** rather than static strings. At call time, each agent renders its `.md` prompt template by filling these slots:

| Slot | Who uses it | What it does |
|------|-------------|--------------|
| `{attempt_number}` | Generator + Validator (both stages) | Tells the LLM which attempt it is |
| `{max_attempts}` | Generator + Validator (both stages) | Tells the LLM the retry cap |
| `{fixes_block}` | Generator (both stages) | Injects the validator's `fixes[]` as a structured block; stripped on attempt 1 |
| `{final_attempt_warning}` | Validator (both stages) | Adds a final-attempt warning on the last try so the LLM returns `retry` (not `yes`) even if issues remain, enabling clean escalation |

The `[ORCHESTRATOR: ...]` comments embedded in the `.md` files are instructions to this rendering code — they are stripped from the rendered prompt the LLM sees.

Stage 3 agents use static system prompts (no template slots needed — they don't retry).

---

## Concurrency Model

All async LLM calls share a single `asyncio.Semaphore` (the `_LLM_SEMAPHORE` in `base.py`), sized by `--max-concurrency`. This prevents blast-radius from large specs with many modules hitting provider rate limits simultaneously.

The semaphore is acquired per `acall_llm` call (the innermost unit), not per module, so the limit applies across all in-flight calls from all modules and all stages at once.

---

## State Management

`PipelineState` is a `TypedDict` with LangGraph-compatible `Annotated` reducers:

| Key | Reducer | Description |
|-----|---------|-------------|
| `functional_desc` | `_last_value` | Parsed spec input (modules list + navigation text) |
| `structural_model_results` | `_last_value` | List of per-module AST results |
| `structural_model_critique_results` | `_last_value` | List of per-module validator verdicts (includes `forced_ship`, `needs_clarification`, `clarifications`) |
| `workflow_results` | `_last_value` | List of per-module workflow lists |
| `workflow_critique_results` | `_last_value` | List of per-module workflow validator verdicts (includes `forced_ship`, `needs_clarification`, `clarifications`) |
| `test_results` | `_last_value` | List of per-module merged test cases |
| `output` | `_last_value` | Final assembled output dict |

---

## Resumability

Every `--generate` run gets a unique `run_id` (`<slug>-YYYYMMDD-HHmmss-<6hex>`). The `run_id` doubles as the LangGraph `thread_id` for its checkpoint in `outputs/.checkpoints/test_generation.sqlite`. A sidecar `.json` file stores the original inputs (spec path, model, output dir). Passing `--resume <run_id>` re-invokes the graph from the last successfully committed node.

---

## Error Handling

- Per-module exceptions in `asyncio.gather` are caught with `return_exceptions=True`. A failed module records an `error` key in its result and the pipeline continues with remaining modules.
- JSON parse failures in `BaseAgent.acall_llm_json` retry up to `max_retries=2` times, stripping markdown fences and retrying without `response_format` if the provider rejects it.
- LiteLLM's `drop_params=True` silently drops unsupported parameters (e.g. `temperature` on `o`-series models).
- `needs_clarification` verdicts (both stages) halt the retry loop for that module immediately. The module is recorded with `needs_clarification=True` and `clarifications[]` so the pipeline can complete all other modules while surfacing the problematic spec text for human review.
