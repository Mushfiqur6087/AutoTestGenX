# Workflow Critique — Moodleteacher

Generated: 2026-05-25T15:32:10.514173Z

## Login

**Verdict:** yes  
**Forced ship:** no  

All required workflows are present and map to AST actions; no phantom workflows or incorrect conditional branches were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Dashboard

**Verdict:** yes  
**Forced ship:** no  

Workflows cover all interactive elements in the AST (timeline controls, calendar controls, and links); no missing or phantom workflows detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Dashboard — Edit Mode

**Verdict:** yes  
**Forced ship:** no  

Workflows cover all form submit actions (each block option and Cancel), all visible buttons/menus (Reset, + Add a block, move handle, Configure/Move/Delete), and conditional branches reference existing fields, so the list is complete and correct.

**Missing workflows:** none

**Phantom workflows:** none

---

## My Courses

**Verdict:** yes  
**Forced ship:** no  

All interactive elements in the AST (control bar fields, course link, and card menu actions) have corresponding workflows; no phantoms or conditional errors detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Course Page

**Verdict:** yes  
**Forced ship:** no  

All actions in the AST are represented by workflows, there are no phantom terminal actions, and no missing conditional/state/form workflows.

**Missing workflows:** none

**Phantom workflows:** none

---

## Course Edit Mode and Activity Chooser

**Verdict:** yes  
**Forced ship:** no  

The workflow list covers all submit/available actions in the AST, references valid conditional fields, contains no phantom terminal actions, and includes concrete on_success results.

**Missing workflows:** none

**Phantom workflows:** none

---

## Assignment Creation

**Verdict:** yes  
**Forced ship:** no  

Workflows cover all submit actions for every combination of visible conditions (File_submissions × Group_submissions), no phantom actions, and conditional branches reference real fields.

**Missing workflows:** none

**Phantom workflows:** none

---

## Course Settings

**Verdict:** yes  
**Forced ship:** no  

The workflow list is complete and correct: it covers both submit actions for all combinations of Enable_Course_End_Date, Course_Format, and Groups_Group_Mode, with no phantoms or invalid conditional references and concrete on_success values.

**Missing workflows:** none

**Phantom workflows:** none

---

## Participants Management

**Verdict:** yes  
**Forced ship:** no  

Workflows cover all form submit actions, data-table row and bulk actions, and UI controls described in the AST; no missing or phantom workflows detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Assignment — Teacher View

**Verdict:** yes  
**Forced ship:** no  

All required workflows present and correct for the interactive components in the AST.

**Missing workflows:** none

**Phantom workflows:** none

---

## Assignment Submissions

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Workflows must be regenerated because the conditional_branch expressions reference a field name ('Quick_Grading') that is not defined in the AST under the required locations (visible_when/required_when/state keys) and the checkbox actions/terminal action naming is inconsistent with the AST.

**Missing workflows:** none

**Phantom workflows:** none

**Fixes applied:**

- WF-002 and WF-003: Fix conditional_branch to reference a real field/key declared in the AST (e.g., change 'Quick_Grading == true/false' to reference 'Quick_Grading_Toggle' or add a concrete 'Quick_Grading' field entry under the AST with visible_when/required_when as appropriate).
- WF-002 and WF-003: Make terminal_action names explicit and aligned with AST or description (e.g., use 'Enable Quick Grading' and 'Disable Quick Grading' or add corresponding on_check/on_uncheck actions to the AST for the Quick_Grading_Toggle component).
- Submission_Filters form: If an apply/submit action exists in the UI, add submit_actions[] to the form in the AST and regenerate workflows so there is a workflow for the filter form's submit action; if not, ensure the AST explicitly indicates there is no submit action.

---

## Gradebook — Grader Report

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow list must be regenerated because WF-003's conditional_branch references a field name that does not match the AST (uses 'Edit_Mode_Toggle' vs AST's 'Edit_Mode'), so conditional names are inconsistent.

**Missing workflows:** none

**Phantom workflows:** none

**Fixes applied:**

- Update WF-003 conditional_branch to reference the AST's precondition name: change 'Edit_Mode_Toggle == true' to 'Edit_Mode == true', or alternatively make the AST use 'Edit_Mode_Toggle' consistently across enabled_when and preconditions.
- Regenerate workflows ensuring all conditional_branch expressions use field/state identifiers that appear verbatim in the AST (e.g., align workflows with Grades_Table.cell_field_spec.enabled_when and Save_Changes_Action.preconditions).

---

## Profile

**Verdict:** yes  
**Forced ship:** no  

Workflows cover all actionable AST fields (buttons and links); no missing or phantom workflows detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Profile Edit

**Verdict:** yes  
**Forced ship:** no  

Workflows cover both form submit actions (Update profile, Cancel); no missing workflows, phantoms, or conditional/state/data-table issues detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

The single workflow correctly covers the Logout button action and its on_success behavior; no missing workflows or phantoms were found.

**Missing workflows:** none

**Phantom workflows:** none

---
