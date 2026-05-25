# Semantic Critique — Moodleteacher

Generated: 2026-05-22T21:50:14.089535Z

## Login

**Verdict:** yes  
**Forced ship:** no  

The AST correctly captures the form fields, submit behavior (success and failure), the disabled 'Lost password?' link, and the guest and cookies buttons as described.

**Missing:** none

**Phantoms:** none

---

## Dashboard

**Verdict:** yes  
**Forced ship:** no  

AST includes all interactive elements from the description (timeline dropdowns, search, empty state; calendar filter, new event button, nav arrows, links) with no significant extraneous items.

**Missing:** none

**Phantoms:** none

---

## Dashboard — Edit Mode

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures all interactive elements from the description; only one minor inferred row action was added for adding a block.

**Missing:** none

**Phantoms (hallucinations):**

- Add_a_block_Page.row_actions[0] (Add action not explicitly named in the description)

---

## My Courses

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive controls (status, search, sort, layout), repeating course cards with clickable course name, and per-card menu actions (Star, Remove) matching the description.

**Missing:** none

**Phantoms:** none

---

## Course Page

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements: navigation tab bar, Collapse all link, repeating collapsible sections with a per-section toggle, and clickable activity/resource items.

**Missing:** none

**Phantoms:** none

---

## Course Edit Mode and Activity Chooser

**Verdict:** yes  
**Forced ship:** no  

AST correctly captures all interactive elements described (edit toggle, section/activity inline controls and menus, selection for bulk actions, add buttons, Activity Chooser with filters/search/tiles/favorites, and creation forms).

**Missing:** none

**Phantoms:** none

---

## Assignment Creation

**Verdict:** yes  
**Forced ship:** no  

AST accurately represents the interactive elements, panels, controls, conditional visibility/enabling, and submit actions described for the assignment creation form.

**Missing:** none

**Phantoms:** none

---

## Course Settings

**Verdict:** yes  
**Forced ship:** no  

The AST accurately captures all interactive elements, required validations, conditional logic (end-date toggle and format-dependent layout), collapsible panels, and the Save/Cancel actions described.

**Missing:** none

**Phantoms:** none

---

## Participants Management

**Verdict:** yes  
**Forced ship:** no  

The AST accurately represents the interactive elements from the description (scope dropdown, enrol button/dialog, filter builder with Any toggle and add-condition, alphabetical filters, table columns/row actions/bulk actions, and enrol dialog fields).

**Missing:** none

**Phantoms:** none

---

## Assignment — Teacher View

**Verdict:** yes  
**Forced ship:** no  

The AST correctly includes the Grade button (with its effect), a placeholder grading interface, and the tab bar with the five named tabs; no required interactive items from the description are missing.

**Missing:** none

**Phantoms:** none

---

## Assignment Submissions

**Verdict:** yes  
**Forced ship:** no  

AST is largely correct and includes the interactive filters, quick-grading toggle, table links, file/feedback link groups, and row action; the only minor omission is that the Final_Grade column lacks an explicit editable input type for quick grading.

**Missing:**

- Submissions_Table.columns.Final_Grade.type (should be an editable input field when Quick_Grading_Mode is enabled)

**Phantoms:** none

---

## Gradebook — Grader Report

**Verdict:** yes  
**Forced ship:** no  

AST includes the report-type selector, user search and group filter, per-column and per-cell actions, edit-mode toggle, inline-editable grade cells with range validation, and Save changes with blocking constraint — matching the description.

**Missing:** none

**Phantoms:** none

---

## Profile

**Verdict:** yes  
**Forced ship:** no  

The AST includes all interactive elements described (Message button, Edit profile link, data retention link, course/profile links, miscellaneous links, reports links) and correctly leaves passive displays out; no missing items or extraneous phantoms found.

**Missing:** none

**Phantoms:** none

---

## Profile Edit

**Verdict:** yes  
**Forced ship:** no  

AST correctly represents the described collapsible Edit profile form, fields, upload behavior, and actions with no critical omissions.

**Missing:** none

**Phantoms:** none

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the single interactive element (Log out button), its precondition, success behavior, and effect on authentication state.

**Missing:** none

**Phantoms:** none

---
