# Workflow Critique — Parabank

Generated: 2026-06-04T14:24:43.772554Z

## Login

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

The workflow for the failed login attempt has an incorrect on_success message.

**Missing workflows:** none

**Phantom workflows:** none

**Fixes applied:**

- Update WF-002 on_success to match the AST: 'Incorrect email or password. Please try again.'

---

## Register

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions.

**Missing workflows:**

- No workflow for Sign_Up_Form: action=Register

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for Sign_Up_Form: action=Register

---

## Accounts Overview

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for row actions in the data table.

**Missing workflows:**

- No workflow for data_table: action=View Account Number

**Phantom workflows:** none

**Fixes applied:**

- Add workflow for data_table: action=View Account Number

---

## Open New Account

**Verdict:** yes  
**Forced ship:** no  

All required workflows are present and correctly defined.

**Missing workflows:** none

**Phantom workflows:** none

---

## Transfer Funds

**Verdict:** yes  
**Forced ship:** no  

All workflows are present and correctly defined for the form actions.

**Missing workflows:** none

**Phantom workflows:** none

---

## Payments

**Verdict:** retry (forced ship)  
**Forced ship:** yes  

Missing workflows for form submit actions based on constraints.

**Missing workflows:**

- No workflow for Payment_Form: action=Pay with constraints: account numbers must match
- No workflow for Payment_Form: action=Pay with constraints: must have sufficient funds

**Phantom workflows:** none

**Fixes applied:**

- Add workflows for Payment_Form: action=Pay with constraints: account numbers must match
- Add workflows for Payment_Form: action=Pay with constraints: must have sufficient funds

---

## Request Loan

**Verdict:** yes  
**Forced ship:** no  

All workflows are present and correctly defined for the loan application process.

**Missing workflows:** none

**Phantom workflows:** none

---

## Update Contact Info

**Verdict:** yes  
**Forced ship:** no  

All required workflows are present and correct.

**Missing workflows:** none

**Phantom workflows:** none

---

## Manage Cards

**Verdict:** yes  
**Forced ship:** no  

All workflows are present and correctly defined according to the AST.

**Missing workflows:** none

**Phantom workflows:** none

---

## Investments

**Verdict:** yes  
**Forced ship:** no  

All workflows are present and correctly defined according to the AST and description.

**Missing workflows:** none

**Phantom workflows:** none

---

## Account Statements

**Verdict:** yes  
**Forced ship:** no  

All workflows are present and correctly defined according to the AST.

**Missing workflows:** none

**Phantom workflows:** none

---

## Security Settings

**Verdict:** yes  
**Forced ship:** no  

All required workflows are present and correctly defined.

**Missing workflows:** none

**Phantom workflows:** none

---

## Support Center

**Verdict:** yes  
**Forced ship:** no  

All workflows are present and correctly defined for the actions in the forms.

**Missing workflows:** none

**Phantom workflows:** none

---
