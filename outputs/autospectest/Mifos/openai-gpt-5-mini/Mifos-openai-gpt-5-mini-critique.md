# Semantic Critique — Mifos

Generated: 2026-05-25T14:33:08.684030Z

## Login

**Verdict:** yes  
**Forced ship:** no  

AST accurately represents the interactive elements, validation, and submission behaviors; only a single minor inferred action (Forgot Password link navigation) was added.

**Missing:** none

**Phantoms (hallucinations):**

- Authentication_Interface.links[0].on_click (navigates to Forgot Password page not specified in description)

---

## Home Page

**Verdict:** yes  
**Forced ship:** no  

AST correctly represents the interactive elements (Search Activity field and Dashboard button) and the login precondition; no missing or extraneous interactive items found.

**Missing:** none

**Phantoms:** none

---

## Dashboard

**Verdict:** yes  
**Forced ship:** no  

The AST correctly captures the interactive elements (Home 'Dashboard' button, 'Search Activity' field, and the 'Client Trends' chart with legends and office binding); the summary cards are passive displays and may be omitted.

**Missing:** none

**Phantoms:** none

---

## Global Search

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements (search launcher, input, real-time grouped results with name/identifier/status, navigation on select, and no-results message) and the stated constraints.

**Missing:** none

**Phantoms:** none

---

## Client Management

**Verdict:** yes  
**Forced ship:** no  

The AST accurately captures all interactive elements, actions, wizard steps, filters, search targets, import flows, state-bound actions, and tabs described; no critical items are missing.

**Missing:** none

**Phantoms:** none

---

## Group Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

AST introduces state-bound conditional actions and embedded preconditions/fields that are not specified in the description (phantoms); regenerate with simpler action definitions or explicit conditional triggers in the description.

**Missing:** none

**Phantoms (hallucinations):**

- Group_Detail_Page.Group_Action_Bar (state_bound_action_bar with explicit states and state-specific available_actions) — description only lists action buttons, it does not specify state-dependent availability.
- Group_Detail_Page.Group_Action_Bar.states.*.*.preconditions (e.g., 'status must be Pending') — preconditions/availability per-state were not specified in the description.
- Group_Detail_Page.Group_Action_Bar.states.*.available_actions[].fields.Staff (Assign Staff contains an embedded required Staff field) — the description only names the Assign Staff action, it does not describe the action UI or required fields.

**Fixes applied:**

- Replace Group_Detail_Page.Group_Action_Bar (state_bound_action_bar) with a simple action_bar listing actions: Activate, Edit, Close, Assign Staff, Transfer Clients at path Group_Detail_Page.Group_Action_Bar; remove state-specific 'states' map and any 'preconditions' unless the description is extended to explicitly define when each action is available.
- If Assign Staff requires an input form, move the Staff field out of action definitions and model Assign Staff as an action that opens a separate form/modal at path Group_Detail_Page.Group_Action_Bar.available_actions[] named 'Assign Staff' with its own fields: { 'Staff': { 'type': 'dropdown' } }. Do not mark it required in the action definition unless the description explicitly states 'Assign Staff requires selecting a Staff'.
- If state-dependent availability is intended, update the description to explicitly state triggers (e.g., 'Activate is only available when status is Pending') and then regenerate so the AST can accurately include state_bound_action_bar.states with the specified preconditions.

---

## Center Management

**Verdict:** yes  
**Forced ship:** no  

The AST accurately represents the interactive elements (centers table with link, Import/Create actions, Create Center form fields and submit, bulk import template/upload, detail page actions and tabs, and the collection sheet) with no significant missing items or extraneous phantoms.

**Missing:** none

**Phantoms:** none

---

## Loan Products

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the wizard steps, table, detail view, and accounting conditional logic; only minor inferred elements present.

**Missing:** none

**Phantoms (hallucinations):**

- components.Loan_Products_Filter_Bar.fields.Search (search field inferred from 'filter bar' but not explicitly named)
- components.Create_Loan_Product_Wizard.steps[4].fields.Selected_Charges.item_fields.Remove (remove button inferred for selected charges but not explicitly described)

---

## Savings Products

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements and conditional logic described; only a minor inferred action name is present.

**Missing:** none

**Phantoms (hallucinations):**

- Savings_Products_Page.Products_Table.row_actions[0] (action_name 'View' was inferred; description only specified 'Name' is a clickable link)

---

## Share Products

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is mostly complete but is missing the auto-calculated Capital Value field and includes a few phantom actions that are not specified in the description.

**Missing:**

- Create_Share_Product_Wizard.steps[3].fields.Capital_Value

**Phantoms (hallucinations):**

- Share_Products_Table.row_actions[0] (Edit action not described on the table; Edit is only described in the detail view)
- Share_Products_Table.row_actions[1] (Delete action not described on the table; Delete is only described in the detail view)
- Create_Share_Product_Wizard.submit_actions[0] (Create Share Product button label/submit action text was not specified in the description)

**Fixes applied:**

- Create_Share_Product_Wizard.steps[3].fields.Capital_Value: Add a read-only numeric field named Capital_Value with metadata indicating it is auto-calculated (e.g., "auto_calculated": true) and an optional note of the calculation formula (e.g., Total_Number_of_Shares * Nominal_Unit_Price).
- Share_Products_Table.row_actions: Remove the Edit and Delete actions from the table row_actions array; retain Edit and Delete only in Share_Product_Detail.actions as described.
- Create_Share_Product_Wizard.submit_actions[0]: Remove or make generic (e.g., replace explicit labeled button with a generic wizard submit action) since the description did not specify the exact submit button text; do not invent a specific button label unless present in the description.

---

## Charges

**Verdict:** yes  
**Forced ship:** no  

AST accurately covers all interactive elements from the description; only two minor inferred items (an Edit form and a redundant row action) are present but acceptable.

**Missing:** none

**Phantoms (hallucinations):**

- components.Charges_Table.row_actions[0] (Open Detail row_action duplicates the Name clickable link described)
- components.Edit_Charge_Form (Edit opening a separate form was inferred though description only specifies an Edit option in the detail view)

---

## Floating Rates

**Verdict:** yes  
**Forced ship:** no  

The AST correctly captures the interactive elements described (data table with clickable Floating Rate Name, Create button and form with required fields and repeating Rate Periods, add-row action, and detail view Edit action), with appropriate constraints and submit behavior.

**Missing:** none

**Phantoms:** none

---

## Delinquency Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

AST contains multiple inferred elements not explicitly stated (phantoms); adjust detail page fields and remove or justify inferred form controls.

**Missing:** none

**Phantoms (hallucinations):**

- components.Delinquency_Bucket_Detail.fields (description only names a clickable Bucket Name link; no detail fields were specified)
- components.Delinquency_Bucket_Detail.fields.Bucket_Ranges (detail page fields were not described and are inferred)
- components.Delinquency_Bucket_Detail.fields.Linked_Loan_Products (detail fields were not specified)
- components.Create_Delinquency_Bucket_Form.Bucket_Ranges.add_action.element_name ("Add Range" button label is inferred, not present in description)
- components.Delinquency_Bucket_Detail.Bucket_Ranges.add_action.element_name ("Add Range" on detail is inferred)
- components.Create_Delinquency_Bucket_Form.Linked_Loan_Products (the description states buckets are linked to Loan Products but does not explicitly state there is a Link/Dropdown field on the create form)

**Fixes applied:**

- components.Delinquency_Bucket_Detail.fields: Clear this object to an empty object {} (the description only specifies that Bucket Name is a clickable link; no detail fields were described).
- components.Delinquency_Bucket_Detail.fields.Bucket_Ranges: Remove this repeating_group; if detail fields are required, the description must explicitly list them.
- components.Delinquency_Bucket_Detail.fields.Linked_Loan_Products: Remove this field from the detail page unless the description explicitly requires it.
- components.Create_Delinquency_Bucket_Form.Bucket_Ranges.add_action.element_name: Remove or leave unspecified the element_name ("Add Range") unless the exact control label is provided in the description.
- components.Delinquency_Bucket_Detail.Bucket_Ranges.add_action.element_name: Remove this add_action from the detail page unless explicitly described.
- components.Create_Delinquency_Bucket_Form.Linked_Loan_Products: Either remove this field or update the description to explicitly state that the create form includes a multi-select/dropdown to link Loan Products.

---

## Loan Account

**Verdict:** yes  
**Forced ship:** no  

AST accurately represents the interactive elements in the description with no significant missing or extraneous interactive items.

**Missing:** none

**Phantoms:** none

---

## Savings Account

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements and state-bound actions from the description; only minor omissions/inferences noted.

**Missing:**

- Create_Savings_Account_Form.fields.Charges.add_action (explicit 'Add Charge' control to add more charges)

**Phantoms (hallucinations):**

- Savings_Account_Detail_Actions.states.Approved.available_actions[1].on_success (Undo Approval 'reverts to Submitted and Pending Approval status' effect is an inferred behavior not explicitly stated)

---

## Share Account

**Verdict:** yes  
**Forced ship:** no  

The AST accurately captures the interactive elements (application form fields, submit action, state-bound actions with their fields, and the three tabs with tables); no significant missing items or extraneous phantoms were found.

**Missing:** none

**Phantoms:** none

---

## Fixed & Recurring Deposit Accounts

**Verdict:** yes  
**Forced ship:** no  

AST correctly captures the interactive elements (creation actions, form fields, tabs, and detail actions) with only two minor inferred fields (Interest_Rate) that are non-critical.

**Missing:** none

**Phantoms (hallucinations):**

- Fixed_Deposit_Account_Creation_Form.fields.Interest_Rate
- Recurring_Deposit_Account_Creation_Form.fields.Interest_Rate

---

## Accounting — Chart of Accounts

**Verdict:** yes  
**Forced ship:** no  

AST matches the described interactive elements (create form with all fields and constraints, tree with row click to detail, edit/delete actions); only minor inferred element present.

**Missing:** none

**Phantoms (hallucinations):**

- components.Edit_GL_Account_Form.fields (Edit action was mentioned but the description did not enumerate edit form fields; fields were inferred)

---

## Accounting — Journal Entries & Closures

**Verdict:** yes  
**Forced ship:** no  

AST is acceptable for use; only minor issues (a missing running total display and an inferred min on entry lines) were found.

**Missing:**

- Add_Journal_Entry_Form.fields.Running_Total (debit_total, credit_total, difference display)

**Phantoms (hallucinations):**

- Add_Journal_Entry_Form.fields.Entry_Lines.min (min: 1 inferred but not specified in description)

---

## Accounting Rules & Financial Activity Mappings

**Verdict:** yes  
**Forced ship:** no  

AST matches the described interactive elements; only minor inferred details (Edit form fields and save button) are present but acceptable.

**Missing:** none

**Phantoms (hallucinations):**

- Accounting_Rule_Detail_View.actions[0].fields (Edit form fields were not explicitly listed in the description)
- Accounting_Rule_Detail_View.actions[0].submit_actions[0] (Save Changes button name/action not explicitly specified in the description)

---

## Provisioning

**Verdict:** yes  
**Forced ship:** no  

AST matches the description with only minor issues: it omits an explicit add-row control for the Definitions repeating table and includes one inferred constraint not stated in the description.

**Missing:**

- Provisioning_Criteria_Form.fields.Definitions.add_row_action

**Phantoms (hallucinations):**

- Provisioning_Criteria_Form.fields.Definitions.constraints[0] (Minimum_Age must be <= Maximum_Age)

---

## Offices

**Verdict:** yes  
**Forced ship:** no  

The AST accurately captures the interactive elements described: the hierarchical offices table with clickable Office Name, the + Create Office button and its form fields (with required constraints), and the Office Detail page Edit action with an edit form; no missing or extraneous interactive items identified.

**Missing:** none

**Phantoms:** none

---

## Employees

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements (table, name link, create button + form with required fields, and staff detail with Edit action); the only minor phantom is the detailed Edit form fields which were not explicitly described but are reasonable to include.

**Missing:** none

**Phantoms (hallucinations):**

- components.Edit_Employee_Form.fields (the description only mentions an Edit option on the Staff Detail page, but does not enumerate the edit form fields)

---

## Teller & Cashier Management

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements described (tables, buttons, forms, fields, actions) with no significant missing or extraneous items.

**Missing:** none

**Phantoms:** none

---

## Users & Roles

**Verdict:** yes  
**Forced ship:** no  

AST covers the described interactive elements (Users table and create form, Roles table and create form, permissions matrix) with only a minor inferred navigation target.

**Missing:** none

**Phantoms (hallucinations):**

- Users_Page.row_actions[0].navigates_to (User_Detail_Page not explicitly named in description)

---

## Reports

**Verdict:** yes  
**Forced ship:** no  

The AST correctly models the interactive elements described: category tabs, report rows with clickable Name opening the parameters form (Office, Branch, Currency, Loan Product, Date Range, Loan Officer, Fund), a Run Report action that renders a sortable, paginated results table, and the specified export/view output options.

**Missing:** none

**Phantoms:** none

---

## Account Transfers & Standing Instructions

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements from the description; only minor inferred preconditions were added for enable/disable row actions.

**Missing:** none

**Phantoms (hallucinations):**

- Standing_Instructions_Table.row_actions[0].preconditions[0] ("status must be Disabled" - inferred precondition for Enable action not explicitly stated)
- Standing_Instructions_Table.row_actions[1].preconditions[0] ("status must be Active" - inferred precondition for Disable action not explicitly stated)

---

## Tax Management

**Verdict:** yes  
**Forced ship:** no  

AST matches the described interactive elements (tables, links, create buttons, forms, fields, repeating group, and conditional tax-group selection) with only two minor inferred submit actions.

**Missing:** none

**Phantoms (hallucinations):**

- Create_Tax_Component_Form.submit_actions[0] (Create button not explicitly named in description)
- Create_Tax_Group_Form.submit_actions[0] (Create button not explicitly named in description)

---

## Organization Settings

**Verdict:** yes  
**Forced ship:** no  

AST is largely correct with one missing table column and one minor phantom element; acceptable to use with small adjustments.

**Missing:**

- Holidays_Table.columns (missing "Status" column)

**Phantoms (hallucinations):**

- Holiday_State_Actions (state_bound_action_bar not described in the input)

---

## System Administration

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

AST contains multiple inferred/unsupported elements (phantoms) that are not explicitly stated in the description and should be removed or aligned; regeneration recommended.

**Missing:** none

**Phantoms (hallucinations):**

- Manage_Scheduler_Jobs_Table.row_fields.CRON_Expression.constraints (CRON validation constraint not explicitly specified in description)
- Manage_Scheduler_Jobs_Table.sortable_columns (sortable columns were not mentioned in the description)
- Manage_Data_Tables.row_actions.Delete_Data_Table.preconditions[0] (user must confirm deletion precondition not stated in description)
- Create_Data_Table_Form.fields.Column_Definitions.min (min: 0 inferred default not mentioned in description)
- Create_Data_Table_Form.submit_actions[1] (Cancel button was not specified in the description)

**Fixes applied:**

- Remove Manage_Scheduler_Jobs_Table.row_fields.CRON_Expression.constraints or replace with an explicit requirement only if the description is updated to require client-side CRON validation; JSON path: Manage_Scheduler_Jobs_Table.row_fields.CRON_Expression.constraints (delete array).
- Remove Manage_Scheduler_Jobs_Table.sortable_columns if sorting behavior was not specified in the description; JSON path: Manage_Scheduler_Jobs_Table.sortable_columns (delete property) — alternatively add explicit row_field definitions for any sortable columns if they should be present.
- Remove the implicit deletion confirmation precondition from Manage_Data_Tables.row_actions.Delete_Data_Table.preconditions or change it to a neutral note if confirmation is desired; JSON path: Manage_Data_Tables.row_actions[1].preconditions (delete or replace entry).
- Remove the inferred 'min' property from Create_Data_Table_Form.fields.Column_Definitions since the description did not specify a minimum; JSON path: Create_Data_Table_Form.fields.Column_Definitions.min (delete property).
- Remove the Cancel submit action from Create_Data_Table_Form.submit_actions unless the description explicitly requires a Cancel button; JSON path: Create_Data_Table_Form.submit_actions[1] (delete the Cancel action) — keep only the Create submit action if Cancel was not specified.

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

The AST correctly captures the profile icon trigger, the dropdown items (Profile Settings and Log Out) with the logout side effects, and the post-logout redirect/auth guard; no missing or extraneous interactive elements found.

**Missing:** none

**Phantoms:** none

---
