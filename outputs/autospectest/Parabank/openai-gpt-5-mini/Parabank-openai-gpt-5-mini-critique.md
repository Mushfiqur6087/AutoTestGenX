# Semantic Critique — Parabank

Generated: 2026-05-25T15:44:48.806981Z

## Login

**Verdict:** yes  
**Forced ship:** no  

AST matches the described interactive elements and behaviors; only a minor inferred navigation target on the 'Forgot Password?' link was added.

**Missing:** none

**Phantoms (hallucinations):**

- Login_Form.links[0].on_click (navigates to Forgot Password page) - the description names the link but does not specify its navigation target

---

## Register

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures all interactive fields, the State dropdown options, validation constraints (including patterns and automatic formatting), the Register submit action, success message and redirect, and error handling.

**Missing:** none

**Phantoms:** none

---

## Accounts Overview

**Verdict:** yes  
**Forced ship:** no  

AST correctly captures the interactive elements (clickable masked Account Number with row action and masking constraint, table columns, and default sort by Open_Date) and contains no missing or phantom critical items.

**Missing:** none

**Phantoms:** none

---

## Open New Account

**Verdict:** yes  
**Forced ship:** no  

The AST accurately captures the interactive elements (account-type selection, initial deposit field with conditional minimums, funding account dropdown, realtime validation, and the Open Account action with success message and redirect) and contains no extraneous items.

**Missing:** none

**Phantoms:** none

---

## Transfer Funds

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the described interactive elements and validations; only a minor inferred label for the submit action was added.

**Missing:** none

**Phantoms (hallucinations):**

- Transfer_Form.submit_actions[0].element_name (Submit Transfer button label was not explicitly named in the description)

---

## Payments

**Verdict:** yes  
**Forced ship:** no  

AST includes the payment form with all described interactive fields, account-number match and funds checks, submit action, success/failure behaviors, and inline error handling; no extraneous elements found.

**Missing:** none

**Phantoms:** none

---

## Request Loan

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive elements, validations, and simulated credit behavior; only minor inferred items are present.

**Missing:** none

**Phantoms (hallucinations):**

- components.Loan_Request_Form.submit_actions[0] (Submit Application button label not explicitly named in the description)
- components.Loan_Request_Form.fields.*.required (fields marked required were not explicitly stated in the description)

---

## Update Contact Info

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the editable pre-filled form, all seven fields, submit button, validation behavior, and success/failure outcomes with no extra elements.

**Missing:** none

**Phantoms:** none

---

## Manage Cards

**Verdict:** yes  
**Forced ship:** no  

AST correctly captures both forms, all interactive fields (including travel notice details), submit actions, and the specified validations/results; no significant missing items or extraneous elements found.

**Missing:** none

**Phantoms:** none

---

## Investments

**Verdict:** yes  
**Forced ship:** no  

AST includes both forms, all specified fields, validation rules, submit actions, and success/failure behaviors matching the description.

**Missing:** none

**Phantoms:** none

---

## Account Statements

**Verdict:** yes  
**Forced ship:** no  

AST includes both forms, all interactive fields, validation rules, and success/failure behaviors described, with no significant missing elements or unsupported phantoms.

**Missing:** none

**Phantoms:** none

---

## Security Settings

**Verdict:** yes  
**Forced ship:** no  

The AST accurately captures the collapsible panel, the change-password form with all three password fields, the Change Password button, validation constraints (current-password verification, strong-password policy, match check), and success/error behaviors; no missing or extraneous interactive elements found.

**Missing:** none

**Phantoms:** none

---

## Support Center

**Verdict:** yes  
**Forced ship:** no  

AST accurately models both forms and their validations; only minor issues (non-critical) around Reason_for_Call being marked required and Phone_Number type labeled 'unspecified'.

**Missing:**

- Schedule_Callback_Form.fields.Phone_Number.type (expected a phone/tel input type rather than 'unspecified')

**Phantoms (hallucinations):**

- Schedule_Callback_Form.fields.Reason_for_Call.required (the description did not state this field was required)

---
