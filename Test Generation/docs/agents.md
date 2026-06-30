# Agents — Test Generation

Every agent inherits from `BaseAgent` (`framework/agents/base.py`). `BaseAgent` handles:
- LiteLLM call routing (sync `call_llm` / async `acall_llm`)
- JSON parsing with automatic markdown-fence stripping and retry (`call_llm_json` / `acall_llm_json`)
- Concurrency throttle via a shared `asyncio.Semaphore`
- Debug logging to per-stage files when `--debug` is enabled

---

## Test Generation Agents

### `ModuleContextExtractorAgent`

| Attribute | Value |
|-----------|-------|
| **File** | `agents/module_context_extractor.py` |
| **Prompt** | `prompts/module_context_extractor.md` |
| **Stage** | 0 — Module Context Extraction |
| **Role** | Synthesizes global navigation and module lists into a per-module context to ground preconditions and prevent hallucination. |
| **Inputs** | `module_title`, `description`, `navigation_overview`, `all_modules` |
| **Output** | `{ "summary": "...", "where_it_fits": "...", "assumed_state_on_entry": "..." }` |
| **LLM params** | `temperature=0.1`, `max_tokens=1024`, `reasoning_effort="low"` |

This agent runs once per module at the very start of the pipeline. Its output (`<module_context>`) is injected as the first input block into every downstream agent's prompt to ensure they understand where the module fits in the broader application lifecycle.

---

### `StructuralModelGeneratorAgent`

| Attribute | Value |
|-----------|-------|
| **File** | `agents/structural_model_generator.py` |
| **Prompt** | `prompts/structural_model_generator.md` |
| **Stage** | 1 — Structural Model generation |
| **Role** | Converts a module's natural-language functional description into a structured UI component tree (AST). |
| **Inputs** | `module` dict (`title` + `description`), optional `fixes[]` from the previous validator, `attempt` (int, 1-based), `max_attempts` (int) |
| **Output** | `{ "module_name": "...", "components": { ... } }` |
| **LLM params** | `temperature=0.1`, `max_tokens=8192`, `reasoning_effort="medium"` |

The agent renders its system prompt template at call time, filling three slots:
- `{attempt_number}` / `{max_attempts}` — visible to the LLM so it knows how many retries remain.
- `{fixes_block}` — omitted on attempt 1; on attempts 2+ the validator's `fixes[]` array is injected as a structured block so the LLM applies every fix before generating.

Only **interactive** elements are captured: form fields, buttons, table row/bulk actions, wizard steps, tabs, and state-bound action bars. Passive display text produces zero AST nodes.

---

### `StructuralModelValidatorAgent`

| Attribute | Value |
|-----------|-------|
| **File** | `agents/structural_model_validator.py` |
| **Prompt** | `prompts/structural_model_validator.md` |
| **Stage** | 1 — Structural Model audit |
| **Role** | Audits an AST against the source description; returns a `yes`, `retry`, or `needs_clarification` verdict. |
| **Inputs** | Raw description text, generated AST JSON, `attempt` (int, 1-based), `max_attempts` (int) |
| **Output** | See schema below |
| **LLM params** | `temperature=0.1`, `max_tokens=6144`, `reasoning_effort="medium"` |

The validator renders its system prompt template at call time, filling:
- `{attempt_number}` / `{max_attempts}` — echoed into the output JSON so logs are self-documenting.
- `{final_attempt_warning}` — injected only on the last attempt, instructing the LLM to return `retry` so the orchestrator can escalate cleanly rather than silently shipping a bad AST.

**Output schema:**
```json
{
  "verdict": "yes | retry | needs_clarification",
  "attempt": 2,
  "summary": "<one sentence>",
  "missing": [
    { "path": "Component.field", "severity": "critical | minor", "reason": "..." }
  ],
  "phantoms": [
    { "path": "Component.field", "severity": "critical | minor", "reason": "..." }
  ],
  "structural_errors": ["<description of Step 5 violation and its AST path>"],
  "fixes": ["<actionable instruction referencing the exact JSON path>"],
  "clarifications": ["<exact quoted phrase from description that is ambiguous>"]
}
```

**Verdict rules:**
- `yes` — 0–2 minor missing/phantoms only, no structural errors. `fixes` must be `[]`.
- `retry` — any critical missing/phantom, 3+ minor missing/phantoms, or any structural error. `fixes` must be populated.
- `needs_clarification` — description is genuinely unresolvable (not a judgment call). Orchestrator stops retrying and surfaces `clarifications[]` for human review. `fixes` must be `[]`.

When `verdict=retry`, the `fixes[]` array is fed directly back to `StructuralModelGeneratorAgent` for the next attempt. When `verdict=needs_clarification`, the loop stops immediately — retrying against a broken source description would waste budget. When all attempts are exhausted without `yes`, the orchestrator escalates with a severity-broken report (critical missing, critical phantoms, structural errors) rather than silently shipping the last AST.

---

### `WorkflowExtractorAgent`

| Attribute | Value |
|-----------|-------|
| **File** | `agents/workflow_extractor.py` |
| **Prompt** | `prompts/workflow_extractor.md` |
| **Stage** | 2 — Workflow extraction |
| **Role** | Enumerates every distinct executable path through a module's AST. |
| **Inputs** | `module_title`, `ast` JSON, raw `description`, optional `fixes[]`, `attempt` (int, 1-based), `max_attempts` (int) |
| **Output** | `{ "workflows": [ { "wf_id": "WF-001", "name": "...", "actor": "...", "conditional_branch": null\|"...", "terminal_action": "...", "on_success": "..." }, ... ] }` |
| **LLM params** | `temperature=0.2`, `max_tokens=8192` |

The agent renders its system prompt template at call time, filling three slots:
- `{attempt_number}` / `{max_attempts}` — visible to the LLM so it knows how many retries remain.
- `{fixes_block}` — omitted on attempt 1; on attempts 2+ the validator's `fixes[]` array is injected as a structured block.

The prompt includes a 9-item **SELF-CHECK** section that the LLM verifies before outputting (every submit_action has a workflow, every state × action pair is covered, sequential wf_id numbering, etc.).

One workflow per:
- `form` submit action (× conditional branch if `visible_when` fields exist)
- `wizard` step sequence
- `state_bound_action_bar` state × action pair
- `data_table` row action + each bulk action
- `tab_container` tab with a form submit

The agent also exposes `format_workflows_block(workflows)` — a static helper that renders a compact `<workflows>` XML-like block. This block is appended verbatim to all Stage 3 agent prompts so test agents have a fixed, machine-parseable workflow reference.

---

### `WorkflowValidatorAgent`

| Attribute | Value |
|-----------|-------|
| **File** | `agents/workflow_validator.py` |
| **Prompt** | `prompts/workflow_validator.md` |
| **Stage** | 2 — Workflow audit |
| **Role** | Validates the extracted workflow list for completeness and accuracy; returns a `yes`, `retry`, or `needs_clarification` verdict. |
| **Inputs** | Raw description, AST JSON, `workflows[]` list, `attempt` (int, 1-based), `max_attempts` (int) |
| **Output** | See schema below |
| **LLM params** | `temperature=0.1`, `max_tokens=4096`, `reasoning_effort="medium"` |

The validator renders its system prompt template at call time, filling:
- `{attempt_number}` / `{max_attempts}` — echoed into the output JSON so logs are self-documenting.
- `{final_attempt_warning}` — injected only on the last attempt, instructing the LLM to return `retry` so the orchestrator can escalate cleanly.

**Seven Checks:** missing form workflows, missing state-machine workflows, missing data table workflows, phantom workflows, wrong conditional branches, empty/generic on_success, zero-workflow failures.

**Output schema:**
```json
{
  "verdict": "yes | retry | needs_clarification",
  "attempt": 2,
  "summary": "<one sentence>",
  "missing": [
    { "path": "AST path or state×action", "severity": "critical | minor", "reason": "..." }
  ],
  "phantoms": [
    { "path": "WF-NNN terminal_action=X", "severity": "critical | minor", "reason": "..." }
  ],
  "structural_errors": ["<description of Check 5/6 violation>"],
  "fixes": ["<actionable instruction>"],
  "clarifications": ["<exact quoted phrase from description>"]
}
```

**Verdict rules:**
- `yes` — 0–2 minor missing/phantoms only, no structural errors. `fixes` must be `[]`.
- `retry` — any critical missing/phantom, 3+ minor issues, or any structural error. `fixes` must be populated.
- `needs_clarification` — description is genuinely unresolvable. Orchestrator stops retrying and surfaces `clarifications[]`. `fixes` must be `[]`.

When all attempts are exhausted without `yes`, the orchestrator escalates with a severity-broken report (critical missing, critical phantoms, structural errors) rather than silently shipping the last workflow list.

---

### `PositiveTestCaseGeneratorAgent`

| Attribute | Value |
|-----------|-------|
| **File** | `agents/positive_test_case_generator.py` |
| **Prompt** | `prompts/positive_test_case_generator.md` |
| **Stage** | 3 — Positive test generation |
| **Role** | Generates happy-path test cases, one per workflow minimum. |
| **Inputs** | `module_title`, `ast`, `description`, `workflows[]` |
| **Output** | `{ "test_cases": [ { "tc_id": "...", "wf_ref": "WF-001", "test_case": "...", "preconditions": [...], "steps": [...], "expected_result": "...", "priority": "high\|medium\|low" }, ... ] }` |
| **LLM params** | `temperature=0.3`, `max_tokens=16384` |

Every `wf_id` in the approved workflow list must be covered by at least one positive TC. The TC's `wf_ref` links it back to the workflow.

Uses the shared `build_test_prompt()` utility from `agents/utils.py` for user prompt assembly.

---

### `NegativeTestCaseGeneratorAgent`

| Attribute | Value |
|-----------|-------|
| **File** | `agents/negative_test_case_generator.py` |
| **Prompt** | `prompts/negative_test_case_generator.md` |
| **Stage** | 3 — Negative test generation |
| **Role** | Generates workflow-aware failure-injection test cases. |
| **Inputs** | Same as `PositiveTestCaseGeneratorAgent` |
| **Output** | Same schema |
| **LLM params** | `temperature=0.3`, `max_tokens=16384` |

For each workflow with a form interaction, generates the most critical blocking failure for that workflow's branch. Adds one negative TC only when it catches a unique bug not covered by any other workflow's negative test.

Uses the shared `build_test_prompt()` utility from `agents/utils.py` for user prompt assembly.

---

### `EdgeTestCaseGeneratorAgent`

| Attribute | Value |
|-----------|-------|
| **File** | `agents/edge_test_case_generator.py` |
| **Prompt** | `prompts/edge_test_case_generator.md` |
| **Stage** | 3 — Edge/boundary test generation |
| **Role** | Generates boundary and edge-case test cases. |
| **Inputs** | Same as `PositiveTestCaseGeneratorAgent` |
| **Output** | Same schema + `subcategory`: `boundary\|input_edge\|interaction_edge\|state_edge\|data_edge` |
| **LLM params** | `temperature=0.3`, `max_tokens=16384` |

For each workflow where `conditional_branch` activates a numeric or date field with a boundary, generates or confirms a boundary edge TC. `wf_ref` may be `null` for non-workflow-specific edges.

Uses the shared `build_test_prompt()` utility from `agents/utils.py` for user prompt assembly.

---

