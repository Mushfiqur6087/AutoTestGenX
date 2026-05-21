# Semantic Critique — Mifos

Generated: 2026-05-21T16:21:26.912513Z

## Login

**Verdict:** yes  
**Forced ship:** no  

AST matches the described interactive elements (language selector, tenant dropdown, username, password, remember me, login button with enablement rule, and forgot-password link) with only two minor inferred details.

**Missing:** none

**Phantoms (hallucinations):**

- components.Forgot_Password_Link.on_trigger (navigates to Forgot Password page not explicitly stated in description)
- components.Login_Form.submit_actions[0].on_failure (shows error message 'Invalid credentials' — exact message text not provided in description)

---

## Home Page

**Verdict:** yes  
**Forced ship:** no  

AST correctly captures the interactive elements (Search Activity input and Dashboard button) and the login precondition; no missing or extraneous interactive items found.

**Missing:** none

**Phantoms:** none

---

## Dashboard

**Verdict:** yes  
**Forced ship:** no  

The AST accurately includes the Home page Dashboard button, the Dashboard page with the Search Activity field, the Client Trends chart with legends for New Clients and Closed Clients, and the two summary cards that display 'No Data' when appropriate.

**Missing:** none

**Phantoms:** none

---

## Global Search

**Verdict:** yes  
**Forced ship:** no  

AST accurately models the global search icon, input, scoped live search, grouped results with name/identifier/status, selection navigation, no-results message, and stated search constraints.

**Missing:** none

**Phantoms:** none

---

## Client Management

**Verdict:** yes  
**Forced ship:** no  

AST correctly captures the interactive elements, actions, state-bound behaviors, wizard steps, and tab structure; only minor inferred items (identifiers as a repeating group and a duplicate constraint in the Create Client wizard) are present but non-critical.

**Missing:** none

**Phantoms (hallucinations):**

- Create_Client_Wizard.steps[3].fields.Identifiers.type (repeating_group inferred for the wizard step though the description only named the fields)
- Create_Client_Wizard.steps[3].fields.Identifiers.constraints[0] (duplicate-prevention constraint was explicitly described for the detail Identifiers tab but not explicitly for the wizard step)

---

## Group Management

**Verdict:** yes  
**Forced ship:** no  

AST accurately covers the interactive elements from the description; only minor inferred items (Edit form fields and Assign Staff dialog field requirement) were added but are acceptable.

**Missing:** none

**Phantoms (hallucinations):**

- Edit_Group_Form.fields (detailed edit form fields were inferred from the Create form but not explicitly described)
- Assign_Staff_Dialog.fields.Staff.required (the requirement on the Assign Staff field was inferred)

---

## Center Management

**Verdict:** yes  
**Forced ship:** no  

AST covers all interactive elements from the description; only minor inferred items (Edit form and an Assign Staff field) were added but are acceptable.

**Missing:** none

**Phantoms (hallucinations):**

- Edit_Center_Form (full Edit form component inferred from the Edit action but not explicitly described)
- Center_Detail_Actions.available_actions[3].fields.Staff (Assign Staff action includes a Staff field which was not explicitly detailed in the description)

---

## Loan Products

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements, steps, fields, conditional logic, and detail view; only minor inferred button names were added.

**Missing:** none

**Phantoms (hallucinations):**

- Create_Loan_Product_Wizard.submit_actions[0] (Create button label not explicitly named in description)
- Create_Loan_Product_Wizard.submit_actions[1] (Cancel button label not explicitly named in description)

---

## Savings Products

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is mostly complete but includes a few phantom items (a repeating GL_Mappings group and an unjustified required constraint on Recurring_Frequency); please regenerate after removing these phantoms and making Recurring_Frequency optional.

**Missing:** none

**Phantoms (hallucinations):**

- components.Savings_Product_Wizard.steps[6].fields.GL_Mappings (repeating_group not described in the spec — description lists specific GL_* mappings instead)
- components.Recurring_Deposit_Product_Wizard.steps[4].fields.Recurring_Frequency.required (the description did not state Recurring Frequency is required)

**Fixes applied:**

- Remove the extraneous repeating group at components.Savings_Product_Wizard.steps[6].fields.GL_Mappings — the description specifies individual GL account mapping fields (GL_Savings_Reference, GL_Savings_Control, GL_Transfers_in_Suspense, GL_Interest_on_Savings, GL_Income_from_Fees, GL_Income_from_Penalties, GL_Escheat_Liability) and does not describe a generic repeating mapping; delete the GL_Mappings entry.
- Change components.Recurring_Deposit_Product_Wizard.steps[4].fields.Recurring_Frequency.required from true to false and remove any description asserting it is required (the input was not specified as required in the description).

---

## Share Products

**Verdict:** yes  
**Forced ship:** no  

The AST includes all interactive elements described (table with clickable product name, create button, full 7-step wizard with required fields, repeating market-price rows, search-and-add charges, accounting radio with conditional GL fields, and detail view actions); only one minor inferred dependency was added.

**Missing:** none

**Phantoms (hallucinations):**

- Create_Share_Product_Wizard.steps[2].fields.Capital_Value.computed_from (explicit dependency on fields inferred rather than stated)

---

## Charges

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements (table, create form with fields and conditional charge time options, submit, detail view with edit/delete); only minor unlabeled button names were added.

**Missing:** none

**Phantoms (hallucinations):**

- Charges_Table.row_actions[0].action_name (action label 'Open Details' is not explicitly named in the description)
- Edit_Charge_Form.submit_actions[0] (button label 'Save' for edit form is not explicitly named in the description)

---

## Floating Rates

**Verdict:** yes  
**Forced ship:** no  

AST captures all interactive elements described (table, create button, forms with repeating rate periods, and detail/edit flow); only minor naming details differ from the description.

**Missing:**

- Floating_Rates_Table.columns[0] (Floating Rate Name should be explicitly represented as a clickable link to the Floating_Rate_Detail_View)

**Phantoms (hallucinations):**

- Floating_Rates_Table.row_actions[0] (action_name 'Open Details' was not explicitly named in the description — the clickable link was described but the action name was not)
- Create_Floating_Rate_Form.Rate_Periods.add_row_action.element_name (the 'Add Rate Period' button label was not specified in the description)

---

## Delinquency Management

**Verdict:** yes  
**Forced ship:** no  

The AST correctly captures the Delinquency Ranges and Delinquency Buckets tables, clickable row links, create actions, required/optional fields, and the repeating-range interface for buckets.

**Missing:** none

**Phantoms:** none

---

## Loan Account

**Verdict:** yes  
**Forced ship:** no  

AST matches the described interactive elements; only a minor extra state entry was added that does not affect structure.

**Missing:** none

**Phantoms (hallucinations):**

- Loan_Detail_Actions.states["Approved (no further actions)"] (state label not present in the description)

---

## Savings Account

**Verdict:** yes  
**Forced ship:** no  

The AST accurately captures the interactive elements, states, actions, forms, and transaction table described; no critical items are missing.

**Missing:** none

**Phantoms:** none

---

## Share Account

**Verdict:** yes  
**Forced ship:** no  

AST correctly captures the interactive elements (create button, application form fields, submit action, state-bound actions, and tabs/tables); one minor inferred structure (Charges as a repeating_group) is acceptable.

**Missing:** none

**Phantoms (hallucinations):**

- Share_Account_Application_Form.fields.Charges (defined as a repeating_group.item_fields {} — description only mentioned a Charges section without field structure)

---

## Fixed & Recurring Deposit Accounts

**Verdict:** yes  
**Forced ship:** no  

AST accurately includes the creation forms, their fields, detail-page action buttons, and the Summary/Transactions/Charges tabs for both FD and RD as specified; no required interactive elements are missing.

**Missing:** none

**Phantoms:** none

---

## Accounting — Chart of Accounts

**Verdict:** yes  
**Forced ship:** no  

AST accurately represents the interactive elements (hierarchical tree, create button and form with required fields and constraints, detail view with Edit/Delete, and edit form) and includes the explicit Parent Account filtering and GL Code uniqueness validation.

**Missing:** none

**Phantoms:** none

---

## Accounting — Journal Entries & Closures

**Verdict:** yes  
**Forced ship:** no  

AST matches the description with two minor omissions (Add Row control and running totals display) and two minor inferred submit button labels.

**Missing:**

- Journal_Entry_Form.fields.Entry_Lines.Add_Row_Button
- Journal_Entry_Form.display_fields.Running_Total (Debit_Total, Credit_Total, Difference)

**Phantoms (hallucinations):**

- Journal_Entry_Form.submit_actions[0].element_name (Create Journal Entry) - label not specified in description
- Create_Closure_Form.submit_actions[0].element_name (Create Closure) - label not specified in description

---

## Accounting Rules & Financial Activity Mappings

**Verdict:** yes  
**Forced ship:** no  

AST accurately represents the interactive elements described (tables, create/edit forms, fields, buttons, and mapping constraints) with no missing items or extraneous phantoms.

**Missing:** none

**Phantoms:** none

---

## Provisioning

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements; only minor inferred items (an Add-row action missing from the Definitions repeating group and two small inferred items present) were noted but are non-critical.

**Missing:**

- Provisioning_Criteria_Form.fields.Definitions.add_row_action (ability to add additional definition rows)

**Phantoms (hallucinations):**

- Provisioning_Criteria_Form.submit_actions[0] (Save button name not specified in description)
- Provisioning_Criteria_Form.fields.Definitions.item_fields.Provisioning_Percentage.constraints[0] (percentage constraint 'must be between 0 and 100' not stated in description)

---

## Offices

**Verdict:** yes  
**Forced ship:** no  

AST includes the table, columns, row link, Create button and form fields (with required flags), Office detail and Edit action — one minor inferred constraint was added for Parent Office.

**Missing:** none

**Phantoms (hallucinations):**

- Create_Office_Form.fields.Parent_Office.constraints[0] (must select an existing office as parent)

---

## Employees

**Verdict:** yes  
**Forced ship:** no  

AST matches the described interactive elements (Employees table with Name link, Create Employee button + form fields, Employee detail Edit option); minor assumptions about submit buttons are present but acceptable.

**Missing:** none

**Phantoms (hallucinations):**

- Create_Employee_Form.submit_actions[0] (Save button not explicitly named in description)
- Edit_Employee_Form.submit_actions[0] (Save button not explicitly named in description)

---

## Teller & Cashier Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST adds detailed fields and a submit action for Edit_Teller_Form that the description did not specify (the description only names an Edit option), so regenerate after removing those invented fields/actions.

**Missing:** none

**Phantoms (hallucinations):**

- Edit_Teller_Form.fields.Office (field not specified in description; Edit option had no fields listed)
- Edit_Teller_Form.fields.Teller_Name (field not specified in description; Edit option had no fields listed)
- Edit_Teller_Form.fields.Description (field not specified in description; Edit option had no fields listed)
- Edit_Teller_Form.fields.Start_Date (field not specified in description; Edit option had no fields listed)
- Edit_Teller_Form.fields.End_Date (field not specified in description; Edit option had no fields listed)
- Edit_Teller_Form.fields.Status (field not specified in description; Edit option had no fields listed)
- Edit_Teller_Form.submit_actions[0] (Save action not specified in description)

**Fixes applied:**

- Edit_Teller_Form.fields — replace the entire fields object with an empty object: "fields": {} because the description names an Edit option but provides no fields.
- Edit_Teller_Form.submit_actions — remove the submit_actions array (or leave empty) since no submit action/labels for Edit were specified in the description.

---

## Users & Roles

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

AST mostly covers the described functionality but has missing submit button details and contains a couple of phantom elements that should be removed or clarified before use.

**Missing:**

- components.Create_User_Form.submit_actions[0] (submit action object is empty — missing submit button label and on_success behavior)
- components.Create_Role_Form.submit_actions[0].action_name (submit action has on_success but no action/button name)

**Phantoms (hallucinations):**

- components.Users_Table.row_actions[0] (Open User action not explicitly named in the description; description only states Username is a clickable link)
- components.Role_Permissions_Page.notes (freeform notes block is documentation, not an interactive element described in the spec)

**Fixes applied:**

- components.Create_User_Form.submit_actions[0] — replace the empty object with a concrete submit action, e.g. { "action_name": "Create User", "type": "submit", "on_success": "close_form_and_refresh_Users_Table" } (or an equivalent submit action defined in the spec).
- components.Create_Role_Form.submit_actions[0] — add an action_name (e.g. "Create Role") to the existing submit action object so the submit button is explicitly defined: add "action_name": "Create Role".
- components.Users_Table.row_actions[0] — remove this row action object if the description does not explicitly name the action; alternatively, if you intend to keep it, ensure the description explicitly states the effect (e.g., 'clicking Username opens the user details') and update the spec accordingly.
- components.Role_Permissions_Page.notes — remove this notes block from the interactive AST (move it to non-interactive documentation) because it is not an interactive element required by the description.

---

## Reports

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements (tabs, report list, parameter form, run action, and result exports); only minor inferred items flagged.

**Missing:** none

**Phantoms (hallucinations):**

- Report_Parameters_Form.fields.Output_Format (Output format field is inferred — description only listed output options but did not explicitly state a form field)
- Report_Parameters_Form.fields.Start_Date / Report_Parameters_Form.fields.End_Date (Date Range was split into two fields; the description only specified 'Date Range')

---

## Account Transfers & Standing Instructions

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the described interactive elements; only minor inferred preconditions for enable/disable row actions were added but are acceptable.

**Missing:** none

**Phantoms (hallucinations):**

- Standing_Instructions_List.row_actions[0].preconditions (Status == Disabled) - not explicitly stated in description
- Standing_Instructions_List.row_actions[1].preconditions (Status == Active) - not explicitly stated in description

---

## Tax Management

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements described; only minor inferred submit button labels were added.

**Missing:** none

**Phantoms (hallucinations):**

- Create_Tax_Component_Form.submit_actions[0] (Create button label not specified in description)
- Create_Tax_Group_Form.submit_actions[0] (Create button label not specified in description)

---

## Organization Settings

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures all interactive elements described (pages, tables, create buttons/forms, fields, checkboxes, dropdowns, file uploads, and import templates) with no significant missing items or extraneous phantoms.

**Missing:** none

**Phantoms:** none

---

## System Administration

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

AST contains several inferred elements not explicitly described (phantoms) and one filter control modeled incorrectly; please remove or adjust inferred fields and make the Date Range filter a proper range control.

**Missing:**

- components.Audit_Trails.filters.Date_Range (should be a date range control with start_date and end_date rather than a single 'date' field)

**Phantoms (hallucinations):**

- components.Audit_Trails.row_actions[2].fields.Rejection_Reason (Rejection reason input was not specified in the description)
- components.Data_Table_Create_Form.submit_actions[1] (Cancel button not described in the Create form)
- components.Manage_Data_Tables.row_actions[1] (View action not mentioned in the description of Manage Data Tables)

**Fixes applied:**

- components.Audit_Trails.filters.Date_Range: Change 'type' from 'date' to a date-range control (e.g., replace with an object { start_date: { type: 'date' }, end_date: { type: 'date' } } or type: 'date_range') so the filter explicitly supports a range as described.
- components.Audit_Trails.row_actions[2].fields.Rejection_Reason: Remove this field (or at minimum set 'required': false) unless the description is updated to explicitly state that a rejection reason is required when rejecting a pending command.
- components.Data_Table_Create_Form.submit_actions[1]: Remove the 'Cancel' submit action entry (submit_actions[1]) unless the description explicitly requires a Cancel control on the Create form.
- components.Manage_Data_Tables.row_actions[1]: Remove the 'View' row action (row_actions[1]) or document it in the description; the specification only required listing and editing/creating data tables, so do not invent an unspecified 'View' action.

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements (profile icon button, dropdown with Profile Settings and Log Out, log out consequences, and the authenticated-page redirect guard) with no missing or extraneous elements.

**Missing:** none

**Phantoms:** none

---
