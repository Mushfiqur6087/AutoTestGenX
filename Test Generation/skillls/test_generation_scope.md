# Test Generation Scope — What AutoTestGenX Produces (and What It Does Not)

This skill documents the actual test-generation surface of the AutoTestGenX pipeline
as it operates against the raw functional descriptions in `dataset/raw_specifications/`
(Moodle Teacher / Student, Mifos, PHPTravels, Parabank, SwagLab).

The pipeline runs eight agents in four stages: a **module context** is synthesized globally, a **structural model** (AST) is
extracted from the spec, **workflows** are enumerated from the AST, then three
parallel test generators (positive / negative / edge) produce JSON test cases
referencing the workflows via `wf_ref`.

---

## 1. The System Under Test — What the Input Describes

Every raw specification is a **single web application's natural-language UI
specification**. It describes pages, forms, buttons, tables, dialogs, tabs,
state-bound action bars, and validation rules at the level a manual tester would
read. It does **not** contain:

- Server-side architecture, APIs, or database schemas
- Non-functional requirements (performance, load, security)
- Mobile or native client behavior (everything is browser-based)
- Backend integrations (payment gateways, email delivery, SSO, etc.)

The system under test is therefore **a single web UI module's interactive
surface, exercised by one user at a time, in a browser**.

---

## 2. What IS Generated

All three generators consume the same per-module inputs:
- the **AST** (UI component tree with `form`, `wizard`, `data_table`,
  `tab_container`, `state_bound_action_bar`, `repeating_group` nodes)
- the **original functional description**
- the **workflow list** (`WF-001…WF-NNN`) with `conditional_branch` and
  `on_success`

Every test case is emitted as JSON with `tc_id`, `wf_ref`, `preconditions`,
`steps`, `expected_result`, and `priority`. Below is what each category covers.

### 2.1 Positive / Functional Tests (`positive_test_case_generator.py`)

Generated happy-path tests, one per distinct success outcome:

| AST node | Positive coverage |
|---|---|
| `form` | One happy path per `on_success`; one extra per `visible_when` branch; one per `submit_actions[]` button if they lead to different outcomes |
| `wizard` | One happy path that traverses all steps; one **dedicated** TC per step beyond Step 1 that has its own named field group (e.g., "Address Details", "Family Members") |
| `state_bound_action_bar` | One TC per `available_actions` entry per state; precondition = that state |
| `tab_container` | One navigation TC across all tabs; **OR** one submission TC per tab if tabs switch between entirely different forms |
| `data_table` | One TC per `row_actions`; one per `bulk_actions`; one applying a search/filter that asserts the **filtered content**; one removing a single filter chip; one clicking "Reset All" / "Clear Filters" |
| `repeating_group` | Step pattern "Click Add Row" → fill `item_fields` |
| Action dialogs opened from a state-bound action | One positive TC per dialog (e.g., Activate requires Activation Date, Reject requires Reason) — distinct from the state-transition TC |
| Empty / zero-result states explicitly described in the spec | One TC reaching that state through a valid user action and asserting the empty-state message |
| Role-specific views (tab/button visible to one role but not another) | One TC asserting the element's presence for the role that should see it |

**Coverage Completeness Gate:** every action verb in the spec (e.g., "Approve,
Reject, Withdraw, Disburse, Waive Interest, Write Off, Reschedule") must be
covered by at least one positive TC, even if the AST is missing the node — the
description is trusted.

### 2.2 Negative / Failure-Injection Tests (`negative_test_case_generator.py`)

Workflow-aware failure-mode tests. Generated for **every workflow's
conditional_branch** plus deduplicated field-level and cross-cutting checks:

| Negative coverage | When generated |
|---|---|
| Required field blank-and-submit, **deduplicated by field type** (text, email, password, number, date, dropdown, file_upload) | Any form with `required: true` fields |
| All-required-fields-empty submit | Any form with 2+ required fields |
| Format violation per format-relevant field | Field is `email`, `number`, `date`, or `password` and the spec/AST implies format validation |
| Numeric bound violation | Spec describes min/max amounts or balance checks |
| Unique / match / not-same-as-current constraint violation | Each unique `constraints[]` entry |
| Cross-field date/numeric ordering rule violation | Spec describes "X must be after Y" or similar |
| Pre-existing system-state constraint | "cannot close with active accounts", "cannot transfer to the same office" — generates **two** TCs: the standard violation plus a constraint-timing test (block-on-open vs block-on-submit) |
| Unauthenticated access | Any page/action requiring login |
| Wrong-role access | Spec explicitly restricts a feature to a role (e.g., Teacher only) |
| Wrong-state action | For each state in `state_bound_action_bar.states`, at least one action **not** in `available_actions` is attempted |
| Empty `available_actions` state | One TC asserting no action buttons are visible in that state |
| Action-dialog required field blank | **Per action dialog**, not deduplicated against main form blank-field tests |

**Hard exclusions for negative tests** (explicit in the prompt's SCOPE GATE):
backend data integrity, security vulnerabilities, infrastructure failures,
race conditions, anything not described in the spec.

### 2.3 Edge / Boundary Tests (`edge_test_case_generator.py`)

Tests at the limits of valid/invalid input, with a `subcategory` field of
`boundary | input_edge | interaction_edge | state_edge | data_edge`:

| Subcategory | Generated when | Examples |
|---|---|---|
| `boundary` | AST `constraints[]` has a numeric/date/count threshold OR description names one | min value passes / one unit below fails; max entries passes / one more fails; date A = date B passes / date A = date B − 1 day fails; range endpoints on both ends (up to 4 tests per constraint) |
| `input_edge` | Any free-text, number, or date field | long text (200+ chars); special characters / emoji / unicode; leading/trailing whitespace; zero when minimum > 0; decimal precision beyond field support |
| `interaction_edge` | Component types present in AST | browser back after successful form redirect (rapid re-submission); wizard step-skip enforced navigation; wizard step-skip free navigation; repeating-group add-then-remove-all |
| `state_edge` | `state_bound_action_bar` present | rapid consecutive state transitions |
| `data_edge` | `date` or `file_upload` fields present | today / yesterday / far future dates; Feb 29 leap-year (free-text entry only — skipped if a calendar picker is used); file exactly at size limit; file one byte over limit |

**RELEVANCE RULE** is hard: a login form does not get repeating-group edge
tests; a data table does not get wizard-skip tests. If the module has no
constraints, no `repeating_group`, no `date`/`number`/`file_upload` fields, and
no `state_bound_action_bar`, only 1–3 generic input-edge tests are produced
and the generator stops.

**MINIMUM OUTPUT RULE:** if the module has any numeric/date/count threshold,
at least 2 boundary tests must be produced — zero is a generation failure.

### 2.4 Coverage Obligations Carried by the Workflows Block

When the `<workflows>` block is present, every Stage 3 generator enforces a
specific obligation:

- **Positive** — collectively covers every `wf_id`; each TC carries a
  `wf_ref` (or `null` for navigation-only tests).
- **Negative** — for each workflow whose terminal action is a submit/save/
  create/approve, identifies the most critical blocking failure for that
  workflow's `conditional_branch` and adds one negative TC **only if** it
  catches a bug not already covered by another workflow's negative test.
- **Edge** — for each workflow where `conditional_branch` activates a
  numeric or date field, confirms or adds a boundary edge TC for it.

---

## 3. What is NOT Generated

The pipeline deliberately stays inside a single module's UI surface. The
following categories are out of scope:

### 3.1 Multi-Module / Cross-Page Journeys

- **No end-to-end (E2E) flows across modules.** A test ends with the assertion
  that a cross-module redirect occurred; it does not interact with the next
  page.
- **No multi-actor flows.** If a downstream action requires a different user
  (e.g., a Checker approving a Maker's entry), the second user's actions are
  not included.
- **No backend result verification.** Submitting a form that triggers a
  downstream effect is asserted only by the immediate visible UI change on
  the current page, not by inspecting the downstream entity.

### 3.2 Non-UI / Out-of-Browser

- **No backend data integrity checks** (DB state, transaction consistency,
  audit trails).
- **No API-level tests** (REST endpoints, GraphQL, direct database writes).
- **No security / vulnerability tests** (XSS, SQL injection, CSRF, auth
  bypass, session fixation, privilege escalation beyond the wrong-role UI
  check).
- **No performance / load / stress tests** (response time, concurrent users,
  throughput, memory).
- **No infrastructure / DevOps tests** (failover, network partitioning,
  container restarts, DB connection pool exhaustion).
- **No concurrency / race-condition tests** (two users editing the same
  record simultaneously).
- **No accessibility audits** (WCAG, screen-reader behavior, color-contrast
  ratios, keyboard-only navigation completeness) — beyond what is described
  in the raw spec as visible UI behavior.
- **No localization / i18n tests** (locale-specific date/number formats,
  RTL layouts, translated strings) unless explicitly stated in the spec.
- **No cross-browser / cross-device parity tests** (Chrome vs Firefox,
  desktop vs mobile responsive behavior).
- **No email / SMS / push-notification delivery verification** unless the
  notification's on-screen rendering is part of the current module.

### 3.3 Tests That Require Non-Standard Tools

The negative and edge prompts both enforce a "UI-executable" scope gate. The
following are excluded because a tester cannot trigger them through clicking,
typing, selecting, or navigating in a browser:

- Dev-tools / DOM-inspection assertions
- Server-side error simulation
- API-call verifications
- Concurrent-user scenarios
- Network throttling / offline mode (unless the spec explicitly describes
  the offline UI behavior)

### 3.4 Tests That Are Display-Only Behavior

- A negative TC that just asserts "the page shows X" is rejected as
  "positive in disguise." Display-only modules get at most 1–2 negative TCs
  (unauthenticated access, or a non-implemented link if the spec describes
  one).

### 3.5 Invented / Speculative Behavior

- **No specific data values** are invented in steps or preconditions. All
  values use generic placeholders (`<valid email>`, `<amount exceeding
  available balance>`) unless the spec mandates a hardcoded system value
  (e.g., "Select 'Card' layout", `"$25 minimum"`).
- **No boundary values invented** beyond what the constraint structurally
  implies (`<minimum value>`, `<one unit below minimum>`, never `'500.00'`).
- **No format errors for fields where the spec does not imply format
  validation** (e.g., no email-format test for a field whose `type` is
  `text/unspecified` and which has no format constraint in the spec).
- **No phantom components** — components that appear only in the AST
  validator's `phantoms[]` list are excluded by Stage 1 before Stage 3 ever
  sees them. Components that appear in the spec but not in the AST are
  included by the positive Coverage Completeness Gate.

---

## 4. Granularity and Style Rules That Shape Output

These are not test categories — they are constraints that determine the
shape of every TC that *is* produced.

- **STRICT MODULE BOUNDARY:** each TC is a "unit test for the UI." It tests
  only the module provided. Cross-module redirects terminate the test.
- **One atomic action per step.** No grouping ("Fill the form and submit"
  is banned).
- **Preconditions vs. steps boundary:** "Ensure X is open" / "Verify Y
  shows Z" are preconditions, not steps. If a precondition says a dialog is
  open, there must be a step that opens it.
- **Generic data rule:** `<placeholder>` style only; no invented concrete
  values.
- **Verbatim quoting:** when the spec quotes an exact success message
  (`"Account opened successfully!"`) or error string
  (`"Incorrect email or password. Please try again."`), it is copied
  character-for-character into `expected_result`.
- **Assert the visible UI change, not the action.** `expected_result`
  names the row, badge, notification, or filtered list that a tester sees —
  it does not restate "creates X" or "updates Y."
- **Hard step cap:** 15 steps per TC. If exceeded, split at the first
  sub-feature boundary into separate TCs.
- **No banned patterns:** `"creates/updates/deletes [entity]"`, `"[system]
  adjusts/recalculates automatically"`, `"when X, result A; when Y, result
  B"` in a single TC, `"a success message is displayed"` when the spec
  quotes the exact text, `"filter is applied"` without describing filtered
  content.
- **Deduplication gates** in each generator (positive: same code path →
  merge; negative: same field type → one representative, but action-dialog
  required fields are never deduplicated against main-form blanks; edge:
  relevance-rule before generating).

---

## 5. Calibration Targets (Tests Per Module)

The prompts specify rough test-count targets by module complexity, applied
**after** the deduplication and scope gates:

| Category | Simple module | Medium module | Complex module |
|---|---|---|---|
| Positive | 2–4 | 4–8 | 8–15 |
| Negative | 2–4 | 4–8 | 10–16 |
| Edge | 2–4 | 4–8 | 6–10 |

State-machine modules with 4+ states produce 4–5 negative state-violation TCs
even on otherwise simple modules — that is expected and not deduplicated
away.

---

## 6. Worked Example: MoodleTeacher `Assignment Creation`

The spec describes a wizard with collapsible panels (General, Availability,
Submission types, Feedback types, etc.), conditional reveals (enabling File
submissions reveals max files / max size / file types), three submit
buttons (`Save and return to course`, `Save and display`, `Cancel`), and
inline validation.

**Generated (representative, not exhaustive):**

- **Positive:** one happy path per submit button (3), one per conditional
  branch (File submissions enabled), one for each required panel with named
  field groups, role-specific view (Teacher sees Assignment creation; Student
  does not).
- **Negative:** one blank-text-field representative, one blank-date-field
  representative, one invalid email format, one date A before date B
  violation, one file size exceeded, one file type rejected, one required
  toggled sub-field blank (e.g., max submission size when File submissions
  is enabled).
- **Edge:** boundary at minimum/maximum submission size (passes / fails),
  boundary at maximum number of files, long Description text input edge,
  File submissions toggle boundary (zero files vs one vs max+1), leap-year
  date for Due date (free-text entry only), browser-back rapid re-submission
  after `Save and return to course`.

**Not generated:** end-to-end flow that creates an assignment → logs in as a
student → submits → returns to teacher to grade; backend verification that
the assignment row exists in the DB; performance of the rich-text editor;
mobile-rendering parity; WCAG conformance of the panels.

---
