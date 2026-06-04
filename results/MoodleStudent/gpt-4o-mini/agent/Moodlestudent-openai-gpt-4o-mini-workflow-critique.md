# Workflow Critique — Moodlestudent

Generated: 2026-06-04T14:37:59.763678Z

## Login

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions.

**Missing workflows:**

- No workflow for Login_Form: action=Log in

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Login_Form: action=Log in

---

## Dashboard

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form actions in the Timeline block.

**Missing workflows:**

- No workflow for Timeline_Block: action=Sort Order
- No workflow for Timeline_Block: action=Time Range

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for Timeline_Block: action=Sort Order
- Add workflows for Timeline_Block: action=Time Range

---

## My Courses

**Verdict:** yes  
**Forced ship:** no  

All workflows are present and correctly defined.

**Missing workflows:** none

**Phantom workflows:** none

---

## Course Page

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for activities and resources in sections.

**Missing workflows:**

- No workflow for Sections: action=View Activities and Resources

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Sections: action=View Activities and Resources

---

## Participants

**Verdict:** yes  
**Forced ship:** no  

All workflows are present and correctly defined based on the AST.

**Missing workflows:** none

**Phantom workflows:** none

---

## Grades

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for row actions in the data table.

**Missing workflows:**

- No workflow for data_table: row_action=View for Course Name 1
- No workflow for data_table: row_action=View for Course Name 2

**Phantom workflows:** none

**Fixes applied:**

- Generate workflows for missing row actions in the Grades_Table.

---

## Assignment

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions.

**Missing workflows:**

- No workflow for Submission_Form: action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add a workflow for Submission_Form: action=Submit

---

## Activities

**Verdict:** yes  
**Forced ship:** no  

All workflows are accounted for and correctly defined.

**Missing workflows:** none

**Phantom workflows:** none

---

## Profile

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions.

**Missing workflows:**

- No workflow for Profile_Form: submit_action=Update Profile

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Profile_Form: submit_action=Update Profile

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

All checks passed with no missing workflows or phantoms.

**Missing workflows:** none

**Phantom workflows:** none

---
