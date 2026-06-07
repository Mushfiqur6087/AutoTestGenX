# Post-Verification Specifications

### [TC-001] Send secure message (basic) with required message body
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to the Support Center page
2. 2. In the Secure Message form, enter <optional subject> in the Subject field
3. 3. Select <Category> from the Category dropdown
4. 4. Enter <valid message body> in the Message Body rich text editor
5. 5. (Optional) Leave Attachment empty
6. 6. Click the 'Send Message' button

**Original Expected Result:** A success notification displays: "Message sent successfully. Returns ticket ID." and the notification shows a visible ticket ID

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Login page`
- **Observe**:
  - Sign In form present (Email/Username and Password fields)
  - No active session / Accounts Overview not displayed

**Post-Check**
- **Navigate To**: `Login page`
- **Observe**:
  - Enter the registered Email/Username and Password and submit the Sign In form
  - Flash message: 'Signed in successfully.'
  - Redirected to Accounts Overview page
  - Welcome message contains the registered first and last name
  - Accounts table is displayed (rows and footer total balance present)

**Expected Change**: The newly registered credentials authenticate successfully: signing in with the registered email/username and password shows 'Signed in successfully.' and redirects to the Accounts Overview with the user's welcome message and accounts table, proving the user account was created in the backend.

---

### [TC-002] Send secure message with a valid attachment
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to the Support Center page
2. 2. In the Secure Message form, enter <optional subject> in the Subject field
3. 3. Select <Category> from the Category dropdown
4. 4. Enter <valid message body> in the Message Body rich text editor
5. 5. Click 'Upload' on the Attachment control and select <valid allowed file> from the OS file dialog
6. 6. Confirm the attachment appears in the form upload list
7. 7. Click the 'Send Message' button

**Original Expected Result:** A success notification displays: "Message sent successfully. Returns ticket ID." and the support message list shows a new message row with the entered Subject and a visible attachment name

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Registration page`
- **Observe**:
  - Registration form is displayed with fields for First Name, Last Name, ZIP Code, Phone Number, SSN, Username (email), Password, Confirm Password
  - Username (email) field is available to enter a new email address

**Post-Check**
- **Navigate To**: `Login page`
- **Observe**:
  - Flash message 'Account created successfully — please sign in' is shown
  - Able to authenticate using the newly registered Username (email) and Password
  - After authentication, user is redirected to Accounts Overview
  - Accounts Overview displays a welcome message containing the registered user's first and last name and the accounts table (may be empty for a new user)

**Expected Change**: A new user account was created in the backend: the newly registered credentials successfully authenticate, producing 'Signed in successfully.' and redirecting to Accounts Overview where the welcome message shows the registered name.

---

### [TC-003] Request callback with valid next-business-day date, time window and editable phone number
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to the Support Center page
2. 2. In the Schedule Callback form, select <Reason for Call> from the Reason for Call dropdown
3. 3. Select <valid date at least next business day> in the Preferred Date field
4. 4. Select <Preferred Time Window> in the Preferred Time Window control
5. 5. Verify Phone Number is pre-filled, edit it to <valid phone number> if needed
6. 6. Click the 'Request Callback' button

**Original Expected Result:** A confirmation banner displays: "Callback request submitted. Sends email confirmation." and the confirmation panel shows the selected Preferred Date, Preferred Time Window and the Phone Number used for the request

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Login page`
- **Observe**:
  - Attempt to sign in using the same Username (email) and Password values that will be used in the registration test
  - Authentication failure banner text (e.g., "Incorrect email or password. Please try again.") or lack of successful sign-in

**Post-Check**
- **Navigate To**: `Login page`
- **Observe**:
  - Successful sign-in flash message: "Signed in successfully."
  - Redirect to Accounts Overview page
  - Welcome message that includes the registered user's name
  - Accounts table or dashboard elements (account rows, total balance footer)

**Expected Change**: Before registration, signing in with the test email/password fails with an authentication error. After completing the registration steps, signing in with the same email/password succeeds, flashes "Signed in successfully.", and redirects to Accounts Overview where the welcome message shows the new user's name and the accounts/dashboard is displayed.

---

### [TC-004] Send Message: leave Message Body blank and submit
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Leave the Message Body field blank
2. 2. Enter <valid Subject> in the Subject field
3. 3. Select <Category option> in the Category dropdown
4. 4. (Optional) Upload <valid attachment of allowed type> in Attachment
5. 5. Click the Send Message button

**Original Expected Result:** Message Body field displays an inline validation error indicating it is required; form does not submit; no ticket is created and the page remains on the Secure Message form

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Login page`
- **Observe**:
  - Attempt to sign in using the exact Username (email) and Password planned for registration
  - Expected failed authentication response: 'Incorrect email or password. Please try again.' (verifies account does not yet exist)

**Post-Check**
- **Navigate To**: `Login page`
- **Observe**:
  - Flash message 'Signed in successfully.' after submitting the registered credentials
  - Redirect to Accounts Overview page
  - Welcome message contains the registered First Name and Last Name
  - Accounts Overview displays the accounts table footer (total balance) or at least the Accounts Overview left-hand navigation item present

**Expected Change**: After registration the same credentials can be used to sign in successfully; user is redirected to Accounts Overview and the welcome message shows the registered name, proving the user account was created in the backend.

---

### [TC-001] Send secure message (basic) with required message body
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to the Support Center page
2. 2. In the Secure Message form, enter <optional subject> in the Subject field
3. 3. Select <Category> from the Category dropdown
4. 4. Enter <valid message body> in the Message Body rich text editor
5. 5. (Optional) Leave Attachment empty
6. 6. Click the 'Send Message' button

**Original Expected Result:** A success notification displays: "Message sent successfully. Returns ticket ID." and the notification shows a visible ticket ID

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - count of account rows
  - table footer: total balance across all accounts
  - for the funding source account: masked account number and current balance
  - for each account row: Account Type, masked Account Number, Current Balance, Account Status, Open Date (rows ordered by Open Date, earliest first)

**Post-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - count of account rows
  - table footer: total balance across all accounts
  - presence of a new account row (should be the most recently opened account — appears as the last row given earliest-first ordering)
  - new account row details: Account Type, masked Account Number, Current Balance, Account Status, Open Date
  - for the funding source account: masked account number and updated current balance

**Expected Change**: Number of account rows increased by 1. A new account row exists for a Checking account with Current Balance = $25, Account Status = 'Active', and Open Date = today (appearing as the most recently created row). The funding source account's current balance decreased by $25. The table footer total balance across all accounts remains unchanged (the $25 was moved internally from the funding account into the new checking account).

---

### [TC-002] Send secure message with a valid attachment
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to the Support Center page
2. 2. In the Secure Message form, enter <optional subject> in the Subject field
3. 3. Select <Category> from the Category dropdown
4. 4. Enter <valid message body> in the Message Body rich text editor
5. 5. Click 'Upload' on the Attachment control and select <valid allowed file> from the OS file dialog
6. 6. Confirm the attachment appears in the form upload list
7. 7. Click the 'Send Message' button

**Original Expected Result:** A success notification displays: "Message sent successfully. Returns ticket ID." and the support message list shows a new message row with the entered Subject and a visible attachment name

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - number of accounts (row count)
  - accounts table rows with columns: Account Number (masked), Account Type, Current Balance, Account Status, Open Date
  - identify and note the funding source account row and its Current Balance
  - total balance across all accounts (footer total)

**Post-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - number of accounts (row count)
  - presence of a new account row with Account Type 'Savings' and Current Balance $100.00
  - new account row shows Account Status 'Active' and an Open Date equal to today's date and an Account Number masked as ****last4
  - funding source account row's Current Balance
  - total balance across all accounts (footer total)

**Expected Change**: Account count increased by 1; a new 'Savings' account row appears (typically the most recently opened row) showing Current Balance = $100.00, Account Status = 'Active', and Open Date = today's date with a masked account number. The original funding source account's balance has decreased by $100.00. The footer total balance across all accounts remains unchanged (funds moved internally between accounts).

---

### [TC-001] Send secure message (basic) with required message body
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to the Support Center page
2. 2. In the Secure Message form, enter <optional subject> in the Subject field
3. 3. Select <Category> from the Category dropdown
4. 4. Enter <valid message body> in the Message Body rich text editor
5. 5. (Optional) Leave Attachment empty
6. 6. Click the 'Send Message' button

**Original Expected Result:** A success notification displays: "Message sent successfully. Returns ticket ID." and the notification shows a visible ticket ID

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounts Overview -> open Source Account details (Transactions tab) and view Accounts table`
- **Observe**:
  - current balance of source account (as shown on Accounts Overview and in Source Account details)
  - current balance of destination account (as shown on Accounts Overview)
  - most recent transaction ID or timestamp in source account transaction list (if present)

**Post-Check**
- **Navigate To**: `Accounts Overview -> open Source Account details (Transactions tab) and open Destination Account details (Transactions tab)`
- **Observe**:
  - updated balance of source account
  - updated balance of destination account
  - new transaction entry in source account transactions containing the transaction ID shown on the transfer success screen and the transfer amount
  - new transaction entry in destination account transactions referencing the same transaction ID (or corresponding deposit entry) and the transfer amount

**Expected Change**: Source account balance decreased by the transfer amount; destination account balance increased by the same transfer amount; combined total across both accounts remains unchanged; a new transaction appears in the source (debit) and destination (credit) transaction lists showing the same transaction ID displayed on the transfer success page and matching the transfer amount.

---

### [TC-002] Send secure message with a valid attachment
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to the Support Center page
2. 2. In the Secure Message form, enter <optional subject> in the Subject field
3. 3. Select <Category> from the Category dropdown
4. 4. Enter <valid message body> in the Message Body rich text editor
5. 5. Click 'Upload' on the Attachment control and select <valid allowed file> from the OS file dialog
6. 6. Confirm the attachment appears in the form upload list
7. 7. Click the 'Send Message' button

**Original Expected Result:** A success notification displays: "Message sent successfully. Returns ticket ID." and the support message list shows a new message row with the entered Subject and a visible attachment name

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - balance of Source account (capture value as pre_balance)
  - total balance footer (capture value as pre_total_balance)

**Post-Check**
- **Navigate To**: `Accounts Overview; Statements -> Generate Statement (select Source account and a date range covering the transfer date)`
- **Observe**:
  - balance of Source account (capture value as post_balance)
  - total balance footer (capture value as post_total_balance)
  - Generated statement / transactions list for the Source account showing recent transactions
  - Transaction entry with the Transaction ID shown on the transfer success screen (or a transaction matching the transfer amount and external payee details, account numbers masked)

**Expected Change**: Source account balance decreased by the transfer amount (post_balance = pre_balance - transfer_amount); total balance footer decreased by the same amount. A transaction appears in the generated statement/transactions list corresponding to the transfer, with the same transfer amount and the Transaction ID that was displayed on the transfer success screen (external account details shown masked as per UI).

---

### [TC-001] Send secure message (basic) with required message body
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to the Support Center page
2. 2. In the Secure Message form, enter <optional subject> in the Subject field
3. 3. Select <Category> from the Category dropdown
4. 4. Enter <valid message body> in the Message Body rich text editor
5. 5. (Optional) Leave Attachment empty
6. 6. Click the 'Send Message' button

**Original Expected Result:** A success notification displays: "Message sent successfully. Returns ticket ID." and the notification shows a visible ticket ID

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - balance of <Source_Account> (as shown in the accounts table)

**Post-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - balance of <Source_Account> (as shown in the accounts table)

**Expected Change**: The Source Account balance is decreased by the <payment amount> (new_balance = old_balance - payment amount). The deduction equals the submitted Payment Amount. Additionally, the Payments page displayed a success notification containing a visible reference code for the transaction when the payment was submitted.

---

### [TC-002] Send secure message with a valid attachment
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to the Support Center page
2. 2. In the Secure Message form, enter <optional subject> in the Subject field
3. 3. Select <Category> from the Category dropdown
4. 4. Enter <valid message body> in the Message Body rich text editor
5. 5. Click 'Upload' on the Attachment control and select <valid allowed file> from the OS file dialog
6. 6. Confirm the attachment appears in the form upload list
7. 7. Click the 'Send Message' button

**Original Expected Result:** A success notification displays: "Message sent successfully. Returns ticket ID." and the support message list shows a new message row with the entered Subject and a visible attachment name

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Payments -> Bill Payment form (Payments page with Bill Payment form visible)`
- **Observe**:
  - displayed balance of <alternate Source_Account> on the Payments page (record this value as pre_check_balance)
  - no success notification for the current payment is present

**Post-Check**
- **Navigate To**: `Payments -> Bill Payment form (then Accounts Overview to cross-check balances)`
- **Observe**:
  - success notification text on screen
  - visible reference code within the success notification
  - displayed balance of <alternate Source_Account> on the Payments page
  - displayed balance of <alternate Source_Account> on the Accounts Overview page (if present)

**Expected Change**: A success notification appears containing the exact message 'Payment submitted successfully. Returns a reference code and updates account balances.' and includes a visible reference code; the displayed balance for <alternate Source_Account> is reduced by <payment amount> compared to the pre_check_balance on the Payments page, and the same reduced balance is reflected on the Accounts Overview page (post-check balance = pre_check_balance - <payment amount>).

---

### [TC-001] Send secure message (basic) with required message body
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to the Support Center page
2. 2. In the Secure Message form, enter <optional subject> in the Subject field
3. 3. Select <Category> from the Category dropdown
4. 4. Enter <valid message body> in the Message Body rich text editor
5. 5. (Optional) Leave Attachment empty
6. 6. Click the 'Send Message' button

**Original Expected Result:** A success notification displays: "Message sent successfully. Returns ticket ID." and the notification shows a visible ticket ID

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - list of account rows and their Account Type values
  - count of accounts (number of rows)
  - absence of any account row with Account Type 'Personal' or 'Loan' that matches the forthcoming loan details

**Post-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - presence of a new account row representing the approved loan
  - Account Type value showing 'Personal' (or 'Loan - Personal')
  - Account Identifier displayed (masked showing only last 4 digits, e.g., ****1234)
  - Current Balance / Principal equal to the approved Loan Amount shown in the loan details
  - Account Status badge (e.g., 'Active') for the new loan account
  - Open Date displayed for the new loan account
  - total account count increased by 1 compared to pre_check (footer row or row count)

**Expected Change**: A new loan account row for the approved Personal loan appears in Accounts Overview with a loan account identifier (masked), Account Type 'Personal', Current Balance/Principal equal to the approved Loan Amount, an 'Active' status badge, an Open Date corresponding to creation, and the total number of accounts increased by one.

---

### [TC-002] Send secure message with a valid attachment
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to the Support Center page
2. 2. In the Secure Message form, enter <optional subject> in the Subject field
3. 3. Select <Category> from the Category dropdown
4. 4. Enter <valid message body> in the Message Body rich text editor
5. 5. Click 'Upload' on the Attachment control and select <valid allowed file> from the OS file dialog
6. 6. Confirm the attachment appears in the form upload list
7. 7. Click the 'Send Message' button

**Original Expected Result:** A success notification displays: "Message sent successfully. Returns ticket ID." and the support message list shows a new message row with the entered Subject and a visible attachment name

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - total number of accounts listed
  - for each account row: Account Type, masked Account Number (last 4 digits), Current Balance, Account Status, Open Date
  - count/list of any existing accounts with Account Type containing 'Auto' (and their displayed balances)

**Post-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - a new account row with Account Type containing 'Auto'
  - masked Account Number in the new row whose last 4 digits match the loan account identifier (last 4 digits) shown on the loan-success confirmation screen
  - displayed Current Balance or displayed loan amount for that account equals the approved Loan_Amount returned on the success screen
  - Account Status for the new row shows 'Active' (or equivalent active badge)
  - Open Date for the new row is today's date (or the loan creation date returned on the success screen)

**Expected Change**: The Accounts Overview shows one additional account row representing the approved Auto loan: an Account Type containing 'Auto' appears, the masked account number's last 4 digits match the loan identifier returned by the success screen, the displayed amount matches the approved Loan_Amount, the account status is Active, and the account's Open Date equals the loan creation date. The total account count increases by 1.

---

### [TC-003] Request callback with valid next-business-day date, time window and editable phone number
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to the Support Center page
2. 2. In the Schedule Callback form, select <Reason for Call> from the Reason for Call dropdown
3. 3. Select <valid date at least next business day> in the Preferred Date field
4. 4. Select <Preferred Time Window> in the Preferred Time Window control
5. 5. Verify Phone Number is pre-filled, edit it to <valid phone number> if needed
6. 6. Click the 'Request Callback' button

**Original Expected Result:** A confirmation banner displays: "Callback request submitted. Sends email confirmation." and the confirmation panel shows the selected Preferred Date, Preferred Time Window and the Phone Number used for the request

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounts Overview`
- **Observe**:
  - count of account rows in the accounts table
  - list of account rows showing Account Type and masked Account Number (e.g., ****1234)
  - Current Balance for the collateral account selected in the application (record the balance value)

**Post-Check**
- **Navigate To**: `Accounts Overview -> (click the newest account row corresponding to the loan) -> Loan Details`
- **Observe**:
  - accounts table has one additional row compared to pre-check
  - new account row with Account Type 'Loan' or 'Home Loan' appears (masked account number shown)
  - masked account number on the new row matches the loan account identifier shown on the application success screen
  - open the new loan account row to view Loan Details page showing: Loan Type 'Home', Approved Loan Amount, Loan Account Identifier, Account Status (e.g., Active), and Open Date
  - Current Balance of the collateral account recorded in pre-check is unchanged

**Expected Change**: Accounts table contains one additional account row representing the newly created loan; the new loan's masked account identifier matches the identifier shown on the loan-approval success screen; the Loan Details page displays Loan Type 'Home', the approved loan amount, loan account identifier, status 'Active', and today's open date. The collateral account balance remains unchanged (no debit).

---

### [TC-008] Request Callback: clear pre-filled Phone Number and submit (required field left blank)
**Category**: `negative` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Clear the Phone Number field so it is empty
2. 2. Select <valid Reason_for_Call> in the Reason for Call dropdown
3. 3. Enter <valid Preferred_Date at least next business day> in Preferred Date
4. 4. Select <valid Preferred_Time_Window> in Preferred Time Window
5. 5. Click the Request Callback button

**Original Expected Result:** Phone Number field displays an inline validation error indicating it is required; form does not submit; no callback request is created

---

#### Verification Plan

**Actor A (Role: `applicant`)**
- **Action**: Execute the steps from the core test case (open Request Loan page, submit application with Down_Payment < 10% of Loan_Amount).

**Actor B (Role: `loan_officer`)**
- **Session**: `new_session`
- **Navigate To**: `Admin -> Loan Applications (or Loan Processing Queue)`
- **Action**: 
- **Observe**:
  - applicant username or name
  - application ID or reference
  - loan type
  - loan amount
  - down payment amount
  - collateral account (identifier and balance)
  - application submission timestamp
  - application status (e.g., Denied / Declined)
  - denial reason/message (text shown by credit engine)

**Expected Change**: A new loan application record exists for the applicant with the submitted Loan_Amount and Down_Payment; the record's status is 'Denied' (or equivalent) and the denial reason explicitly states the down payment requirement was not met (i.e., Down_Payment is below the minimum 10% of Loan_Amount). No loan account should have been created.

---

### [TC-001] Send secure message (basic) with required message body
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to the Support Center page
2. 2. In the Secure Message form, enter <optional subject> in the Subject field
3. 3. Select <Category> from the Category dropdown
4. 4. Enter <valid message body> in the Message Body rich text editor
5. 5. (Optional) Leave Attachment empty
6. 6. Click the 'Send Message' button

**Original Expected Result:** A success notification displays: "Message sent successfully. Returns ticket ID." and the notification shows a visible ticket ID

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounts Overview -> Update Contact Info (Customer Profile) page`
- **Observe**:
  - First Name
  - Last Name
  - Street Address
  - City
  - State
  - ZIP Code
  - Phone Number

**Post-Check**
- **Navigate To**: `Accounts Overview -> Update Contact Info (Customer Profile) page (refresh or navigate away and return to verify persistence)`
- **Observe**:
  - First Name
  - Last Name
  - Street Address
  - City
  - State
  - ZIP Code
  - Phone Number
  - Success notification/banner text

**Expected Change**: After submitting the update, the profile fields show the newly submitted values: First Name = <valid first name>, Last Name = <valid last name>, Street Address = <valid street address>, City = <valid city>, State = <valid state>, ZIP Code = <valid ZIP/postal code>, Phone Number = <valid phone number>. The success notification 'Profile updated successfully.' is displayed, and the updated values persist after a refresh or after navigating away and returning to the Contact Profile page.

---

### [TC-002] Send secure message with a valid attachment
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to the Support Center page
2. 2. In the Secure Message form, enter <optional subject> in the Subject field
3. 3. Select <Category> from the Category dropdown
4. 4. Enter <valid message body> in the Message Body rich text editor
5. 5. Click 'Upload' on the Attachment control and select <valid allowed file> from the OS file dialog
6. 6. Confirm the attachment appears in the form upload list
7. 7. Click the 'Send Message' button

**Original Expected Result:** A success notification displays: "Message sent successfully. Returns ticket ID." and the support message list shows a new message row with the entered Subject and a visible attachment name

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Update Contact Info / Contact Profile page`
- **Observe**:
  - Phone Number (current value)
  - First Name
  - Last Name

**Post-Check**
- **Navigate To**: `Update Contact Info / Contact Profile page`
- **Observe**:
  - Phone Number (displayed value)
  - Success notification text 'Profile updated successfully.'
  - First Name
  - Last Name

**Expected Change**: Phone Number now equals the new value entered ('<valid phone number>') and is persisted on the profile after refresh; First Name and Last Name remain unchanged; a success notification 'Profile updated successfully.' was displayed upon submission.

---

### [TC-003] Request callback with valid next-business-day date, time window and editable phone number
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `partial`

**Coverage Note**: *The UI exposes the profile fields and a success message but does not guarantee visibility of backend audit metadata (e.g., 'last updated' timestamp or an audit log). Only the UI refresh and unchanged field values can be fully verified in-app; backend update records (if any) require access to logs or an API and are not observable here.*

**Original Steps:**
1. 1. Navigate to the Support Center page
2. 2. In the Schedule Callback form, select <Reason for Call> from the Reason for Call dropdown
3. 3. Select <valid date at least next business day> in the Preferred Date field
4. 4. Select <Preferred Time Window> in the Preferred Time Window control
5. 5. Verify Phone Number is pre-filled, edit it to <valid phone number> if needed
6. 6. Click the 'Request Callback' button

**Original Expected Result:** A confirmation banner displays: "Callback request submitted. Sends email confirmation." and the confirmation panel shows the selected Preferred Date, Preferred Time Window and the Phone Number used for the request

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Account Dashboard -> Update Contact Info (Customer Profile) page`
- **Observe**:
  - First Name (value)
  - Last Name (value)
  - Street Address (value)
  - City (value)
  - State (value)
  - ZIP Code (value)
  - Phone Number (value)
  - Presence of a 'Profile updated' or 'Last updated' timestamp field (if visible)

**Post-Check**
- **Navigate To**: `Account Dashboard -> Update Contact Info (Customer Profile) page (refresh or reload view after submission)`
- **Observe**:
  - Success notification text: "Profile updated successfully."
  - First Name (value)
  - Last Name (value)
  - Street Address (value)
  - City (value)
  - State (value)
  - ZIP Code (value)
  - Phone Number (value)
  - Presence of a 'Profile updated' or 'Last updated' timestamp field (if visible)

**Expected Change**: A success notification 'Profile updated successfully.' is displayed and the profile form remains visible showing the same pre-filled values for all fields. If the UI exposes a 'last updated' timestamp or similar audit indicator, it should advance/update to reflect the submission; otherwise, field values must remain identical to the pre-check values (no unintended modifications).

---

### [TC-001] Send secure message (basic) with required message body
**Category**: `positive` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to the Support Center page
2. 2. In the Secure Message form, enter <optional subject> in the Subject field
3. 3. Select <Category> from the Category dropdown
4. 4. Enter <valid message body> in the Message Body rich text editor
5. 5. (Optional) Leave Attachment empty
6. 6. Click the 'Send Message' button

**Original Expected Result:** A success notification displays: "Message sent successfully. Returns ticket ID." and the notification shows a visible ticket ID

---

#### Verification Plan

**Actor A (Role: `customer`)**
- **Action**: Execute the steps from the core test case. When the success message appears, copy the displayed tracking ID and note the card type, linked account, and full shipping address that were submitted.

**Actor B (Role: `support_agent`)**
- **Session**: `new_session`
- **Navigate To**: `Admin Dashboard -> Card Requests (or Support Center -> Card Requests queue)`
- **Action**: 
- **Observe**:
  - ticket list contains a ticket with the customer's tracking ID
  - ticket fields: requestor username/email, card type, linked account number (masked or last 4), full shipping address
  - ticket status (expected 'Open' or 'Submitted')
  - ticket creation timestamp

**Expected Change**: A new card-request ticket exists in the Card Requests queue with the same tracking ID shown to the customer, matching card type, linked account, and shipping address; the ticket status is 'Open' or 'Submitted' and the creation timestamp is recent (within a few minutes of submission).

---

### [TC-002] Send secure message with a valid attachment
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to the Support Center page
2. 2. In the Secure Message form, enter <optional subject> in the Subject field
3. 3. Select <Category> from the Category dropdown
4. 4. Enter <valid message body> in the Message Body rich text editor
5. 5. Click 'Upload' on the Attachment control and select <valid allowed file> from the OS file dialog
6. 6. Confirm the attachment appears in the form upload list
7. 7. Click the 'Send Message' button

**Original Expected Result:** A success notification displays: "Message sent successfully. Returns ticket ID." and the support message list shows a new message row with the entered Subject and a visible attachment name

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Manage Cards -> Card Controls card`
- **Observe**:
  - Select Existing Card dropdown contains <Selected Card> and shows current selection
  - Displayed Card Status for <Selected Card> (expected 'Active')
  - Displayed New/Current Spending Limit for <Selected Card> (record current value)

**Post-Check**
- **Navigate To**: `Manage Cards -> Card Controls card (refresh page or re-open Manage Cards to ensure persisted state)`
- **Observe**:
  - Select Existing Card dropdown contains and selects <Selected Card>
  - Displayed Card Status for <Selected Card>
  - Displayed Spending Limit for <Selected Card>
  - Success banner text if present (e.g., 'Card controls updated successfully.')

**Expected Change**: After the update, the selected card's Status is 'Frozen' (was 'Active' in pre-check) and the Spending Limit equals the <valid spending limit within policy> entered during the test; these values persist after a page refresh/navigation.

---

### [TC-003] Request callback with valid next-business-day date, time window and editable phone number
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to the Support Center page
2. 2. In the Schedule Callback form, select <Reason for Call> from the Reason for Call dropdown
3. 3. Select <valid date at least next business day> in the Preferred Date field
4. 4. Select <Preferred Time Window> in the Preferred Time Window control
5. 5. Verify Phone Number is pre-filled, edit it to <valid phone number> if needed
6. 6. Click the 'Request Callback' button

**Original Expected Result:** A confirmation banner displays: "Callback request submitted. Sends email confirmation." and the confirmation panel shows the selected Preferred Date, Preferred Time Window and the Phone Number used for the request

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Manage Cards -> Card Controls`
- **Observe**:
  - Selected card shown as <Selected Card> in Select Existing Card dropdown
  - Travel Notice summary for <Selected Card> (dates and destinations) — may be empty
  - Number of existing travel notices listed for <Selected Card>

**Post-Check**
- **Navigate To**: `Manage Cards -> Card Controls (reload or new session recommended) and select <Selected Card>`
- **Observe**:
  - Travel Notice summary for <Selected Card> (dates and destinations)
  - List of destinations for the active travel notice(s) for <Selected Card>
  - Number of travel notices listed for <Selected Card>

**Expected Change**: A travel notice for <Selected Card> exists showing the date range <valid start date> – <valid end date> and includes '<destination A>' in its destinations list; if no travel notice existed in pre_check, the number of travel notices for <Selected Card> has increased by 1, otherwise the newly created notice is present among the listed notices.

---

### [TC-004] Send Message: leave Message Body blank and submit
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Leave the Message Body field blank
2. 2. Enter <valid Subject> in the Subject field
3. 3. Select <Category option> in the Category dropdown
4. 4. (Optional) Upload <valid attachment of allowed type> in Attachment
5. 5. Click the Send Message button

**Original Expected Result:** Message Body field displays an inline validation error indicating it is required; form does not submit; no ticket is created and the page remains on the Secure Message form

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Manage Cards -> Card Controls (select <Selected Card>)`
- **Observe**:
  - Travel Notice summary start date for <Selected Card> (if present)
  - Travel Notice summary end date for <Selected Card> (if present)
  - Travel Notice summary destinations list for <Selected Card> (could be empty)

**Post-Check**
- **Navigate To**: `Manage Cards -> Card Controls (refresh page or navigate away and return, then select <Selected Card>)`
- **Observe**:
  - Travel Notice summary start date for <Selected Card>
  - Travel Notice summary end date for <Selected Card>
  - Travel Notice summary destinations list for <Selected Card>

**Expected Change**: Travel Notice summary for <Selected Card> shows the entered <valid start date> – <valid end date> and the destinations list includes both '<destination A>' and '<destination B>'. These values persist after a page refresh or navigating away and back, indicating the changes were saved to the backend.

---

### [TC-001] Send secure message (basic) with required message body
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to the Support Center page
2. 2. In the Secure Message form, enter <optional subject> in the Subject field
3. 3. Select <Category> from the Category dropdown
4. 4. Enter <valid message body> in the Message Body rich text editor
5. 5. (Optional) Leave Attachment empty
6. 6. Click the 'Send Message' button

**Original Expected Result:** A success notification displays: "Message sent successfully. Returns ticket ID." and the notification shows a visible ticket ID

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Investments -> Portfolio Snapshot (and open Trade History if available)`
- **Observe**:
  - holding row for <existing fund symbol> (record current share quantity, average cost per share, and market value) or note 'no holding' if absent
  - available buying power for <funding account with sufficient buying power> (record numeric value) — visible in Investments funding-account info or Accounts Overview
  - top entry of Trade History (record latest order ID and status if present) to use as baseline

**Post-Check**
- **Navigate To**: `Investments -> Portfolio Snapshot and Trade History`
- **Observe**:
  - holding row for <existing fund symbol> (updated share quantity, average cost per share, and market value)
  - available buying power for <funding account with sufficient buying power> (numeric value)
  - most recent Trade History entry (order ID displayed, Action = 'Buy', Symbol = <existing fund symbol>, Quantity = <valid quantity>, Status = 'Executed' or 'Completed')

**Expected Change**: The holding row for <existing fund symbol> shows the share quantity increased by <valid quantity> compared to the pre-check (or a new holding row appears with quantity = <valid quantity> if previously absent); the available buying power for <funding account with sufficient buying power> decreased by the approximate purchase cost (purchase price × <valid quantity> plus any fees) relative to the pre-check value; and a new Trade History entry exists with an order ID and status indicating the trade executed.

---

### [TC-002] Send secure message with a valid attachment
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to the Support Center page
2. 2. In the Secure Message form, enter <optional subject> in the Subject field
3. 3. Select <Category> from the Category dropdown
4. 4. Enter <valid message body> in the Message Body rich text editor
5. 5. Click 'Upload' on the Attachment control and select <valid allowed file> from the OS file dialog
6. 6. Confirm the attachment appears in the form upload list
7. 7. Click the 'Send Message' button

**Original Expected Result:** A success notification displays: "Message sent successfully. Returns ticket ID." and the support message list shows a new message row with the entered Subject and a visible attachment name

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Investments page -> Portfolio Snapshot (Holdings section)`
- **Observe**:
  - holdings row for <existing fund symbol>: share quantity
  - holdings row for <existing fund symbol>: market value
  - portfolio total market value

**Post-Check**
- **Navigate To**: `Investments page -> Portfolio Snapshot (Holdings section)`
- **Observe**:
  - success notification text and order ID (e.g., 'Trade executed successfully.' with order ID)
  - holdings row for <existing fund symbol>: updated share quantity
  - holdings row for <existing fund symbol>: updated market value
  - portfolio total market value

**Expected Change**: The holdings row for <existing fund symbol> shows the share quantity decreased by <valid quantity> (new_quantity = pre_check_quantity - <valid quantity>); the Investments page displays 'Trade executed successfully.' with an order ID; the holdings' market value and portfolio total market value reflect the reduction accordingly.

---

### [TC-003] Request callback with valid next-business-day date, time window and editable phone number
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to the Support Center page
2. 2. In the Schedule Callback form, select <Reason for Call> from the Reason for Call dropdown
3. 3. Select <valid date at least next business day> in the Preferred Date field
4. 4. Select <Preferred Time Window> in the Preferred Time Window control
5. 5. Verify Phone Number is pre-filled, edit it to <valid phone number> if needed
6. 6. Click the 'Request Callback' button

**Original Expected Result:** A confirmation banner displays: "Callback request submitted. Sends email confirmation." and the confirmation panel shows the selected Preferred Date, Preferred Time Window and the Phone Number used for the request

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Investments page -> Recurring Investment Plans section`
- **Observe**:
  - list of recurring plans (each row shows: fund symbol, frequency, contribution amount, start date, funding account, status)
  - count of recurring plans
  - whether a plan already exists for <existing fund symbol> with <Start_Date> and <valid contribution amount>

**Post-Check**
- **Navigate To**: `Investments page -> Recurring Investment Plans section`
- **Observe**:
  - list of recurring plans (each row shows: fund symbol, frequency, contribution amount, start date, funding account, status)
  - count of recurring plans
  - a plan row for <existing fund symbol> with the configured <Frequency>, <valid contribution amount>, <Start_Date>, and <funding account with adequate balance>

**Expected Change**: The Recurring Plans list contains a new row for <existing fund symbol> with Frequency = <Weekly or Monthly>, Contribution Amount = <valid contribution amount>, Start Date = <Start_Date>, Funding Account = <funding account with adequate balance>, and a status indicating the plan is scheduled/active; the total count of recurring plans has increased by one; the UI also displayed the confirmation message 'Plan created successfully.' after creation.

---

### [TC-003] Request callback with valid next-business-day date, time window and editable phone number
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to the Support Center page
2. 2. In the Schedule Callback form, select <Reason for Call> from the Reason for Call dropdown
3. 3. Select <valid date at least next business day> in the Preferred Date field
4. 4. Select <Preferred Time Window> in the Preferred Time Window control
5. 5. Verify Phone Number is pre-filled, edit it to <valid phone number> if needed
6. 6. Click the 'Request Callback' button

**Original Expected Result:** A confirmation banner displays: "Callback request submitted. Sends email confirmation." and the confirmation panel shows the selected Preferred Date, Preferred Time Window and the Phone Number used for the request

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Account Statements -> e-Statement Preference form`
- **Observe**:
  - Paperless opt-in checkbox state
  - Email Address field value

**Post-Check**
- **Navigate To**: `Accounts Overview -> Account Statements -> e-Statement Preference form (refresh or navigate away and back to ensure persistence)`
- **Observe**:
  - Paperless opt-in checkbox state
  - Email Address field value
  - transient success banner or flash message

**Expected Change**: After saving, the Paperless opt-in checkbox is checked and the Email Address field displays the saved address (<valid email>). The success banner 'e-Statement preference updated.' is shown immediately after saving, and the checked state and email persist after navigating away and returning to the e-Statement Preference form.

---

### [TC-004] Send Message: leave Message Body blank and submit
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Leave the Message Body field blank
2. 2. Enter <valid Subject> in the Subject field
3. 3. Select <Category option> in the Category dropdown
4. 4. (Optional) Upload <valid attachment of allowed type> in Attachment
5. 5. Click the Send Message button

**Original Expected Result:** Message Body field displays an inline validation error indicating it is required; form does not submit; no ticket is created and the page remains on the Secure Message form

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Account Statements -> e-Statement Preference section`
- **Observe**:
  - Paperless e-Statement opt-in checkbox state (checked or unchecked)
  - Email Address field value shown for e-statements
  - Presence/absence of a recent 'e-Statement preference updated.' success message

**Post-Check**
- **Navigate To**: `Account Statements -> e-Statement Preference section (reload page or open in a new session)`
- **Observe**:
  - Paperless e-Statement opt-in checkbox state (expected to be unchecked)
  - Email Address field value (expected unchanged unless edited)
  - Visible success banner or flash message: 'e-Statement preference updated.'

**Expected Change**: After saving, the Paperless e-Statement opt-in checkbox is unchecked and the change persists on page reload (preference stored in backend); a success message 'e-Statement preference updated.' is displayed and the Email Address remains unchanged.

---

### [TC-001] Send secure message (basic) with required message body
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to the Support Center page
2. 2. In the Secure Message form, enter <optional subject> in the Subject field
3. 3. Select <Category> from the Category dropdown
4. 4. Enter <valid message body> in the Message Body rich text editor
5. 5. (Optional) Leave Attachment empty
6. 6. Click the 'Send Message' button

**Original Expected Result:** A success notification displays: "Message sent successfully. Returns ticket ID." and the notification shows a visible ticket ID

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounts Overview -> Security Settings (open Change Password panel)`
- **Observe**:
  - Change Password form is visible with fields: Current Password, New Password, Confirm New Password and 'Change Password' button
  - Tester has an active session (user is currently signed in) and knows the current password

**Post-Check**
- **Navigate To**: `Log Out -> Login page`
- **Observe**:
  - Attempt to sign in with the OLD (pre-change) password
  - Attempt to sign in with the NEW (post-change) password

**Expected Change**: Signing in with the old password fails with the message 'Incorrect email or password. Please try again.'; signing in with the new password succeeds, the user is redirected to Accounts Overview and a flash message 'Signed in successfully.' is displayed.

---

### [TC-001] Send secure message (basic) with required message body
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to the Support Center page
2. 2. In the Secure Message form, enter <optional subject> in the Subject field
3. 3. Select <Category> from the Category dropdown
4. 4. Enter <valid message body> in the Message Body rich text editor
5. 5. (Optional) Leave Attachment empty
6. 6. Click the 'Send Message' button

**Original Expected Result:** A success notification displays: "Message sent successfully. Returns ticket ID." and the notification shows a visible ticket ID

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Support Center -> My Tickets / Message History`
- **Observe**:
  - list of recent support tickets (ticket ID, subject, category, date/time)
  - count of tickets visible in the list
  - most recent ticket's ticket ID (if any) and timestamp

**Post-Check**
- **Navigate To**: `Support Center -> My Tickets / Message History`
- **Observe**:
  - success notification containing the returned ticket ID
  - list of recent support tickets (ticket ID, subject, category, date/time)
  - top/newest ticket's ticket ID, subject, category, timestamp, and message preview
  - updated count of tickets visible in the list

**Expected Change**: A new ticket is created and appears in My Tickets/Message History. The success notification's ticket ID matches the ticket ID shown on the new ticket entry. The new ticket is listed at the top (or newest position) with the selected category, the entered subject (or a placeholder if left blank), a message preview matching the sent message body, a timestamp near the send time, and the total ticket count increased by 1.

---

### [TC-002] Send secure message with a valid attachment
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to the Support Center page
2. 2. In the Secure Message form, enter <optional subject> in the Subject field
3. 3. Select <Category> from the Category dropdown
4. 4. Enter <valid message body> in the Message Body rich text editor
5. 5. Click 'Upload' on the Attachment control and select <valid allowed file> from the OS file dialog
6. 6. Confirm the attachment appears in the form upload list
7. 7. Click the 'Send Message' button

**Original Expected Result:** A success notification displays: "Message sent successfully. Returns ticket ID." and the support message list shows a new message row with the entered Subject and a visible attachment name

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Support Center -> Secure Messages (Message List / Sent Messages)`
- **Observe**:
  - number of messages listed on the first page of the support message list
  - subjects of the most recent messages (first page)
  - attachment names (if any) shown for those recent messages
  - presence or absence of a ticket ID column/field in the message list

**Post-Check**
- **Navigate To**: `Support Center -> Secure Messages (Message List / Sent Messages)`
- **Observe**:
  - number of messages listed on the first page of the support message list
  - subject of the newest/most-recent message row
  - attachment name shown for the newest message row
  - ticket ID shown for the newest message row
  - sent timestamp or status (e.g., 'Sent') for the newest message row

**Expected Change**: The support message list contains one additional message compared to pre_check. The newest message row has the Subject exactly matching the submitted subject, displays the uploaded attachment filename in the attachment column, shows a ticket ID for that message, and has a recent sent timestamp/status indicating it was just submitted.

---

### [TC-003] Request callback with valid next-business-day date, time window and editable phone number
**Category**: `positive` | **Verification Type**: `other` | **Coverage**: `partial`

**Coverage Note**: *There is no documented in-app persistent view for submitted callback requests (no support-queue view specified). Full backend persistence cannot be verified in-app; verification relies on the external email confirmation sent to the user's email inbox. Email delivery may be delayed or routed externally, so mailbox access is required.*

**Original Steps:**
1. 1. Navigate to the Support Center page
2. 2. In the Schedule Callback form, select <Reason for Call> from the Reason for Call dropdown
3. 3. Select <valid date at least next business day> in the Preferred Date field
4. 4. Select <Preferred Time Window> in the Preferred Time Window control
5. 5. Verify Phone Number is pre-filled, edit it to <valid phone number> if needed
6. 6. Click the 'Request Callback' button

**Original Expected Result:** A confirmation banner displays: "Callback request submitted. Sends email confirmation." and the confirmation panel shows the selected Preferred Date, Preferred Time Window and the Phone Number used for the request

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Support Center -> Schedule Callback form`
- **Observe**:
  - Schedule Callback form is displayed
  - No confirmation banner is present
  - Confirmation panel (for a recent callback) is not visible on-screen

**Post-Check**

---
