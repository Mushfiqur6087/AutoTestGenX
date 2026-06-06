# Architecture — Test Case Generation

## Overview

Test Case Generation is a **multi-agent pipeline** built on [LangGraph](https://github.com/langchain-ai/langgraph) and [LiteLLM](https://github.com/BerriAI/litellm). It runs two fully independent pipelines that can be invoked separately or chained:

1. **Test Generation Pipeline** — takes a markdown spec, produces structured JSON test cases.
2. **Post-Verification Pipeline** — takes existing test cases, produces `pre_check`/`post_check` schemas.

---

## Package Structure

```
test_case_generation/
├── cli.py                          # argparse entry point; dispatches to pipelines
├── __main__.py                     # enables `python -m test_case_generation`
├── framework/
│   ├── agents/
│   │   ├── base.py                 # BaseAgent — LiteLLM wrapper, semaphore, debug logging
│   │   ├── structural_model_generator.py   # Stage 1 generator
│   │   ├── structural_model_validator.py   # Stage 1 critic
│   │   ├── workflow_extractor.py           # Stage 2 extractor
│   │   ├── workflow_validator.py           # Stage 2 critic
│   │   ├── positive_test_case_generator.py # Stage 3 positive
│   │   ├── negative_test_case_generator.py # Stage 3 negative
│   │   ├── edge_test_case_generator.py     # Stage 3 edge/boundary
│   │   └── post_verifier.py               # StateChangeAgent + PostVerificationAgent
│   └── orchestrator/
│       ├── generator.py            # TestGenerationPipeline — drives the LangGraph
│       ├── post_verification_generator.py  # PostVerificationGenerator
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
    ├── state_change.md
    └── post_verification.md
```

---

## Pipeline 1 — Test Generation

### LangGraph Node Graph

```
generate_and_critique ──► extract_workflows ──► generate_tests ──► finalize ──► END
```

Each node is an `async` function that reads `PipelineState` and returns a dict of state updates. All modules are processed **concurrently** within each node using `asyncio.gather`.

### Node: `generate_and_critique`

- **Purpose:** Stage 1 — produce a Structural Model JSON for every module.
- **Per-module loop (max 3 attempts):**
  1. `StructuralModelGeneratorAgent` reads the module's functional description (+ any `fixes[]` from the previous critique) and emits a structured JSON AST of all interactive UI components.
  2. `StructuralModelValidatorAgent` audits the AST against the description, returning `verdict=yes/retry` and a `fixes[]` array.
  3. If `verdict=yes` → done. If `retry` → pass `fixes[]` back to the generator. After 3 attempts, ship as-is (`forced_ship=True`).
- **Output state keys:** `structural_model_results`, `structural_model_critique_results`

### Node: `extract_workflows`

- **Purpose:** Stage 2 — enumerate every distinct executable path through each module.
- **Per-module loop (max 3 attempts):**
  1. `WorkflowExtractorAgent` reads the AST + description and emits a list of `Workflow` objects (each with `wf_id`, `name`, `actor`, `conditional_branch`, `terminal_action`, `on_success`).
  2. `WorkflowValidatorAgent` audits for missing paths, phantom workflows, and wrong terminal actions.
  3. Same retry logic as Stage 1.
- **Output state keys:** `workflow_results`, `workflow_critique_results`

### Node: `generate_tests`

- **Purpose:** Stage 3 — generate comprehensive test cases for every module.
- **Per-module:** Three agents run in **parallel** (`asyncio.gather`):
  - `PositiveTestCaseGeneratorAgent` — must cover every `wf_id`; at least one TC per workflow.
  - `NegativeTestCaseGeneratorAgent` — one blocking failure per workflow with form interaction.
  - `EdgeTestCaseGeneratorAgent` — boundary conditions for workflows with numeric/date fields.
- All three receive the approved workflow list as a `<workflows>` context block in their prompt.
- Results are merged and TC IDs are renumbered sequentially per module.
- **Output state key:** `test_results`

### Node: `finalize`

- Serialises all state into output JSON and markdown files.
- Writes: `structural-model.json`, `structural-model-critique.json`, `workflows.json`, `workflow-validator-critique.json`, `test-cases.json`, and `.md` reports.

---

## Pipeline 2 — Post-Verification

Runs as a standalone `asyncio` loop (no LangGraph). For each positive test case:

1. **`StateChangeAgent`** (Gate): classifies whether the TC mutates state. Returns `requires_post_verification: true/false`. Negative/edge/read-only TCs are automatically skipped.
2. **`PostVerificationAgent`**: for TCs that pass the gate, generates a schema with `pre_check`, `post_check`, and `verification_type` (`same_actor_navigation` / `cross_actor` / `other`).

All test cases are processed concurrently, throttled by `--max-concurrency`.

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
| `structural_model_critique_results` | `_last_value` | List of per-module critic verdicts |
| `workflow_results` | `_last_value` | List of per-module workflow lists |
| `workflow_critique_results` | `_last_value` | List of per-module workflow critic verdicts |
| `test_results` | `_last_value` | List of per-module merged test cases |
| `output` | `_last_value` | Final assembled output dict |

---

## Resumability

Every `--generate` run gets a unique `run_id` (`<slug>-YYYYMMDD-HHmmss-<6hex>`). The `run_id` doubles as the LangGraph `thread_id` for its checkpoint in `outputs/.checkpoints/test_case_generation.sqlite`. A sidecar `.json` file stores the original inputs (spec path, model, output dir). Passing `--resume <run_id>` re-invokes the graph from the last successfully committed node.

---

## Error Handling

- Per-module exceptions in `asyncio.gather` are caught with `return_exceptions=True`. A failed module records an `error` key in its result and the pipeline continues with remaining modules.
- JSON parse failures in `BaseAgent.acall_llm_json` retry up to `max_retries=2` times, stripping markdown fences and retrying without `response_format` if the provider rejects it.
- LiteLLM's `drop_params=True` silently drops unsupported parameters (e.g. `temperature` on `o`-series models).
