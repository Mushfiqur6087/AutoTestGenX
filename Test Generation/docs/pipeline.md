# Pipeline Walkthrough — Test Generation

This document traces a single execution of the full Test Generation Pipeline for a concrete module: **"Client Management"** from the Mifos spec.

---

## Setup

```
spec file: dataset/raw_specifications/Mifos/Mifos.md
model:     openai/gpt-4o
output:    outputs/test_generation/Mifos/openai-gpt-4o/
```

The CLI parses the markdown and extracts 6 modules. "Client Management" is module `id=1`.

---

## Stage 1 — Structural Model Generation

### Attempt 1 of 3 — StructuralModelGeneratorAgent

The generator's system prompt is rendered with:

```
Attempt: 1 of 3
[fixes_block: omitted — first attempt]
```

**User message:**

```
Module: Client Management

The Clients page displays a data table of all clients with columns for Name
(clickable link), Account No., External ID, Status (...), Office, and Staff.
A search field allows searching by name... Two buttons at the top-right provide
"Import Client" and "Create Client."

The Create Client form is a multi-step wizard. Step 1 (General Details) contains
Office (required), Legal Form, First Name (required), Last Name (required),
Date of Birth, Gender, Staff, Mobile Number, Email Address, Client Type,
Client Classification, External ID (must be unique), Submitted On (required),
Is Staff checkbox, Active checkbox, and Open Savings Account option.
Step 2 covers Address Details. Step 3 covers Family Members. Step 4 covers
Identifiers (Document Type and Document Key). Clicking "Submit" creates the
client in Pending status....
```

**LLM output (truncated):**

```json
{
  "module_name": "Client Management",
  "components": {
    "Clients_Table": {
      "type": "data_table",
      "sortable_columns": ["Name", "Status"],
      "row_actions": [
        { "action_name": "View" },
        { "action_name": "Deactivate", "preconditions": ["status must be Active"] }
      ],
      "bulk_actions": [{ "action_name": "Export" }]
    },
    "Create_Client_Wizard": {
      "type": "wizard",
      "steps": [
        {
          "step": 1,
          "title": "General Details",
          "fields": {
            "Office":      { "type": "dropdown",    "required": true },
            "First_Name":  { "type": "unspecified", "required": true },
            "Last_Name":   { "type": "unspecified", "required": true },
            "External_ID": { "type": "unspecified", "constraints": ["must be unique"] },
            "Submitted_On":{ "type": "date",        "required": true }
          },
          "submit_actions": [{ "action_name": "Submit", "on_success": "Client created in Pending status" }]
        }
      ]
    },
    "Client_Detail_Action_Bar": {
      "type": "state_bound_action_bar",
      "states": {
        "Pending": {
          "available_actions": [
            { "action_name": "Activate", "fields": { "Activation_Date": { "type": "date", "required": true } } },
            { "action_name": "Edit" },
            { "action_name": "Reject",   "fields": { "Reason": { "type": "unspecified", "required": true } } },
            { "action_name": "Withdraw", "fields": { "Reason": { "type": "unspecified", "required": true } } }
          ]
        },
        "Active": {
          "available_actions": [
            { "action_name": "Edit" },
            { "action_name": "Transfer Client", "fields": { "Destination_Office": { "type": "dropdown", "required": true } } },
            { "action_name": "Close", "fields": { "Closure_Reason": { "type": "unspecified", "required": true } } }
          ]
        },
        "Closed": {
          "available_actions": [{ "action_name": "Reactivate" }]
        }
      }
    }
  }
}
```

---

### Attempt 1 of 3 — StructuralModelValidatorAgent

The validator's system prompt is rendered with:

```
Attempt: 1 of 3
[final_attempt_warning: omitted — not the last attempt]
```

**Verdict: `retry`**

```json
{
  "verdict": "retry",
  "attempt": 1,
  "summary": "Multiple required wizard steps missing; Identifiers tab not captured.",
  "missing": [
    {
      "path": "Create_Client_Wizard.steps[2]",
      "severity": "critical",
      "reason": "Step 2 'Address Details' is described in the spec but absent from AST"
    },
    {
      "path": "Create_Client_Wizard.steps[3]",
      "severity": "critical",
      "reason": "Step 3 'Family Members' is described in the spec but absent from AST"
    },
    {
      "path": "Create_Client_Wizard.steps[4]",
      "severity": "critical",
      "reason": "Step 4 'Identifiers' with Document_Type and Document_Key is absent"
    }
  ],
  "phantoms": [],
  "structural_errors": [],
  "fixes": [
    "Add wizard step 2 'Address Details' (description says step 2 covers address details)",
    "Add wizard step 3 'Family Members'",
    "Add wizard step 4 'Identifiers' with fields: Document_Type (dropdown), Document_Key (unspecified)"
  ],
  "clarifications": []
}
```

Console output:

```
  ~~ Client Management | attempt 1/3 | verdict=retry | missing=3 phantoms=0 | retrying...
```

---

### Attempt 2 of 3 — StructuralModelGeneratorAgent (with fixes)

The generator's system prompt is now rendered with the `fixes[]` block injected:

```
Attempt: 2 of 3

--- VALIDATOR FIXES — APPLY ALL OF THESE BEFORE GENERATING ---
- Add wizard step 2 'Address Details' (description says step 2 covers address details)
- Add wizard step 3 'Family Members'
- Add wizard step 4 'Identifiers' with fields: Document_Type (dropdown), Document_Key (unspecified)
Every item above is a confirmed error from the previous attempt. Do not repeat them.
--- END FIXES ---
```

The generator now produces a wizard with all 4 steps.

---

### Attempt 2 of 3 — StructuralModelValidatorAgent

**Verdict: `yes`** — All 4 wizard steps now present, no missing or phantom items.

```json
{
  "verdict": "yes",
  "attempt": 2,
  "summary": "All 4 wizard steps present; state machine and table correctly captured.",
  "missing": [],
  "phantoms": [],
  "structural_errors": [],
  "fixes": [],
  "clarifications": []
}
```

Console output:

```
  OK Client Management | attempt 2/3 | 3 component(s)
```

AST ships. Stage 1 complete.

---

## Stage 2 — Workflow Extraction

### Attempt 1 of 3 — WorkflowExtractorAgent

System prompt rendered with `Attempt: 1 of 3`, no fixes block.

The agent runs its 9-item self-check before outputting, then emits:

```json
{
  "workflows": [
    { "wf_id": "WF-001", "name": "View client",            "terminal_action": "View",            "conditional_branch": null },
    { "wf_id": "WF-002", "name": "Deactivate Active client","terminal_action": "Deactivate",       "conditional_branch": "entity_state == Active" },
    { "wf_id": "WF-003", "name": "Bulk Export clients",    "terminal_action": "Export",           "conditional_branch": null },
    { "wf_id": "WF-004", "name": "Create Client wizard",   "terminal_action": "Submit",           "conditional_branch": null },
    { "wf_id": "WF-005", "name": "Activate Pending client","terminal_action": "Activate",         "conditional_branch": "entity_state == Pending" },
    { "wf_id": "WF-006", "name": "Reject Pending client",  "terminal_action": "Reject",           "conditional_branch": "entity_state == Pending" },
    { "wf_id": "WF-007", "name": "Withdraw Pending client","terminal_action": "Withdraw",         "conditional_branch": "entity_state == Pending" },
    { "wf_id": "WF-008", "name": "Transfer Active client", "terminal_action": "Transfer Client",  "conditional_branch": "entity_state == Active" },
    { "wf_id": "WF-009", "name": "Close Active client",    "terminal_action": "Close",            "conditional_branch": "entity_state == Active" },
    { "wf_id": "WF-010", "name": "Reactivate Closed client","terminal_action": "Reactivate",     "conditional_branch": "entity_state == Closed" }
  ],
  "total": 10
}
```

---

### Attempt 1 of 3 — WorkflowValidatorAgent

**Verdict: `yes`** — All state × action pairs covered, no phantoms, no structural errors.

```json
{
  "verdict": "yes",
  "attempt": 1,
  "summary": "All 10 expected paths covered; no missing state×action pairs.",
  "missing": [],
  "phantoms": [],
  "structural_errors": [],
  "fixes": [],
  "clarifications": []
}
```

Console output:

```
  OK Client Management | attempt 1/3 | 10 workflow(s)
```

---

## Stage 3 — Test Generation (Parallel)

Three agents run simultaneously for the "Client Management" module. All three receive the approved workflow list as a compact `<workflows>` block (built by `build_test_prompt()` in `agents/utils.py`):

```
<workflows>
WF-001 | View client | actor: <role> | branch: none | terminal: View | on_success: Client detail page opens
WF-002 | Deactivate Active client | actor: <role> | branch: entity_state == Active | terminal: Deactivate | on_success: Status badge updates to Inactive
...
</workflows>
```

### PositiveTestCaseGeneratorAgent

Produces 10 positive TCs — one covering every `wf_id`. Each TC references its workflow via `wf_ref`.

### NegativeTestCaseGeneratorAgent

Produces 6 negative TCs — e.g.:
- `WF-004`: Submit Create Client wizard with First Name missing → inline validation error shown, client not created.
- `WF-005`: Activate client with Activation Date before Submitted On → error toast, status remains Pending.

### EdgeTestCaseGeneratorAgent

Produces 4 edge TCs — e.g.:
- `WF-008`: Transfer client to the same office → blocked (spec says same-office transfer is not allowed).
- `WF-009`: Close client with an active loan account → error shown, closure rejected.

---

## Stage 4 — Finalize

All three result sets are merged. TC IDs are renumbered `TC-001` through `TC-020`:

- `TC-001` to `TC-010` — positive (`category=positive`, `wf_ref=WF-00x`)
- `TC-011` to `TC-016` — negative (`category=negative`)
- `TC-017` to `TC-020` — edge (`category=edge`)

Output files written:

```
outputs/test_generation/Mifos/openai-gpt-4o/
├── structural-model.json
├── structural-model-critique.json
├── workflows.json
├── workflow-validator-critique.json
├── test-cases.json
├── Mifos-openai-gpt-4o-critique.md
├── Mifos-openai-gpt-4o-workflow-validator-critique.md
└── Mifos-openai-gpt-4o-tests.md
```

---

## Escalation Paths

### `forced_ship` (max attempts reached)

If all 3 attempts are exhausted without a `yes` verdict, the orchestrator prints a severity-broken report and records `forced_ship=True`:

```
  !! Client Management | max attempts reached — ESCALATING
     | critical_missing=2 critical_phantoms=0 structural_errors=1
     MISSING  [critical] Create_Client_Wizard.steps[3]: Family Members step absent
     MISSING  [critical] Create_Client_Wizard.steps[4]: Identifiers step absent
     STRUCT   Create_Client_Wizard.submit_actions[0].on_success is generic ('success')
```

The final AST is still recorded in `structural-model.json` but `forced_ship=True` in the critique signals that it did not pass validation.

### `needs_clarification` (broken source text)

If the validator determines the description is genuinely unresolvable — not a generator failure — it returns `needs_clarification` and the loop stops immediately:

```
  ?? Client Management | attempt 1/3 | verdict=needs_clarification
     | 2 question(s) — source text is ambiguous, stopping
     CLARIFY  "The form submits to either the approval queue or directly activates"
              — unclear which path is the default and which requires a condition
     CLARIFY  "Step 3 is optional depending on configuration"
              — no spec-defined condition is given for when Step 3 is skipped
```

The module is recorded with `needs_clarification=True` and `clarifications[]`. All other modules continue processing normally.