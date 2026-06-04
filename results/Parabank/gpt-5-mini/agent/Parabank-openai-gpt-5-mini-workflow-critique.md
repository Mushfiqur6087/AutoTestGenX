# Workflow Critique — Parabank

Generated: 2026-05-25T15:44:48.821004Z

## Login

**Verdict:** yes  
**Forced ship:** no  

Workflows cover the form submit action 'Sign In' and the 'Forgot Password?' link, no missing state/form/table actions, no phantoms, and on_success values match the AST.

**Missing workflows:** none

**Phantom workflows:** none

---

## Register

**Verdict:** yes  
**Forced ship:** no  

The provided workflow covers the form's Register submit action, matches the AST on_success text, and no phantom or conditional-branch issues were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Accounts Overview

**Verdict:** yes  
**Forced ship:** no  

All data_table row actions are covered by workflows; no phantoms, conditional issues, or empty on_success values detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Open New Account

**Verdict:** yes  
**Forced ship:** no  

Workflows correctly cover the form submit action for both Account_Type conditions; no missing or phantom workflows detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Transfer Funds

**Verdict:** yes  
**Forced ship:** no  

Workflows cover both Transfer_Type branches and match the form's submit action and on_success; no missing workflows, phantoms, or conditional errors were found.

**Missing workflows:** none

**Phantom workflows:** none

---

## Payments

**Verdict:** yes  
**Forced ship:** no  

Workflows are complete and correct: the form submit action 'Pay' is covered, no phantom workflows, conditional branches and on_success match the AST.

**Missing workflows:** none

**Phantom workflows:** none

---

## Request Loan

**Verdict:** yes  
**Forced ship:** no  

The workflows cover the form's submit action and all referenced field conditions; there are no phantom terminal actions, invalid conditional references, or empty generic on_success values.

**Missing workflows:** none

**Phantom workflows:** none

---

## Update Contact Info

**Verdict:** yes  
**Forced ship:** no  

The workflow list is complete and correct: the form's 'Update Profile' submit action has a matching workflow, there are no phantom workflows, and conditional/on_success fields are valid.

**Missing workflows:** none

**Phantom workflows:** none

---

## Manage Cards

**Verdict:** yes  
**Forced ship:** no  

All required workflows for the two form submit actions are present, no phantom terminal actions, and no incorrect conditional branches or empty on_success values.

**Missing workflows:** none

**Phantom workflows:** none

---

## Investments

**Verdict:** yes  
**Forced ship:** no  

All form submit actions are covered (Execute Trade has workflows for both Action==Buy and Action==Sell; Create Plan is present); no phantom terminal actions or incorrect conditional branches detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Account Statements

**Verdict:** yes  
**Forced ship:** no  

All required workflows are present and correct: both Generate Statement period branches and both e-Statement preference branches are covered, no phantom workflows or incorrect conditional branches detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Security Settings

**Verdict:** yes  
**Forced ship:** no  

Workflows cover the form submit action correctly; no missing workflows, phantoms, or incorrect branches detected.

**Missing workflows:** none

**Phantom workflows:** none

---

## Support Center

**Verdict:** yes  
**Forced ship:** no  

All form submit actions are covered by workflows, there are no phantom terminal actions, conditional branches correctly reference no missing fields, and on_success texts match the AST.

**Missing workflows:** none

**Phantom workflows:** none

---
