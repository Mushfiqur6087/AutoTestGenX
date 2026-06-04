# Workflow Critique — Moodleteacher

Generated: 2026-06-04T14:33:52.568351Z

## Login

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow for the form's submit action 'Log in' is missing.

**Missing workflows:**

- No workflow for Login_Form: action=Log in

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Login_Form: action=Log in

---

## Dashboard

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for the Timeline block's dropdowns and search field.

**Missing workflows:**

- No workflow for Timeline_Block: action=Time_Range
- No workflow for Timeline_Block: action=Sort_Order
- No workflow for Timeline_Block: action=Search_Activities

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for Timeline_Block actions: Time_Range, Sort_Order, Search_Activities

---

## Dashboard — Edit Mode

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for existing block actions in the repeating group.

**Missing workflows:**

- No workflow for Existing_Blocks: action=configure
- No workflow for Existing_Blocks: action=move
- No workflow for Existing_Blocks: action=delete

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for Existing_Blocks actions: configure, move, delete

---

## My Courses

**Verdict:** yes  
**Forced ship:** no  

All workflows are present and correct for the actions defined in the AST.

**Missing workflows:** none

**Phantom workflows:** none

---

## Course Page

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for the 'Collapse all' action.

**Missing workflows:**

- No workflow for Collapse_All_Link: action=collapses all sections

**Phantom workflows:** none

**Fixes applied:**

- Add a workflow for Collapse_All_Link: action=collapses all sections

---

## Course Edit Mode and Activity Chooser

**Verdict:** yes  
**Forced ship:** no  

All workflows are present and correctly match the actions defined in the AST.

**Missing workflows:** none

**Phantom workflows:** none

---

## Assignment Creation

**Verdict:** yes  
**Forced ship:** no  

All workflows are present and correctly defined for the form's submit actions.

**Missing workflows:** none

**Phantom workflows:** none

---

## Course Settings

**Verdict:** yes  
**Forced ship:** no  

All workflows are present and correctly match the actions defined in the AST.

**Missing workflows:** none

**Phantom workflows:** none

---

## Participants Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions and state actions.

**Missing workflows:**

- No workflow for Filter_System: action=Apply Filters
- No workflow for Filter_System: action=Clear Filters

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for Filter_System actions: Apply Filters, Clear Filters

---

## Assignment — Teacher View

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow for the 'Grade' button is missing a matching submit action in the AST.

**Missing workflows:**

- No workflow for Assignment_Page: action=Grade_Button

**Phantom workflows:** none

**Fixes applied:**

- Add a workflow for Assignment_Page: action=Grade_Button

---

## Assignment Submissions

**Verdict:** yes  
**Forced ship:** no  

All required workflows are present and correctly defined.

**Missing workflows:** none

**Phantom workflows:** none

---

## Gradebook — Grader Report

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions and state actions.

**Missing workflows:**

- No workflow for form: action=Save Changes
- No workflow for state_bound_action_bar: state=Enabled, action=Save Changes

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for form: action=Save Changes
- Add workflow for state_bound_action_bar: state=Enabled, action=Save Changes

---

## Profile

**Verdict:** yes  
**Forced ship:** no  

All workflows are present and correctly mapped to the AST actions.

**Missing workflows:** none

**Phantom workflows:** none

---

## Profile Edit

**Verdict:** yes  
**Forced ship:** no  

All required workflows are present and correct.

**Missing workflows:** none

**Phantom workflows:** none

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

All workflows are accounted for and correctly defined.

**Missing workflows:** none

**Phantom workflows:** none

---
