# Data Models — Test Generation

This document describes the structured JSON schemas produced and consumed by the pipeline.

---

## Input: Parsed Spec

`cli.py` parses the input markdown and passes this dict to the pipeline:

```json
{
  "project_name": "My Application",
  "navigation_overview": "Sidebar with links to Clients, Reports, Settings.",
  "modules": [
    {
      "id": 1,
      "title": "Clients",
      "description": "The Clients page displays a data table..."
    }
  ]
}
```

Each `## ` heading in the markdown becomes one module. A `## Navigation` section is extracted as `navigation_overview` metadata and not processed as a module.

---

## `structural-model.json`

Top-level wrapper written by the `finalize` node.

```json
{
  "project_name": "My Application",
  "generated_at": "2026-05-03T12:00:00Z",
  "modules": [
    {
      "module_id": 1,
      "module_title": "Clients",
      "ast": {
        "module_name": "Clients",
        "components": {
          "Clients_Table": {
            "type": "data_table",
            "sortable_columns": ["Name", "Status"],
            "row_actions": [
              { "action_name": "View" },
              { "action_name": "Deactivate", "preconditions": ["status must be Active"] }
            ],
            "bulk_actions": [{ "action_name": "Export" }]
          }
        }
      },
      "attempts": 1
    }
  ]
}
```

### AST Component Types

| Type | Used for | Key fields |
|------|----------|------------|
| `form` | Single-page forms | `fields{}`, `submit_actions[]` |
| `wizard` | Multi-step forms | `steps[]` (each has `fields{}`, `submit_actions[]`) |
| `tab_container` | Pages with tabs | `tabs[]` (each has `fields{}`, may nest `tabs[]`) |
| `data_table` | Tables | `row_actions[]`, `bulk_actions[]`, `sortable_columns[]` |
| `state_bound_action_bar` | State-conditional action bars | `states{}` (each state has `available_actions[]`) |
| `repeating_group` | Add-row input patterns | `item_fields{}`, `min`, `max` |

### Field-level attributes

`type`, `required`, `required_when`, `visible_when`, `enabled_when`, `options[]`, `constraints[]`

### Action-level attributes

`on_success`, `preconditions[]`, `fields{}` (for modal/inline forms triggered by the action)

---

## `structural-model-critique.json`

```json
{
  "project_name": "My Application",
  "generated_at": "2026-05-03T12:00:00Z",
  "modules": [
    {
      "module_id": 1,
      "module_title": "Clients",
      "critique": {
        "verdict": "yes",
        "attempt": 2,
        "summary": "All interactive elements captured correctly.",
        "missing": [],
        "phantoms": [],
        "structural_errors": [],
        "fixes": [],
        "clarifications": []
      },
      "forced_ship": false,
      "needs_clarification": false,
      "clarifications": []
    }
  ]
}
```

**`missing[]` and `phantoms[]` are severity-tagged objects:**

```json
{
  "path": "Create_Client_Wizard.steps[2]",
  "severity": "critical | minor",
  "reason": "Step 2 'Address Details' is described but not present in AST"
}
```

**`forced_ship: true`** means the module hit the 3-attempt cap. Inspect `critique.missing` and `critique.fixes` (especially items with `"severity": "critical"`) to understand what to address in the spec or prompt.

**`needs_clarification: true`** means the validator found the source description genuinely unresolvable. `clarifications[]` on the outer object lists the exact phrases from the description that are ambiguous. The module was not retried further.

**`structural_errors[]`** contains human-readable descriptions of structural violations that prevent safe verdict (e.g., wrong AST nesting, generic `on_success` values) found during checks.

---

## `workflows.json`

```json
{
  "project_name": "My Application",
  "generated_at": "2026-05-03T12:00:00Z",
  "modules": [
    {
      "module_id": 1,
      "module_title": "Clients",
      "workflows": [
        {
          "wf_id": "WF-001",
          "name": "View client row action",
          "actor": "<role>",
          "conditional_branch": null,
          "terminal_action": "View",
          "on_success": "Client detail page opens"
        },
        {
          "wf_id": "WF-002",
          "name": "Deactivate Active client",
          "actor": "<role>",
          "conditional_branch": "entity_state == Active",
          "terminal_action": "Deactivate",
          "on_success": "Status badge updates to Inactive"
        }
      ],
      "attempts": 1
    }
  ]
}
```

`conditional_branch` is `null` for unconditional paths; otherwise describes the condition that must be true to reach the terminal action.

---

## `workflow-validator-critique.json`

Same outer structure as `structural-model-critique.json`. The `critique` object contains:

```json
{
  "verdict": "yes | retry | needs_clarification",
  "attempt": 1,
  "summary": "<one sentence>",
  "missing": [
    {
      "path": "state_bound_action_bar: state=Active, action=Close Client",
      "severity": "critical | minor",
      "reason": "No workflow covers the Close action from Active state"
    }
  ],
  "phantoms": [
    {
      "path": "WF-003 terminal_action=Approve",
      "severity": "critical | minor",
      "reason": "Approve not found in any AST node"
    }
  ],
  "structural_errors": ["WF-005 on_success is 'done' — too generic; AST has concrete value"],
  "fixes": ["Add workflow for state=Active, action=Close Client"],
  "clarifications": []
}
```

The outer object also carries `forced_ship`, `needs_clarification`, and `clarifications[]` fields with the same semantics as the structural model critique.

---

## `test-cases.json`

```json
{
  "project_name": "My Application",
  "generated_at": "2026-05-03T12:00:00Z",
  "model": "openai/gpt-4o",
  "modules": [
    {
      "module": "Clients",
      "test_cases": [
        {
          "tc_id": "TC-001",
          "wf_ref": "WF-001",
          "category": "positive",
          "test_case": "View client detail page",
          "preconditions": ["User logged in", "At least one client exists"],
          "steps": ["1. Navigate to Clients page", "2. Click View on any row"],
          "expected_result": "Client detail page opens showing all client information",
          "priority": "high"
        },
        {
          "tc_id": "TC-010",
          "wf_ref": "WF-002",
          "category": "negative",
          "test_case": "Attempt Deactivate on already Inactive client",
          "preconditions": ["User logged in", "Client in Inactive status"],
          "steps": ["1. Open client detail page", "2. Observe action bar"],
          "expected_result": "Deactivate action is not available in the action bar",
          "priority": "high"
        },
        {
          "tc_id": "TC-015",
          "wf_ref": null,
          "category": "edge",
          "subcategory": "interaction_edge",
          "test_case": "Double-click Export button on bulk selection",
          "preconditions": ["User logged in", "Multiple clients exist"],
          "steps": ["1. Select 3 clients via checkbox", "2. Double-click Export"],
          "expected_result": "Export triggered once, not twice",
          "priority": "low"
        }
      ],
      "summary": {
        "total": 18,
        "positive": 8,
        "negative": 6,
        "boundary": 2,
        "edge": 2,
        "high_priority": 10,
        "medium_priority": 6,
        "low_priority": 2
      }
    }
  ],
  "total_summary": {
    "total_modules": 1,
    "total_tests": 18,
    "positive": 8,
    "negative": 6,
    "boundary": 2,
    "edge": 2,
    "high_priority": 10,
    "medium_priority": 6,
    "low_priority": 2
  }
}
```

### Test case fields

| Field | Type | Description |
|-------|------|-------------|
| `tc_id` | string | Sequential `TC-NNN` within the module |
| `wf_ref` | string \| null | `wf_id` of the workflow this TC covers; `null` for non-workflow-specific tests |
| `category` | string | `positive \| negative \| edge` |
| `subcategory` | string | Edge tests only: `boundary \| input_edge \| interaction_edge \| state_edge \| data_edge` |
| `test_case` | string | Short descriptive title |
| `preconditions` | string[] | What must be true before executing steps |
| `steps` | string[] | Numbered action steps |
| `expected_result` | string | Observable outcome |
| `priority` | string | `high \| medium \| low` |

---

## `PipelineState` TypedDict

Defined in `framework/orchestrator/state.py`. Used as the LangGraph state schema.

```python
class PipelineState(TypedDict, total=False):
    functional_desc: Dict[str, Any]     # Parsed spec input
    api_key: str
    model: str
    debug: bool
    debug_file: str
    debug_dir: str
    output_dir: str
    test_types: Set[str]                # {"positive", "negative", "edge"}
    structural_model_results: List[Dict[str, Any]]
    structural_model_critique_results: List[Dict[str, Any]]
    workflow_results: List[Dict[str, Any]]
    workflow_critique_results: List[Dict[str, Any]]
    test_results: List[Dict[str, Any]]
    output: Dict[str, Any]
```

All fields use `_last_value` reducer — later writes overwrite earlier writes (standard single-writer pattern per LangGraph node).

---

## `RunMetadata` Dataclass

Defined in `framework/orchestrator/runs.py`. Written as a JSON sidecar alongside the checkpoint DB.

```python
@dataclass
class RunMetadata:
    run_id: str         # "<slug>-YYYYMMDD-HHmmss-<6hex>"
    input_path: str     # Absolute path to the spec file
    model: str          # LiteLLM model string
    output_dir: str     # Output directory for this run
    started_at: str     # ISO-8601 UTC timestamp
```