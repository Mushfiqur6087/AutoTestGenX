# Post-Verification Specifications

### [TC-001] Send a secure message successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <valid subject> in the Subject field
2. 2. Select 'Technical' from the Category dropdown
3. 3. Enter <valid message body> in the Message Body field
4. 4. Click 'Send Message'

**Original Expected Result:** Message sent successfully with ticket ID

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - welcome message
  - list of accounts

**Post-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - welcome message
  - list of accounts

**Expected Change**: A new account appears in the list of accounts with the correct details.

---

### [TC-001] Send a secure message successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <valid subject> in the Subject field
2. 2. Select 'Technical' from the Category dropdown
3. 3. Enter <valid message body> in the Message Body field
4. 4. Click 'Send Message'

**Original Expected Result:** Message sent successfully with ticket ID

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - list of accounts
  - total balance

**Post-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - list of accounts
  - total balance

**Expected Change**: A new Checking account appears in the list of accounts with a balance of $25, and the total balance has increased by $25.

---

### [TC-002] Request a callback successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Select <valid reason for call> from the Reason for Call dropdown
2. 2. Enter <valid date> in the Preferred Date field
3. 3. Enter <valid time window> in the Preferred Time Window field
4. 4. Verify the Phone Number field is pre-filled
5. 5. Click 'Request Callback'

**Original Expected Result:** Callback request submitted and email confirmation sent

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - list of accounts
  - total balance

**Post-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - list of accounts
  - total balance

**Expected Change**: A new Savings account appears in the list of accounts with a balance of 100, and the total balance has increased accordingly.

---

### [TC-001] Send a secure message successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <valid subject> in the Subject field
2. 2. Select 'Technical' from the Category dropdown
3. 3. Enter <valid message body> in the Message Body field
4. 4. Click 'Send Message'

**Original Expected Result:** Message sent successfully with ticket ID

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - balance of Checking account
  - total balance across all accounts

**Post-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - balance of Checking account
  - total balance across all accounts

**Expected Change**: Checking account balance decreased by the transfer amount; total balance across all accounts remains unchanged.

---

### [TC-002] Request a callback successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Select <valid reason for call> from the Reason for Call dropdown
2. 2. Enter <valid date> in the Preferred Date field
3. 3. Enter <valid time window> in the Preferred Time Window field
4. 4. Verify the Phone Number field is pre-filled
5. 5. Click 'Request Callback'

**Original Expected Result:** Callback request submitted and email confirmation sent

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - balance of Savings account
  - transaction history

**Post-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - balance of Savings account
  - transaction history

**Expected Change**: Savings account balance decreased by the transfer amount; transaction history includes a new entry for the external transfer.

---

### [TC-001] Send a secure message successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <valid subject> in the Subject field
2. 2. Select 'Technical' from the Category dropdown
3. 3. Enter <valid message body> in the Message Body field
4. 4. Click 'Send Message'

**Original Expected Result:** Message sent successfully with ticket ID

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Payments Overview`
- **Observe**:
  - payment history
  - current balance of source account

**Post-Check**
- **Navigate To**: `Payments Overview`
- **Observe**:
  - payment history
  - current balance of source account

**Expected Change**: Payment history includes the new payment entry with the correct reference code, and the current balance of the source account reflects the deducted payment amount.

---

### [TC-001] Send a secure message successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <valid subject> in the Subject field
2. 2. Select 'Technical' from the Category dropdown
3. 3. Enter <valid message body> in the Message Body field
4. 4. Click 'Send Message'

**Original Expected Result:** Message sent successfully with ticket ID

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - total balance across all accounts
  - loan account section

**Post-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - total balance across all accounts
  - loan account section

**Expected Change**: A new loan account appears in the loan account section with the correct loan amount and status.

---

### [TC-002] Request a callback successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Select <valid reason for call> from the Reason for Call dropdown
2. 2. Enter <valid date> in the Preferred Date field
3. 3. Enter <valid time window> in the Preferred Time Window field
4. 4. Verify the Phone Number field is pre-filled
5. 5. Click 'Request Callback'

**Original Expected Result:** Callback request submitted and email confirmation sent

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - loan account section
  - total balance across all accounts

**Post-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - loan account section
  - total balance across all accounts

**Expected Change**: A new loan account appears in the loan account section, and the total balance across all accounts reflects the new loan amount.

---

### [TC-003] Leave the Message Body field blank and submit
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Leave the Message Body field blank
2. 2. Fill in Subject and Category with valid values
3. 3. Click Send Message

**Original Expected Result:** Inline validation error appears on the Message Body field indicating it is required

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - loan account details
  - total balance

**Post-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - loan account details
  - total balance

**Expected Change**: A new loan account appears in the Accounts Overview with the correct loan amount and the total balance reflects the new loan.

---

### [TC-001] Send a secure message successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <valid subject> in the Subject field
2. 2. Select 'Technical' from the Category dropdown
3. 3. Enter <valid message body> in the Message Body field
4. 4. Click 'Send Message'

**Original Expected Result:** Message sent successfully with ticket ID

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Customer Profile`
- **Observe**:
  - First Name
  - Last Name
  - Street Address
  - City
  - State
  - ZIP Code
  - Phone Number

**Post-Check**
- **Navigate To**: `Customer Profile`
- **Observe**:
  - First Name
  - Last Name
  - Street Address
  - City
  - State
  - ZIP Code
  - Phone Number

**Expected Change**: All fields reflect the updated contact information entered by the user.

---

### [TC-001] Send a secure message successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <valid subject> in the Subject field
2. 2. Select 'Technical' from the Category dropdown
3. 3. Enter <valid message body> in the Message Body field
4. 4. Click 'Send Message'

**Original Expected Result:** Message sent successfully with ticket ID

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Manage Cards`
- **Observe**:
  - Card request form
  - Shipping Address field
  - Account to Link field

**Post-Check**
- **Navigate To**: `Manage Cards`
- **Observe**:
  - Card request form
  - Shipping Address field
  - Account to Link field

**Expected Change**: A new card request is submitted and the user receives a confirmation message indicating 'Card request submitted successfully.'

---

### [TC-002] Request a callback successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Select <valid reason for call> from the Reason for Call dropdown
2. 2. Enter <valid date> in the Preferred Date field
3. 3. Enter <valid time window> in the Preferred Time Window field
4. 4. Verify the Phone Number field is pre-filled
5. 5. Click 'Request Callback'

**Original Expected Result:** Callback request submitted and email confirmation sent

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Manage Cards`
- **Observe**:
  - current spending limit of selected card
  - current travel notice
  - current card status

**Post-Check**
- **Navigate To**: `Manage Cards`
- **Observe**:
  - new spending limit of selected card
  - updated travel notice
  - updated card status

**Expected Change**: Spending limit updated to the new value; travel notice reflects the entered date range and destination; card status is now 'Active'.

---

### [TC-001] Send a secure message successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <valid subject> in the Subject field
2. 2. Select 'Technical' from the Category dropdown
3. 3. Enter <valid message body> in the Message Body field
4. 4. Click 'Send Message'

**Original Expected Result:** Message sent successfully with ticket ID

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Investments`
- **Observe**:
  - current fund holdings
  - market value
  - unrealised gain or loss

**Post-Check**
- **Navigate To**: `Investments`
- **Observe**:
  - current fund holdings
  - market value
  - unrealised gain or loss

**Expected Change**: The current fund holdings reflect the newly executed trade, updating the market value and unrealised gain or loss accordingly.

---

### [TC-002] Request a callback successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Select <valid reason for call> from the Reason for Call dropdown
2. 2. Enter <valid date> in the Preferred Date field
3. 3. Enter <valid time window> in the Preferred Time Window field
4. 4. Verify the Phone Number field is pre-filled
5. 5. Click 'Request Callback'

**Original Expected Result:** Callback request submitted and email confirmation sent

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Investments`
- **Observe**:
  - current fund holdings
  - recurring investment plans section

**Post-Check**
- **Navigate To**: `Investments`
- **Observe**:
  - current fund holdings
  - recurring investment plans section

**Expected Change**: A new recurring investment plan appears in the recurring investment plans section with the correct fund symbol, contribution amount, frequency, and start date.

---

### [TC-002] Request a callback successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Select <valid reason for call> from the Reason for Call dropdown
2. 2. Enter <valid date> in the Preferred Date field
3. 3. Enter <valid time window> in the Preferred Time Window field
4. 4. Verify the Phone Number field is pre-filled
5. 5. Click 'Request Callback'

**Original Expected Result:** Callback request submitted and email confirmation sent

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `e-Statement Preference section`
- **Observe**:
  - current e-Statement preference status
  - current email address

**Post-Check**
- **Navigate To**: `e-Statement Preference section`
- **Observe**:
  - updated e-Statement preference status
  - updated email address

**Expected Change**: e-Statement preference status changed to 'Opted into Paperless' and email address updated to the new value.

---

### [TC-001] Send a secure message successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <valid subject> in the Subject field
2. 2. Select 'Technical' from the Category dropdown
3. 3. Enter <valid message body> in the Message Body field
4. 4. Click 'Send Message'

**Original Expected Result:** Message sent successfully with ticket ID

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Security Settings`
- **Observe**:
  - Current Password field
  - New Password field
  - Confirm New Password field

**Post-Check**
- **Navigate To**: `Security Settings`
- **Observe**:
  - Current Password field
  - New Password field
  - Confirm New Password field

**Expected Change**: User is able to log in with the new password, confirming that the password has been successfully changed.

---

### [TC-001] Send a secure message successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <valid subject> in the Subject field
2. 2. Select 'Technical' from the Category dropdown
3. 3. Enter <valid message body> in the Message Body field
4. 4. Click 'Send Message'

**Original Expected Result:** Message sent successfully with ticket ID

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Support Center`
- **Observe**:
  - Subject field
  - Category dropdown
  - Message Body field

**Post-Check**
- **Navigate To**: `Support Center`
- **Observe**:
  - Message sent successfully.
  - Ticket ID

**Expected Change**: A confirmation message appears indicating the message was sent successfully along with a ticket ID.

---

### [TC-002] Request a callback successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Select <valid reason for call> from the Reason for Call dropdown
2. 2. Enter <valid date> in the Preferred Date field
3. 3. Enter <valid time window> in the Preferred Time Window field
4. 4. Verify the Phone Number field is pre-filled
5. 5. Click 'Request Callback'

**Original Expected Result:** Callback request submitted and email confirmation sent

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Support Center`
- **Observe**:
  - callback request form
  - existing callback requests

**Post-Check**
- **Navigate To**: `Support Center`
- **Observe**:
  - existing callback requests
  - email confirmation

**Expected Change**: A new callback request appears in the existing requests list, and an email confirmation is received.

---
