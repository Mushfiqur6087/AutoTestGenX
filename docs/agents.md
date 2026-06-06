# Agents — Test Case Generation

Every agent inherits from `BaseAgent` (`framework/agents/base.py`). `BaseAgent` handles:
- LiteLLM call routing (sync `call_llm` / async `acall_llm`)
- JSON parsing with automatic markdown-fence stripping and retry (`call_llm_json` / `acall_llm_json`)
- Concurrency throttle via a shared `asyncio.Semaphore`
- Debug logging to per-stage files when `--debug` is enabled

---

## Test Generation Agents

### `StructuralModelGeneratorAgent`

| Attribute | Value |
|-----------|-------|
| **File** | `agents/structural_model_generator.py` |
| **Prompt** | `prompts/structural_model_generator.md` |
| **Stage** | 1 — Structural Model generation |
| **Role** | Converts a module's natural-language functional description into a structured UI component tree (AST). |
| **Inputs** | `module` dict (`title` + `description`), optional `fixes[]` from the previous critic |
| **Output** | `{ "module_name": "...", "components": { ... } }` |
| **LLM params** | `temperature=0.1`, `max_tokens=8192`, `reasoning_effort="medium"` |

The agent only captures **interactive** elements: form fields, buttons, table row/bulk actions, wizard steps, tabs, and state-bound action bars. Passive display text produces no AST nodes. When `fixes` are provided, they are appended to the prompt as a numbered critic-feedback block.

---

### `StructuralModelValidatorAgent`

| Attribute | Value |
|-----------|-------|
| **File** | `agents/structural_model_validator.py` |
| **Prompt** | `prompts/structural_model_validator.md` |
| **Stage** | 1 — Structural Model audit |
| **Role** | Audits an AST against the source description; returns a binary `yes/retry` verdict. |
| **Inputs** | Raw description text, generated AST JSON |
| **Output** | `{ "verdict": "yes\|retry", "summary": "...", "missing": [...], "phantoms": [...], "fixes": [...] }` |
| **LLM params** | `temperature=0.1`, `max_tokens=6144`, `reasoning_effort="medium"` |

**Verdict rules:**
- `yes` — 0–2 minor missing/phantoms, no critical structural errors.
- `retry` — 3+ missing OR 3+ phantoms OR any required field/state absent OR wrong nesting.

When `verdict=retry`, the `fixes[]` array is fed directly back to `StructuralModelGeneratorAgent` for the next attempt.

---

### `WorkflowExtractorAgent`

| Attribute | Value |
|-----------|-------|
| **File** | `agents/workflow_extractor.py` |
| **Prompt** | `prompts/workflow_extractor.md` |
| **Stage** | 2 — Workflow extraction |
| **Role** | Enumerates every distinct executable path through a module's AST. |
| **Inputs** | `module_title`, `ast` JSON, raw `description`, optional `fixes[]` |
| **Output** | `{ "workflows": [ { "wf_id": "WF-001", "name": "...", "actor": "...", "conditional_branch": null\|"...", "terminal_action": "...", "on_success": "..." }, ... ] }` |
| **LLM params** | `temperature=0.2`, `max_tokens=8192` |

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
| **Role** | Validates the extracted workflow list for completeness and accuracy. |
| **Inputs** | Raw description, AST JSON, `workflows[]` list |
| **Output** | Same schema as `StructuralModelValidatorAgent` (`verdict`, `summary`, `missing`, `phantoms`, `fixes`) |
| **LLM params** | `temperature=0.1`, `max_tokens=6144` |

Checks for: missing form submit paths, missing state × action pairs, missing table row/bulk actions, phantom workflows not traceable to the AST, wrong terminal action names, bad conditional field references, zero-workflow failures.

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

---

## Post-Verification Agents

### `StateChangeAgent`

| Attribute | Value |
|-----------|-------|
| **File** | `agents/post_verifier.py` |
| **Prompt** | `prompts/state_change.md` |
| **Role** | Gate — classifies whether a positive TC mutates application state. |
| **Inputs** | A single `test_case` JSON object |
| **Output** | `{ "requires_post_verification": true\|false, "reason": "..." }` |
| **LLM params** | `temperature=0.0`, `max_tokens=4096` |

Passes TCs that **create, update, delete, or execute financial/transactional operations**. Automatically skips read-only, navigational, form-validation-only, negative, and edge TCs.

---

### `PostVerificationAgent`

| Attribute | Value |
|-----------|-------|
| **File** | `agents/post_verifier.py` |
| **Prompt** | `prompts/post_verification.md` |
| **Role** | Generates a `pre_check` + `post_check` verification schema for a state-mutating TC. |
| **Inputs** | Merged functional description, single `test_case` JSON |
| **Output** | `{ "test_case_id": "TC-001", "verification_type": "same_actor_navigation\|cross_actor\|other", "coverage": "verifiable\|partial\|unverifiable", "body": { "pre_check": {...}, "post_check": {...} } }` |
| **LLM params** | `temperature=0.2`, `max_tokens=4096` |

`test_case_id` always mirrors the source `tc_id` — guaranteed 1-to-1 link between execution steps and verification wrapper. For cross-actor verifications, `body` contains `actor_a` and `actor_b` objects instead.
