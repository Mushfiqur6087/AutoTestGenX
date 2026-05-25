# Workflow Critique — Moodlestudent

Generated: 2026-05-25T15:11:46.713534Z

## Login

**Verdict:** yes  
**Forced ship:** no  

All required workflows are present: the form submit action 'Log in' and the two standalone buttons are covered; no missing workflows or phantoms were detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Dashboard

**Verdict:** yes  
**Forced ship:** no  

Workflows cover all actionable elements in the AST (buttons, menus, links, and edit-mode conditional actions); no missing or phantom workflows were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## My Courses

**Verdict:** yes  
**Forced ship:** no  

The workflow list covers all interactive elements in the AST (toolbar fields, layout options, course link, and card menu actions); no missing or phantom workflows detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Course Page

**Verdict:** yes  
**Forced ship:** no  

Workflows correctly cover the interactive elements in the AST (collapse all link, per-section toggle, item navigation, and Edit mode preconditioned), with no missing or phantom workflows and no incorrect conditional branches or empty on_success where AST defines one.

**Missing workflows:** none

**Phantom workflows:** none

---

## Participants

**Verdict:** yes  
**Forced ship:** no  

All required workflows are present and match AST actions (form submit actions, data-table row action, and field on_change actions); no phantoms or incorrect conditional branches detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Grades

**Verdict:** yes  
**Forced ship:** no  

Workflow list is complete and correct: the single workflow matches the data_table's group header interaction and its on_success matches the AST.

**Missing workflows:** none

**Phantom workflows:** none

---

## Assignment

**Verdict:** yes  
**Forced ship:** no  

Workflows cover all form submit-action condition combinations and all state×action pairs; no phantom or incorrect conditional references were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Activities

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Workflows reference non-existent conditional fields (Forums_Section, Resources_Section, Activity_Type_Section); regenerate with corrected conditional branches or define those fields in the AST.

**Missing workflows:**

- WF-002 conditional_branch 'Forums_Section == collapsed' references no visible_when/required_when field or state key 'Forums_Section' in AST
- WF-003 conditional_branch 'Resources_Section == collapsed' references no visible_when/required_when field or state key 'Resources_Section' in AST
- WF-004 conditional_branch 'Activity_Type_Section == collapsed' references no visible_when/required_when field or state key 'Activity_Type_Section' in AST

**Phantom workflows:** none

**Fixes applied:**

- For WF-002: Either add a visible/required/state field named 'Forums_Section' to the AST (with possible values like 'collapsed'/'expanded'), or remove/replace the conditional_branch so it references an existing AST field or omit it if not needed.
- For WF-003: Either add a visible/required/state field named 'Resources_Section' to the AST (with possible values like 'collapsed'/'expanded'), or remove/replace the conditional_branch so it references an existing AST field or omit it if not needed.
- For WF-004: Either add a visible/required/state field named 'Activity_Type_Section' to the AST (with possible values like 'collapsed'/'expanded'), or remove/replace the conditional_branch so it references an existing AST field or omit it if not needed.

---

## Profile

**Verdict:** yes  
**Forced ship:** no  

All form submit actions and page actions are covered by workflows, no phantom workflows or invalid conditional branches were found, and on_success values are appropriate.

**Missing workflows:** none

**Phantom workflows:** none

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

The single workflow correctly covers the Logout_Button's 'Log out' action and its on_success behavior; no missing workflows or phantoms were found.

**Missing workflows:** none

**Phantom workflows:** none

---
