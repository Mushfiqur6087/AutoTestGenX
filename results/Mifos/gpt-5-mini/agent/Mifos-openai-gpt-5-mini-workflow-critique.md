# Workflow Critique — Mifos

Generated: 2026-05-25T14:33:08.705374Z

## Login

**Verdict:** yes  
**Forced ship:** no  

Workflows cover the form submit (Login) and the Forgot Password link with correct conditions and on_success actions; no missing or phantom workflows detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Home Page

**Verdict:** yes  
**Forced ship:** no  

Workflows cover all interactive elements in the AST (Search_Activity and Dashboard); no missing or phantom workflows detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Dashboard

**Verdict:** yes  
**Forced ship:** no  

The provided workflow covers the Dashboard button navigation and matches the AST; no missing workflows or phantom terminal actions were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Global Search

**Verdict:** yes  
**Forced ship:** no  

Workflows cover the launcher (Search Icon), result selection (Select), and the no-results path; no missing or phantom workflows detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Client Management

**Verdict:** yes  
**Forced ship:** no  

Workflows cover all form submit actions, state-bound actions for each state, data table row actions, and identifier item actions; no phantoms or incorrect conditional branches detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Group Management

**Verdict:** yes  
**Forced ship:** no  

All required workflows for forms, state-bound actions, and data-table actions are present; no phantom workflows or incorrect conditional branches detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Center Management

**Verdict:** yes  
**Forced ship:** no  

All required workflows are present and consistent with the AST; no missing state/form/table workflows or phantom terminal actions were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Loan Products

**Verdict:** yes  
**Forced ship:** no  

The workflow list is complete and correct: all AST actions (Create button, table Open, detail Edit, Add/Remove charge) are covered with matching terminal_action and on_success values; no missing workflows or phantom actions detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Savings Products

**Verdict:** yes  
**Forced ship:** no  

Workflows cover the data table View action and the Create Savings Product button; no missing or phantom workflows detected against the AST.

**Missing workflows:** none

**Phantom workflows:** none

---

## Share Products

**Verdict:** yes  
**Forced ship:** no  

All required workflows are present and valid: submit actions, data table row actions, and conditional branches are covered; no phantoms or incorrect conditional references detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Charges

**Verdict:** yes  
**Forced ship:** no  

Workflows cover all form submit actions, data-table actions, and detail view actions with valid conditional branches and no phantom or empty-on-success workflows.

**Missing workflows:** none

**Phantom workflows:** none

---

## Floating Rates

**Verdict:** yes  
**Forced ship:** no  

All form submit actions, data table row actions, and action-bar actions are represented; no phantom terminal actions or incorrect conditional branches were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Delinquency Management

**Verdict:** yes  
**Forced ship:** no  

All required workflows for forms and table link actions are present; no phantom terminal actions or incorrect conditional branches were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Loan Account

**Verdict:** yes  
**Forced ship:** no  

All required workflows for wizard submit, state-bound actions, data-table row actions, and UI buttons/links are present; no phantom workflows or incorrect conditional branches were detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Savings Account

**Verdict:** yes  
**Forced ship:** no  

Workflows cover all form submit and state-bound actions; no missing workflows, phantoms, or invalid conditional branches detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Share Account

**Verdict:** yes  
**Forced ship:** no  

All required workflows are present and correctly map to the form submit action and each state-bound action; no phantom workflows or incorrect conditional branches detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Fixed & Recurring Deposit Accounts

**Verdict:** yes  
**Forced ship:** no  

All form submit actions and action-bar available actions in the AST are represented by workflows; no phantom terminal actions or invalid conditional branches were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Accounting — Chart of Accounts

**Verdict:** yes  
**Forced ship:** no  

All required workflows are present and consistent with the AST; no missing form/state/table workflows, phantoms, or conditional/on_success errors were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Accounting — Journal Entries & Closures

**Verdict:** yes  
**Forced ship:** no  

All form submit actions in the AST have matching workflows; no phantom terminal actions or invalid conditional branches were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Accounting Rules & Financial Activity Mappings

**Verdict:** yes  
**Forced ship:** no  

All required workflows for form submits, data table row actions, and detail view actions are present and match AST actions; no phantoms or incorrect conditional branches detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Provisioning

**Verdict:** yes  
**Forced ship:** no  

All required workflows are present and match the AST actions; no missing state/form/table actions, phantoms, or conditional/state mismatches detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Offices

**Verdict:** yes  
**Forced ship:** no  

The workflow list matches the AST: create button, office name link, and edit button workflows are present; no missing or phantom workflows detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Employees

**Verdict:** yes  
**Forced ship:** no  

All form submit actions, the data-table row action, and the detail-page Edit action are covered; no phantom workflows or incorrect conditional branches detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Teller & Cashier Management

**Verdict:** yes  
**Forced ship:** no  

All form submit actions, data-table row actions, and page actions are covered by workflows; no phantom workflows or conditional/on_success issues found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Users & Roles

**Verdict:** yes  
**Forced ship:** no  

Workflows cover all submit, row, and top actions present in the AST; no phantoms or conditional errors found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Reports

**Verdict:** yes  
**Forced ship:** no  

All required workflows are present and match the AST actions (form submit and result output options); no missing or phantom workflows detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Account Transfers & Standing Instructions

**Verdict:** yes  
**Forced ship:** no  

All form submit actions and data table row actions have matching workflows; no phantoms or incorrect conditional branches found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Tax Management

**Verdict:** yes  
**Forced ship:** no  

All form submit actions, table row actions, and toolbar actions in the AST are represented by workflows; no phantom terminal actions or incorrect conditional branches were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Organization Settings

**Verdict:** yes  
**Forced ship:** no  

All required workflows for the AST's form submit actions, page selection, and bulk import download/upload actions are present; no phantoms or incorrect conditional branches detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## System Administration

**Verdict:** yes  
**Forced ship:** no  

All required workflows for forms, data tables, and actions are present and match the AST; no phantom workflows or incorrect conditional branches were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Logout

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Workflows must be regenerated because the conditional_branch in both workflows references a non-supported AST key ('preconditions') rather than a visible/required field or state.

**Missing workflows:** none

**Phantom workflows:** none

**Fixes applied:**

- Fix conditional_branch for WF-001: "User_Profile_Menu.trigger.preconditions == 'user must be logged in'" — 'preconditions' is not a visible_when/required_when field or a state key; remove or replace with a valid condition (e.g., user.is_authenticated == true) or omit conditional_branch.
- Fix conditional_branch for WF-002: "User_Profile_Menu.trigger.preconditions == 'user must be logged in'" — 'preconditions' is not a visible_when/required_when field or a state key; remove or replace with a valid condition (e.g., user.is_authenticated == true) or omit conditional_branch.

---
