# Semantic Critique — Parabank

Generated: 2026-05-22T21:34:18.810093Z

## Login

**Verdict:** yes  
**Forced ship:** no  

AST correctly captures the form fields, validations, submit behavior, success/failure outcomes, and the Forgot Password link; only a minor inference was made about the link's navigation target.

**Missing:** none

**Phantoms (hallucinations):**

- Forgot_Password_Link.on_click (navigates to Password Reset page — destination not explicitly stated in description)

---

## Register

**Verdict:** yes  
**Forced ship:** no  

The AST accurately includes all interactive elements (all required fields, state dropdown with options, validation constraints including patterns and auto-formatting, submit action with success message and redirect, and failure behavior), with no significant missing items or extraneous phantoms.

**Missing:** none

**Phantoms:** none

---

## Accounts Overview

**Verdict:** yes  
**Forced ship:** no  

The AST accurately captures the interactive elements: welcome message, masked clickable account number link, table columns including open date, footer total balance, and ordering; no critical items missing or extraneous.

**Missing:** none

**Phantoms:** none

---

## Open New Account

**Verdict:** yes  
**Forced ship:** no  

AST correctly captures all interactive elements (account-type selection, deposit amount input, funding account dropdown, Open Account button), validations (minimums per account type, numeric check, funding sufficiency), real-time errors, and success redirect.

**Missing:** none

**Phantoms:** none

---

## Transfer Funds

**Verdict:** yes  
**Forced ship:** no  

The AST correctly represents the described interactive elements, validations, and conditional destination logic with no missing or extraneous elements.

**Missing:** none

**Phantoms:** none

---

## Payments

**Verdict:** yes  
**Forced ship:** no  

The AST includes the form, all listed fields (including dropdown and numeric amount), the Pay button, account-match and funds checks, success and inline-failure behaviors—matching the description.

**Missing:** none

**Phantoms:** none

---

## Request Loan

**Verdict:** yes  
**Forced ship:** no  

The AST accurately represents the interactive elements (loan type selection, loan amount with type-specific ranges, down payment, collateral account dropdown, validations, and credit engine behavior) and matches the described success/failure outcomes.

**Missing:** none

**Phantoms:** none

---

## Update Contact Info

**Verdict:** yes  
**Forced ship:** no  

The AST correctly includes the editable pre-filled form fields, the Update Profile submit action, per-field validation, success message with data refresh, and failure behavior with field highlights and an inline error banner.

**Missing:** none

**Phantoms:** none

---

## Manage Cards

**Verdict:** yes  
**Forced ship:** no  

The AST captures the two forms, their fields, constraints, and submit behaviors as described; only a minor inference was made about Travel_Notice being a repeating group with Start_Date/End_Date fields.

**Missing:** none

**Phantoms (hallucinations):**

- Card_Controls_Form.fields.Travel_Notice (modeled as a repeating_group with Start_Date/End_Date and Destination — the description only mentioned optional dates and destinations but did not specify multiplicity or explicit start/end field names)

---

## Investments

**Verdict:** yes  
**Forced ship:** no  

AST accurately captures the interactive forms, fields, validations, conditional checks, and submit behaviors described; no critical elements are missing.

**Missing:** none

**Phantoms:** none

---

## Account Statements

**Verdict:** yes  
**Forced ship:** no  

AST correctly captures both forms, their fields, buttons, validations, and success/failure behaviors; only minor inferred conditionals are present.

**Missing:** none

**Phantoms (hallucinations):**

- Generate_Statement_Form.fields.Month_Year.visible_when (conditional visibility inferred though description did not explicitly state visibility rules)
- EStatement_Preference_Form.fields.Email_Address.required_when (required-when inference — description did not explicitly state the email is required only when Paperless is checked)

---

## Security Settings

**Verdict:** yes  
**Forced ship:** no  

AST matches the description: collapsible panel containing the change-password form with the three password fields, Change Password button, verification/constraints, success message, and validation behavior.

**Missing:** none

**Phantoms:** none

---

## Support Center

**Verdict:** yes  
**Forced ship:** no  

The AST accurately captures both forms, their fields, validation constraints, submit actions, and success/failure behaviors as described.

**Missing:** none

**Phantoms:** none

---
