# Test Case Generation

Convert natural-language functional specifications into structured, machine-readable Structural Models, enumerate every executable workflow path, generate comprehensive positive, negative, and edge test cases — and optionally generate **Post-Verification schemas** that prove each state-mutating test case actually changed the system — fully automatically.

---

## How it works

Test Case Generation has **two independent pipelines**. Run them in sequence, or run post-verification standalone against any existing test-cases.json.

### Pipeline 1 — Test Generation

A functional spec markdown file goes in; structured JSON and markdown reports come out.

```
spec.md (## Module sections)
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│  Test Case Generation Pipeline  (--generate)                        │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  [1/4] generate_and_critique  (parallel per module)  │   │
│  │                                                      │   │
│  │  For each module (concurrent):                       │   │
│  │    attempt 1: StructuralModelGeneratorAgent → StructuralModelValidatorAgent       │   │
│  │      verdict=yes  ──────────────────────► done       │   │
│  │      verdict=retry → fixes[] fed back                │   │
│  │    attempt 2: StructuralModelGeneratorAgent(fixes) → Critic             │   │
│  │      verdict=yes  ──────────────────────► done       │   │
│  │      verdict=retry → fixes[] fed back                │   │
│  │    attempt 3: StructuralModelGeneratorAgent(fixes) → ship as-is         │   │
│  └──────────────────────────────────────────────────────┘   │
│                           ↓                                 │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  [2/4] extract_workflows  (parallel per module)    │   │
│  │                                                      │   │
│  │  For each module (concurrent):                       │   │
│  │    attempt 1: WorkflowExtractorAgent                 │   │
│  │               → WorkflowValidatorAgent                  │   │
│  │      verdict=yes  ──────────────────────► done       │   │
│  │      verdict=retry → fixes[] fed back                │   │
│  │    attempt 2/3: same retry loop (max 3)              │   │
│  └──────────────────────────────────────────────────────┘   │
│                           ↓                                 │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  [3/4] generate_tests  (parallel per module)         │   │
│  │                                                      │   │
│  │  For each module (concurrent):                       │   │
│  │    PositiveTestCaseGeneratorAgent  ┐                              │   │
│  │    NegativeTestCaseGeneratorAgent  ├── parallel → merge           │   │
│  │    EdgeTestCaseGeneratorAgent      ┘                              │   │
│  │    (each receives the approved workflow list)        │   │
│  └──────────────────────────────────────────────────────┘   │
│                           ↓                                 │
│  ┌──────────────────────┐                                   │
│  │  [4/4] finalize      │ → structural-model.json                     │
│  │                      │ → structural-model-critique.json          │
│  │                      │ → workflows.json                  │
│  │                      │ → workflow-validator-critique.json          │
│  │                      │ → test-cases.json                 │
│  │                      │ → {project}-{model}-critique.md   │
│  │                      │ → {project}-{model}-workflow-     │
│  │                      │       critique.md                 │
│  │                      │ → {project}-{model}-tests.md      │
│  └──────────────────────┘                                   │
└─────────────────────────────────────────────────────────────┘
```

**Stage 1 — StructuralModelGeneratorAgent + StructuralModelValidatorAgent** — For each module, the generator emits a UI component tree and the critic audits it with a binary `yes/retry` verdict. On retry, the critic's `fixes[]` array is fed directly back to the generator. Maximum 3 attempts per module.

**Stage 2 — WorkflowExtractorAgent + WorkflowValidatorAgent** — For each module, the extractor enumerates every distinct executable path through the module (one workflow per submit action, per state × action pair, per table row/bulk action, per conditional branch). The critic then audits the list for missing paths, phantom workflows, and wrong terminal actions — with the same 3-attempt retry loop. The approved workflow list is passed directly into Stage 2.

**Stage 3 — Three test agents** — For each module, three agents run in parallel against both the approved AST and the workflow list: positive tests (must cover every workflow), negative tests (workflow-aware failure injection), and edge/boundary tests (workflow-aware boundary scoping). Each test case carries a `wf_ref` linking it back to the workflow it covers. Results are merged into a single per-module test suite with sequential TC IDs.

All modules run concurrently across all stages.

---

### Pipeline 2 — Post-Verification (Separate)

Post-verification is an **independent pipeline** that runs after test generation. It reads the generated `test-cases.json` and a **merged functional description** (e.g. Teacher + Student spec concatenated for Moodle), then generates `pre_check` / `post_check` schemas that prove state-mutating tests actually changed the system.

> **Why a merged description?** When two roles (e.g. Teacher and Student) have separate spec files, cross-actor verification (Teacher creates → Student observes) requires the LLM to understand both actors simultaneously. Concatenate the relevant specs before passing to `--post-verify`.

```
test-cases.json  +  merged-description.md
         │
         ▼
┌─────────────────────────────────────────────────────────────┐
│  Post-Verification Pipeline  (--post-verify)                │
│                                                             │
│  For each positive test case (concurrent):                  │
│                                                             │
│  ┌────────────────────────────────────────────────────┐     │
│  │  [Gate] StateChangeAgent                     │     │
│  │                                                    │     │
│  │  requires_post_verification=false ──► skip         │     │
│  │  requires_post_verification=true  ──► continue     │     │
│  └────────────────────────────────────────────────────┘     │
│                           ↓ (only state-mutating TCs)       │
│  ┌────────────────────────────────────────────────────┐     │
│  │  PostVerificationAgent                             │     │
│  │                                                    │     │
│  │  Determines verification_type:                     │     │
│  │    same_actor_navigation — actor navigates to      │     │
│  │      another page to observe the state change      │     │
│  │    cross_actor — Actor B (different role/session)  │     │
│  │      verifies what Actor A did                     │     │
│  │    other — effect is outside the app (partial)     │     │
│  │                                                    │     │
│  │  Emits pre_check + post_check (or actor_a/b)       │     │
│  │  Inherits tc_id from the source test case          │     │
│  └────────────────────────────────────────────────────┘     │
│                           ↓                                 │
│  ┌──────────────────────┐                                   │
│  │  finalize            │ → post-verifications.json         │
│  └──────────────────────┘                                   │
└─────────────────────────────────────────────────────────────┘
```

**Gate — StateChangeAgent** — Classifies each positive test case as requiring post-verification or not. Only tests that create, update, delete, or execute financial/transactional operations pass through. Read-only, navigational, form-validation, and negative test cases are skipped automatically, saving LLM tokens.

**PostVerificationAgent** — For each test case that passes the gate, generates a structured schema containing a `pre_check` (what to observe before running the test) and a `post_check` (what to observe after, and the expected change). The output `test_case_id` always matches the source `tc_id`, ensuring a perfect 1-to-1 link between the execution steps and the verification wrapper.

---

## Installation

**Requirements:** Python 3.9+

```bash
git clone https://github.com/Mushfiqur6087/Test Case Generation
cd Test Case Generation
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

---

## Quick start

```bash
test-case-generation --generate \
  --input dataset/my-app-spec.md \
  --api-key "sk-..." \
  --model "openai/gpt-4o" \
  --output outputs/my-run
```

This writes the following files to `outputs/my-run/`:

| File | Contents |
|------|----------|
| `structural-model.json` | Generated Structural Model for every module |
| `structural-model-critique.json` | Critic verdict and audit for every module (Stage 1) |
| `workflows.json` | Enumerated workflow list for every module (Stage 2) |
| `workflow-validator-critique.json` | Workflow critic verdict and audit for every module (Stage 2) |
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

### Test Generation

```
test-case-generation --generate --input SPEC --api-key KEY [options]
test-case-generation --resume RUN_ID --api-key KEY
```

| Flag | Default | Description |
|------|---------|-------------|
| `--input` / `-i` | — | Path to `.md` spec file (required for `--generate`) |
| `--api-key` | — | API key for the LLM provider |
| `--model` | `openai/gpt-4o` | LiteLLM model string (must include provider prefix) |
| `--output` / `-o` | `outputs/autospectest/<project>/<model>/` | Output directory |
| `--type` | all | Subset of test types: `positive`, `negative`, `edge` |
| `--max-concurrency` | `10` | Max concurrent in-flight LLM calls |
| `--debug` | off | Write per-stage debug logs to `<output>/debug/` |
| `--resume RUN_ID` | — | Resume an interrupted run from its checkpoint |
| `--version` | — | Print version and exit |

### Post-Verification

```
test-case-generation --post-verify --input MERGED_DESC --test-cases TC_JSON --api-key KEY [options]
```

| Flag | Default | Description |
|------|---------|-------------|
| `--input` / `-i` | — | Path to merged `.md` description file (all relevant actor specs combined) |
| `--test-cases` | — | Path to `test-cases.json` produced by `--generate` |
| `--api-key` | — | API key for the LLM provider |
| `--model` | `openai/gpt-4o` | LiteLLM model string (must include provider prefix) |
| `--output` / `-o` | `output` | Output directory for `post-verifications.json` |
| `--max-concurrency` | `10` | Max concurrent in-flight LLM calls |
| `--debug` | off | Enable debug logging |

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

### `structural-model.json`

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

### `structural-model-critique.json`

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

### `workflow-validator-critique.json`

Same structure as `structural-model-critique.json`. The `critique` object contains `verdict`, `summary`, `missing` (missing workflow paths), `phantoms` (invented workflows not traceable to the AST), and `fixes`.

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

### `post-verifications.json`

Produced by `--post-verify`. Each entry maps directly to a source test case via `test_case_id`.

```json
[
  {
    "test_case_id": "TC-001",
    "verification_type": "same_actor_navigation",
    "coverage": "verifiable",
    "body": {
      "pre_check": {
        "navigate_to": "Accounts Overview",
        "observe": ["balance of source account", "balance of destination account"]
      },
      "post_check": {
        "navigate_to": "Accounts Overview",
        "observe": ["balance of source account", "balance of destination account"],
        "expected_change": "Source account balance decreased by transfer amount; destination account balance increased by the same amount."
      }
    }
  },
  {
    "test_case_id": "TC-015",
    "verification_type": "cross_actor",
    "coverage": "verifiable",
    "body": {
      "actor_a": {
        "role": "teacher",
        "action": "Execute the steps from the core test case."
      },
      "actor_b": {
        "role": "student",
        "session": "new_session",
        "navigate_to": "Course X -> Activities tab -> Assignments section",
        "observe": ["assignment name", "due date", "submission status column"],
        "expected_change": "Assignment appears with correct due date and submission status 'No submission'."
      }
    }
  }
]
```

**Verification types:**

| Type | When used |
|---|---|
| `same_actor_navigation` | The same user can navigate elsewhere in the app to observe the state change |
| `cross_actor` | The change is performed by Actor A but must be verified by Actor B in a separate session |
| `other` | The effect is outside the app boundary (e.g. external bank, external email inbox); `coverage` is set to `partial` |

**Coverage values:**

| Value | Meaning |
|---|---|
| `verifiable` | The full state change is observable within the app |
| `partial` | Only part of the state change is observable (e.g. source side of an external transfer) |
| `unverifiable` | The state change cannot be confirmed from any in-app page |

> **Note:** Test cases that are read-only, navigational, form-validation-only, or negative are automatically excluded by the Gate. Only state-mutating positive tests appear in `post-verifications.json`.

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

The `WorkflowValidatorAgent` checks for: missing form submit paths, missing state × action pairs, missing table row/bulk actions, phantom workflows, wrong terminal action names, bad conditional field references, and zero-workflow failures.

---

## Test agent workflow obligations

Each Stage 2 agent receives the approved workflow list as a compact `<workflows>` block appended to its prompt.

**PositiveTestCaseGeneratorAgent** — must collectively cover every workflow: at least one TC per `wf_id` that activates its `conditional_branch` and asserts its `on_success`.

**NegativeTestCaseGeneratorAgent** — for each workflow with a form interaction, identifies the most critical blocking failure for that workflow's branch. Adds one negative TC only when it catches a bug not covered by any other workflow's negative test.

**EdgeTestCaseGeneratorAgent** — for each workflow where `conditional_branch` activates a numeric or date field with a boundary, generates or confirms a boundary edge TC for it.

---

## Structural Model schema

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
test-case-generation --resume my-app-20260503-120000-abc123 --api-key "sk-..."
```

The run ID is printed at the start of every `--generate` invocation. Checkpoints are stored in `outputs/.checkpoints/autospectest.sqlite`; sidecar metadata (original inputs) lives in `outputs/.checkpoints/<run-id>.json`.

---

## Debug mode

```bash
test-case-generation --generate --input spec.md --api-key "..." --model openai/gpt-4o \
  --output outputs/debug-run --debug
```

With `--debug`, per-module log files are written to `outputs/debug-run/debug/<Module_Name>/`:

| File | Contents |
|------|----------|
| `01_ui_ast.log` | System prompt, user prompt, and raw LLM response for every StructuralModelGeneratorAgent call |
| `02_semantic_critic.log` | Same for every StructuralModelValidatorAgent call |
| `02b_workflow_extractor.log` | Same for every WorkflowExtractorAgent call |
| `02c_workflow_critic.log` | Same for every WorkflowValidatorAgent call |
| `03_test_positive.log` | Same for every PositiveTestCaseGeneratorAgent call |
| `04_test_negative.log` | Same for every NegativeTestCaseGeneratorAgent call |
| `05_test_edge.log` | Same for every EdgeTestCaseGeneratorAgent call |

Useful for diagnosing why a critic keeps retrying, why a workflow is missing, or why a test case lacks a `wf_ref`.

---

## Dataset and baselines

- `dataset/` — Input markdown specs
- `baselines/` — Single-prompt and few-shot reference implementations for ablation studies; see `baselines/README.md`

---

## Concurrency tuning

`--max-concurrency` controls how many LLM calls can be in-flight simultaneously across all modules and stages. The default of 10 is safe for most providers. Lower it if you hit rate limits; raise it for providers with high per-minute token quotas.

### Test Generation pipeline

A single module can make up to **10 LLM calls** at peak:
- Stage 1: up to 3 StructuralModelGeneratorAgent + 3 StructuralModelValidatorAgent calls (if all retries are used)
- Stage 2: up to 3 WorkflowExtractorAgent + 3 WorkflowValidatorAgent calls
- Stage 2: 3 test agent calls (positive, negative, edge) in parallel

With `--max-concurrency 10` and 5 modules, peak concurrency is bounded at 10 regardless of how many modules are retrying simultaneously.

### Post-Verification pipeline

Each test case that passes the Gate generates **2 LLM calls** (Gate + PostVerifier). All test cases are processed concurrently, bounded by `--max-concurrency`. For a typical suite of 80 test cases where 30 pass the gate, peak concurrency stays well within the default limit of 10.
