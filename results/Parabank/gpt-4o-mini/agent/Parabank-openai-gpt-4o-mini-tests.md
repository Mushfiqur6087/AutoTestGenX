# Test Cases — Parabank

Generated: 2026-06-04T14:24:43.764164Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 13 | 180 | 21 | 94 | 65 | 91 | 72 | 17 |

## Login

Total: **12** (positive: 1, negative: 6, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful login with valid credentials | User logged in as <User> | 1. Enter <valid email> in the Email/Username field<br>2. Enter <valid password> in the Password field<br>3. Click Sign In | Signed in successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the Email field blank and submit |  | 1. Leave the Email_Username field blank<br>2. Fill the Password field with a valid password<br>3. Click Sign In | Inline validation error appears on the Email_Username field indicating it is required | high |
| TC-003 |  | Leave the Password field blank and submit |  | 1. Fill the Email_Username field with a valid email<br>2. Leave the Password field blank<br>3. Click Sign In | Inline validation error appears on the Password field indicating it is required | high |
| TC-004 |  | Submit with an invalid email format |  | 1. Enter <invalid email format> in the Email_Username field<br>2. Fill the Password field with a valid password<br>3. Click Sign In | Inline validation error appears on the Email_Username field indicating it must be a valid email format | medium |
| TC-005 |  | Submit with a password that does not meet requirements |  | 1. Fill the Email_Username field with a valid email<br>2. Enter <password shorter than 8 characters> in the Password field<br>3. Click Sign In | Inline validation error appears on the Password field indicating it must be at least 8 characters | medium |
| TC-006 |  | Submit with a password that lacks required complexity |  | 1. Fill the Email_Username field with a valid email<br>2. Enter <password without uppercase, lowercase, number, and special character> in the Password field<br>3. Click Sign In | Inline validation error appears on the Password field indicating it must include uppercase, lowercase, number, and special character | medium |
| TC-007 |  | Submit with incorrect credentials |  | 1. Fill the Email_Username field with a valid email<br>2. Enter <incorrect password> in the Password field<br>3. Click Sign In | Form does not submit; error shown: 'Incorrect email or password. Please try again.'; Password field is cleared | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) |  | Password meets minimum length requirement |  | 1. Enter a valid email format in the Email/Username field<br>2. Enter a password with exactly 8 characters, including uppercase, lowercase, number, and special character<br>3. Click Sign In | Signed in successfully. | medium |
| TC-009 (boundary) |  | Password fails minimum length requirement |  | 1. Enter a valid email format in the Email/Username field<br>2. Enter a password with exactly 7 characters, including uppercase, lowercase, number, and special character<br>3. Click Sign In | Incorrect email or password. Please try again. | medium |
| TC-010 (input_edge) |  | Email field accepts maximum length string |  | 1. Enter an email address that is at the maximum allowed length in the Email/Username field<br>2. Enter a valid password in the Password field<br>3. Click Sign In | Signed in successfully. | low |
| TC-011 (input_edge) |  | Email field with special characters |  | 1. Enter an email address with special characters in the Email/Username field<br>2. Enter a valid password in the Password field<br>3. Click Sign In | Signed in successfully. | low |
| TC-012 (input_edge) |  | Password with leading and trailing whitespace |  | 1. Enter a valid email format in the Email/Username field<br>2. Enter a password with leading and trailing spaces, but valid length and characters in the Password field<br>3. Click Sign In | Signed in successfully. | low |

---

## Register

Total: **19** (positive: 1, negative: 11, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful registration with valid inputs | User logged in as <Role> | 1. Enter <First Name> in the First Name field<br>2. Enter <Last Name> in the Last Name field<br>3. Enter <Street Address> in the Street Address field<br>4. Enter <City> in the City field<br>5. Select <State> from the State dropdown<br>6. Enter <ZIP Code> in the ZIP Code field<br>7. Enter <Phone Number> in the Phone Number field<br>8. Enter <Social Security Number> in the Social Security Number field<br>9. Enter <valid email> in the Username field<br>10. Enter <Password> in the Password field<br>11. Enter <Password> in the Confirm Password field<br>12. Click the Register button | Account created successfully — please sign in | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the First Name field blank and submit |  | 1. Leave the First Name field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the First_Name field indicating it is required | high |
| TC-003 |  | Leave the Last Name field blank and submit |  | 1. Leave the Last Name field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Last_Name field indicating it is required | high |
| TC-004 |  | Leave the Street Address field blank and submit |  | 1. Leave the Street Address field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Street_Address field indicating it is required | high |
| TC-005 |  | Leave the City field blank and submit |  | 1. Leave the City field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the City field indicating it is required | high |
| TC-006 |  | Leave the State field unselected and submit |  | 1. Leave the State field unselected<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the State field indicating it is required | high |
| TC-007 |  | Leave the ZIP Code field blank and submit |  | 1. Leave the ZIP Code field blank<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the ZIP_Code field indicating it is required | high |
| TC-008 |  | Enter an invalid format in the Phone Number field and submit |  | 1. Enter <invalid phone number format> in the Phone_Number field<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Phone_Number field indicating it must follow the format (123) 456-7890 | medium |
| TC-009 |  | Enter an invalid format in the Social Security Number field and submit |  | 1. Enter <invalid SSN format> in the Social_Security_Number field<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Social_Security_Number field indicating it must follow the format 123-45-6789 | medium |
| TC-010 |  | Enter an invalid email format in the Username field and submit |  | 1. Enter <invalid email format> in the Username field<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Username field indicating it must be a valid email format | medium |
| TC-011 |  | Enter a short password in the Password field and submit |  | 1. Enter <password shorter than 8 characters> in the Password field<br>2. Fill all other required fields<br>3. Click Register | Inline validation error appears on the Password field indicating it must be at least 8 characters | medium |
| TC-012 |  | Enter mismatched passwords in Password and Confirm Password fields and submit |  | 1. Enter <valid password> in the Password field<br>2. Enter <different password> in the Confirm_Password field<br>3. Fill all other required fields<br>4. Click Register | Inline validation error appears on the Confirm_Password field indicating 'Confirm Password must match Password' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 (boundary) |  | ZIP Code with exactly 5 digits |  | 1. Enter a 5-digit number in the ZIP Code field | Form submits successfully; account is created with the provided ZIP Code | medium |
| TC-014 (boundary) |  | ZIP Code with 5+4 format |  | 1. Enter a ZIP Code in the 5+4 format (12345-6789) in the ZIP Code field | Form submits successfully; account is created with the provided ZIP Code | medium |
| TC-015 (boundary) |  | Phone Number with valid format |  | 1. Enter a phone number in the format (123) 456-7890 in the Phone Number field | Form submits successfully; account is created with the provided Phone Number | medium |
| TC-016 (boundary) |  | Social Security Number with valid format |  | 1. Enter a Social Security Number in the format 123-45-6789 in the Social Security Number field | Form submits successfully; account is created with the provided Social Security Number | medium |
| TC-017 (boundary) |  | Password with exactly 8 characters |  | 1. Enter a password with exactly 8 characters in the Password field<br>2. Enter the same password in the Confirm Password field | Form submits successfully; account is created with the provided Password | medium |
| TC-018 (input_edge) |  | Username with special characters |  | 1. Enter a valid email with special characters in the Username field | Form submits successfully; account is created with the provided Username | low |
| TC-019 (input_edge) |  | Leading/trailing whitespace in First Name |  | 1. Enter '  John  ' in the First Name field<br>2. Fill all other required fields with valid data<br>3. Click Register | Leading/trailing whitespace is trimmed; saved value shown in detail page has 'John' | low |

---

## Accounts Overview

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Account Number displays correct account number | User logged in as <Role> | 1. Navigate to the Accounts Overview page<br>2. Click on the Account Number cell for an account | Account number displayed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to view account number when action is not implemented |  | 1. Click on the Account Number column | No action occurs; the account number is not displayed as the action is not implemented yet. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | Attempt to click on the Account Number link | User is logged in and on the Accounts Overview page | 1. Locate the Account Number column in the table<br>2. Click on the Account Number link | No action occurs; a message indicates the feature is not implemented yet. | medium |
| TC-004 (input_edge) |  | Check display of masked account numbers | User is logged in and on the Accounts Overview page | 1. Observe the Account Number column in the table | Account numbers are displayed masked, showing only the last 4 digits as ****5001. | low |

---

## Open New Account

Total: **15** (positive: 2, negative: 9, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Checking Account with valid details | User logged in as <Role> | 1. Select 'Checking' as the Account Type<br>2. Enter '25' in the Initial Deposit Amount field<br>3. Select a <valid funding source account> from the Funding Source Account dropdown<br>4. Click 'Open Account' | Account opened successfully!; redirects to accounts overview | high |
| TC-002 | WF-002 | Open Savings Account with valid details | User logged in as <Role> | 1. Select 'Savings' as the Account Type<br>2. Enter '100' in the Initial Deposit Amount field<br>3. Select a <valid funding source account> from the Funding Source Account dropdown<br>4. Click 'Open Account' | Account opened successfully!; redirects to accounts overview | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave Account Type blank and submit |  | 1. Leave the Account Type field blank<br>2. Fill in the Initial Deposit Amount and Funding Source Account fields<br>3. Click Open Account | Inline validation error appears on the Account Type field indicating it is required | high |
| TC-004 |  | Leave Initial Deposit Amount blank and submit |  | 1. Leave the Initial Deposit Amount field blank<br>2. Select an Account Type and Funding Source Account<br>3. Click Open Account | Inline validation error appears on the Initial Deposit Amount field indicating it is required | high |
| TC-005 |  | Enter non-numeric value in Initial Deposit Amount |  | 1. Enter <non-numeric value> in the Initial Deposit Amount field<br>2. Select an Account Type and Funding Source Account<br>3. Click Open Account | Inline validation error appears on the Initial Deposit Amount field indicating it must be numeric | medium |
| TC-006 |  | Enter amount less than minimum for Checking and submit |  | 1. Enter <amount below $25> in the Initial Deposit Amount field<br>2. Select Checking as Account Type and Funding Source Account<br>3. Click Open Account | Inline validation error appears on the Initial Deposit Amount field indicating it must be at least $25 for Checking | medium |
| TC-007 |  | Enter amount less than minimum for Savings and submit |  | 1. Enter <amount below $100> in the Initial Deposit Amount field<br>2. Select Savings as Account Type and Funding Source Account<br>3. Click Open Account | Inline validation error appears on the Initial Deposit Amount field indicating it must be at least $100 for Savings | medium |
| TC-008 |  | Leave Funding Source Account blank and submit |  | 1. Leave the Funding Source Account field blank<br>2. Select an Account Type and enter Initial Deposit Amount<br>3. Click Open Account | Inline validation error appears on the Funding Source Account field indicating it is required | high |
| TC-009 |  | Select Funding Source Account with insufficient balance and submit |  | 1. Select an Account Type<br>2. Enter <valid amount> in the Initial Deposit Amount field<br>3. Select a Funding Source Account with insufficient balance<br>4. Click Open Account | Inline validation error appears on the Funding Source Account field indicating it must have sufficient balance | medium |
| TC-010 | WF-001 | Attempt to open account with Checking type without meeting minimum deposit |  | 1. Select Checking as Account Type<br>2. Enter <amount below $25> in the Initial Deposit Amount field<br>3. Select a Funding Source Account<br>4. Click Open Account | Form does not submit; error shown on Initial Deposit Amount field indicating it must be at least $25 for Checking | medium |
| TC-011 | WF-002 | Attempt to open account with Savings type without meeting minimum deposit |  | 1. Select Savings as Account Type<br>2. Enter <amount below $100> in the Initial Deposit Amount field<br>3. Select a Funding Source Account<br>4. Click Open Account | Form does not submit; error shown on Initial Deposit Amount field indicating it must be at least $100 for Savings | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) | WF-001 | Minimum deposit for Checking account | Account Type is set to Checking | 1. Enter $25 in the Initial Deposit Amount field<br>2. Select a Funding Source Account with sufficient balance<br>3. Click Open Account | Account opened successfully!; user is redirected to accounts overview | medium |
| TC-013 (boundary) | WF-001 | One unit below minimum deposit for Checking account | Account Type is set to Checking | 1. Enter $24 in the Initial Deposit Amount field<br>2. Select a Funding Source Account with sufficient balance<br>3. Click Open Account | Inline error shown indicating deposit must be at least $25 | medium |
| TC-014 (boundary) | WF-002 | Minimum deposit for Savings account | Account Type is set to Savings | 1. Enter $100 in the Initial Deposit Amount field<br>2. Select a Funding Source Account with sufficient balance<br>3. Click Open Account | Account opened successfully!; user is redirected to accounts overview | medium |
| TC-015 (boundary) | WF-002 | One unit below minimum deposit for Savings account | Account Type is set to Savings | 1. Enter $99 in the Initial Deposit Amount field<br>2. Select a Funding Source Account with sufficient balance<br>3. Click Open Account | Inline error shown indicating deposit must be at least $100 | medium |

---

## Transfer Funds

Total: **13** (positive: 2, negative: 6, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Transfer funds from My ParaBank Account | User logged in as <User Role> | 1. Select 'My ParaBank Account' as the Transfer Type<br>2. Enter <valid amount> in the Transfer Amount field<br>3. Select 'Checking' from the Source Account dropdown<br>4. Click Transfer | Transfer completed successfully. | high |
| TC-002 | WF-002 | Transfer funds to an External Account | User logged in as <User Role> | 1. Select 'External Account' as the Transfer Type<br>2. Enter <valid amount> in the Transfer Amount field<br>3. Select 'Savings' from the Source Account dropdown<br>4. Click 'Add Destination' to enter an external account<br>5. Enter <valid external account number> in the External Account Number field<br>6. Click Transfer | Transfer completed successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave Transfer Amount blank and submit |  | 1. Select 'My ParaBank Account' for Transfer Type<br>2. Leave the Transfer Amount field blank<br>3. Select a Source Account<br>4. Click Transfer | Inline validation error appears on the Transfer Amount field indicating it is required | high |
| TC-004 |  | Enter invalid amount in Transfer Amount field |  | 1. Select 'My ParaBank Account' for Transfer Type<br>2. Enter <invalid amount> in the Transfer Amount field<br>3. Select a Source Account<br>4. Click Transfer | Inline validation error appears on the Transfer Amount field indicating it must be a valid amount | medium |
| TC-005 |  | Select Source Account and leave External Account Number blank |  | 1. Select 'External Account' for Transfer Type<br>2. Enter <valid amount> in the Transfer Amount field<br>3. Select a Source Account<br>4. Leave the External Account Number field blank<br>5. Click Transfer | Inline validation error appears on the External Account Number field indicating it must be a valid account number | high |
| TC-006 |  | Enter invalid account number for External Account |  | 1. Select 'External Account' for Transfer Type<br>2. Enter <valid amount> in the Transfer Amount field<br>3. Select a Source Account<br>4. Enter <invalid account number> in the External Account Number field<br>5. Click Transfer | Inline validation error appears on the External Account Number field indicating it must be a valid account number | medium |
| TC-007 | WF-001 | Attempt transfer without sufficient funds |  | 1. Select 'My ParaBank Account' for Transfer Type<br>2. Enter <amount exceeding available balance> in the Transfer Amount field<br>3. Select a Source Account<br>4. Click Transfer | Error shown: 'Insufficient funds' | high |
| TC-008 | WF-002 | Attempt transfer with mismatched account numbers for External Account |  | 1. Select 'External Account' for Transfer Type<br>2. Enter <valid amount> in the Transfer Amount field<br>3. Select a Source Account<br>4. Enter <valid account number> in the External Account Number field<br>5. Enter <different valid account number> in the confirm field<br>6. Click Transfer | Error shown: 'Account numbers do not match' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-002 | Transfer amount at minimum valid value |  | 1. Select 'External Account' as the Transfer Type<br>2. Enter the minimum valid amount in the Transfer Amount field<br>3. Select a Source Account from the dropdown<br>4. Add an External Account Number in the repeating group<br>5. Click Transfer | Transfer completes successfully with a transaction ID. | medium |
| TC-010 (boundary) | WF-002 | Transfer amount just below minimum valid value |  | 1. Select 'External Account' as the Transfer Type<br>2. Enter an amount just below the minimum valid amount in the Transfer Amount field<br>3. Select a Source Account from the dropdown<br>4. Add an External Account Number in the repeating group<br>5. Click Transfer | Transfer is blocked; error shown indicating insufficient funds. | medium |
| TC-011 (boundary) | WF-002 | Add maximum allowed entries to the repeating group |  | 1. Select 'External Account' as the Transfer Type<br>2. Enter a valid amount in the Transfer Amount field<br>3. Select a Source Account from the dropdown<br>4. Add the maximum allowed External Account Numbers in the repeating group<br>5. Click Transfer | Transfer completes successfully with a transaction ID. | medium |
| TC-012 (boundary) | WF-002 | Attempt to add one more entry to the repeating group |  | 1. Select 'External Account' as the Transfer Type<br>2. Enter a valid amount in the Transfer Amount field<br>3. Select a Source Account from the dropdown<br>4. Add the maximum allowed External Account Numbers in the repeating group<br>5. Attempt to add one more External Account Number to the repeating group | Adding the entry is blocked; no additional entry is accepted. | medium |
| TC-013 (input_edge) | WF-002 | Enter an invalid account number format |  | 1. Select 'External Account' as the Transfer Type<br>2. Enter a valid amount in the Transfer Amount field<br>3. Select a Source Account from the dropdown<br>4. Add an invalid External Account Number format in the repeating group<br>5. Click Transfer | Transfer is blocked; error shown indicating 'must be a valid account number'. | low |

---

## Payments

Total: **17** (positive: 1, negative: 12, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit payment with valid details | User logged in as <Role> | 1. Enter <valid payee name> in the Payee Name field<br>2. Enter <valid street address> in the Street Address field<br>3. Enter <valid city> in the City field<br>4. Enter <valid state> in the State field<br>5. Enter <valid ZIP code> in the ZIP Code field<br>6. Enter <valid phone number> in the Phone Number field<br>7. Enter <valid payee account number> in the Payee Account Number field<br>8. Enter <same payee account number> in the Confirm Account Number field<br>9. Enter <valid payment amount> in the Payment Amount field<br>10. Select <valid source account> from the Source Account dropdown<br>11. Click Pay | Payment submitted successfully with reference code | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave Payee Name blank and submit |  | 1. Leave the Payee_Name field blank<br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears on the Payee_Name field indicating it is required | high |
| TC-003 |  | Leave Street Address blank and submit |  | 1. Leave the Street_Address field blank<br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears on the Street_Address field indicating it is required | high |
| TC-004 |  | Leave City blank and submit |  | 1. Leave the City field blank<br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears on the City field indicating it is required | high |
| TC-005 |  | Leave State blank and submit |  | 1. Leave the State field blank<br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears on the State field indicating it is required | high |
| TC-006 |  | Leave ZIP Code blank and submit |  | 1. Leave the ZIP_Code field blank<br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears on the ZIP_Code field indicating it is required | high |
| TC-007 |  | Leave Phone Number blank and submit |  | 1. Leave the Phone_Number field blank<br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears on the Phone_Number field indicating it is required | high |
| TC-008 |  | Leave Payee Account Number blank and submit |  | 1. Leave the Payee_Account_Number field blank<br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears on the Payee_Account_Number field indicating it is required | high |
| TC-009 |  | Leave Confirm Account Number blank and submit |  | 1. Leave the Confirm_Account_Number field blank<br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears on the Confirm_Account_Number field indicating it is required | high |
| TC-010 |  | Leave Payment Amount blank and submit |  | 1. Leave the Payment_Amount field blank<br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears on the Payment_Amount field indicating it is required | high |
| TC-011 |  | Leave Source Account blank and submit |  | 1. Leave the Source_Account field blank<br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears on the Source_Account field indicating it is required | high |
| TC-012 | WF-002 | Submit payment with account number mismatch |  | 1. Fill Payee_Account_Number with <valid account number><br>2. Fill Confirm_Account_Number with <different account number><br>3. Fill all other required fields<br>4. Click Pay | Inline validation error appears indicating 'Account numbers do not match' | high |
| TC-013 | WF-003 | Submit payment with insufficient funds |  | 1. Fill Payment_Amount with <amount exceeding available balance><br>2. Fill all other required fields<br>3. Click Pay | Inline validation error appears indicating 'Insufficient funds' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 (boundary) | WF-001 | Payment Amount at minimum value |  | 1. Enter a valid Payee Name in the Payee_Name field<br>2. Enter a valid Street Address in the Street_Address field<br>3. Enter a valid City in the City field<br>4. Enter a valid State in the State field<br>5. Enter a valid ZIP Code in the ZIP_Code field<br>6. Enter a valid Phone Number in the Phone_Number field<br>7. Enter a valid Payee Account Number in the Payee_Account_Number field<br>8. Enter the same Payee Account Number in the Confirm_Account_Number field<br>9. Enter the minimum allowed Payment Amount in the Payment_Amount field<br>10. Select a valid Source Account from the dropdown<br>11. Click Pay | Payment submitted successfully with reference code | medium |
| TC-015 (boundary) | WF-001 | Payment Amount just below minimum value |  | 1. Enter a valid Payee Name in the Payee_Name field<br>2. Enter a valid Street Address in the Street_Address field<br>3. Enter a valid City in the City field<br>4. Enter a valid State in the State field<br>5. Enter a valid ZIP Code in the ZIP_Code field<br>6. Enter a valid Phone Number in the Phone_Number field<br>7. Enter a valid Payee Account Number in the Payee_Account_Number field<br>8. Enter the same Payee Account Number in the Confirm_Account_Number field<br>9. Enter an amount just below the minimum allowed in the Payment_Amount field<br>10. Select a valid Source Account from the dropdown<br>11. Click Pay | Payment is blocked; inline error shows 'Payment amount is below the minimum allowed' | medium |
| TC-016 (boundary) | WF-002 | Confirm Account Number does not match Payee Account Number |  | 1. Enter a valid Payee Name in the Payee_Name field<br>2. Enter a valid Street Address in the Street_Address field<br>3. Enter a valid City in the City field<br>4. Enter a valid State in the State field<br>5. Enter a valid ZIP Code in the ZIP_Code field<br>6. Enter a valid Phone Number in the Phone_Number field<br>7. Enter a valid Payee Account Number in the Payee_Account_Number field<br>8. Enter a different value in the Confirm_Account_Number field<br>9. Enter a valid Payment Amount in the Payment_Amount field<br>10. Select a valid Source Account from the dropdown<br>11. Click Pay | Payment is blocked; inline error shows 'Account numbers do not match' | medium |
| TC-017 (boundary) | WF-003 | Payment Amount exceeds available balance |  | 1. Enter a valid Payee Name in the Payee_Name field<br>2. Enter a valid Street Address in the Street_Address field<br>3. Enter a valid City in the City field<br>4. Enter a valid State in the State field<br>5. Enter a valid ZIP Code in the ZIP_Code field<br>6. Enter a valid Phone Number in the Phone_Number field<br>7. Enter a valid Payee Account Number in the Payee_Account_Number field<br>8. Enter the same Payee Account Number in the Confirm_Account_Number field<br>9. Enter a Payment Amount that exceeds available funds in the Payment_Amount field<br>10. Select a valid Source Account from the dropdown<br>11. Click Pay | Payment is blocked; inline error shows 'Insufficient funds' | medium |

---

## Request Loan

Total: **20** (positive: 3, negative: 9, edge: 8)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Loan Application for Personal Loan | User logged in as <Role> | 1. Select 'Personal' from the Loan Type cards<br>2. Enter <valid amount within $1,000-$50,000> in the Loan Amount field<br>3. Enter <valid down payment amount (minimum 10% of Loan Amount)> in the Down Payment Amount field<br>4. Select a valid Collateral Account from the dropdown<br>5. Click Submit Loan Application | Loan approved and created successfully! | high |
| TC-002 | WF-002 | Submit Loan Application for Auto Loan | User logged in as <Role> | 1. Select 'Auto' from the Loan Type cards<br>2. Enter <valid amount within $5,000-$75,000> in the Loan Amount field<br>3. Enter <valid down payment amount (minimum 10% of Loan Amount)> in the Down Payment Amount field<br>4. Select a valid Collateral Account from the dropdown<br>5. Click Submit Loan Application | Loan approved and created successfully! | high |
| TC-003 | WF-003 | Submit Loan Application for Home Loan | User logged in as <Role> | 1. Select 'Home' from the Loan Type cards<br>2. Enter <valid amount within $50,000-$500,000> in the Loan Amount field<br>3. Enter <valid down payment amount (minimum 10% of Loan Amount)> in the Down Payment Amount field<br>4. Select a valid Collateral Account from the dropdown<br>5. Click Submit Loan Application | Loan approved and created successfully! | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave Loan Amount blank and submit |  | 1. Leave the Loan Amount field blank<br>2. Fill all other required fields<br>3. Click Submit Loan Application | Inline validation error appears on the Loan Amount field indicating it is required | high |
| TC-005 |  | Leave Down Payment Amount blank and submit |  | 1. Leave the Down Payment Amount field blank<br>2. Fill all other required fields<br>3. Click Submit Loan Application | Inline validation error appears on the Down Payment Amount field indicating it is required | high |
| TC-006 |  | Enter Down Payment Amount greater than Loan Amount |  | 1. Enter <amount greater than Loan Amount> in the Loan Amount field<br>2. Enter <amount greater than Loan Amount> in the Down Payment Amount field<br>3. Click Submit Loan Application | Form does not submit; error shown on Down Payment Amount field indicating it must be less than Loan Amount | high |
| TC-007 |  | Enter Down Payment Amount less than 10% of Loan Amount |  | 1. Enter <Loan Amount> in the Loan Amount field<br>2. Enter <amount less than 10% of Loan Amount> in the Down Payment Amount field<br>3. Click Submit Loan Application | Form does not submit; error shown on Down Payment Amount field indicating it must be at least 10% of Loan Amount | high |
| TC-008 |  | Enter insufficient collateral value |  | 1. Select <Collateral Account> from the dropdown<br>2. Enter <amount less than 20% of collateral value> in the Collateral Account field<br>3. Click Submit Loan Application | Form does not submit; error shown indicating insufficient collateral funds | high |
| TC-009 |  | Submit Loan Application without sufficient collateral |  | 1. Select a Loan Type<br>2. Enter <Loan Amount> in the Loan Amount field<br>3. Enter <Down Payment Amount> in the Down Payment Amount field<br>4. Select <Collateral Account> from the dropdown<br>5. Click Submit Loan Application | Form does not submit; error shown indicating inadequate collateral value | high |
| TC-010 | WF-001 | Submit Loan Application for Personal Loan with invalid Loan Amount |  | 1. Select Personal as Loan Type<br>2. Enter <amount less than $1,000> in the Loan Amount field<br>3. Enter <Down Payment Amount> in the Down Payment Amount field<br>4. Select <Collateral Account> from the dropdown<br>5. Click Submit Loan Application | Form does not submit; error shown on Loan Amount field indicating it must be between $1,000 and $50,000 | high |
| TC-011 | WF-002 | Submit Loan Application for Auto Loan with invalid Loan Amount |  | 1. Select Auto as Loan Type<br>2. Enter <amount less than $5,000> in the Loan Amount field<br>3. Enter <Down Payment Amount> in the Down Payment Amount field<br>4. Select <Collateral Account> from the dropdown<br>5. Click Submit Loan Application | Form does not submit; error shown on Loan Amount field indicating it must be between $5,000 and $75,000 | high |
| TC-012 | WF-003 | Submit Loan Application for Home Loan with invalid Loan Amount |  | 1. Select Home as Loan Type<br>2. Enter <amount less than $50,000> in the Loan Amount field<br>3. Enter <Down Payment Amount> in the Down Payment Amount field<br>4. Select <Collateral Account> from the dropdown<br>5. Click Submit Loan Application | Form does not submit; error shown on Loan Amount field indicating it must be between $50,000 and $500,000 | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 (boundary) | WF-001 | Test minimum Loan Amount for Personal Loan | Select 'Personal' loan type | 1. Enter $1,000 in the Loan Amount field<br>2. Enter $100 in the Down Payment Amount field<br>3. Click Submit Loan Application | Loan approved and created successfully! | medium |
| TC-014 (boundary) | WF-001 | Test maximum Loan Amount for Personal Loan | Select 'Personal' loan type | 1. Enter $50,000 in the Loan Amount field<br>2. Enter $5,000 in the Down Payment Amount field<br>3. Click Submit Loan Application | Loan approved and created successfully! | medium |
| TC-015 (boundary) | WF-001 | Test Down Payment Amount less than minimum required for Personal Loan | Select 'Personal' loan type, Enter $10,000 in the Loan Amount field | 1. Enter $900 in the Down Payment Amount field<br>2. Click Submit Loan Application | Down Payment Amount must be at least 10% of Loan Amount. | medium |
| TC-016 (boundary) | WF-002 | Test maximum Loan Amount for Auto Loan | Select 'Auto' loan type | 1. Enter $75,000 in the Loan Amount field<br>2. Enter $7,500 in the Down Payment Amount field<br>3. Click Submit Loan Application | Loan approved and created successfully! | medium |
| TC-017 (boundary) | WF-003 | Test maximum Loan Amount for Home Loan | Select 'Home' loan type | 1. Enter $500,000 in the Loan Amount field<br>2. Enter $50,000 in the Down Payment Amount field<br>3. Click Submit Loan Application | Loan approved and created successfully! | medium |
| TC-018 (boundary) | WF-003 | Test Down Payment Amount exceeds Loan Amount for Home Loan | Select 'Home' loan type, Enter $100,000 in the Loan Amount field | 1. Enter $110,000 in the Down Payment Amount field<br>2. Click Submit Loan Application | Down Payment Amount must be less than Loan Amount. | medium |
| TC-019 (input_edge) |  | Test long text in Loan Amount field |  | 1. Enter a string of 200+ characters in the Loan Amount field<br>2. Click Submit Loan Application | Loan Amount field displays an error indicating invalid input. | low |
| TC-020 (input_edge) |  | Test special characters in Loan Amount field |  | 1. Enter special characters in the Loan Amount field<br>2. Click Submit Loan Application | Loan Amount field displays an error indicating invalid input. | low |

---

## Update Contact Info

Total: **12** (positive: 1, negative: 8, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit updated contact information | User logged in as <Customer>, Profile form is pre-filled with existing contact information | 1. Enter <valid first name> in the First Name field<br>2. Enter <valid last name> in the Last Name field<br>3. Enter <valid street address> in the Street Address field<br>4. Enter <valid city> in the City field<br>5. Select <valid state> from the State dropdown<br>6. Enter <valid ZIP code> in the ZIP Code field<br>7. Enter <valid phone number> in the Phone Number field<br>8. Click Update Profile | A success notification is displayed; the message 'Profile updated successfully.' is shown. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave First Name blank and submit |  | 1. Leave the First_Name field blank<br>2. Fill all other required fields<br>3. Click Update Profile | Inline validation error appears on the First_Name field indicating it is required | high |
| TC-003 |  | Leave Last Name blank and submit |  | 1. Leave the Last_Name field blank<br>2. Fill all other required fields<br>3. Click Update Profile | Inline validation error appears on the Last_Name field indicating it is required | high |
| TC-004 |  | Leave Street Address blank and submit |  | 1. Leave the Street_Address field blank<br>2. Fill all other required fields<br>3. Click Update Profile | Inline validation error appears on the Street_Address field indicating it is required | high |
| TC-005 |  | Leave City blank and submit |  | 1. Leave the City field blank<br>2. Fill all other required fields<br>3. Click Update Profile | Inline validation error appears on the City field indicating it is required | high |
| TC-006 |  | Leave State blank and submit |  | 1. Leave the State field blank<br>2. Fill all other required fields<br>3. Click Update Profile | Inline validation error appears on the State field indicating it is required | high |
| TC-007 |  | Leave ZIP Code blank and submit |  | 1. Leave the ZIP_Code field blank<br>2. Fill all other required fields<br>3. Click Update Profile | Inline validation error appears on the ZIP_Code field indicating it is required | high |
| TC-008 |  | Leave Phone Number blank and submit |  | 1. Leave the Phone_Number field blank<br>2. Fill all other required fields<br>3. Click Update Profile | Inline validation error appears on the Phone_Number field indicating it is required | high |
| TC-009 |  | Submit with all required fields empty |  | 1. Leave all required fields blank<br>2. Click Update Profile | Inline validation error appears on the First_Name, Last_Name, Street_Address, City, State, ZIP_Code, and Phone_Number fields indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) | WF-001 | Enter maximum length string in First Name field |  | 1. Enter a very long string (200+ characters) in the First Name field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Profile updated successfully. | medium |
| TC-011 (input_edge) | WF-001 | Enter special characters in Phone Number field |  | 1. Enter special characters in the Phone Number field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Highlights invalid fields and displays an inline error banner. | low |
| TC-012 (input_edge) | WF-001 | Enter leading/trailing whitespace in Last Name field |  | 1. Enter '   Doe   ' in the Last Name field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Leading/trailing whitespace is trimmed; saved value shown on the detail page has no extra spaces. | low |

---

## Manage Cards

Total: **18** (positive: 2, negative: 8, edge: 8)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit a card request with valid details | User logged in as <Role>, address must be complete, account must be in good standing | 1. Select 'Debit' from the Card Type dropdown<br>2. Enter <valid account> in the Account to Link field<br>3. Enter <complete shipping address> in the Shipping Address field<br>4. Click 'Request Card' | Card request submitted successfully. | high |
| TC-002 | WF-002 | Update card controls with valid details | User logged in as <Role> | 1. Select <existing card> from the Select Existing Card dropdown<br>2. Enter <valid numeric limit> in the New Spending Limit field<br>3. Click 'Add Date' in the Travel Notice section<br>4. Enter <valid date range> in the Date field<br>5. Enter <valid destination> in the Destination field<br>6. Select 'Active' from the Card Status dropdown<br>7. Click 'Update Controls' | Card controls updated successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Account to Link field blank and submit |  | 1. Leave the Account to Link field blank<br>2. Fill all other required fields<br>3. Click Request Card | Inline validation error appears on the Account to Link field indicating it is required | high |
| TC-004 |  | Leave the Shipping Address field incomplete and submit |  | 1. Fill the Account to Link field<br>2. Leave the Shipping Address field incomplete<br>3. Click Request Card | Inline validation error appears on the Shipping Address field indicating 'address must be complete' | high |
| TC-005 |  | Leave the Select Existing Card field blank and submit |  | 1. Leave the Select Existing Card field blank<br>2. Fill all other required fields<br>3. Click Update Controls | Inline validation error appears on the Select Existing Card field indicating it is required | high |
| TC-006 |  | Enter a non-numeric value in the New Spending Limit field |  | 1. Fill the Select Existing Card field<br>2. Enter <non-numeric value> in the New Spending Limit field<br>3. Click Update Controls | Inline validation error appears on the New Spending Limit field indicating 'must be a valid numeric limit' | medium |
| TC-007 |  | Enter an invalid date range in the Travel Notice |  | 1. Fill the Select Existing Card field<br>2. Fill the New Spending Limit field<br>3. Enter <invalid date range> in the Travel Notice Date field<br>4. Fill the Destination field<br>5. Click Update Controls | Inline validation error appears on the Travel Notice Date field indicating 'must be a valid date range' | medium |
| TC-008 |  | Select an invalid status transition in the Card Status field |  | 1. Fill the Select Existing Card field<br>2. Fill the New Spending Limit field<br>3. Fill the Travel Notice<br>4. Select <invalid status transition> in the Card Status field<br>5. Click Update Controls | Inline validation error appears on the Card Status field indicating 'must be a valid status transition' | medium |
| TC-009 | WF-001 | Attempt to request a card when the address is incomplete |  | 1. Fill the Account to Link field<br>2. Leave the Shipping Address field incomplete<br>3. Click Request Card | Form does not submit; card request is not created; inline validation error appears on the Shipping Address field indicating 'address must be complete' | high |
| TC-010 | WF-002 | Attempt to update controls without selecting an existing card |  | 1. Leave the Select Existing Card field blank<br>2. Click Update Controls | Form does not submit; card controls are not updated; inline validation error appears on the Select Existing Card field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) | WF-001 | Test complete address for card request |  | 1. Select 'Debit' from the Card Type dropdown<br>2. Enter a complete address in the Shipping Address field<br>3. Fill in a valid account in the Account to Link field<br>4. Click 'Request Card' | Card request submitted successfully. | medium |
| TC-012 (boundary) | WF-001 | Test incomplete address for card request |  | 1. Select 'Credit' from the Card Type dropdown<br>2. Enter an incomplete address in the Shipping Address field<br>3. Fill in a valid account in the Account to Link field<br>4. Click 'Request Card' | Form displays an error indicating the address must be complete. | medium |
| TC-013 (boundary) | WF-002 | Test valid numeric limit for spending limit |  | 1. Select an existing card from the Select Existing Card dropdown<br>2. Enter a valid numeric limit in the New Spending Limit field<br>3. Click 'Update Controls' | Card controls updated successfully. | medium |
| TC-014 (boundary) | WF-002 | Test invalid numeric limit for spending limit |  | 1. Select an existing card from the Select Existing Card dropdown<br>2. Enter an invalid numeric limit in the New Spending Limit field (e.g., negative number)<br>3. Click 'Update Controls' | Inline error appears indicating the limit is invalid. | medium |
| TC-015 (boundary) | WF-002 | Test valid date range for travel notice |  | 1. Select an existing card from the Select Existing Card dropdown<br>2. Add a travel notice with a valid date range in the Travel Notice section<br>3. Click 'Update Controls' | Card controls updated successfully. | medium |
| TC-016 (boundary) | WF-002 | Test invalid date range for travel notice |  | 1. Select an existing card from the Select Existing Card dropdown<br>2. Add a travel notice with an invalid date range (start date after end date) in the Travel Notice section<br>3. Click 'Update Controls' | Inline error appears indicating the date range is invalid. | medium |
| TC-017 (boundary) | WF-002 | Test valid status transition for card status |  | 1. Select an existing card from the Select Existing Card dropdown<br>2. Change the Card Status to 'Frozen'<br>3. Click 'Update Controls' | Card controls updated successfully. | medium |
| TC-018 (boundary) | WF-002 | Test invalid status transition for card status |  | 1. Select an existing card from the Select Existing Card dropdown<br>2. Change the Card Status to an invalid transition (if applicable, e.g., from 'Frozen' back to 'Active' without meeting conditions)<br>3. Click 'Update Controls' | Inline error appears indicating the status transition is invalid. | medium |

---

## Investments

Total: **16** (positive: 2, negative: 8, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Execute a trade successfully | User logged in as <Trader>, User has sufficient buying power | 1. Select 'Buy' from the Action dropdown<br>2. Enter <valid fund symbol> in the Fund Symbol field<br>3. Enter <valid quantity greater than zero> in the Quantity field<br>4. Select <valid funding account> from the Funding or Destination Account dropdown<br>5. Click Execute Trade | Trade executed successfully. with order ID | high |
| TC-002 | WF-002 | Create a recurring investment plan successfully | User logged in as <Investor>, User has adequate balance in the funding account | 1. Enter <valid fund symbol> in the Fund Symbol field<br>2. Enter <valid contribution amount meeting minimum> in the Contribution Amount field<br>3. Select 'Weekly' from the Frequency dropdown<br>4. Enter <valid future date> in the Start Date field<br>5. Select <valid funding account> from the Funding Account dropdown<br>6. Click Create Plan | Plan created successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Leave the Fund Symbol blank and submit |  | 1. Leave the Fund Symbol field blank<br>2. Fill in the Quantity with a valid number<br>3. Select a valid Action<br>4. Select a valid Funding or Destination Account<br>5. Click Execute Trade | Inline validation error appears on the Fund Symbol field indicating it is required | high |
| TC-004 | WF-001 | Enter a non-existent Fund Symbol and submit |  | 1. Enter <non-existent fund symbol> in the Fund Symbol field<br>2. Fill in the Quantity with a valid number<br>3. Select a valid Action<br>4. Select a valid Funding or Destination Account<br>5. Click Execute Trade | Inline validation error appears on the Fund Symbol field indicating 'symbol must exist' | high |
| TC-005 | WF-001 | Enter zero quantity and submit |  | 1. Enter <0> in the Quantity field<br>2. Fill in the Fund Symbol with a valid symbol<br>3. Select a valid Action<br>4. Select a valid Funding or Destination Account<br>5. Click Execute Trade | Inline validation error appears on the Quantity field indicating 'must be greater than zero' | high |
| TC-006 | WF-001 | Select a Funding or Destination Account without sufficient balance and submit |  | 1. Fill in the Fund Symbol with a valid symbol<br>2. Fill in the Quantity with a valid number<br>3. Select a valid Action<br>4. Select a Funding or Destination Account with insufficient balance<br>5. Click Execute Trade | Inline validation error appears on the Funding or Destination Account field indicating 'must have sufficient buying power or share balance' | high |
| TC-007 | WF-002 | Leave the Contribution Amount blank and submit |  | 1. Leave the Contribution Amount field blank<br>2. Fill in the Fund Symbol with a valid symbol<br>3. Select a Frequency<br>4. Enter a valid Start Date<br>5. Select a valid Funding Account<br>6. Click Create Plan | Inline validation error appears on the Contribution Amount field indicating it is required | high |
| TC-008 | WF-002 | Enter a Contribution Amount below minimum and submit |  | 1. Enter <amount below minimum> in the Contribution Amount field<br>2. Fill in the Fund Symbol with a valid symbol<br>3. Select a Frequency<br>4. Enter a valid Start Date<br>5. Select a valid Funding Account<br>6. Click Create Plan | Inline validation error appears on the Contribution Amount field indicating 'must meet minimum contribution' | high |
| TC-009 | WF-002 | Enter a Start Date in the past and submit |  | 1. Enter <past date> in the Start Date field<br>2. Fill in the Fund Symbol with a valid symbol<br>3. Select a Frequency<br>4. Enter a valid Contribution Amount<br>5. Select a valid Funding Account<br>6. Click Create Plan | Inline validation error appears on the Start Date field indicating 'must be in the future' | high |
| TC-010 | WF-002 | Select a Funding Account without adequate balance and submit |  | 1. Fill in the Fund Symbol with a valid symbol<br>2. Fill in the Contribution Amount with a valid number<br>3. Select a Frequency<br>4. Enter a valid Start Date<br>5. Select a Funding Account with inadequate balance<br>6. Click Create Plan | Inline validation error appears on the Funding Account field indicating 'must have adequate balance' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) | WF-001 | Quantity is exactly 1 | User has sufficient buying power, Fund symbol exists | 1. Select 'Buy' from the Action dropdown<br>2. Enter '1' in the Quantity field<br>3. Select a valid Fund Symbol<br>4. Select a Funding or Destination Account<br>5. Click Execute Trade | Trade executes successfully; order ID is displayed. | medium |
| TC-012 (boundary) | WF-001 | Quantity is 0 | User has sufficient buying power, Fund symbol exists | 1. Select 'Buy' from the Action dropdown<br>2. Enter '0' in the Quantity field<br>3. Select a valid Fund Symbol<br>4. Select a Funding or Destination Account<br>5. Click Execute Trade | Inline error shown: 'Quantity must be greater than zero'. | medium |
| TC-013 (boundary) | WF-002 | Start Date is today | Contribution amount meets minimum, Funding account has adequate balance | 1. Enter a valid Fund Symbol<br>2. Enter a valid Contribution Amount<br>3. Select 'Weekly' from the Frequency dropdown<br>4. Enter today's date in the Start Date field<br>5. Select a Funding Account<br>6. Click Create Plan | Inline error shown: 'Start date must be in the future'. | medium |
| TC-014 (boundary) | WF-002 | Start Date is in the future | Contribution amount meets minimum, Funding account has adequate balance | 1. Enter a valid Fund Symbol<br>2. Enter a valid Contribution Amount<br>3. Select 'Weekly' from the Frequency dropdown<br>4. Enter a date that is one day in the future in the Start Date field<br>5. Select a Funding Account<br>6. Click Create Plan | Plan created successfully; schedule is stored. | medium |
| TC-015 (input_edge) |  | Enter long Fund Symbol |  | 1. Enter a Fund Symbol that exceeds the typical length (e.g., 50 characters)<br>2. Observe the input behavior | Field accepts input or shows an error indicating the length limit. | low |
| TC-016 (input_edge) |  | Enter special characters in Contribution Amount |  | 1. Enter special characters (e.g., '@#$%') in the Contribution Amount field<br>2. Observe the input behavior | Inline error shown indicating invalid input. | low |

---

## Account Statements

Total: **10** (positive: 2, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Generate account statement successfully | User logged in as <Role> | 1. Select a valid <Statement Period> from the date options<br>2. Select a valid <Account> from the dropdown<br>3. Click 'Generate Statement' | Statement generated successfully. | high |
| TC-002 | WF-002 | Save e-Statement preference successfully | User logged in as <Role> | 1. Check the 'Opt into Paperless' checkbox<br>2. Enter a valid <Email Address> in the Email Address field<br>3. Click 'Save Preference' | e-Statement preference updated. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Attempt to generate statement with blank Statement Period |  | 1. Leave the Statement Period field blank<br>2. Select an Account from the dropdown<br>3. Click Generate Statement | Form does not submit; Statement Period field is highlighted with an error indicating it is required | high |
| TC-004 | WF-001 | Attempt to generate statement with invalid dates |  | 1. Enter <invalid date format> in the Statement Period field<br>2. Select an Account from the dropdown<br>3. Click Generate Statement | Form does not submit; error shown indicating dates must be valid | high |
| TC-005 | WF-002 | Attempt to save e-statement preference with blank Email Address |  | 1. Leave the Email Address field blank<br>2. Check the Opt into Paperless checkbox<br>3. Click Save Preference | Form does not submit; Email Address field is highlighted with an error indicating it is required | high |
| TC-006 | WF-002 | Attempt to save e-statement preference with invalid email format |  | 1. Enter <invalid email format> in the Email Address field<br>2. Check the Opt into Paperless checkbox<br>3. Click Save Preference | Form does not submit; Email Address field displays an error: 'Must be a valid email address' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) | WF-001 | Generate statement with invalid date range |  | 1. Enter an invalid date range in the Statement Period field<br>2. Select an account from the dropdown<br>3. Click Generate Statement | Unable to generate statement — please try again later. | medium |
| TC-008 (boundary) | WF-002 | Save preference with invalid email address |  | 1. Enter an invalid email address in the Email_Address field<br>2. Check the Opt_into_Paperless checkbox<br>3. Click Save Preference | Email_Address field is highlighted with guidance. | medium |
| TC-009 (input_edge) |  | Enter long email address |  | 1. Enter a very long email address (over 254 characters) in the Email_Address field<br>2. Click Save Preference | Email_Address field is highlighted with guidance. | low |
| TC-010 (input_edge) |  | Enter email address with special characters |  | 1. Enter an email address with special characters (e.g., 'user!#$%&'*+/=?^_`{|}~@example.com') in the Email_Address field<br>2. Click Save Preference | Email_Address field is highlighted with guidance. | low |

---

## Security Settings

Total: **10** (positive: 1, negative: 6, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Change Password with valid credentials | User logged in as <Role> | 1. Enter <valid current password> in the Current Password field<br>2. Enter <valid new password> in the New Password field<br>3. Enter <same valid new password> in the Confirm New Password field<br>4. Click Change Password | Password changed successfully. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Leave Current Password blank and submit |  | 1. Leave the Current Password field blank<br>2. Fill New Password and Confirm New Password with valid values<br>3. Click Change Password | Inline validation error appears on the Current Password field indicating it is required | high |
| TC-003 | WF-001 | Leave New Password blank and submit |  | 1. Fill Current Password with valid value<br>2. Leave the New Password field blank<br>3. Fill Confirm New Password with valid value<br>4. Click Change Password | Inline validation error appears on the New Password field indicating it is required | high |
| TC-004 | WF-001 | Leave Confirm New Password blank and submit |  | 1. Fill Current Password with valid value<br>2. Fill New Password with valid value<br>3. Leave the Confirm New Password field blank<br>4. Click Change Password | Inline validation error appears on the Confirm New Password field indicating it is required | high |
| TC-005 | WF-001 | Enter Current Password incorrectly and submit |  | 1. Enter <incorrect current password> in the Current Password field<br>2. Fill New Password and Confirm New Password with valid values<br>3. Click Change Password | Inline validation error appears indicating 'must verify current password' | high |
| TC-006 | WF-001 | Enter New Password that does not meet strong-password policy |  | 1. Fill Current Password with valid value<br>2. Enter <weak password> in the New Password field<br>3. Fill Confirm New Password with the same <weak password><br>4. Click Change Password | Inline validation error appears on the New Password field indicating 'must meet strong-password policy' | high |
| TC-007 | WF-001 | Enter mismatched New Password and Confirm New Password |  | 1. Fill Current Password with valid value<br>2. Fill New Password with valid value<br>3. Fill Confirm New Password with a different value<br>4. Click Change Password | Inline validation error appears on the Confirm New Password field indicating 'must match New Password' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) | WF-001 | Enter a valid Current Password that matches the existing password |  | 1. Enter the valid Current Password in the Current Password field<br>2. Enter a New Password that meets the strong-password policy in the New Password field<br>3. Enter the same New Password in the Confirm New Password field<br>4. Click Change Password | Password changed successfully. | medium |
| TC-009 (boundary) | WF-001 | Enter a New Password that is just below the strong-password policy requirements |  | 1. Enter the valid Current Password in the Current Password field<br>2. Enter a New Password that does not meet the strong-password policy in the New Password field<br>3. Enter the same New Password in the Confirm New Password field<br>4. Click Change Password | Validation error highlights the New Password field indicating it must meet strong-password policy. | medium |
| TC-010 (boundary) | WF-001 | Enter a Confirm New Password that does not match the New Password |  | 1. Enter the valid Current Password in the Current Password field<br>2. Enter a valid New Password in the New Password field<br>3. Enter a different password in the Confirm New Password field<br>4. Click Change Password | Validation error highlights the Confirm New Password field indicating it must match New Password. | medium |

---

## Support Center

Total: **14** (positive: 2, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Send a secure message successfully | User logged in as <Role> | 1. Enter <valid subject> in the Subject field<br>2. Select 'Technical' from the Category dropdown<br>3. Enter <valid message body> in the Message Body field<br>4. Click 'Send Message' | Message sent successfully with ticket ID | high |
| TC-002 | WF-002 | Request a callback successfully | User logged in as <Role> | 1. Select <valid reason for call> from the Reason for Call dropdown<br>2. Enter <valid date> in the Preferred Date field<br>3. Enter <valid time window> in the Preferred Time Window field<br>4. Verify the Phone Number field is pre-filled<br>5. Click 'Request Callback' | Callback request submitted and email confirmation sent | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Message Body field blank and submit |  | 1. Leave the Message Body field blank<br>2. Fill in Subject and Category with valid values<br>3. Click Send Message | Inline validation error appears on the Message Body field indicating it is required | high |
| TC-004 |  | Leave the Preferred Date field blank and submit |  | 1. Leave the Preferred Date field blank<br>2. Fill in Reason for Call and Phone Number with valid values<br>3. Click Request Callback | Inline validation error appears on the Preferred Date field indicating it is required | high |
| TC-005 |  | Submit the secure message form with an invalid subject length |  | 1. Enter <invalid subject length> in the Subject field<br>2. Fill in Message Body with valid content<br>3. Click Send Message | Inline validation error appears on the Subject field indicating 'subject length must be valid' | medium |
| TC-006 |  | Submit the schedule callback form with an invalid phone number format |  | 1. Enter <invalid phone number format> in the Phone Number field<br>2. Fill in Reason for Call and Preferred Date with valid values<br>3. Click Request Callback | Inline validation error appears on the Phone Number field indicating 'phone number format must be valid' | medium |
| TC-007 |  | Submit the schedule callback form with a Preferred Date that is not the next business day |  | 1. Enter <date not next business day> in the Preferred Date field<br>2. Fill in Reason for Call and Phone Number with valid values<br>3. Click Request Callback | Inline validation error appears on the Preferred Date field indicating 'date must be at least the next business day' | medium |
| TC-008 |  | Submit the secure message form with an invalid attachment type |  | 1. Attach a file with an invalid type in the Attachment field<br>2. Fill in Subject and Message Body with valid values<br>3. Click Send Message | Inline validation error appears on the Attachment field indicating 'attachment types must be valid' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-002 | Test preferred date as the next business day | User is on the Schedule Callback Form | 1. Select a date that is the next business day in the Preferred_Date field<br>2. Fill in all other required fields<br>3. Click Request Callback | Callback request submitted and email confirmation sent | medium |
| TC-010 (boundary) | WF-002 | Test preferred date as one day before the next business day | User is on the Schedule Callback Form | 1. Select a date that is one day before the next business day in the Preferred_Date field<br>2. Fill in all other required fields<br>3. Click Request Callback | Inline error shown indicating the date must be at least the next business day | medium |
| TC-011 (boundary) | WF-001 | Test subject length at the minimum valid length | User is on the Secure Message Form | 1. Enter the minimum valid length subject in the Subject field<br>2. Select a category from the dropdown<br>3. Enter a message body in the Message_Body field<br>4. Click Send Message | Message sent successfully with ticket ID | medium |
| TC-012 (boundary) | WF-001 | Test subject length below the minimum valid length | User is on the Secure Message Form | 1. Enter a subject that is below the minimum valid length in the Subject field<br>2. Select a category from the dropdown<br>3. Enter a message body in the Message_Body field<br>4. Click Send Message | Inline error shown indicating the subject length must be valid | medium |
| TC-013 (input_edge) |  | Test message body with a very long text | User is on the Secure Message Form | 1. Enter a very long text (200+ characters) in the Message_Body field<br>2. Enter a valid subject in the Subject field<br>3. Select a category from the dropdown<br>4. Click Send Message | Message sent successfully with ticket ID or inline error shown indicating message body must be present | low |
| TC-014 (input_edge) |  | Test phone number with invalid format | User is on the Schedule Callback Form | 1. Enter an invalid phone number format in the Phone_Number field<br>2. Select a reason for the call from the dropdown<br>3. Select a valid preferred date<br>4. Click Request Callback | Inline error shown indicating phone number format must be valid | low |

---
