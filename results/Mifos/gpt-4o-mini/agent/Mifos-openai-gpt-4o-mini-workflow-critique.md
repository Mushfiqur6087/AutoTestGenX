# Workflow Critique — Mifos

Generated: 2026-06-04T14:20:14.490293Z

## Login

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for the form's submit action under different conditions.

**Missing workflows:**

- No workflow for Login_Form: action=Login with conditional branch=Username == '' OR Password == ''

**Phantom workflows:** none

**Fixes applied:**

- Add a workflow for Login_Form: action=Login with conditional branch=Username == '' OR Password == ''

---

## Home Page

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflow for the Search Activity input field.

**Missing workflows:**

- No workflow for Search_Activity_Input: action=Search

**Phantom workflows:** none

**Fixes applied:**

- Add a workflow for Search_Activity_Input with the appropriate terminal action.

---

## Dashboard

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form actions and state actions.

**Missing workflows:**

- No workflow for Search_Activity_Field: action=Search Activity

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Search_Activity_Field: action=Search Activity

---

## Global Search

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for search results and entity selection.

**Missing workflows:**

- No workflow for Search_Results: action=select entity

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Search_Results: action=select entity

---

## Client Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for some form submit actions and state-action pairs.

**Missing workflows:**

- No workflow for data_table: row_action=View
- No workflow for state_bound_action_bar: state=Pending, action=Activate
- No workflow for state_bound_action_bar: state=Active, action=Edit
- No workflow for state_bound_action_bar: state=Active, action=Transfer Client
- No workflow for state_bound_action_bar: state=Active, action=Close
- No workflow for state_bound_action_bar: state=Active, action=Add Charge
- No workflow for state_bound_action_bar: state=Active, action=New Loan
- No workflow for state_bound_action_bar: state=Active, action=New Savings
- No workflow for state_bound_action_bar: state=Active, action=New Share Account
- No workflow for state_bound_action_bar: state=Closed, action=Reactivate

**Phantom workflows:** none

**Fixes applied:**

- Generate workflows for missing row actions and state-action pairs.

---

## Group Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for the Bulk Import Groups page and the Collection Sheet feature.

**Missing workflows:**

- No workflow for Bulk_Import_Groups_Page: action=Download_Button
- No workflow for Bulk_Import_Groups_Page: action=File_Picker
- No workflow for Collection_Sheet_Feature: action=Generate Collection Sheet

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for missing actions in Bulk_Import_Groups_Page and Collection_Sheet_Feature

---

## Center Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for the data table row action 'View'.

**Missing workflows:**

- No workflow for data_table: action=View

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for data_table: action=View

---

## Loan Products

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions in the Create Loan Product stepper.

**Missing workflows:**

- No workflow for Create_Loan_Product_Stepper: step=1, action=Submit
- No workflow for Create_Loan_Product_Stepper: step=2, action=Submit
- No workflow for Create_Loan_Product_Stepper: step=3, action=Submit
- No workflow for Create_Loan_Product_Stepper: step=4, action=Submit
- No workflow for Create_Loan_Product_Stepper: step=5, action=Submit
- No workflow for Create_Loan_Product_Stepper: step=6, action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Generate workflows for Create_Loan_Product_Stepper: step=1, action=Submit
- Generate workflows for Create_Loan_Product_Stepper: step=2, action=Submit
- Generate workflows for Create_Loan_Product_Stepper: step=3, action=Submit
- Generate workflows for Create_Loan_Product_Stepper: step=4, action=Submit
- Generate workflows for Create_Loan_Product_Stepper: step=5, action=Submit
- Generate workflows for Create_Loan_Product_Stepper: step=6, action=Submit

---

## Savings Products

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for forms in the stepper wizards.

**Missing workflows:**

- No workflow for Savings_Product_Stepper: step=1, action=Submit
- No workflow for Fixed_Deposit_Product_Stepper: step=1, action=Submit
- No workflow for Recurring_Deposit_Product_Stepper: step=1, action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Generate workflows for Savings_Product_Stepper: step=1, action=Submit
- Generate workflows for Fixed_Deposit_Product_Stepper: step=1, action=Submit
- Generate workflows for Recurring_Deposit_Product_Stepper: step=1, action=Submit

---

## Share Products

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions and state actions.

**Missing workflows:**

- No workflow for Create_Share_Product_Stepper: step=1, action=Create Share Product

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Create_Share_Product_Stepper: step=1, action=Create Share Product

---

## Charges

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions.

**Missing workflows:**

- No workflow for Charge_Creation_Form: action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Charge_Creation_Form: action=Submit

---

## Floating Rates

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions and state actions.

**Missing workflows:**

- No workflow for Create_Floating_Rate_Form: submit_action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Create_Floating_Rate_Form: submit_action=Submit

---

## Delinquency Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions.

**Missing workflows:**

- No workflow for Create_Delinquency_Range_Form: terminal_action=Submit
- No workflow for Create_Delinquency_Bucket_Form: terminal_action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for Create_Delinquency_Range_Form and Create_Delinquency_Bucket_Form with terminal_action=Submit

---

## Loan Account

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions and state actions.

**Missing workflows:**

- No workflow for Loan_Application_Wizard: action=Submit
- No workflow for state_bound_action_bar: state=Pending Approval, action=Approve
- No workflow for state_bound_action_bar: state=Pending Approval, action=Reject
- No workflow for state_bound_action_bar: state=Pending Approval, action=Withdraw
- No workflow for state_bound_action_bar: state=Pending Approval, action=Delete
- No workflow for state_bound_action_bar: state=Approved, action=Disburse
- No workflow for state_bound_action_bar: state=Approved, action=Undo Approval
- No workflow for state_bound_action_bar: state=Active, action=Make Repayment
- No workflow for state_bound_action_bar: state=Active, action=Waive Interest
- No workflow for state_bound_action_bar: state=Active, action=Write Off
- No workflow for state_bound_action_bar: state=Active, action=Close
- No workflow for state_bound_action_bar: state=Active, action=Reschedule
- No workflow for state_bound_action_bar: state=Active, action=Prepay Loan
- No workflow for state_bound_action_bar: state=Active, action=Foreclosure
- No workflow for state_bound_action_bar: state=Active, action=Charge Off
- No workflow for state_bound_action_bar: state=Active, action=Assign Loan Officer

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Loan_Application_Wizard: action=Submit
- Add workflow for state_bound_action_bar: state=Pending Approval, action=Approve
- Add workflow for state_bound_action_bar: state=Pending Approval, action=Reject
- Add workflow for state_bound_action_bar: state=Pending Approval, action=Withdraw
- Add workflow for state_bound_action_bar: state=Pending Approval, action=Delete
- Add workflow for state_bound_action_bar: state=Approved, action=Disburse
- Add workflow for state_bound_action_bar: state=Approved, action=Undo Approval
- Add workflow for state_bound_action_bar: state=Active, action=Make Repayment
- Add workflow for state_bound_action_bar: state=Active, action=Waive Interest
- Add workflow for state_bound_action_bar: state=Active, action=Write Off
- Add workflow for state_bound_action_bar: state=Active, action=Close
- Add workflow for state_bound_action_bar: state=Active, action=Reschedule
- Add workflow for state_bound_action_bar: state=Active, action=Prepay Loan
- Add workflow for state_bound_action_bar: state=Active, action=Foreclosure
- Add workflow for state_bound_action_bar: state=Active, action=Charge Off
- Add workflow for state_bound_action_bar: state=Active, action=Assign Loan Officer

---

## Savings Account

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for the data table actions in the Savings Account Detail.

**Missing workflows:**

- No workflow for data_table: row_action=View/Details

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for missing row actions in the Savings Account Detail data table.

---

## Share Account

**Verdict:** yes  
**Forced ship:** no  

All workflows are present and correctly defined according to the AST and description.

**Missing workflows:** none

**Phantom workflows:** none

---

## Fixed & Recurring Deposit Accounts

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions.

**Missing workflows:**

- No workflow for FD_Account_Creation_Form: terminal_action=Submit
- No workflow for RD_Account_Creation_Form: terminal_action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for FD_Account_Creation_Form: terminal_action=Submit
- Add workflows for RD_Account_Creation_Form: terminal_action=Submit

---

## Accounting — Chart of Accounts

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions.

**Missing workflows:**

- No workflow for Create_GL_Account_Form: terminal_action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Create_GL_Account_Form: terminal_action=Submit

---

## Accounting — Journal Entries & Closures

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions.

**Missing workflows:**

- No workflow for Add_Journal_Entry_Form: action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Add_Journal_Entry_Form: action=Submit

---

## Accounting Rules & Financial Activity Mappings

**Verdict:** yes  
**Forced ship:** no  

All workflows are present and correctly match the actions defined in the AST.

**Missing workflows:** none

**Phantom workflows:** none

---

## Provisioning

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions and state actions.

**Missing workflows:**

- No workflow for Creation_Form: action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Creation_Form: action=Submit

---

## Offices

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions and state actions.

**Missing workflows:**

- No workflow for Create_Office_Form: submit action=Create Office

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Create_Office_Form: submit action=Create Office

---

## Employees

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow for submitting the Create Employee form is missing.

**Missing workflows:**

- No workflow for Create_Employee_Form: submit_action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add a workflow for Create_Employee_Form: submit_action=Submit

---

## Teller & Cashier Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions and state actions.

**Missing workflows:**

- No workflow for Create_Teller_Form: terminal_action=Submit
- No workflow for Allocate_Cashier_Form: terminal_action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for Create_Teller_Form and Allocate_Cashier_Form submit actions.

---

## Users & Roles

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions and state actions.

**Missing workflows:**

- No workflow for Create_User_Form: terminal_action=Submit
- No workflow for Create_Role_Form: terminal_action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for Create_User_Form and Create_Role_Form submit actions.

---

## Reports

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions.

**Missing workflows:**

- No workflow for data_table: action=View Parameters, terminal action=Run_Report

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for data_table: action=View Parameters, terminal action=Run_Report

---

## Account Transfers & Standing Instructions

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for the Create Standing Instruction form and no row actions in the Standing Instructions table.

**Missing workflows:**

- No workflow for Create_Standing_Instruction_Form: action=Submit
- No workflow for Standing_Instructions_Table: action=Enable
- No workflow for Standing_Instructions_Table: action=Disable
- No workflow for Standing_Instructions_Table: action=Delete

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for Create_Standing_Instruction_Form: action=Submit
- Add workflows for Standing_Instructions_Table: action=Enable
- Add workflows for Standing_Instructions_Table: action=Disable
- Add workflows for Standing_Instructions_Table: action=Delete

---

## Tax Management

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions and state actions.

**Missing workflows:**

- No workflow for Create_Tax_Group_Form: action=+ Create Tax Group
- No workflow for Create_Tax_Component_Form: action=+ Create Tax Component

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for missing form submit actions.
- Add workflows for Create_Tax_Group_Form and Create_Tax_Component_Form.

---

## Organization Settings

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions and state actions.

**Missing workflows:**

- No workflow for Create_Holiday_Form: submit action=Submit
- No workflow for Working_Days_Page: submit action=Submit
- No workflow for Bulk_Import_Page: submit action=Upload

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Create_Holiday_Form: submit action=Submit
- Add workflow for Working_Days_Page: submit action=Submit
- Add workflow for Bulk_Import_Page: submit action=Upload

---

## System Administration

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions and state actions.

**Missing workflows:**

- No workflow for Manage_Data_Tables: action=Submit

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Manage_Data_Tables: action=Submit

---

## Logout

**Verdict:** yes  
**Forced ship:** no  

All workflows are accounted for and correctly defined.

**Missing workflows:** none

**Phantom workflows:** none

---
