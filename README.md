# AutoSpecTest

Convert natural-language functional specifications into structured, machine-readable UI Abstract Syntax Trees (UI-AST), enumerate every executable workflow path, and generate comprehensive positive, negative, and edge test cases — fully automatically.

---

## How it works

A functional spec markdown file goes in; structured JSON and markdown reports come out.

```
spec.md (## Module sections)
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│  AutoSpecTest Pipeline                                      │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  [1/3] generate_and_critique  (parallel per module)  │   │
│  │                                                      │   │
│  │  For each module (concurrent):                       │   │
│  │    attempt 1: UIASTAgent → SemanticCriticAgent       │   │
│  │      verdict=yes  ──────────────────────► done       │   │
│  │      verdict=retry → fixes[] fed back                │   │
│  │    attempt 2: UIASTAgent(fixes) → Critic             │   │
│  │      verdict=yes  ──────────────────────► done       │   │
│  │      verdict=retry → fixes[] fed back                │   │
│  │    attempt 3: UIASTAgent(fixes) → ship as-is         │   │
│  └──────────────────────────────────────────────────────┘   │
│                           ↓                                 │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  [1.5/3] extract_workflows  (parallel per module)    │   │
│  │                                                      │   │
│  │  For each module (concurrent):                       │   │
│  │    attempt 1: WorkflowExtractorAgent                 │   │
│  │               → WorkflowCriticAgent                  │   │
│  │      verdict=yes  ──────────────────────► done       │   │
│  │      verdict=retry → fixes[] fed back                │   │
│  │    attempt 2/3: same retry loop (max 3)              │   │
│  └──────────────────────────────────────────────────────┘   │
│                           ↓                                 │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  [2/3] generate_tests  (parallel per module)         │   │
│  │                                                      │   │
│  │  For each module (concurrent):                       │   │
│  │    TestPositiveAgent  ┐                              │   │
│  │    TestNegativeAgent  ├── parallel → merge           │   │
│  │    TestEdgeAgent      ┘                              │   │
│  │    (each receives the approved workflow list)        │   │
│  └──────────────────────────────────────────────────────┘   │
│                           ↓                                 │
│  ┌──────────────────────┐                                   │
│  │  [3/3] finalize      │ → ui-ast.json                    │
│  │                      │ → semantic-critique.json          │
│  │                      │ → workflows.json                  │
│  │                      │ → workflow-critique.json          │
│  │                      │ → test-cases.json                 │
│  │                      │ → {project}-{model}-critique.md   │
│  │                      │ → {project}-{model}-workflow-     │
│  │                      │       critique.md                 │
│  │                      │ → {project}-{model}-tests.md      │
│  └──────────────────────┘                                   │
└─────────────────────────────────────────────────────────────┘
```

**Stage 1 — UIASTAgent + SemanticCriticAgent** — For each module, the generator emits a UI component tree and the critic audits it with a binary `yes/retry` verdict. On retry, the critic's `fixes[]` array is fed directly back to the generator. Maximum 3 attempts per module.

**Stage 1.5 — WorkflowExtractorAgent + WorkflowCriticAgent** — For each module, the extractor enumerates every distinct executable path through the module (one workflow per submit action, per state × action pair, per table row/bulk action, per conditional branch). The critic then audits the list for missing paths, phantom workflows, and wrong terminal actions — with the same 3-attempt retry loop. The approved workflow list is passed directly into Stage 2.

**Stage 2 — Three test agents** — For each module, three agents run in parallel against both the approved AST and the workflow list: positive tests (must cover every workflow), negative tests (workflow-aware failure injection), and edge/boundary tests (workflow-aware boundary scoping). Each test case carries a `wf_ref` linking it back to the workflow it covers. Results are merged into a single per-module test suite with sequential TC IDs.

All modules run concurrently across all stages.

---

## Installation

**Requirements:** Python 3.9+

```bash
git clone https://github.com/Mushfiqur6087/AutoSpecTest
cd AutoSpecTest
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

After installation, the `autospectest` command is available in the venv.

---

## Quick start

```bash
autospectest --generate \
  --input dataset/my-app-spec.md \
  --api-key "sk-..." \
  --model "openai/gpt-4o" \
  --output outputs/my-run
```

This writes the following files to `outputs/my-run/`:

| File | Contents |
|------|----------|
| `ui-ast.json` | Generated UI-AST for every module |
| `semantic-critique.json` | Critic verdict and audit for every module (Stage 1) |
| `workflows.json` | Enumerated workflow list for every module (Stage 1.5) |
| `workflow-critique.json` | Workflow critic verdict and audit for every module (Stage 1.5) |
| `test-cases.json` | Merged positive/negative/edge test cases with `wf_ref` per TC |
| `{project}-{model}-critique.md` | Human-readable semantic critique report |
| `{project}-{model}-workflow-critique.md` | Human-readable workflow critique report |
| `{project}-{model}-tests.md` | Human-readable test case table with WF Ref column |

---

## Input format

The input is a markdown file. Each `## ` heading becomes one module. A `## Navigation` section is extracted as metadata and not processed as a module.

```markdown
# My Application

## Navigation
Sidebar with links to Clients, Reports, Settings.

## Clients
The Clients page is a data table with columns Name, Status, Account Number.
Rows have a three-dot menu with View and Deactivate (only when Status is Active).
A checkbox column enables bulk Export. The table is sortable by Name and Status.

## Create Client
A wizard with 3 steps: Basic Info, Contact, Review.
Step 1 collects First Name (required), Last Name (required), Email (required, must be valid email).
Step 2 collects Phone, Address (required).
Step 3 is read-only review. Submit creates the client in Pending status.
```

The file stem (e.g. `my-app-spec`) becomes the project name in the output.

---

## CLI reference

```
autospectest --generate --input SPEC --api-key KEY [options]
autospectest --resume RUN_ID --api-key KEY
```

| Flag | Default | Description |
|------|---------|-------------|
| `--input` / `-i` | — | Path to `.md` spec file (required for `--generate`) |
| `--api-key` | — | API key for the LLM provider |
| `--model` | `openai/gpt-4o` | LiteLLM model string (must include provider prefix) |
| `--output` / `-o` | `outputs/autospectest/<project>/<model>/` | Output directory |
| `--max-concurrency` | `10` | Max concurrent in-flight LLM calls |
| `--debug` | off | Write per-stage debug logs to `<output>/debug/` |
| `--resume RUN_ID` | — | Resume an interrupted run from its checkpoint |
| `--version` | — | Print version and exit |

---

## LLM providers

All LLM calls go through [LiteLLM](https://github.com/BerriAI/litellm). The `--model` flag accepts any LiteLLM model string with a provider prefix:

```bash
# OpenAI
--model openai/gpt-4o
--model openai/gpt-4o-mini

# Anthropic
--model anthropic/claude-3-5-sonnet-20241022

# OpenRouter (proxies 100+ models)
--model openrouter/anthropic/claude-3.5-sonnet
--model openrouter/openai/gpt-4o

# GitHub Models
--model github/gpt-4o
```

The `--api-key` value is passed directly to LiteLLM and must match the provider (OpenAI key for OpenAI models, Anthropic key for Anthropic, OpenRouter key for OpenRouter, etc.).

Parameters unsupported by a given model (e.g. `temperature` on o-series models) are silently dropped — no manual per-model configuration needed.

---

## Output files

### `ui-ast.json`

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

### `semantic-critique.json`

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
        "summary": "All interactive elements captured correctly.",
        "missing": [],
        "phantoms": [],
        "fixes": []
      },
      "forced_ship": false
    }
  ]
}
```

**`forced_ship: true`** means the module hit the 3-attempt cap — the final attempt's output was shipped regardless of the critic's verdict. Check `critique.missing` and `critique.fixes` to understand what to fix in the spec or prompt.

---

### `workflows.json`

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

Each workflow represents one distinct, complete interaction path. `conditional_branch` is `null` for unconditional paths; otherwise it describes the condition that must be true to reach that terminal action.

---

### `workflow-critique.json`

Same structure as `semantic-critique.json`. The `critique` object contains `verdict`, `summary`, `missing` (missing workflow paths), `phantoms` (invented workflows not traceable to the AST), and `fixes`.

---

### `test-cases.json`

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

Each test case carries:
- **`wf_ref`** — which workflow this TC covers (`null` for navigation-only or generic tests)
- **`category`** — `positive | negative | edge` (set automatically during merge)
- **`subcategory`** — edge tests only: `boundary | input_edge | interaction_edge | state_edge | data_edge`

TC IDs are renumbered sequentially across all categories within each module.

---

## Workflow extraction

The workflow extractor enumerates distinct paths based on AST node type:

| AST node type | What is enumerated |
|---|---|
| `form` with no conditionals | One workflow per `submit_actions[]` entry |
| `form` with `visible_when` fields | One workflow per unique conditional branch × submit action |
| `wizard` | One workflow per distinct step sequence or `submit_actions[]` entry |
| `state_bound_action_bar` | One workflow per state × available action (state × action = one workflow) |
| `data_table` | One workflow per `row_actions[]` entry + one per `bulk_actions[]` entry |
| `tab_container` | One workflow per tab containing a form with a submit action |
| `repeating_group` | Not a standalone source — part of the form workflow that activates it |

The `WorkflowCriticAgent` checks for: missing form submit paths, missing state × action pairs, missing table row/bulk actions, phantom workflows, wrong terminal action names, bad conditional field references, and zero-workflow failures.

---

## Test agent workflow obligations

Each Stage 2 agent receives the approved workflow list as a compact `<workflows>` block appended to its prompt.

**TestPositiveAgent** — must collectively cover every workflow: at least one TC per `wf_id` that activates its `conditional_branch` and asserts its `on_success`.

**TestNegativeAgent** — for each workflow with a form interaction, identifies the most critical blocking failure for that workflow's branch. Adds one negative TC only when it catches a bug not covered by any other workflow's negative test.

**TestEdgeAgent** — for each workflow where `conditional_branch` activates a numeric or date field with a boundary, generates or confirms a boundary edge TC for it.

---

## UI-AST schema

The AST captures **interactive elements only**. The critic enforces this — passive display labels ("the page shows the client name") produce zero expected items and are not emitted.

| Component type | Used for |
|---|---|
| `form` | Single-page forms with `fields` |
| `wizard` | Multi-step forms with `steps[]`, each step has `fields` |
| `tab_container` | Pages with `tabs[]`, each tab has `fields` and can nest more `tabs[]` |
| `data_table` | Tables with `row_actions[]`, `bulk_actions[]`, `sortable_columns[]` |
| `state_bound_action_bar` | Action buttons that change by entity state (Pending/Active/Closed) with `states{}` |
| `repeating_group` | Add-row patterns; has `item_fields{}`, optional `min`/`max` |

Field-level attributes: `type`, `required`, `required_when`, `visible_when`, `enabled_when`, `options[]`, `constraints[]`.

Action-level attributes: `on_success`, `preconditions[]`, `fields{}` (for modal/inline forms triggered by the action).

---

## Resumability

Every run gets a unique run ID (`<project>-YYYYMMDD-HHmmss-<6char>`). If a run is interrupted mid-pipeline, resume it with:

```bash
autospectest --resume my-app-20260503-120000-abc123 --api-key "sk-..."
```

The run ID is printed at the start of every `--generate` invocation. Checkpoints are stored in `outputs/.checkpoints/autospectest.sqlite`; sidecar metadata (original inputs) lives in `outputs/.checkpoints/<run-id>.json`.

---

## Debug mode

```bash
autospectest --generate --input spec.md --api-key "..." --model openai/gpt-4o \
  --output outputs/debug-run --debug
```

With `--debug`, per-module log files are written to `outputs/debug-run/debug/<Module_Name>/`:

| File | Contents |
|------|----------|
| `01_ui_ast.log` | System prompt, user prompt, and raw LLM response for every UIASTAgent call |
| `02_semantic_critic.log` | Same for every SemanticCriticAgent call |
| `02b_workflow_extractor.log` | Same for every WorkflowExtractorAgent call |
| `02c_workflow_critic.log` | Same for every WorkflowCriticAgent call |
| `03_test_positive.log` | Same for every TestPositiveAgent call |
| `04_test_negative.log` | Same for every TestNegativeAgent call |
| `05_test_edge.log` | Same for every TestEdgeAgent call |

Useful for diagnosing why a critic keeps retrying, why a workflow is missing, or why a test case lacks a `wf_ref`.

---

## Docker

```bash
docker build -t autospectest .

# Mount a host directory for outputs
docker run --rm \
  -v $(pwd)/outputs:/app/outputs \
  -v $(pwd)/dataset:/app/dataset \
  autospectest \
  --generate \
  --input dataset/my-spec.md \
  --api-key "sk-..." \
  --model openai/gpt-4o
```

The Docker image installs dependencies in a separate layer so source-only changes rebuild in seconds. Runs as a non-root user to avoid root-owned output files on bind mounts.

---

## Dataset and baselines

- `dataset/` — Input markdown specs
- `baselines/` — Single-prompt and few-shot reference implementations for ablation studies; see `baselines/README.md`

---

## Concurrency tuning

`--max-concurrency` controls how many LLM calls can be in-flight simultaneously across all modules and stages. The default of 10 is safe for most providers. Lower it if you hit rate limits; raise it for providers with high per-minute token quotas.

With the workflow stage added, a single module can now make up to **10 LLM calls** at peak:
- Stage 1: up to 3 UIASTAgent + 3 SemanticCriticAgent calls (if all retries are used)
- Stage 1.5: up to 3 WorkflowExtractorAgent + 3 WorkflowCriticAgent calls
- Stage 2: 3 test agent calls (positive, negative, edge) in parallel

With `--max-concurrency 10` and 5 modules, peak concurrency is bounded at 10 regardless of how many modules are retrying simultaneously.
