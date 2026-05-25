# Semantic Critique — Mifos

Generated: 2026-05-21T22:36:26.545692Z

## Login

**Verdict:** yes  
**Forced ship:** no  

AST includes all interactive elements and behaviors from the description; only a minor phantom (explicit error message text) is present.

**Missing:** none

**Phantoms (hallucinations):**

- Login_Form.submit_actions[0].on_failure (shows error message 'Invalid credentials' — exact message text was not specified in the description)

---

## Home Page

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements (Search Activity input and Dashboard button); only a minor inferred submit action for Search is present.

**Missing:** none

**Phantoms (hallucinations):**

- Home_Page.submit_actions[0] (Search action/button not explicitly mentioned in the description)

---

## Dashboard

**Verdict:** yes  
**Forced ship:** no  

AST correctly models the Dashboard button navigation, the Search Activity field, the Client Trends chart with legends for New Clients and Closed Clients, and the two summary cards with 'No Data' behavior.

**Missing:** none

**Phantoms:** none

---

## Global Search

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the global search button, live search input, grouped results (Clients, Groups, Loans, Savings accounts), result item fields (name, identifier, status), navigation on selection, empty state, and matching constraints.

**Missing:** none

**Phantoms:** none

---

## Client Management

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements, actions, conditional logic, wizard steps, import workflow, and detail-page tabs/actions as described.

**Missing:** none

**Phantoms:** none

---

## Group Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST adds inferred action preconditions and an extra 'Generate Collection Sheet' action that are not specified in the description; remove those inferred constraints/actions or make them explicit in the description before reuse.

**Missing:** none

**Phantoms (hallucinations):**

- Group_Detail_Page.Detail_Action_Bar.states.Pending.available_actions[0].preconditions[0] ("status must be Pending" — not stated in description)
- Group_Detail_Page.Detail_Action_Bar.states.Active.available_actions[0].preconditions[0] ("status must be Active" — not stated in description)
- Group_Detail_Page.Detail_Action_Bar.states.Closed.available_actions[0].preconditions[0] ("status must be Active or Pending" — contradictory and not stated in description)
- Group_Detail_Page.Detail_Action_Bar.states.Active.available_actions[4] ("Generate Collection Sheet" action — the description mentions a Collection Sheet feature but does not state there is an action button in the detail action bar)

**Fixes applied:**

- Remove the inferred precondition at Group_Detail_Page.Detail_Action_Bar.states.Pending.available_actions[0].preconditions[0]; replace the 'preconditions' array with an empty array or remove the 'preconditions' property entirely.
- Remove the inferred precondition at Group_Detail_Page.Detail_Action_Bar.states.Active.available_actions[0].preconditions[0]; replace the 'preconditions' array with an empty array or remove the 'preconditions' property entirely.
- Remove or correct the contradictory inferred precondition at Group_Detail_Page.Detail_Action_Bar.states.Closed.available_actions[0].preconditions[0]; set 'preconditions' to an empty array or remove it (the description does not specify any preconditions for Edit in Closed state).
- Remove the 'Generate Collection Sheet' action from Group_Detail_Page.Detail_Action_Bar.states.Active.available_actions[4] (or move it out of the state_bound_action_bar into the standalone Collection_Sheet component) because the description does not explicitly state there is an action button for generating the collection sheet in the detail action bar.

---

## Center Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Reject: the AST introduces multiple phantom elements not present in the description (an explicit 'Generate Collection Sheet' action, several Member_Groups table columns, and inferred numeric constraints); please remove or align these with the spec.

**Missing:** none

**Phantoms (hallucinations):**

- components.Center_Detail_Page.action_bar.states.Any.available_actions[4] (Generate Collection Sheet action not explicitly described in the input)
- components.Center_Detail_Page.tabs[0].components.Member_Groups_Table.columns[1] (Member_Groups_Table column 'Group External Id' not specified in the input)
- components.Center_Detail_Page.tabs[0].components.Member_Groups_Table.columns[2] (Member_Groups_Table column 'Status' not specified in the input)
- components.Center_Detail_Page.tabs[0].components.Member_Groups_Table.columns[3] (Member_Groups_Table column 'Office Name' not specified in the input)
- components.Collection_Sheet.row_fields.Loan_Repayment_Amount.constraints (non-negative constraint inferred but not stated in the input)
- components.Collection_Sheet.row_fields.Savings_Deposit_Amount.constraints (non-negative constraint inferred but not stated in the input)

**Fixes applied:**

- Remove components.Center_Detail_Page.action_bar.states.Any.available_actions[4] (the 'Generate Collection Sheet' action) unless the description explicitly names a button/action on the Center Detail page to open the Collection Sheet; if the description is updated to name such an action, add it back with the exact label and trigger.
- Replace components.Center_Detail_Page.tabs[0].components.Member_Groups_Table.columns with ["Name"] and keep link_column set to "Name" — the description only specifies a list of member groups with links and does not enumerate additional columns.
- Delete components.Collection_Sheet.row_fields.Loan_Repayment_Amount.constraints — do not add inferred validation constraints unless explicitly specified in the description.
- Delete components.Collection_Sheet.row_fields.Savings_Deposit_Amount.constraints — do not add inferred validation constraints unless explicitly specified in the description.

---

## Loan Products

**Verdict:** yes  
**Forced ship:** no  

AST correctly captures the filter, table, Create button, 6-step wizard with all specified fields and step-6 conditional GL mappings, and the product detail Edit action.

**Missing:** none

**Phantoms:** none

---

## Savings Products

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures all interactive elements, steps, fields, options, and conditional logic described for Savings, Fixed Deposit, and Recurring Deposit product wizards and the Savings Products page.

**Missing:** none

**Phantoms:** none

---

## Share Products

**Verdict:** yes  
**Forced ship:** no  

The AST accurately represents the interactive elements described: the data table with clickable Product Name, the + Create Share Product wizard with all 7 steps and fields (including repeating market-price rows and charges search-and-add), the accounting conditional fields, and the product detail Edit/Delete actions.

**Missing:** none

**Phantoms:** none

---

## Charges

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the described interactive elements; only minor row-level Edit/Delete actions in the table are extra but non-critical.

**Missing:** none

**Phantoms (hallucinations):**

- components.Charges_Table.row_actions[1] (Edit row action not explicitly described; Edit is only mentioned in the detail view)
- components.Charges_Table.row_actions[2] (Delete row action not explicitly described; Delete is only mentioned in the detail view)

---

## Floating Rates

**Verdict:** yes  
**Forced ship:** no  

AST correctly captures the interactive elements, constraints, repeating rate periods, table/link actions, create/edit flows, and detail view; only minor inferred submit button labels were added.

**Missing:** none

**Phantoms (hallucinations):**

- Create_Floating_Rate_Form.submit_actions[0] (element_name 'Create' — submit button label was not explicitly specified in the description)
- Edit_Floating_Rate_Form.submit_actions[0] (element_name 'Save' — submit button label was not explicitly specified in the description)

---

## Delinquency Management

**Verdict:** yes  
**Forced ship:** no  

The AST correctly represents both pages, their data tables (including clickable columns), the create forms with required/optional fields, and the repeating ranges interface for buckets matching the description.

**Missing:** none

**Phantoms:** none

---

## Loan Account

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements, steps, actions, and tabs described; no critical items are missing and there are no extraneous phantom elements.

**Missing:** none

**Phantoms:** none

---

## Savings Account

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements, states, actions, forms, and tabs described; only minor non-critical extras (empty row/bulk action placeholders) are present.

**Missing:** none

**Phantoms (hallucinations):**

- Savings_Account_Detail_Tabs.tabs[1].fields.Transactions_Table.row_actions
- Savings_Account_Detail_Tabs.tabs[1].fields.Transactions_Table.bulk_actions

---

## Share Account

**Verdict:** yes  
**Forced ship:** no  

The AST correctly includes all interactive elements (create link, application form fields including Charges section, submit action, state-bound actions with their fields, and the three detail tabs/tables) without extraneous phantoms.

**Missing:** none

**Phantoms:** none

---

## Fixed & Recurring Deposit Accounts

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements described (creation actions, form fields, detail-page actions, and tabs); only one minor inferred field (RD deposit period unit) that is reasonable.

**Missing:** none

**Phantoms (hallucinations):**

- components.RD_Account_Creation_Form.fields.Deposit_Period_Unit (Deposit period unit options for RD were not explicitly specified in the description)

---

## Accounting — Chart of Accounts

**Verdict:** yes  
**Forced ship:** no  

The AST correctly models the tree, create form (with filtered Parent Account and GL code uniqueness validation), and account detail actions; only a generic submit action in the form is an extra minor element.

**Missing:** none

**Phantoms (hallucinations):**

- Create_GL_Account_Form.submit_actions[0] (submit button not explicitly mentioned in description)

---

## Accounting — Journal Entries & Closures

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

AST is missing the explicit 'Add Row' action for entry lines and includes several phantom elements (per-line Type and explicit submit button labels) that are not present in the description.

**Missing:**

- Add_Journal_Entry_Form.fields.Entry_Lines.Add_Row_Button (explicit '+ Add Row' action to append another entry line)

**Phantoms (hallucinations):**

- Add_Journal_Entry_Form.fields.Entry_Lines.item_fields.Type (per-line 'Type' field not specified in the description for the creation form)
- Add_Journal_Entry_Form.submit_actions[0].element_name (Create Journal Entry button label not specified in the description)
- Create_Closure_Form.submit_actions[0].element_name (Create Closure button label not specified in the description)

**Fixes applied:**

- Add_Journal_Entry_Form.fields.Entry_Lines.Add_Row_Button: add an explicit action/button with element_name '+ Add Row' (or similar) that appends a new item to the repeating Entry_Lines group.
- Remove or make unspecified: Add_Journal_Entry_Form.fields.Entry_Lines.item_fields.Type — remove this field unless the description is updated to explicitly state that each entry line includes a Debit/Credit selector; if you keep it, ensure the description mentions per-line Type.
- Remove or mark unspecified: Add_Journal_Entry_Form.submit_actions[0].element_name — the description did not specify the submit button label; either remove the explicit element_name or set it to a generic unspecified value (e.g., 'Submit').
- Remove or mark unspecified: Create_Closure_Form.submit_actions[0].element_name — the description did not specify the submit button label; either remove the explicit element_name or set it to a generic unspecified value (e.g., 'Submit').

---

## Accounting Rules & Financial Activity Mappings

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements for both pages; only a single minor inferred Edit form (reasonable) was added beyond the explicit description.

**Missing:** none

**Phantoms (hallucinations):**

- components.Edit_Rule_Form (edit form fields inferred though description only mentioned an Edit option on the detail view)

---

## Provisioning

**Verdict:** yes  
**Forced ship:** no  

AST captures all interactive elements described (tables, create buttons, form with repeating Definitions rows, entries table with create/review/recreate actions); only minor inferred UI details (save button and category shown as dropdown in detail view) are present but acceptable.

**Missing:** none

**Phantoms (hallucinations):**

- Provisioning_Criteria_Form.submit_actions[0] (Save button and its on_success behavior are not explicitly named in the description)
- Provisioning_Entry_Detail.columns[1] (Category rendered as a dropdown in the detail breakdown is an inferred control not explicitly specified)

---

## Offices

**Verdict:** yes  
**Forced ship:** no  

AST correctly captures the hierarchical offices table, clickable office name, Create Office flow with required fields, and Office Detail page with Edit action; only a minor inferred submit button was added.

**Missing:** none

**Phantoms (hallucinations):**

- Create_Office_Form.submit_actions[0] (Submit button label and explicit submit action are not specified in the description)

---

## Employees

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

AST contains multiple inferred elements (phantoms) not specified in the description (notably a row action and inferred edit-form fields/submit labels); please remove or align these with the description.

**Missing:** none

**Phantoms (hallucinations):**

- components.Employees_Table.row_actions[0] (View Details action not mentioned in description)
- components.Create_Employee_Form.submit_actions[0].element_name (Create Employee button label inside the form is not specified in description)
- components.Edit_Employee_Form.fields (Edit form fields were inferred but the description only states there is an Edit option on the detail page)
- components.Edit_Employee_Form.submit_actions[0].element_name (Save Changes button label was inferred but not specified in description)

**Fixes applied:**

- components.Employees_Table.row_actions — Remove this array or set it to []: the description only specifies that the Name column is a clickable link to the Staff Detail page; do not invent an additional 'View Details' row action.
- components.Create_Employee_Form.submit_actions[0].element_name — Remove the element_name property or set it to null: the description does not provide a label for the form submit button, so do not invent 'Create Employee' as a label. You may keep a submit_actions entry describing the effect, but omit an explicit label.
- components.Edit_Employee_Form.fields — Replace the current fields object with an empty object {}: the description only mentions an Edit option on the Staff Detail page and does not enumerate the edit form fields, so do not populate inferred fields.
- components.Edit_Employee_Form.submit_actions[0].element_name — Remove the element_name property or set it to null: the description does not provide a label for the edit form submit button, so do not invent 'Save Changes' as a label. You may keep an on_success description if needed but omit an explicit label.

---

## Teller & Cashier Management

**Verdict:** yes  
**Forced ship:** no  

The AST accurately captures the interactive elements (tables, buttons, forms, fields, and actions) described for Tellers, Teller Detail, Allocate Cashier, and Cashier Detail pages with no missing critical items or extraneous elements.

**Missing:** none

**Phantoms:** none

---

## Users & Roles

**Verdict:** yes  
**Forced ship:** no  

The AST accurately captures the interactive elements (tables, create buttons, forms, fields, constraints, and the permissions matrix) with only minor inferred details.

**Missing:** none

**Phantoms (hallucinations):**

- components.Role_Permissions_Page.fields.Permission_Categories.item_fields.Category_Name.type (category represented as a dropdown was inferred; description only specified categorized matrix)
- components.Users_Table.row_actions[0].target (User_Detail target name is an inferred navigation target, not explicitly named in the description)

---

## Reports

**Verdict:** yes  
**Forced ship:** no  

AST accurately includes tabs, report list with clickable rows, the parameters form with the specified fields, Run Report and export actions, and the generated sortable/paginated table.

**Missing:** none

**Phantoms:** none

---

## Account Transfers & Standing Instructions

**Verdict:** yes  
**Forced ship:** no  

The AST accurately includes all interactive elements (forms, fields, validations, buttons, table columns, row actions) described for Account Transfers and Standing Instructions with no substantive extras or omissions.

**Missing:** none

**Phantoms:** none

---

## Tax Management

**Verdict:** yes  
**Forced ship:** no  

The AST accurately captures the described interactive elements (tables, clickable Name links, create buttons, forms with required fields, repeating tax-component entries, and references from Savings Products and Charge Definitions) with no missing or extraneous items.

**Missing:** none

**Phantoms:** none

---

## Organization Settings

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements described; only minor omissions (create button label for Funds and two table column entries for Payment Types) that do not require a full regeneration.

**Missing:**

- Funds_Page.page_actions[0].element_name (label for the Create Fund button, e.g., '+ Create Fund')
- Payment_Types_Page.sortable_columns (missing columns: 'Description', 'Is Cash Payment')

**Phantoms:** none

---

## System Administration

**Verdict:** yes  
**Forced ship:** no  

AST accurately covers the interactive elements described (per-row job toggles and editable CRONs, global scheduler toggle, configuration toggles/values, code list detail actions, data table creation form with column definitions, and audit trails with filters and approve/reject actions) with no critical omissions.

**Missing:** none

**Phantoms:** none

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

The AST accurately captures the interactive elements (profile icon button, dropdown with Profile Settings and Log Out, logout effects, and the authenticated route guard) described in the specification.

**Missing:** none

**Phantoms:** none

---
