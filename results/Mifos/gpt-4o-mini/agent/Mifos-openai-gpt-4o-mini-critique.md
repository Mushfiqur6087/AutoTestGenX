# Semantic Critique — Mifos

Generated: 2026-06-04T14:20:14.442705Z

## Login

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required elements and contains phantoms.

**Missing:**

- Login_Form.fields.Tenant.required
- Login_Form.fields.Language_Selector

**Phantoms (hallucinations):**

- Login_Form.fields.Language_Selector (not mentioned in description)

**Fixes applied:**

- Set Login_Form.fields.Tenant.required to true
- Remove Login_Form.fields.Language_Selector

---

## Home Page

**Verdict:** yes  
**Forced ship:** no  

The AST correctly represents the interactive elements described with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Dashboard

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST contains several phantoms and missing elements related to the description.

**Missing:**

- Search_Activity_Field.visible_when (should specify that it appears at the top)
- Client_Trends_Chart.visible_when (should specify that it visualizes client growth over time)
- Summary_Cards.fields.Amount_Pending_Disbursed.visible_when (should specify that it shows 'No Data' if no information is available)
- Summary_Cards.fields.Amount_Collected.visible_when (should specify that it shows 'No Data' if no information is available)

**Phantoms (hallucinations):**

- Summary_Cards.type (unspecified type not mentioned in description)
- Client_Trends_Chart.type (unspecified type not mentioned in description)
- Summary_Cards.type (unspecified type not mentioned in description)

**Fixes applied:**

- Update Search_Activity_Field.visible_when to specify that it appears at the top.
- Update Client_Trends_Chart.visible_when to specify that it visualizes client growth over time.
- Update Summary_Cards.fields.Amount_Pending_Disbursed.visible_when to specify that it shows 'No Data' if no information is available.
- Update Summary_Cards.fields.Amount_Collected.visible_when to specify that it shows 'No Data' if no information is available.
- Remove Summary_Cards.type, Client_Trends_Chart.type, and Summary_Cards.type as they are not specified in the description.

---

## Global Search

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described, with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Client Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing critical elements and contains phantoms.

**Missing:**

- Client_Detail_Page.fields.Client_Name
- Client_Detail_Page.fields.Account_Number
- Client_Detail_Page.fields.Status
- Client_Detail_Page.fields.Activation_Date
- Client_Detail_Page.fields.Office

**Phantoms (hallucinations):**

- Bulk_Import_Page.fields.Upload_File (not explicitly mentioned in description)
- Create_Client_Wizard.steps[1].fields.Legal_Form (not explicitly mentioned in description)
- Create_Client_Wizard.steps[1].fields.Middle_Name (not explicitly mentioned in description)
- Create_Client_Wizard.steps[1].fields.Date_of_Birth (not explicitly mentioned in description)
- Create_Client_Wizard.steps[1].fields.Gender (not explicitly mentioned in description)
- Create_Client_Wizard.steps[1].fields.Staff (not explicitly mentioned in description)
- Create_Client_Wizard.steps[1].fields.Mobile_Number (not explicitly mentioned in description)
- Create_Client_Wizard.steps[1].fields.Email_Address (not explicitly mentioned in description)
- Create_Client_Wizard.steps[1].fields.Client_Type (not explicitly mentioned in description)
- Create_Client_Wizard.steps[1].fields.Client_Classification (not explicitly mentioned in description)
- Create_Client_Wizard.steps[1].fields.Open_Savings_Account (not explicitly mentioned in description)
- Client_Detail_Page.action_buttons.Pending[0].fields.Activation_Date (not explicitly mentioned in description)
- Client_Detail_Page.action_buttons.Active[0].fields.Destination_Office (not explicitly mentioned in description)
- Client_Detail_Page.action_buttons.Active[2].fields.Closure_Reason (not explicitly mentioned in description)

**Fixes applied:**

- Remove phantoms from the AST that are not explicitly mentioned in the description.
- Ensure all required fields in the Client Detail page are included.

---

## Group Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing critical elements and contains phantoms.

**Missing:**

- Groups_Table.bulk_actions
- Bulk_Import_Groups_Page.import_history_table.row_actions
- Group_Detail_Page.fields (missing fields for group details)

**Phantoms (hallucinations):**

- Bulk_Import_Groups_Page.fields.Groups_Template.fields.Download_Button (button not in description)
- Bulk_Import_Groups_Page.fields.Groups_Template.fields.Office (dropdown not specified as required)
- Bulk_Import_Groups_Page.fields.Groups_Template.fields.Staff (dropdown not specified as required)

**Fixes applied:**

- Add bulk_actions to Groups_Table
- Add row_actions to Bulk_Import_Groups_Page.import_history_table
- Add fields to Group_Detail_Page for group details

---

## Center Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing critical elements and contains phantoms.

**Missing:**

- Bulk_Import_Centers_Page.fields
- Center_Detail_Tabs.tabs[0].fields.Groups
- Center_Detail_Tabs.tabs[1].fields.Loan_Accounts
- Center_Detail_Tabs.tabs[2].fields.Savings_Accounts
- Center_Detail_Tabs.tabs[3].fields.Notes
- Center_Detail_Tabs.tabs[4].fields.Calendar/Meeting

**Phantoms (hallucinations):**

- Centers_Table.bulk_actions[0] (Import Center button not in description)
- Centers_Table.bulk_actions[1] (Create Center button not in description)
- Bulk_Import_Centers_Page.submit_actions[0] (Submit button not in description)

**Fixes applied:**

- Remove the phantom actions from Centers_Table.bulk_actions
- Remove the phantom submit action from Bulk_Import_Centers_Page.submit_actions
- Add fields to Bulk_Import_Centers_Page
- Add fields to Center_Detail_Tabs.tabs[0] for Groups
- Add fields to Center_Detail_Tabs.tabs[1] for Loan Accounts
- Add fields to Center_Detail_Tabs.tabs[2] for Savings Accounts
- Add fields to Center_Detail_Tabs.tabs[3] for Notes
- Add fields to Center_Detail_Tabs.tabs[4] for Calendar/Meeting

---

## Loan Products

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and contains phantoms.

**Missing:**

- Create_Loan_Product_Stepper.steps[2].fields.Principal_Amount.constraints
- Create_Loan_Product_Stepper.steps[3].fields.Repayment_Strategy.required
- Create_Loan_Product_Stepper.steps[4].fields.Repaid_Every.required

**Phantoms (hallucinations):**

- Create_Loan_Product_Stepper.steps[5].fields.Search_and_Add_Charges (search-and-add interface not explicitly mentioned in description)

**Fixes applied:**

- Add constraints for Principal_Amount in Currency step.
- Mark Repayment_Strategy as required in Settings step.
- Mark Repaid_Every as required in Terms step.
- Remove Search_and_Add_Charges from Charges step.

---

## Savings Products

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing several required fields and contains phantoms.

**Missing:**

- Savings_Product_Stepper.steps[2].fields.Currency
- Savings_Product_Stepper.steps[2].fields.Decimal_Places
- Savings_Product_Stepper.steps[2].fields.Currency_In_Multiples_Of
- Savings_Product_Stepper.steps[3].fields.Nominal_Annual_Interest_Rate
- Savings_Product_Stepper.steps[3].fields.Interest_Compounding_Period
- Savings_Product_Stepper.steps[3].fields.Interest_Posting_Period
- Savings_Product_Stepper.steps[3].fields.Interest_Calculated_Using
- Savings_Product_Stepper.steps[3].fields.Days_in_Year
- Savings_Product_Stepper.steps[4].fields.Minimum_Opening_Balance
- Savings_Product_Stepper.steps[4].fields.Lock_in_Period
- Savings_Product_Stepper.steps[4].fields.Apply_Withdrawal_Fee_for_Transfers
- Savings_Product_Stepper.steps[4].fields.Minimum_Balance_for_Interest_Calculation
- Savings_Product_Stepper.steps[4].fields.Enforce_Minimum_Required_Balance
- Savings_Product_Stepper.steps[4].fields.Minimum_Required_Balance
- Savings_Product_Stepper.steps[4].fields.Is_Overdraft_Allowed
- Savings_Product_Stepper.steps[4].fields.Maximum_Overdraft_Amount
- Savings_Product_Stepper.steps[4].fields.Overdraft_Interest_Rate
- Savings_Product_Stepper.steps[4].fields.Enable_Withhold_Tax
- Savings_Product_Stepper.steps[4].fields.Tax_Group
- Savings_Product_Stepper.steps[4].fields.Enable_Dormancy_Tracking
- Savings_Product_Stepper.steps[4].fields.Days_to_Inactive
- Savings_Product_Stepper.steps[4].fields.Days_to_Dormancy
- Savings_Product_Stepper.steps[4].fields.Days_to_Escheat
- Fixed_Deposit_Product_Stepper.steps[5].fields.Pre_Mature_Closure_Applicable
- Fixed_Deposit_Product_Stepper.steps[5].fields.Pre_Closure_Penal_Interest
- Fixed_Deposit_Product_Stepper.steps[5].fields.Pre_Closure_Penal_Interest_On
- Fixed_Deposit_Product_Stepper.steps[6].fields.Minimum_Deposit_Term
- Fixed_Deposit_Product_Stepper.steps[6].fields.Maximum_Deposit_Term
- Fixed_Deposit_Product_Stepper.steps[6].fields.In_Multiples_Of
- Fixed_Deposit_Product_Stepper.steps[6].fields.Minimum_Deposit_Amount
- Fixed_Deposit_Product_Stepper.steps[6].fields.Maximum_Deposit_Amount
- Fixed_Deposit_Product_Stepper.steps[6].fields.Default_Deposit_Amount
- Recurring_Deposit_Product_Stepper.steps[7].fields.Mandatory_Recommended_Deposit_Amount
- Recurring_Deposit_Product_Stepper.steps[7].fields.Is_Mandatory_Deposit
- Recurring_Deposit_Product_Stepper.steps[7].fields.Recurring_Frequency

**Phantoms (hallucinations):**

- Savings_Product_Stepper.steps[5].fields.Predefined_Charges
- Fixed_Deposit_Product_Stepper.steps[5].fields.Predefined_Charges
- Recurring_Deposit_Product_Stepper.steps[5].fields.Predefined_Charges

**Fixes applied:**

- Add missing fields to Savings_Product_Stepper.steps[2] and steps[3] as per description.
- Add missing fields to Savings_Product_Stepper.steps[4] as per description.
- Add missing fields to Fixed_Deposit_Product_Stepper.steps[5] and steps[6] as per description.
- Add missing fields to Recurring_Deposit_Product_Stepper.steps[7] as per description.
- Remove phantom fields from all steppers.

---

## Share Products

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

There are missing required fields and phantoms present in the AST.

**Missing:**

- Create_Share_Product_Stepper.steps[2].fields.Currency (Currency is required but marked as not required)
- Create_Share_Product_Stepper.steps[4].fields.Minimum_Active_Period_Frequency (Minimum Active Period Frequency is required but marked as required)
- Create_Share_Product_Stepper.steps[4].fields.Lock_in_Period (Lock-in Period is required but marked as required)
- Create_Share_Product_Stepper.steps[7].fields.GL_Account_Mappings (GL account mappings for Cash-based are missing)

**Phantoms (hallucinations):**

- Create_Share_Product_Stepper.steps[3].fields.Nominal_Unit_Price (Nominal/Unit Price is not named correctly)
- Create_Share_Product_Stepper.steps[4].fields.Nominal_Shares_per_Client (Nominal Shares per Client is not named correctly)
- Create_Share_Product_Stepper.steps[6].fields (Charges step should have fields defined)

**Fixes applied:**

- Create_Share_Product_Stepper.steps[2].fields.Currency: change 'required' to true
- Create_Share_Product_Stepper.steps[4].fields.Minimum_Active_Period_Frequency: ensure it is marked as required
- Create_Share_Product_Stepper.steps[4].fields.Lock_in_Period: ensure it is marked as required
- Create_Share_Product_Stepper.steps[7].fields.GL_Account_Mappings: add fields for GL account mappings

---

## Charges

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and has phantoms.

**Missing:**

- Charge_Creation_Form.fields.Charge_Time_Type (required status missing)
- Charge_Creation_Form.fields.Tax_Group (missing from description)
- Charge_Creation_Form.fields.Payment_Mode (missing from description)

**Phantoms (hallucinations):**

- Charge_Creation_Form.fields.Charge_Time_Type.options (options inferred without explicit mention)
- Charge_Creation_Form.fields.Charge_Calculation_Type.options (options inferred without explicit mention)

**Fixes applied:**

- Charge_Creation_Form.fields.Charge_Time_Type: set required to true and include only relevant options based on entity type.
- Charge_Creation_Form.fields.Tax_Group: add this field as unspecified.
- Charge_Creation_Form.fields.Payment_Mode: add this field as unspecified.

---

## Floating Rates

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST contains several phantoms and missing elements related to the creation form and detail view.

**Missing:**

- Create_Floating_Rate_Form.fields.Is_Base_Lending_Rate.required (should be true)
- Create_Floating_Rate_Form.fields.Rate_Periods.item_fields.Is_Differential_Rate.required (should be true)
- Floating_Rates_Table.bulk_actions (should include '+ Create Floating Rate' button)

**Phantoms (hallucinations):**

- Floating_Rate_Detail_View.fields.Rate_History (not mentioned in description)
- Floating_Rate_Detail_View.fields.Edit_Option (not mentioned in description)

**Fixes applied:**

- Update Create_Floating_Rate_Form.fields.Is_Base_Lending_Rate.required to true
- Update Create_Floating_Rate_Form.fields.Rate_Periods.item_fields.Is_Differential_Rate.required to true
- Add a bulk action in Floating_Rates_Table for '+ Create Floating Rate'

---

## Delinquency Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing critical elements and contains phantoms.

**Missing:**

- Create_Delinquency_Bucket_Form.fields.Delinquency_Ranges.item_fields.Bucket_Name

**Phantoms (hallucinations):**

- Create_Delinquency_Range_Form.fields.Maximum_Age_Days (optional status not mentioned in description)
- Create_Delinquency_Bucket_Form.fields.Delinquency_Ranges.item_fields.Maximum_Age_Days (not specified in description)

**Fixes applied:**

- Create_Delinquency_Bucket_Form.fields.Delinquency_Ranges.item_fields.Bucket_Name: Add a required field for Bucket Name in the delinquency ranges.

---

## Loan Account

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing several critical elements and contains phantoms.

**Missing:**

- Loan_Application_Wizard.steps[1].fields.Repaid_Every.unit
- Loan_Detail_Tabs.tabs[0].fields.Status_Badge
- Loan_Detail_Tabs.tabs[0].fields.Status_Badge (color-coded status badges not represented)
- Loan_Detail_Tabs.tabs[1].fields.Installment_Number
- Loan_Detail_Tabs.tabs[1].fields.Due_Date
- Loan_Detail_Tabs.tabs[1].fields.Principal_Due
- Loan_Detail_Tabs.tabs[1].fields.Interest_Due
- Loan_Detail_Tabs.tabs[1].fields.Fees_Due
- Loan_Detail_Tabs.tabs[1].fields.Penalties_Due
- Loan_Detail_Tabs.tabs[1].fields.Total_Due
- Loan_Detail_Tabs.tabs[1].fields.Amounts_Paid
- Loan_Detail_Tabs.tabs[1].fields.Total_Outstanding
- Loan_Detail_Tabs.tabs[1].fields.Status_Indicators
- Loan_Detail_Tabs.tabs[2].fields.Date
- Loan_Detail_Tabs.tabs[2].fields.Type
- Loan_Detail_Tabs.tabs[2].fields.Amount
- Loan_Detail_Tabs.tabs[2].fields.Principal/Interest/Fees/Penalties_Portion
- Loan_Detail_Tabs.tabs[2].fields.Outstanding_Balance
- Loan_Detail_Tabs.tabs[3].fields.Charge_Name
- Loan_Detail_Tabs.tabs[3].fields.Amount
- Loan_Detail_Tabs.tabs[3].fields.Due_Date
- Loan_Detail_Tabs.tabs[3].fields.Paid
- Loan_Detail_Tabs.tabs[3].fields.Waived
- Loan_Detail_Tabs.tabs[3].fields.Outstanding

**Phantoms (hallucinations):**

- Loan_Application_Wizard.steps[1].fields.External_ID (not mentioned in description)
- Loan_Detail_Tabs.tabs[0].fields.Loan_Account_Number (not mentioned in description)
- Loan_Detail_Tabs.tabs[0].fields.Product_Name (not mentioned in description)
- Loan_Detail_Tabs.tabs[0].fields.Client_Name (not mentioned in description)
- Loan_Detail_Tabs.tabs[0].fields.Loan_Balance (not mentioned in description)
- Loan_Detail_Tabs.tabs[1].fields.Installments (not mentioned in description)
- Loan_Detail_Tabs.tabs[2].fields.Transaction_Table (not mentioned in description)
- Loan_Detail_Tabs.tabs[3].fields.Charge_Table (not mentioned in description)
- Loan_Detail_Tabs.tabs[4].fields.Collateral_Items (not mentioned in description)
- Loan_Detail_Tabs.tabs[5].fields.Notes_Table (not mentioned in description)
- Loan_Detail_Tabs.tabs[6].fields.Documents_Table (not mentioned in description)

**Fixes applied:**

- Add missing fields to Loan_Application_Wizard.steps[1] and Loan_Detail_Tabs as per description.
- Remove phantom fields that are not mentioned in the description.

---

## Savings Account

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and contains phantoms.

**Missing:**

- Savings_Account_Creation_Form.fields.Field_Officer
- Savings_Account_Creation_Form.fields.Charges.item_fields
- Savings_Account_Creation_Form.fields.Nominal_Annual_Interest_Rate
- Savings_Account_Creation_Form.fields.Lock_in_Period

**Phantoms (hallucinations):**

- Savings_Account_Creation_Form.fields.Nominal_Annual_Interest_Rate (unspecified type not in description)
- Savings_Account_Creation_Form.fields.Lock_in_Period (unspecified type not in description)
- Savings_Account_Action_Bar.states.Active.available_actions[0].fields.Payment_Type.options (options inferred without explicit mention)

**Fixes applied:**

- Add 'Field_Officer' field to 'Savings_Account_Creation_Form.fields'
- Define 'item_fields' for 'Charges' in 'Savings_Account_Creation_Form.fields'
- Change 'Nominal_Annual_Interest_Rate' type to 'unspecified' in 'Savings_Account_Creation_Form.fields'
- Change 'Lock_in_Period' type to 'unspecified' in 'Savings_Account_Creation_Form.fields'

---

## Share Account

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing several expected elements and contains phantoms.

**Missing:**

- Share_Account_Application_Form.fields.Share_Product.options
- Share_Account_Application_Form.fields.Savings_Account_for_Charges.options
- Share_Account_Detail_Tabs.tabs[0].fields.Date.type
- Share_Account_Detail_Tabs.tabs[0].fields.Type.type
- Share_Account_Detail_Tabs.tabs[0].fields.Number_of_Shares.type
- Share_Account_Detail_Tabs.tabs[0].fields.Unit_Price.type
- Share_Account_Detail_Tabs.tabs[0].fields.Amount.type
- Share_Account_Detail_Tabs.tabs[0].fields.Status.type
- Share_Account_Detail_Tabs.tabs[1].fields.Date.type
- Share_Account_Detail_Tabs.tabs[1].fields.Amount_Per_Share.type
- Share_Account_Detail_Tabs.tabs[1].fields.Total_Amount.type

**Phantoms (hallucinations):**

- Share_Account_Detail_Tabs.tabs[0].fields (fields should not be unspecified without description)
- Share_Account_Detail_Tabs.tabs[1].fields (fields should not be unspecified without description)

**Fixes applied:**

- Add options for Share_Product and Savings_Account_for_Charges fields in Share_Account_Application_Form.
- Specify types for fields in Purchased_Shares and Dividends tabs.

---

## Fixed & Recurring Deposit Accounts

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and contains phantoms.

**Missing:**

- FD_Account_Creation_Form.fields.Deposit_Period_Unit
- RD_Account_Creation_Form.fields.Deposit_Frequency

**Phantoms (hallucinations):**

- FD_Account_Creation_Form.fields.Fixed_Deposit_Product (not explicitly mentioned in description)
- RD_Account_Creation_Form.fields.Recurring_Deposit_Product (not explicitly mentioned in description)

**Fixes applied:**

- Add Deposit_Period_Unit field to FD_Account_Creation_Form
- Add Deposit_Frequency field to RD_Account_Creation_Form
- Remove Fixed_Deposit_Product field from FD_Account_Creation_Form
- Remove Recurring_Deposit_Product field from RD_Account_Creation_Form

---

## Accounting — Chart of Accounts

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing several expected elements and contains phantoms.

**Missing:**

- Chart_of_Accounts.sortable_columns[2] (Account Type is missing)
- Chart_of_Accounts.sortable_columns[3] (Usage is missing)
- Create_GL_Account_Form.fields.Manual_Entries_Allowed (checkbox is missing)
- Create_GL_Account_Form.fields.Description (field is missing)
- Create_GL_Account_Form.fields.Tag (dropdown is missing)

**Phantoms (hallucinations):**

- Chart_of_Accounts.row_actions[0] (Edit action is present but not explicitly named in the description)
- Chart_of_Accounts.row_actions[1] (Delete action is present but not explicitly named in the description)

**Fixes applied:**

- Add 'Account Type' to Chart_of_Accounts.sortable_columns
- Add 'Usage' to Chart_of_Accounts.sortable_columns
- Add 'Manual_Entries_Allowed' checkbox to Create_GL_Account_Form.fields
- Add 'Description' field to Create_GL_Account_Form.fields
- Add 'Tag' dropdown to Create_GL_Account_Form.fields

---

## Accounting — Journal Entries & Closures

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing items and phantoms identified in the AST.

**Missing:**

- Add_Journal_Entry_Form.fields.Entry_Lines.item_fields.Add_Row
- Add_Journal_Entry_Form.fields.Entry_Lines.item_fields.Amount (validation error for total debits and credits not specified)
- Journal_Entries_Table.filter_bar

**Phantoms (hallucinations):**

- Add_Journal_Entry_Form.fields.Currency (not specified in description)
- Create_Closure_Form.submit_actions[0] (Create Closure button not named in description)

**Fixes applied:**

- Add 'Add_Row' button to 'Add_Journal_Entry_Form.fields.Entry_Lines.item_fields'
- Specify validation error for total debits and credits in 'Add_Journal_Entry_Form.fields.Entry_Lines.item_fields.Amount'
- Add 'filter_bar' to 'Journal_Entries_Table' with fields for Office, GL Account, Date Range, Transaction ID, and Entry Type

---

## Accounting Rules & Financial Activity Mappings

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and contains phantoms.

**Missing:**

- Create_Rule_Form.fields.Office.required
- Financial_Activity_Mappings_Table.row_actions[0].action_name (Create Mapping button not in description)

**Phantoms (hallucinations):**

- Create_Rule_Form.fields.Debit_Tags_Debit_Account (not explicitly named in description)
- Create_Rule_Form.fields.Credit_Tags_Credit_Account (not explicitly named in description)
- Financial_Activity_Mappings_Table.columns.Financial_Activity (not explicitly named in description)

**Fixes applied:**

- Create_Rule_Form.fields.Office.required should be true
- Remove Create_Rule_Form.fields.Debit_Tags_Debit_Account
- Remove Create_Rule_Form.fields.Credit_Tags_Credit_Account
- Remove Financial_Activity_Mappings_Table.columns.Financial_Activity

---

## Provisioning

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Offices

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing the External ID field in the Create Office Form and contains a phantom for the Edit option in the Office Detail page.

**Missing:**

- Create_Office_Form.fields.External_ID

**Phantoms (hallucinations):**

- Office_Detail_Page.fields.Edit_Option (Edit option not in description)

**Fixes applied:**

- Add External_ID field to Create_Office_Form.fields
- Remove Edit_Option from Office_Detail_Page.fields

---

## Employees

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Teller & Cashier Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and contains phantoms.

**Missing:**

- Tellers_Table.row_actions[0].action_name (Edit action is not explicitly named in the description)
- Teller_Detail.fields.Cashiers.fields (fields for Cashiers section are missing)
- Cashier_Detail.fields.Opening_Balance (Opening Balance is not explicitly named in the description)
- Cashier_Detail.fields.Cash_In_Hand (Cash In Hand is not explicitly named in the description)

**Phantoms (hallucinations):**

- Create_Teller_Form.fields.Description (Description field is not explicitly required)
- Allocate_Cashier_Form.fields.Description (Description field is not explicitly required)
- Cashier_Detail.actions[0] (Allocate Cash action is not explicitly named in the description)
- Cashier_Detail.actions[1] (Settle Cash action is not explicitly named in the description)

**Fixes applied:**

- Add 'Edit' action to Tellers_Table.row_actions
- Add fields to Teller_Detail.fields.Cashiers
- Remove phantom fields from Create_Teller_Form and Allocate_Cashier_Form
- Remove phantom actions from Cashier_Detail.actions

---

## Users & Roles

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and contains phantoms.

**Missing:**

- Create_Role_Form.fields.Role_Name

**Phantoms (hallucinations):**

- Create_Role_Form.fields.Description (not specified in the description)
- Permissions_Page.fields.Permissions (not specified in the description)

**Fixes applied:**

- Add 'Role_Name' field to 'Create_Role_Form.fields'
- Remove 'Description' field from 'Create_Role_Form.fields'
- Remove 'Permissions' field from 'Permissions_Page.fields'

---

## Reports

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing critical elements and contains phantoms.

**Missing:**

- Reports_Page.row_actions[0].fields.Parameters_Form.fields.Loan_Product
- Reports_Page.row_actions[0].fields.Parameters_Form.fields.Date_Range
- Reports_Page.row_actions[0].fields.Parameters_Form.fields.Loan_Officer
- Reports_Page.row_actions[0].fields.Parameters_Form.fields.Fund

**Phantoms (hallucinations):**

- Reports_Page.row_actions[0].action_name (View Parameters button not in description)

**Fixes applied:**

- Remove Reports_Page.row_actions[0].action_name
- Add Reports_Page.row_actions[0].fields.Parameters_Form.fields.Loan_Product with type and required status
- Add Reports_Page.row_actions[0].fields.Parameters_Form.fields.Date_Range with type and required status
- Add Reports_Page.row_actions[0].fields.Parameters_Form.fields.Loan_Officer with type and required status
- Add Reports_Page.row_actions[0].fields.Parameters_Form.fields.Fund with type and required status

---

## Account Transfers & Standing Instructions

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and contains phantoms.

**Missing:**

- Account_Transfers_Form.fields.From_Office
- Account_Transfers_Form.fields.From_Client
- Account_Transfers_Form.fields.From_Account
- Account_Transfers_Form.fields.To_Office
- Account_Transfers_Form.fields.To_Client
- Account_Transfers_Form.fields.To_Account
- Create_Standing_Instruction_Form.fields.From_Account
- Create_Standing_Instruction_Form.fields.To_Account
- Create_Standing_Instruction_Form.fields.Amount
- Create_Standing_Instruction_Form.fields.Validity_From
- Create_Standing_Instruction_Form.fields.Validity_Till

**Phantoms (hallucinations):**

- Create_Standing_Instruction_Form.fields.Transfer_Type (not mentioned in description)
- Create_Standing_Instruction_Form.fields.Priority (not mentioned in description)
- Create_Standing_Instruction_Form.fields.Recurrence_Frequency (not mentioned in description)
- Create_Standing_Instruction_Form.fields.Recurrence_Interval (not mentioned in description)

**Fixes applied:**

- Add missing fields to Account_Transfers_Form: From_Office, From_Client, From_Account, To_Office, To_Client, To_Account
- Add missing fields to Create_Standing_Instruction_Form: From_Account, To_Account, Amount, Validity_From, Validity_Till
- Remove phantom fields from Create_Standing_Instruction_Form: Transfer_Type, Priority, Recurrence_Frequency, Recurrence_Interval

---

## Tax Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST contains several phantoms and missing elements related to the Tax Groups page and its components.

**Missing:**

- Create_Tax_Group_Form.fields.Tax_Components.item_fields.Start_Date
- Create_Tax_Group_Form.fields.Tax_Components.item_fields.End_Date

**Phantoms (hallucinations):**

- Create_Tax_Group_Form.fields.Tax_Components.item_fields.Credit_Account_Type (not explicitly mentioned in description)
- Create_Tax_Group_Form.fields.Tax_Components.item_fields.Credit_Account (not explicitly mentioned in description)

**Fixes applied:**

- Create_Tax_Group_Form.fields.Tax_Components.item_fields.Credit_Account_Type: remove this field as it is not mentioned in the description.
- Create_Tax_Group_Form.fields.Tax_Components.item_fields.Credit_Account: remove this field as it is not mentioned in the description.

---

## Organization Settings

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing required fields and contains phantoms.

**Missing:**

- Working_Days_Page.fields.Repayment_Rescheduling
- Funds_Page.submit_actions[0].element_name (Create Fund button not in description)
- Payment_Types_Page.submit_actions[0].element_name (+ Create button not in description)

**Phantoms (hallucinations):**

- Holidays_Page.submit_actions[0].on_success (opens holiday creation form not in description)
- Funds_Page.submit_actions[0].on_success (opens fund creation form not in description)
- Payment_Types_Page.submit_actions[0].on_success (adds new payment type not in description)

**Fixes applied:**

- Add 'Repayment_Rescheduling' field to 'Working_Days_Page.fields'
- Remove 'on_success' from 'Holidays_Page.submit_actions[0]'
- Remove 'on_success' from 'Funds_Page.submit_actions[0]'
- Remove 'on_success' from 'Payment_Types_Page.submit_actions[0]'

---

## System Administration

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing critical elements and contains phantoms.

**Missing:**

- Manage_Scheduler_Jobs.columns[1] (Is_Active toggle not represented)
- Manage_Scheduler_Jobs.row_actions[0] (Edit CRON Expression action not represented)
- Manage_Codes.row_actions[0] (Add/Edit/Reorder/Deactivate actions not represented)
- Audit_Trails.row_actions[0] (Approve and Reject buttons not represented)

**Phantoms (hallucinations):**

- Manage_Scheduler_Jobs.bulk_actions[0] (Start All button not in description)
- Manage_Scheduler_Jobs.bulk_actions[1] (Stop All button not in description)
- Manage_Data_Tables.fields.Column_Definitions.item_fields.Type.options[7] (dropdown type not mentioned in description)

**Fixes applied:**

- Add Is_Active toggle to Manage_Scheduler_Jobs.columns
- Add Edit CRON Expression action to Manage_Scheduler_Jobs.row_actions
- Add Add/Edit/Reorder/Deactivate actions to Manage_Codes.row_actions
- Add Approve and Reject buttons to Audit_Trails.row_actions

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described, with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---
