# Workflow Critique — Phptravels

Generated: 2026-05-25T14:55:02.785108Z

## Home Page & Search

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Workflows reference components.Search_Widget.active_tab in conditional_branch but the AST does not define an active_tab field, visible_when/required_when conditions, or state keys — conditional branches are invalid and must be corrected.

**Missing workflows:**

- Wrong conditional branch in WF-001: conditional 'components.Search_Widget.active_tab == "Hotels"' references a field/state not present in AST
- Wrong conditional branch in WF-002: conditional 'components.Search_Widget.active_tab == "Flights"' references a field/state not present in AST
- Wrong conditional branch in WF-003: conditional 'components.Search_Widget.active_tab == "Tours"' references a field/state not present in AST
- Wrong conditional branch in WF-004: conditional 'components.Search_Widget.active_tab == "Cars"' references a field/state not present in AST

**Phantom workflows:** none

**Fixes applied:**

- WF-001: Update/regenerate workflow to use a conditional that references a real AST field/state (e.g., add components.Search_Widget.active_tab to the AST with values ["Hotels","Flights","Tours","Cars"]) or remove the conditional_branch and encode tab-specific success via on_success_by_tab.
- WF-002: Update/regenerate workflow to use a conditional that references a real AST field/state (e.g., add components.Search_Widget.active_tab to the AST with values ["Hotels","Flights","Tours","Cars"]) or remove the conditional_branch and encode tab-specific success via on_success_by_tab.
- WF-003: Update/regenerate workflow to use a conditional that references a real AST field/state (e.g., add components.Search_Widget.active_tab to the AST with values ["Hotels","Flights","Tours","Cars"]) or remove the conditional_branch and encode tab-specific success via on_success_by_tab.
- WF-004: Update/regenerate workflow to use a conditional that references a real AST field/state (e.g., add components.Search_Widget.active_tab to the AST with values ["Hotels","Flights","Tours","Cars"]) or remove the conditional_branch and encode tab-specific success via on_success_by_tab.

---

## User Registration

**Verdict:** yes  
**Forced ship:** no  

The workflow list covers the form submit action for Register and matches the AST; no missing workflows, phantom actions, conditional-branch errors, or on_success mismatches were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## User Login

**Verdict:** yes  
**Forced ship:** no  

All required workflows are present and correctly map to the AST actions and conditions; no phantom workflows or incorrect conditional branches were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Forgot Password

**Verdict:** yes  
**Forced ship:** no  

All form submit actions in the AST have matching workflows, there are no phantom terminal actions or incorrect conditional branches, and on_success values are concrete.

**Missing workflows:** none

**Phantom workflows:** none

---

## Hotels Search & Listing

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Workflows contain phantom/invalid terminal actions and conditional branches that reference fields not present in the AST; regenerate after fixing AST or workflows.

**Missing workflows:**

- Wrong conditional branch: Sort_Control.selected == Price: Low to High (field 'Sort_Control.selected' is not defined in AST visible_when/required_when or as a state key)
- Wrong conditional branch: Sort_Control.selected == Price: High to Low (field 'Sort_Control.selected' is not defined in AST visible_when/required_when or as a state key)
- Wrong conditional branch: Sort_Control.selected == Star Rating (field 'Sort_Control.selected' is not defined in AST visible_when/required_when or as a state key)
- Wrong conditional branch: Sort_Control.selected == Guest Rating (field 'Sort_Control.selected' is not defined in AST visible_when/required_when or as a state key)
- Wrong conditional branch: Active_Filters_Summary.item_count > 0 (field 'Active_Filters_Summary.item_count' is not defined in AST visible_when/required_when or as a state key)

**Phantom workflows:**

- WF-002 terminal_action=Sort by not found in AST submit_actions/available_actions/row_actions/bulk_actions or description
- WF-003 terminal_action=Sort by not found in AST submit_actions/available_actions/row_actions/bulk_actions or description
- WF-004 terminal_action=Sort by not found in AST submit_actions/available_actions/row_actions/bulk_actions or description
- WF-005 terminal_action=Sort by not found in AST submit_actions/available_actions/row_actions/bulk_actions or description

**Fixes applied:**

- WF-002, WF-003, WF-004, WF-005: Remove or regenerate these workflows because their terminal_action 'Sort by' is not declared as an actionable item in the AST; either (a) update the AST to list explicit actions for the Sort_Control (e.g., a submit_actions/available_actions entry per sort option) or (b) change the workflows to use terminal_action values that match AST-declared actions (or represent selecting a dropdown option in a consistent AST action list).
- All workflows using conditional_branch expressions that reference UI state (Sort_Control.selected, Active_Filters_Summary.item_count): Update the AST to expose those fields under visible_when/required_when or as explicit state keys, or remove/replace the conditional_branch in the workflows with conditions that reference fields actually present in the AST. Specifically add a definable field for Sort_Control.selected or an explicit state for active filters count if you intend to keep those conditions.
- WF-006 and WF-007: Adjust conditional_branch 'Active_Filters_Summary.item_count > 0' to reference a real AST field or remove the condition; the actions themselves ('Remove Filter' and 'Reset all') are present in the AST but their condition references an undefined field.
- After updating the AST or workflows as above, regenerate the workflows so each workflow's terminal_action and conditional_branch align with the AST.

---

## Hotel Details & Booking

**Verdict:** yes  
**Forced ship:** no  

All required workflows are present and valid: form submit action 'Book Now' and data_table row action 'Select Room' each have matching workflows, conditional branch references an existing field, and no phantom or empty-on_success workflows were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Flights Search & Listing

**Verdict:** yes  
**Forced ship:** no  

Workflows cover the form submit (Search) and both data table row actions (Select, Expand); no missing or phantom workflows detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Flight Booking

**Verdict:** yes  
**Forced ship:** no  

The workflow list covers the form's submit action (Continue) with correct on_success and no phantom or invalid conditional workflows detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Tours Search & Listing

**Verdict:** yes  
**Forced ship:** no  

The single workflow covers the Tours_Search_Form 'Search' submit action and no other form submit_actions, state-bound actions, or table actions exist in the AST, so the list is complete and correct.

**Missing workflows:** none

**Phantom workflows:** none

---

## Tour Details & Booking

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Two workflows reference a conditional_branch ('user must be logged in') that is not a defined visible/required field or state in the AST; regenerate with corrected conditional references.

**Missing workflows:**

- Wrong conditional branch: WF-001 conditional_branch='user must be logged in' does not reference any visible_when/required_when field or state key in the AST
- Wrong conditional branch: WF-003 conditional_branch='user must be logged in' does not reference any visible_when/required_when field or state key in the AST

**Phantom workflows:** none

**Fixes applied:**

- Update WF-001 (Book Now authenticated) conditional_branch to reference a real AST condition: either add a concrete condition (e.g., add a 'user_logged_in' visible/required field or a state in a state_bound_action_bar) or set conditional_branch to null and represent the login-failure path explicitly via a separate workflow using the submit_action's on_failure.
- Update WF-003 (Submit Booking authenticated) conditional_branch to reference a real AST condition: either add a concrete condition (e.g., add a 'user_logged_in' visible/required field or a state in a state_bound_action_bar) or set conditional_branch to null and represent the login-failure path explicitly via a separate workflow using the submit_action's on_failure.

---

## Cars Search & Listing

**Verdict:** yes  
**Forced ship:** no  

The workflow list correctly covers the form submit action and the listing row action; no missing or phantom workflows were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Car Booking

**Verdict:** yes  
**Forced ship:** no  

All required workflows are present and valid: the Confirm Booking workflow matches the form's submit_action, references an existing field condition, and has the correct on_success.

**Missing workflows:** none

**Phantom workflows:** none

---

## Visa Services

**Verdict:** yes  
**Forced ship:** no  

All required workflows are present and correctly map to the AST actions; no phantom workflows or conditional/on_success issues were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## User Dashboard

**Verdict:** yes  
**Forced ship:** no  

All form submit actions, state×action pairs, and data-table row actions in the AST have matching workflows; no phantom terminal actions or incorrect conditional branches were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Booking Management

**Verdict:** yes  
**Forced ship:** no  

All required workflows are present and correct: each state 'default' action (Modify, Cancel) has a matching workflow with the correct conditional branch and concrete on_success, with no phantom workflows or conditional errors.

**Missing workflows:** none

**Phantom workflows:** none

---

## Payment Processing

**Verdict:** yes  
**Forced ship:** no  

All form submit actions and confirmation-page actions are represented; conditional branches reference valid fields and there are no phantom workflows or empty on_success values.

**Missing workflows:** none

**Phantom workflows:** none

---

## Currency & Language Selection

**Verdict:** yes  
**Forced ship:** no  

All on-change actions for both Currency and Language selectors are represented (including auth vs unauth branches and Arabic layout handling), no phantom terminal actions, and on_success values match the AST.

**Missing workflows:** none

**Phantom workflows:** none

---

## Search & Filters

**Verdict:** yes  
**Forced ship:** no  

Workflows cover all filter fields, conditional listing-specific filters, reset/remove actions, and sorting; no missing or phantom workflows detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Reviews & Ratings

**Verdict:** yes  
**Forced ship:** no  

Workflows cover the review submission form (both visible_when branches) and the two entry actions; no missing or phantom terminal actions detected and conditional branches reference real fields.

**Missing workflows:** none

**Phantom workflows:** none

---

## Offers & Deals

**Verdict:** yes  
**Forced ship:** no  

All form submit actions and promotion item actions are represented by workflows; no phantom workflows, incorrect conditional branches, or empty on_success values were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

All required workflows present and correct: the Authenticated state has a Logout workflow matching the state-bound action, no phantom actions, and the on_success matches the AST.

**Missing workflows:** none

**Phantom workflows:** none

---
