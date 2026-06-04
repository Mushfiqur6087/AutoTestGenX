# Semantic Critique — Parabank

Generated: 2026-06-04T14:24:43.756349Z

## Login

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described, with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Register

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST contains several phantoms and missing elements related to validation constraints and the handling of the Confirm Password field.

**Missing:**

- Sign_Up_Form.fields.Confirm_Password.constraints

**Phantoms (hallucinations):**

- Sign_Up_Form.fields.ZIP_Code.type (should be 'text' instead of 'number')
- Sign_Up_Form.fields.Phone_Number.type (should be 'text' instead of 'number')
- Sign_Up_Form.fields.Social_Security_Number.type (should be 'text' instead of 'number')

**Fixes applied:**

- Add constraints to Confirm_Password: Sign_Up_Form.fields.Confirm_Password.constraints
- Change type of ZIP_Code to 'text': Sign_Up_Form.fields.ZIP_Code.type
- Change type of Phone_Number to 'text': Sign_Up_Form.fields.Phone_Number.type
- Change type of Social_Security_Number to 'text': Sign_Up_Form.fields.Social_Security_Number.type

---

## Accounts Overview

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing several expected elements and contains phantoms.

**Missing:**

- Accounts_Table.footer_row
- Accounts_Table.columns.Account_Number.masking

**Phantoms (hallucinations):**

- Accounts_Table.row_actions[0] (View Account Number action not in description)

**Fixes applied:**

- Add footer row to Accounts_Table
- Add masking for Account_Number in Accounts_Table.columns.Account_Number

---

## Open New Account

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described, with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Transfer Funds

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing critical elements related to external transfers and error handling.

**Missing:**

- Transfer_Form.fields.Destination_Options.item_fields.Internal_Account_Number
- Transfer_Form.submit_actions[0].constraints[0] (contextual error for insufficient funds)
- Transfer_Form.submit_actions[0].constraints[1] (contextual error for account numbers do not match)

**Phantoms:** none

**Fixes applied:**

- Add Internal_Account_Number field under Destination_Options.item_fields for internal transfers.
- Add contextual error messages for insufficient funds and account number mismatch under submit_actions constraints.

---

## Payments

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described, with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Request Loan

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements and constraints described, with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Update Contact Info

**Verdict:** yes  
**Forced ship:** no  

The AST correctly represents all interactive elements and their behaviors as described.

**Missing:** none

**Phantoms:** none

---

## Manage Cards

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing critical elements and contains phantoms.

**Missing:**

- Card_Request_Form.fields.Shipping_Address.constraints[0]
- Card_Controls_Form.fields.New_Spending_Limit.constraints[0]
- Card_Controls_Form.fields.Card_Status.constraints[0]

**Phantoms (hallucinations):**

- Card_Request_Form.fields.Account_to_Link (unspecified type not defined in description)
- Card_Controls_Form.fields.Travel_Notice.type (repeating_group not defined in description)

**Fixes applied:**

- Card_Request_Form.fields.Shipping_Address.constraints: Add 'address must be complete'
- Card_Controls_Form.fields.New_Spending_Limit.constraints: Add 'must be a valid numeric limit'
- Card_Controls_Form.fields.Card_Status.constraints: Add 'must be a valid status transition'
- Card_Request_Form.fields.Account_to_Link.type: Change from 'unspecified' to 'dropdown'
- Card_Controls_Form.fields.Travel_Notice.type: Change from 'repeating_group' to 'group'

---

## Investments

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST contains multiple phantoms and missing elements related to validation errors and inline feedback.

**Missing:**

- Trade_Funds_Form.fields.Quantity.constraints[1]
- Trade_Funds_Form.submit_actions[0].constraints[1]
- Recurring_Investment_Plan_Form.fields.Contribution_Amount.constraints[1]
- Recurring_Investment_Plan_Form.submit_actions[0].constraints[0]

**Phantoms (hallucinations):**

- Trade_Funds_Form.fields.Funding_or_Destination_Account.constraints[0] (constraint not explicitly mentioned in description)
- Recurring_Investment_Plan_Form.fields.Fund_Symbol.constraints[0] (no constraints mentioned in description)
- Recurring_Investment_Plan_Form.fields.Funding_Account.constraints[0] (constraint not explicitly mentioned in description)

**Fixes applied:**

- Add validation error messages for Trade_Funds_Form.fields.Quantity and Trade_Funds_Form.submit_actions[0].constraints
- Add validation error messages for Recurring_Investment_Plan_Form.fields.Contribution_Amount and Recurring_Investment_Plan_Form.submit_actions[0].constraints
- Remove phantom constraints from Trade_Funds_Form.fields.Funding_or_Destination_Account and Recurring_Investment_Plan_Form.fields.Fund_Symbol and Recurring_Investment_Plan_Form.fields.Funding_Account

---

## Account Statements

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The AST is missing the 'Generate Statement' button's constraints and has a phantom constraint in the E_Statement_Preference_Form.

**Missing:**

- Generate_Statement_Form.submit_actions[0].constraints[0] (missing validation for Statement_Period)

**Phantoms (hallucinations):**

- E_Statement_Preference_Form.submit_actions[0].constraints[0] (constraint 'Email_Address must be valid' is redundant as it's already specified in the Email_Address field)

**Fixes applied:**

- Add 'Statement_Period must be valid' to Generate_Statement_Form.submit_actions[0].constraints
- Remove the redundant constraint from E_Statement_Preference_Form.submit_actions[0].constraints

---

## Security Settings

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements described, with no missing items or phantoms.

**Missing:** none

**Phantoms:** none

---

## Support Center

**Verdict:** yes  
**Forced ship:** no  

The AST accurately reflects the interactive elements and constraints described.

**Missing:** none

**Phantoms:** none

---
