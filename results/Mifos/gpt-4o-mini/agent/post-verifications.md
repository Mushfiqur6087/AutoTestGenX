# Post-Verification Specifications

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Clients page`
- **Observe**:
  - list of clients
  - status of clients

**Post-Check**
- **Navigate To**: `Clients page`
- **Observe**:
  - list of clients
  - status of clients

**Expected Change**: New client appears in the list with Pending status.

---

### [TC-004] Rapid logout attempts
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Click on 'Log Out'
3. 3. Immediately click on the User Profile Icon again
4. 4. Click on 'Log Out' again

**Original Expected Result:** Second logout attempt is blocked; user remains on the login page without a second session being created.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Detail page`
- **Observe**:
  - status badge

**Post-Check**
- **Navigate To**: `Client Detail page`
- **Observe**:
  - status badge

**Expected Change**: Status badge changes from 'Pending' to 'Active'.

---

### [TC-005] Navigate to authenticated page after logout
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Detail page`
- **Observe**:
  - client name
  - client status
  - <field> with old value

**Post-Check**
- **Navigate To**: `Client Detail page`
- **Observe**:
  - client name
  - client status
  - <field> with new value

**Expected Change**: The <field> value has been updated to <new value>.

---

### [TC-006] Attempt to start all jobs when none are scheduled
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Start All

**Original Expected Result:** No jobs started; error message displayed indicating there are no scheduled jobs to start

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Clients`
- **Observe**:
  - client name
  - status badge

**Post-Check**
- **Navigate To**: `Clients`
- **Observe**:
  - client name
  - status badge

**Expected Change**: Client status badge changes from 'Pending' to 'Rejected'.

---

### [TC-007] Attempt to stop all jobs when none are running
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Stop All

**Original Expected Result:** No jobs stopped; error message displayed indicating there are no jobs currently running

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Detail page`
- **Observe**:
  - client name
  - status badge

**Post-Check**
- **Navigate To**: `Client Detail page`
- **Observe**:
  - client name
  - status badge

**Expected Change**: Client status badge should change from 'Pending' to 'Withdrawn'.

---

### [TC-008] Add maximum allowed entries to Column Definitions
**Category**: `edge` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a valid Data Table Name in the Data_Table_Name field
2. 2. Select an Application Table Name from the dropdown
3. 3. Add exactly maximum allowed entries to the Column Definitions repeating group

**Original Expected Result:** Form submits successfully; custom data table is created with the maximum number of column definitions

---

#### Verification Plan

**Actor A (Role: `user`)**
- **Action**: Transfer the client to a new office.

**Actor B (Role: `staff`)**
- **Session**: `new_session`
- **Navigate To**: `Clients -> Search for the transferred client`
- **Action**: 
- **Observe**:
  - client's office location
  - client's status

**Expected Change**: Client's office location is updated to the new destination office; status remains 'Active'.

---

### [TC-009] Attempt to add one more entry to Column Definitions
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a valid Data Table Name in the Data_Table_Name field
2. 2. Select an Application Table Name from the dropdown
3. 3. Add maximum allowed entries to the Column Definitions repeating group
4. 4. Attempt to add one more entry to the Column Definitions

**Original Expected Result:** Attempt to add entry is blocked; visible error shown indicating maximum entries reached

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Clients`
- **Observe**:
  - client name
  - status badge

**Post-Check**
- **Navigate To**: `Clients`
- **Observe**:
  - client name
  - status badge

**Expected Change**: Client status badge changes from 'Active' to 'Closed'.

---

### [TC-010] Enter maximum length for Name in Column Definitions
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a valid Data Table Name in the Data_Table_Name field
2. 2. Select an Application Table Name from the dropdown
3. 3. Add an entry to the Column Definitions repeating group
4. 4. Enter exactly maximum length for the Name field

**Original Expected Result:** Form submits successfully; custom data table is created with the maximum length Name

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Detail page`
- **Observe**:
  - client name
  - status badge
  - charges section

**Post-Check**
- **Navigate To**: `Client Detail page`
- **Observe**:
  - client name
  - status badge
  - charges section

**Expected Change**: The charges section now includes the newly added charge with the correct details.

---

### [TC-011] Enter one character less than maximum length for Name in Column Definitions
**Category**: `edge` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a valid Data Table Name in the Data_Table_Name field
2. 2. Select an Application Table Name from the dropdown
3. 3. Add an entry to the Column Definitions repeating group
4. 4. Enter one character less than the maximum length for the Name field

**Original Expected Result:** Form submits successfully; custom data table is created with the Name field accepted

---

#### Verification Plan

**Actor A (Role: `loan officer`)**
- **Action**: Create a new loan for an active client.

**Actor B (Role: `client`)**
- **Session**: `new_session`
- **Navigate To**: `Client Detail page`
- **Action**: 
- **Observe**:
  - loan account number
  - loan product name
  - status badge
  - loan balance

**Expected Change**: A new loan account appears with the correct product name and status badge indicating 'Active'.

---

### [TC-012] Enter long text in Data Table Name
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a very long string (200+ characters) in the Data_Table_Name field

**Original Expected Result:** Form submission is either accepted or truncated with a visible indicator

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Detail page`
- **Observe**:
  - status badge
  - total approved savings accounts

**Post-Check**
- **Navigate To**: `Client Detail page`
- **Observe**:
  - status badge
  - total approved savings accounts

**Expected Change**: Total approved savings accounts increased by one.

---

### [TC-013] Enter special characters in Data Table Name
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter special characters in the Data_Table_Name field

**Original Expected Result:** Form submission is either accepted or a specific error shown

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Detail page`
- **Observe**:
  - client name
  - status badge
  - total approved shares
  - total pending shares

**Post-Check**
- **Navigate To**: `Client Detail page`
- **Observe**:
  - client name
  - status badge
  - total approved shares
  - total pending shares

**Expected Change**: Total approved shares increased by the number of shares in the new share account; total pending shares remains unchanged.

---

### [TC-014] Enter leading/trailing whitespace in Data Table Name
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a value with leading/trailing spaces in the Data_Table_Name field

**Original Expected Result:** Leading/trailing whitespace is trimmed; saved value shown on detail page has no extra spaces

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Clients`
- **Observe**:
  - client status
  - client name

**Post-Check**
- **Navigate To**: `Clients`
- **Observe**:
  - client status
  - client name

**Expected Change**: Client status changed from 'Closed' to 'Active'.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Groups page`
- **Observe**:
  - list of existing groups

**Post-Check**
- **Navigate To**: `Groups page`
- **Observe**:
  - list of existing groups
  - new group name

**Expected Change**: The new group appears in the list of existing groups.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Groups Overview`
- **Observe**:
  - list of groups
  - total number of groups

**Post-Check**
- **Navigate To**: `Groups Overview`
- **Observe**:
  - list of groups
  - total number of groups

**Expected Change**: Total number of groups increased by the number of groups in the uploaded file.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Actor A (Role: `user`)**
- **Action**: Click Activate button on the group.

**Actor B (Role: `admin`)**
- **Session**: `new_session`
- **Navigate To**: `Groups page`
- **Action**: 
- **Observe**:
  - Group Name
  - Status

**Expected Change**: Group status changes from 'Pending' to 'Active'.

---

### [TC-004] Rapid logout attempts
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Click on 'Log Out'
3. 3. Immediately click on the User Profile Icon again
4. 4. Click on 'Log Out' again

**Original Expected Result:** Second logout attempt is blocked; user remains on the login page without a second session being created.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Groups -> Group Detail Page`
- **Observe**:
  - group name
  - group status
  - group office

**Post-Check**
- **Navigate To**: `Groups -> Group Detail Page`
- **Observe**:
  - group name
  - group status
  - group office

**Expected Change**: The updated field in the group details reflects the new value.

---

### [TC-005] Navigate to authenticated page after logout
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Groups Overview`
- **Observe**:
  - group status
  - group name

**Post-Check**
- **Navigate To**: `Groups Overview`
- **Observe**:
  - group status
  - group name

**Expected Change**: Group status changed from 'Active' to 'Closed'.

---

### [TC-006] Attempt to start all jobs when none are scheduled
**Category**: `negative` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Start All

**Original Expected Result:** No jobs started; error message displayed indicating there are no scheduled jobs to start

---

#### Verification Plan

**Actor A (Role: `admin`)**
- **Action**: Execute the steps from the core test case.

**Actor B (Role: `group_member`)**
- **Session**: `new_session`
- **Navigate To**: `Groups -> Group Detail page`
- **Action**: 
- **Observe**:
  - staff assigned to the group
  - staff list updated

**Expected Change**: The selected staff appears in the group members list, confirming the assignment.

---

### [TC-007] Attempt to stop all jobs when none are running
**Category**: `negative` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Stop All

**Original Expected Result:** No jobs stopped; error message displayed indicating there are no jobs currently running

---

#### Verification Plan

**Actor A (Role: `<Role>`)**
- **Action**: Execute the steps from the core test case.

**Actor B (Role: `admin`)**
- **Session**: `new_session`
- **Navigate To**: `Groups -> Group Detail -> Members tab`
- **Action**: 
- **Observe**:
  - list of group members
  - status of transferred clients

**Expected Change**: Transferred clients no longer appear in the group members list.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Centers Overview`
- **Observe**:
  - list of centers
  - center name
  - status

**Post-Check**
- **Navigate To**: `Centers Overview`
- **Observe**:
  - list of centers
  - new center name
  - status

**Expected Change**: The new center appears in the Centers Overview with an Active status.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Centers Overview`
- **Observe**:
  - list of centers
  - center status
  - total number of centers

**Post-Check**
- **Navigate To**: `Centers Overview`
- **Observe**:
  - list of centers
  - center status
  - total number of centers

**Expected Change**: The total number of centers has increased by the number of centers imported from the uploaded file.

---

### [TC-004] Rapid logout attempts
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Click on 'Log Out'
3. 3. Immediately click on the User Profile Icon again
4. 4. Click on 'Log Out' again

**Original Expected Result:** Second logout attempt is blocked; user remains on the login page without a second session being created.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Center Detail page`
- **Observe**:
  - status badge
  - action buttons

**Post-Check**
- **Navigate To**: `Center Detail page`
- **Observe**:
  - status badge
  - action buttons

**Expected Change**: Status badge changes to 'Active' and the Activate button is no longer available.

---

### [TC-005] Navigate to authenticated page after logout
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Center Detail page`
- **Observe**:
  - center name
  - status
  - modified field value

**Post-Check**
- **Navigate To**: `Center Detail page`
- **Observe**:
  - center name
  - status
  - modified field value

**Expected Change**: The modified field value reflects the new value entered during the edit.

---

### [TC-006] Attempt to start all jobs when none are scheduled
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Start All

**Original Expected Result:** No jobs started; error message displayed indicating there are no scheduled jobs to start

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Center Detail page`
- **Observe**:
  - status badge
  - action buttons

**Post-Check**
- **Navigate To**: `Center Detail page`
- **Observe**:
  - status badge
  - action buttons

**Expected Change**: Status badge changes to 'Closed'; action buttons are updated to reflect the closed state.

---

### [TC-007] Attempt to stop all jobs when none are running
**Category**: `negative` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Stop All

**Original Expected Result:** No jobs stopped; error message displayed indicating there are no jobs currently running

---

#### Verification Plan

**Actor A (Role: `admin`)**
- **Action**: Assign staff to a center.

**Actor B (Role: `staff`)**
- **Session**: `new_session`
- **Navigate To**: `Center Detail page`
- **Action**: 
- **Observe**:
  - assigned staff member
  - center status

**Expected Change**: The assigned staff member appears in the staff list for the center, confirming the assignment.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Products page`
- **Observe**:
  - list of loan products
  - Edit option for selected loan product

**Post-Check**
- **Navigate To**: `Loan Product Detail page`
- **Observe**:
  - Product Name
  - Short Name
  - Expiry Date
  - Status
  - Edit option

**Expected Change**: The Loan Product Detail page displays the selected loan product's details for editing.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Products page`
- **Observe**:
  - list of existing loan products

**Post-Check**
- **Navigate To**: `Loan Products page`
- **Observe**:
  - list of existing loan products
  - new loan product creation wizard

**Expected Change**: User is now on Step 2 of the Loan Product creation wizard.

---

### [TC-004] Rapid logout attempts
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Click on 'Log Out'
3. 3. Immediately click on the User Profile Icon again
4. 4. Click on 'Log Out' again

**Original Expected Result:** Second logout attempt is blocked; user remains on the login page without a second session being created.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Create Loan Product - Step 3`
- **Observe**:
  - Principal Amount
  - Currency
  - Decimal Places
  - Multiples of Rounding

**Post-Check**
- **Navigate To**: `Create Loan Product - Step 3`
- **Observe**:
  - Principal Amount
  - Currency
  - Decimal Places
  - Multiples of Rounding

**Expected Change**: The values entered in Step 2 are retained and displayed correctly in Step 3.

---

### [TC-005] Navigate to authenticated page after logout
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Create Loan Product - Step 3`
- **Observe**:
  - Repayment Strategy dropdown
  - Grace Period field
  - Arrears Tolerance field

**Post-Check**
- **Navigate To**: `Create Loan Product - Step 4`
- **Observe**:
  - Repayment Strategy dropdown
  - Grace Period field
  - Arrears Tolerance field

**Expected Change**: User successfully navigates to Step 4 of the Create Loan Product stepper.

---

### [TC-006] Attempt to start all jobs when none are scheduled
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Start All

**Original Expected Result:** No jobs started; error message displayed indicating there are no scheduled jobs to start

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Products page`
- **Observe**:
  - list of existing loan products

**Post-Check**
- **Navigate To**: `Loan Products page`
- **Observe**:
  - list of existing loan products
  - new loan product entry

**Expected Change**: A new loan product should appear in the list of existing loan products after submission.

---

### [TC-008] Add maximum allowed entries to Column Definitions
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a valid Data Table Name in the Data_Table_Name field
2. 2. Select an Application Table Name from the dropdown
3. 3. Add exactly maximum allowed entries to the Column Definitions repeating group

**Original Expected Result:** Form submits successfully; custom data table is created with the maximum number of column definitions

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Products page`
- **Observe**:
  - list of loan products
  - total number of loan products

**Post-Check**
- **Navigate To**: `Loan Products page`
- **Observe**:
  - list of loan products
  - total number of loan products

**Expected Change**: Total number of loan products increased by one; new loan product appears in the list.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Products page`
- **Observe**:
  - list of existing savings products

**Post-Check**
- **Navigate To**: `Savings Products page`
- **Observe**:
  - list of existing savings products
  - newly created savings product name

**Expected Change**: The newly created savings product appears in the list of savings products.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Products page`
- **Observe**:
  - list of existing loan products

**Post-Check**
- **Navigate To**: `Loan Products page`
- **Observe**:
  - list of existing loan products
  - new fixed deposit product name

**Expected Change**: The new fixed deposit product appears in the list of loan products.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Products page`
- **Observe**:
  - list of existing savings products

**Post-Check**
- **Navigate To**: `Savings Products page`
- **Observe**:
  - list of existing savings products
  - new recurring deposit product name

**Expected Change**: The new recurring deposit product appears in the list of savings products.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Products page`
- **Observe**:
  - list of existing share products

**Post-Check**
- **Navigate To**: `Share Products page`
- **Observe**:
  - list of existing share products
  - new share product name

**Expected Change**: The new share product appears in the list of existing share products.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Products`
- **Observe**:
  - Product Name
  - Short Name
  - Description

**Post-Check**
- **Navigate To**: `Share Products`
- **Observe**:
  - Product Name
  - Short Name
  - Description

**Expected Change**: Product Name, Short Name, and Description fields reflect the updated values.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Products`
- **Observe**:
  - list of share products
  - Product Name of the share product to be deleted

**Post-Check**
- **Navigate To**: `Share Products`
- **Observe**:
  - list of share products

**Expected Change**: The deleted share product no longer appears in the list of share products.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Charges Overview`
- **Observe**:
  - list of charge definitions

**Post-Check**
- **Navigate To**: `Charges Overview`
- **Observe**:
  - list of charge definitions
  - <Charge Name>

**Expected Change**: The charge definition for <Charge Name> appears in the list of charge definitions.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Charges`
- **Observe**:
  - Charge Name
  - Charge Applies To
  - Is Active

**Post-Check**
- **Navigate To**: `Charges`
- **Observe**:
  - Charge Name
  - Charge Applies To
  - Is Active

**Expected Change**: Charge Name reflects the updated value; other attributes remain unchanged.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Charges`
- **Observe**:
  - list of charges in the Charges Table

**Post-Check**
- **Navigate To**: `Charges`
- **Observe**:
  - list of charges in the Charges Table

**Expected Change**: The deleted charge no longer appears in the Charges Table.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounting -> Floating Rates`
- **Observe**:
  - list of existing floating rates

**Post-Check**
- **Navigate To**: `Accounting -> Floating Rates`
- **Observe**:
  - list of existing floating rates
  - <Floating Rate Name>

**Expected Change**: The new floating rate '<Floating Rate Name>' appears in the list of existing floating rates.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Floating Rates`
- **Observe**:
  - Floating Rate Name
  - Is Base Lending Rate
  - Is Active

**Post-Check**
- **Navigate To**: `Floating Rates`
- **Observe**:
  - Floating Rate Name
  - Is Base Lending Rate
  - Is Active

**Expected Change**: The Floating Rate Name has been updated to the new value entered in the edit form.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Delinquency Ranges`
- **Observe**:
  - list of delinquency ranges

**Post-Check**
- **Navigate To**: `Delinquency Ranges`
- **Observe**:
  - list of delinquency ranges
  - <valid classification>

**Expected Change**: The new delinquency range with classification <valid classification> appears in the list of delinquency ranges.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Delinquency Buckets page`
- **Observe**:
  - list of delinquency buckets

**Post-Check**
- **Navigate To**: `Delinquency Buckets page`
- **Observe**:
  - list of delinquency buckets
  - <valid bucket name>

**Expected Change**: The new delinquency bucket with the name <valid bucket name> appears in the list of delinquency buckets.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Detail page`
- **Observe**:
  - loan application status
  - loan account number

**Post-Check**
- **Navigate To**: `Client Detail page`
- **Observe**:
  - loan application status
  - loan account number

**Expected Change**: Loan application status changes to 'Submitted and Pending Approval' and a new loan account number is generated.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Actor A (Role: `loan officer`)**
- **Action**: Approve Loan Application as per the core test case.

**Actor B (Role: `client`)**
- **Session**: `new_session`
- **Navigate To**: `Client Detail page -> Loan Accounts tab`
- **Action**: 
- **Observe**:
  - loan account status badge
  - loan balance
  - approved amount
  - expected disbursement date

**Expected Change**: Loan account status changes to 'Approved' with the correct approved amount and expected disbursement date.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Actor A (Role: `loan officer`)**
- **Action**: Reject the loan application as per the test case steps.

**Actor B (Role: `client`)**
- **Session**: `new_session`
- **Navigate To**: `Client Detail page -> Loan Accounts tab`
- **Action**: 
- **Observe**:
  - loan application status
  - reason for rejection

**Expected Change**: Loan application status is updated to 'Rejected' with a reason displayed.

---

### [TC-004] Rapid logout attempts
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Click on 'Log Out'
3. 3. Immediately click on the User Profile Icon again
4. 4. Click on 'Log Out' again

**Original Expected Result:** Second logout attempt is blocked; user remains on the login page without a second session being created.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - status badge
  - loan account number

**Post-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - status badge

**Expected Change**: Status badge should change to 'Withdrawn'.

---

### [TC-005] Navigate to authenticated page after logout
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - loan application status
  - loan application details

**Post-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - message indicating loan application deleted
  - loan application not found

**Expected Change**: Loan application no longer appears on the Loan Detail page and is confirmed deleted.

---

### [TC-006] Attempt to start all jobs when none are scheduled
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Start All

**Original Expected Result:** No jobs started; error message displayed indicating there are no scheduled jobs to start

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - loan status
  - loan balance
  - disbursement details

**Post-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - loan status
  - loan balance
  - disbursement details

**Expected Change**: Loan status changed to 'Active'; loan balance reflects the disbursed amount.

---

### [TC-007] Attempt to stop all jobs when none are running
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Stop All

**Original Expected Result:** No jobs stopped; error message displayed indicating there are no jobs currently running

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - loan balance
  - total paid
  - total outstanding

**Post-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - loan balance
  - total paid
  - total outstanding

**Expected Change**: Total paid amount increased by the repayment amount; total outstanding amount decreased by the same amount.

---

### [TC-008] Add maximum allowed entries to Column Definitions
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a valid Data Table Name in the Data_Table_Name field
2. 2. Select an Application Table Name from the dropdown
3. 3. Add exactly maximum allowed entries to the Column Definitions repeating group

**Original Expected Result:** Form submits successfully; custom data table is created with the maximum number of column definitions

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - loan balance
  - interest amount due

**Post-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - loan balance
  - interest amount due

**Expected Change**: Interest amount due is decreased by the waived interest amount.

---

### [TC-009] Attempt to add one more entry to Column Definitions
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a valid Data Table Name in the Data_Table_Name field
2. 2. Select an Application Table Name from the dropdown
3. 3. Add maximum allowed entries to the Column Definitions repeating group
4. 4. Attempt to add one more entry to the Column Definitions

**Original Expected Result:** Attempt to add entry is blocked; visible error shown indicating maximum entries reached

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - loan status badge
  - loan balance

**Post-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - loan status badge
  - loan balance

**Expected Change**: Loan status badge should indicate 'Written Off' and loan balance should be zero.

---

### [TC-010] Enter maximum length for Name in Column Definitions
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a valid Data Table Name in the Data_Table_Name field
2. 2. Select an Application Table Name from the dropdown
3. 3. Add an entry to the Column Definitions repeating group
4. 4. Enter exactly maximum length for the Name field

**Original Expected Result:** Form submits successfully; custom data table is created with the maximum length Name

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - loan status badge
  - loan balance

**Post-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - loan status badge
  - loan balance

**Expected Change**: Loan status badge should change to 'Closed' and loan balance should be zero.

---

### [TC-011] Enter one character less than maximum length for Name in Column Definitions
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a valid Data Table Name in the Data_Table_Name field
2. 2. Select an Application Table Name from the dropdown
3. 3. Add an entry to the Column Definitions repeating group
4. 4. Enter one character less than the maximum length for the Name field

**Original Expected Result:** Form submits successfully; custom data table is created with the Name field accepted

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - status badge
  - due date
  - repayment schedule

**Post-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - status badge
  - adjusted due date
  - repayment schedule

**Expected Change**: The due date has been updated to the new adjusted due date, and the status remains Active.

---

### [TC-012] Enter long text in Data Table Name
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a very long string (200+ characters) in the Data_Table_Name field

**Original Expected Result:** Form submission is either accepted or truncated with a visible indicator

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - loan balance
  - status badge

**Post-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - loan balance
  - status badge

**Expected Change**: Loan balance decreased by the prepaid amount; status badge remains 'Active'.

---

### [TC-013] Enter special characters in Data Table Name
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter special characters in the Data_Table_Name field

**Original Expected Result:** Form submission is either accepted or a specific error shown

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - loan account number
  - status badge

**Post-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - loan account number
  - status badge

**Expected Change**: Status badge changes to 'Written Off' indicating the loan has been foreclosed.

---

### [TC-014] Enter leading/trailing whitespace in Data Table Name
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a value with leading/trailing spaces in the Data_Table_Name field

**Original Expected Result:** Leading/trailing whitespace is trimmed; saved value shown on detail page has no extra spaces

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - loan account number
  - status badge

**Post-Check**
- **Navigate To**: `Loan Detail page`
- **Observe**:
  - loan account number
  - status badge

**Expected Change**: Loan status badge changed to 'Charged Off'.

---

### [TC-015] Create Holiday with From_Date one day before To_Date
**Category**: `edge` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click + Create Holiday
2. 2. Enter a valid Name in the Name field
3. 3. Enter today's date in the From_Date field
4. 4. Enter tomorrow's date in the To_Date field
5. 5. Click Submit

**Original Expected Result:** Holiday is created successfully; From_Date is today and To_Date is tomorrow

---

#### Verification Plan

**Actor A (Role: `loan officer`)**
- **Action**: Execute the steps from the core test case.

**Actor B (Role: `another loan officer or admin`)**
- **Session**: `new_session`
- **Navigate To**: `Loan Detail page of the assigned loan`
- **Action**: 
- **Observe**:
  - Loan Officer name
  - Loan Officer status

**Expected Change**: The Loan Officer name reflects the newly assigned officer.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Detail page`
- **Observe**:
  - status of savings accounts
  - list of existing accounts

**Post-Check**
- **Navigate To**: `Client Detail page`
- **Observe**:
  - status of savings accounts
  - new savings account in 'Submitted and Pending Approval' status

**Expected Change**: A new savings account appears in the list with 'Submitted and Pending Approval' status.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Detail -> Savings Account`
- **Observe**:
  - account balance

**Post-Check**
- **Navigate To**: `Client Detail -> Savings Account`
- **Observe**:
  - account balance

**Expected Change**: Account balance increased by the deposit amount.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Account Detail`
- **Observe**:
  - account balance
  - transaction history

**Post-Check**
- **Navigate To**: `Savings Account Detail`
- **Observe**:
  - account balance
  - transaction history

**Expected Change**: Account balance decreased by the withdrawal amount; transaction history includes the new withdrawal entry.

---

### [TC-004] Rapid logout attempts
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Click on 'Log Out'
3. 3. Immediately click on the User Profile Icon again
4. 4. Click on 'Log Out' again

**Original Expected Result:** Second logout attempt is blocked; user remains on the login page without a second session being created.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Account Detail`
- **Observe**:
  - account balance
  - interest postings

**Post-Check**
- **Navigate To**: `Savings Account Detail`
- **Observe**:
  - account balance
  - interest postings

**Expected Change**: Account balance increased by the posted interest amount, and a new entry appears in the interest postings section.

---

### [TC-006] Attempt to start all jobs when none are scheduled
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Start All

**Original Expected Result:** No jobs started; error message displayed indicating there are no scheduled jobs to start

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Detail -> Savings Accounts`
- **Observe**:
  - account number
  - status badge

**Post-Check**
- **Navigate To**: `Client Detail -> Savings Accounts`
- **Observe**:
  - account number
  - status badge

**Expected Change**: Savings account status badge should change from 'Active' to 'Closed'.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Detail page`
- **Observe**:
  - status badge of Share Account
  - total approved shares
  - total pending shares

**Post-Check**
- **Navigate To**: `Client Detail page`
- **Observe**:
  - status badge of Share Account
  - total approved shares
  - total pending shares

**Expected Change**: A new Share Account appears with status 'Submitted and Pending Approval' and the total pending shares reflects the number of shares requested.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Actor A (Role: `approver`)**
- **Action**: Approve Share Account with valid data.

**Actor B (Role: `client`)**
- **Session**: `new_session`
- **Navigate To**: `Client Detail -> Share Account`
- **Action**: 
- **Observe**:
  - status badge
  - total approved shares
  - total pending shares

**Expected Change**: Share account status changes to 'Approved' with the correct number of approved shares reflected.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Account Detail`
- **Observe**:
  - status badge

**Post-Check**
- **Navigate To**: `Share Account Detail`
- **Observe**:
  - status badge

**Expected Change**: Status badge should change to 'Rejected' after the account is rejected.

---

### [TC-004] Rapid logout attempts
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Click on 'Log Out'
3. 3. Immediately click on the User Profile Icon again
4. 4. Click on 'Log Out' again

**Original Expected Result:** Second logout attempt is blocked; user remains on the login page without a second session being created.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Account Detail page`
- **Observe**:
  - status badge
  - total approved shares
  - total pending shares

**Post-Check**
- **Navigate To**: `Share Account Detail page`
- **Observe**:
  - status badge
  - total approved shares
  - total pending shares

**Expected Change**: Status badge changes to 'Active'; total approved shares remains the same; total pending shares becomes zero.

---

### [TC-005] Navigate to authenticated page after logout
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Account Detail`
- **Observe**:
  - status badge
  - total approved shares

**Post-Check**
- **Navigate To**: `Share Account Detail`
- **Observe**:
  - status badge
  - total approved shares

**Expected Change**: Status badge changes to 'Pending' and total approved shares is reset to zero.

---

### [TC-006] Attempt to start all jobs when none are scheduled
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Start All

**Original Expected Result:** No jobs started; error message displayed indicating there are no scheduled jobs to start

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Account Detail page`
- **Observe**:
  - total approved shares
  - total pending shares
  - unit price

**Post-Check**
- **Navigate To**: `Share Account Detail page`
- **Observe**:
  - total approved shares
  - total pending shares
  - unit price

**Expected Change**: Total approved shares increased by the number of additional shares applied; total pending shares remains unchanged.

---

### [TC-007] Attempt to stop all jobs when none are running
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Stop All

**Original Expected Result:** No jobs stopped; error message displayed indicating there are no jobs currently running

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Account Detail`
- **Observe**:
  - total approved shares
  - total pending shares
  - account balance

**Post-Check**
- **Navigate To**: `Savings Account Detail`
- **Observe**:
  - account balance
  - transaction history

**Expected Change**: Savings account balance increased by the redemption amount calculated from the shares redeemed.

---

### [TC-008] Add maximum allowed entries to Column Definitions
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a valid Data Table Name in the Data_Table_Name field
2. 2. Select an Application Table Name from the dropdown
3. 3. Add exactly maximum allowed entries to the Column Definitions repeating group

**Original Expected Result:** Form submits successfully; custom data table is created with the maximum number of column definitions

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Detail -> Share Account`
- **Observe**:
  - status badge
  - total approved shares
  - total pending shares

**Post-Check**
- **Navigate To**: `Client Detail -> Share Account`
- **Observe**:
  - status badge
  - total approved shares
  - total pending shares

**Expected Change**: Status badge changes to 'Closed'; total approved shares and total pending shares remain unchanged.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Detail page`
- **Observe**:
  - list of accounts
  - status of Fixed Deposit accounts

**Post-Check**
- **Navigate To**: `Client Detail page`
- **Observe**:
  - list of accounts
  - status of Fixed Deposit accounts

**Expected Change**: A new Fixed Deposit account appears in the accounts list with status 'Submitted and Pending Approval'.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Detail page`
- **Observe**:
  - list of accounts
  - status of accounts

**Post-Check**
- **Navigate To**: `Client Detail page`
- **Observe**:
  - list of accounts
  - status of accounts

**Expected Change**: A new Recurring Deposit account appears in the list of accounts with status 'Submitted and Pending Approval'.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `RD Account Detail page`
- **Observe**:
  - status badge
  - account balance

**Post-Check**
- **Navigate To**: `RD Account Detail page`
- **Observe**:
  - status badge
  - account balance

**Expected Change**: Status badge changes from 'Draft' to 'Active'; account balance remains unchanged.

---

### [TC-004] Rapid logout attempts
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Click on 'Log Out'
3. 3. Immediately click on the User Profile Icon again
4. 4. Click on 'Log Out' again

**Original Expected Result:** Second logout attempt is blocked; user remains on the login page without a second session being created.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `RD Account Detail page`
- **Observe**:
  - status badge
  - account balance

**Post-Check**
- **Navigate To**: `RD Account Detail page`
- **Observe**:
  - status badge
  - account balance

**Expected Change**: Status badge changes to 'Closed' and account balance is updated to reflect the closure.

---

### [TC-005] Navigate to authenticated page after logout
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `FD Account Detail page`
- **Observe**:
  - status badge
  - account balance

**Post-Check**
- **Navigate To**: `FD Account Detail page`
- **Observe**:
  - status badge
  - account balance

**Expected Change**: Status badge changes to 'Approved' and account balance remains unchanged.

---

### [TC-006] Attempt to start all jobs when none are scheduled
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Start All

**Original Expected Result:** No jobs started; error message displayed indicating there are no scheduled jobs to start

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `FD Account Detail page`
- **Observe**:
  - status badge
  - account balance

**Post-Check**
- **Navigate To**: `FD Account Detail page`
- **Observe**:
  - status badge
  - account balance

**Expected Change**: Status badge changes to 'Active' and account balance remains unchanged.

---

### [TC-007] Attempt to stop all jobs when none are running
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Stop All

**Original Expected Result:** No jobs stopped; error message displayed indicating there are no jobs currently running

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `FD Account Detail page`
- **Observe**:
  - account number
  - status badge
  - total approved shares
  - total pending shares

**Post-Check**
- **Navigate To**: `FD Account Detail page`
- **Observe**:
  - account number
  - status badge
  - total approved shares
  - total pending shares

**Expected Change**: Status badge changes to 'Closed' and no pending transactions are displayed.

---

### [TC-008] Add maximum allowed entries to Column Definitions
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a valid Data Table Name in the Data_Table_Name field
2. 2. Select an Application Table Name from the dropdown
3. 3. Add exactly maximum allowed entries to the Column Definitions repeating group

**Original Expected Result:** Form submits successfully; custom data table is created with the maximum number of column definitions

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `FD Account Detail page`
- **Observe**:
  - status badge
  - account balance

**Post-Check**
- **Navigate To**: `FD Account Detail page`
- **Observe**:
  - status badge
  - account balance

**Expected Change**: Status badge changes to 'Closed' and account balance is updated to reflect closure.

---

### [TC-009] Attempt to add one more entry to Column Definitions
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a valid Data Table Name in the Data_Table_Name field
2. 2. Select an Application Table Name from the dropdown
3. 3. Add maximum allowed entries to the Column Definitions repeating group
4. 4. Attempt to add one more entry to the Column Definitions

**Original Expected Result:** Attempt to add entry is blocked; visible error shown indicating maximum entries reached

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `RD Account Detail page`
- **Observe**:
  - status badge
  - account balance

**Post-Check**
- **Navigate To**: `RD Account Detail page`
- **Observe**:
  - status badge
  - account balance

**Expected Change**: Status badge changes to 'Approved' and account balance remains unchanged.

---

### [TC-010] Enter maximum length for Name in Column Definitions
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a valid Data Table Name in the Data_Table_Name field
2. 2. Select an Application Table Name from the dropdown
3. 3. Add an entry to the Column Definitions repeating group
4. 4. Enter exactly maximum length for the Name field

**Original Expected Result:** Form submits successfully; custom data table is created with the maximum length Name

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `RD Account Detail page`
- **Observe**:
  - status badge
  - account balance

**Post-Check**
- **Navigate To**: `RD Account Detail page`
- **Observe**:
  - status badge
  - account balance

**Expected Change**: Status badge changes to 'Active' indicating the RD Account is now activated.

---

### [TC-011] Enter one character less than maximum length for Name in Column Definitions
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a valid Data Table Name in the Data_Table_Name field
2. 2. Select an Application Table Name from the dropdown
3. 3. Add an entry to the Column Definitions repeating group
4. 4. Enter one character less than the maximum length for the Name field

**Original Expected Result:** Form submits successfully; custom data table is created with the Name field accepted

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `RD Account Detail page`
- **Observe**:
  - account balance
  - total deposits made

**Post-Check**
- **Navigate To**: `RD Account Detail page`
- **Observe**:
  - account balance
  - total deposits made

**Expected Change**: Account balance increased by the deposit amount; total deposits made increased by one.

---

### [TC-012] Enter long text in Data Table Name
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a very long string (200+ characters) in the Data_Table_Name field

**Original Expected Result:** Form submission is either accepted or truncated with a visible indicator

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `RD Account Detail page`
- **Observe**:
  - account number
  - status badge

**Post-Check**
- **Navigate To**: `RD Account Detail page`
- **Observe**:
  - account number
  - status badge

**Expected Change**: Status badge should change to 'Closed' indicating the RD Account has been closed prematurely.

---

### [TC-013] Enter special characters in Data Table Name
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter special characters in the Data_Table_Name field

**Original Expected Result:** Form submission is either accepted or a specific error shown

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `RD Account Detail page`
- **Observe**:
  - status badge
  - account balance

**Post-Check**
- **Navigate To**: `RD Account Detail page`
- **Observe**:
  - status badge
  - account balance

**Expected Change**: Status badge changes to 'Closed' and account balance is updated to reflect closure.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Chart of Accounts`
- **Observe**:
  - list of GL accounts

**Post-Check**
- **Navigate To**: `Chart of Accounts`
- **Observe**:
  - list of GL accounts
  - <account name>

**Expected Change**: The new GL Account with the name '<account name>' appears in the list of GL accounts.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Chart of Accounts`
- **Observe**:
  - <field> with old value

**Post-Check**
- **Navigate To**: `Chart of Accounts`
- **Observe**:
  - <field> with new value

**Expected Change**: The GL Account field has been updated from <old value> to <new value>.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Chart of Accounts`
- **Observe**:
  - <account name>

**Post-Check**
- **Navigate To**: `Chart of Accounts`
- **Observe**:
  - <account name>

**Expected Change**: <account name> should no longer be displayed in the Chart of Accounts.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Journal Entries`
- **Observe**:
  - Entry ID
  - Office
  - Transaction Date
  - Type
  - GL Account
  - Amount

**Post-Check**
- **Navigate To**: `Journal Entries`
- **Observe**:
  - Entry ID
  - Office
  - Transaction Date
  - Type
  - GL Account
  - Amount

**Expected Change**: A new journal entry appears in the Journal Entries table with the correct details matching the submitted entry.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Journal Entries`
- **Observe**:
  - Entry ID
  - Transaction Date
  - Amount

**Post-Check**
- **Navigate To**: `Journal Entries`
- **Observe**:
  - Entry ID
  - Transaction Date
  - Amount

**Expected Change**: No new journal entries can be posted for dates on or before the created closing date.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounting Rules`
- **Observe**:
  - list of accounting rules

**Post-Check**
- **Navigate To**: `Accounting Rules`
- **Observe**:
  - list of accounting rules
  - <valid rule name>

**Expected Change**: The new accounting rule appears in the Accounting Rules Table.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Financial Activity Mappings`
- **Observe**:
  - list of existing financial activity mappings

**Post-Check**
- **Navigate To**: `Financial Activity Mappings`
- **Observe**:
  - list of existing financial activity mappings
  - newly created financial activity mapping

**Expected Change**: The new financial activity mapping appears in the Financial Activity Mappings Table.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounting Rules`
- **Observe**:
  - Rule Name of the existing accounting rule

**Post-Check**
- **Navigate To**: `Accounting Rules`
- **Observe**:
  - Rule Name of the updated accounting rule

**Expected Change**: The accounting rule details are updated; the Accounting Rules Table displays the new rule name.

---

### [TC-004] Rapid logout attempts
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Click on 'Log Out'
3. 3. Immediately click on the User Profile Icon again
4. 4. Click on 'Log Out' again

**Original Expected Result:** Second logout attempt is blocked; user remains on the login page without a second session being created.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounting Rules`
- **Observe**:
  - list of accounting rules
  - Rule Name of the existing accounting rule

**Post-Check**
- **Navigate To**: `Accounting Rules`
- **Observe**:
  - list of accounting rules

**Expected Change**: The accounting rule is no longer present in the Accounting Rules Table.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Provisioning Criteria`
- **Observe**:
  - list of criteria names
  - creation date
  - provisioning percentage

**Post-Check**
- **Navigate To**: `Provisioning Criteria`
- **Observe**:
  - list of criteria names
  - creation date
  - provisioning percentage

**Expected Change**: New criteria name appears in the list with the correct provisioning percentage and creation date.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Provisioning Entries`
- **Observe**:
  - list of existing provisioning entries

**Post-Check**
- **Navigate To**: `Provisioning Entries`
- **Observe**:
  - list of existing provisioning entries
  - new provisioning entry

**Expected Change**: A new provisioning entry appears in the list based on the current loan portfolio status.

---

### [TC-005] Navigate to authenticated page after logout
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Provisioning Entries`
- **Observe**:
  - Entry Date
  - Journal Entry Created
  - Created By

**Post-Check**
- **Navigate To**: `Provisioning Entries`
- **Observe**:
  - Entry Date
  - Journal Entry Created
  - Created By

**Expected Change**: A new provisioning entry is created with the current date and reflects the updated provisioning amount based on the current loan portfolio status.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Offices`
- **Observe**:
  - list of offices

**Post-Check**
- **Navigate To**: `Offices`
- **Observe**:
  - list of offices
  - new office name

**Expected Change**: The new office appears in the Offices table.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Employees`
- **Observe**:
  - Employee Name
  - Employee Status

**Post-Check**
- **Navigate To**: `Employees`
- **Observe**:
  - Employee Name
  - Employee Status

**Expected Change**: Employee details are updated as per the changes made in the edit form.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Employees page`
- **Observe**:
  - list of employees
  - employee count

**Post-Check**
- **Navigate To**: `Employees page`
- **Observe**:
  - list of employees
  - employee count

**Expected Change**: Employee count increased by one; new employee appears in the list with correct details.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Tellers page`
- **Observe**:
  - list of tellers
  - total number of tellers

**Post-Check**
- **Navigate To**: `Tellers page`
- **Observe**:
  - list of tellers
  - total number of tellers

**Expected Change**: Total number of tellers increased by one; new teller appears in the list with correct details.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Tellers`
- **Observe**:
  - Teller Name
  - Cashiers section

**Post-Check**
- **Navigate To**: `Tellers`
- **Observe**:
  - Teller Name
  - Cashiers section

**Expected Change**: The Cashiers section now includes the newly allocated cashier with the correct start date.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Tellers`
- **Observe**:
  - Teller Name
  - Office

**Post-Check**
- **Navigate To**: `Tellers`
- **Observe**:
  - Teller Name
  - Office

**Expected Change**: The Office field for the teller is updated to the new valid office.

---

### [TC-004] Rapid logout attempts
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Click on 'Log Out'
3. 3. Immediately click on the User Profile Icon again
4. 4. Click on 'Log Out' again

**Original Expected Result:** Second logout attempt is blocked; user remains on the login page without a second session being created.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Cashier Detail page`
- **Observe**:
  - Opening Balance
  - Cash In Hand

**Post-Check**
- **Navigate To**: `Cashier Detail page`
- **Observe**:
  - Opening Balance
  - Cash In Hand

**Expected Change**: Cash In Hand increased by the allocated amount.

---

### [TC-005] Navigate to authenticated page after logout
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Cashier Detail page`
- **Observe**:
  - Opening Balance
  - Cash In Hand

**Post-Check**
- **Navigate To**: `Cashier Detail page`
- **Observe**:
  - Opening Balance
  - Cash In Hand

**Expected Change**: Cash In Hand increased by the settled amount; Opening Balance remains unchanged.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Users`
- **Observe**:
  - list of users
  - username of <unique username>

**Post-Check**
- **Navigate To**: `Users`
- **Observe**:
  - list of users
  - username of <unique username>

**Expected Change**: The new user with username <unique username> appears in the user list.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Users -> Roles`
- **Observe**:
  - list of roles

**Post-Check**
- **Navigate To**: `Users -> Roles`
- **Observe**:
  - list of roles
  - <role name>

**Expected Change**: The new role '<role name>' appears in the list of roles.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Account Overview`
- **Observe**:
  - balance of From Account
  - balance of To Account

**Post-Check**
- **Navigate To**: `Account Overview`
- **Observe**:
  - balance of From Account
  - balance of To Account

**Expected Change**: From Account balance decreased by Transfer Amount; To Account balance increased by the same amount.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Charges -> Tax Components`
- **Observe**:
  - list of existing tax components

**Post-Check**
- **Navigate To**: `Charges -> Tax Components`
- **Observe**:
  - list of existing tax components
  - new tax component with <valid name>

**Expected Change**: The new tax component appears in the list with the correct details including name, percentage, debit account, credit account, and start date.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Tax Management -> Tax Groups`
- **Observe**:
  - list of existing tax groups

**Post-Check**
- **Navigate To**: `Tax Management -> Tax Groups`
- **Observe**:
  - list of existing tax groups
  - new tax group with entered values

**Expected Change**: The new tax group appears in the list with the correct name and associated components.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Holidays Management`
- **Observe**:
  - list of holidays
  - holiday name
  - start date
  - end date

**Post-Check**
- **Navigate To**: `Holidays Management`
- **Observe**:
  - list of holidays
  - holiday name
  - start date
  - end date

**Expected Change**: The new holiday appears in the list with the correct name, start date, and end date.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Organization Settings -> Working Days`
- **Observe**:
  - Monday checkbox status
  - Tuesday checkbox status

**Post-Check**
- **Navigate To**: `Organization Settings -> Working Days`
- **Observe**:
  - Monday checkbox status
  - Tuesday checkbox status

**Expected Change**: Monday and Tuesday checkboxes are checked, indicating they are now configured as working days.

---

### [TC-005] Navigate to authenticated page after logout
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounting -> Chart of Accounts`
- **Observe**:
  - list of funds
  - Fund Name
  - External ID

**Post-Check**
- **Navigate To**: `Accounting -> Chart of Accounts`
- **Observe**:
  - list of funds
  - Fund Name
  - External ID

**Expected Change**: The new fund appears in the list with the correct Fund Name and External ID.

---

### [TC-006] Attempt to start all jobs when none are scheduled
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Start All

**Original Expected Result:** No jobs started; error message displayed indicating there are no scheduled jobs to start

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Payment Types`
- **Observe**:
  - list of payment types

**Post-Check**
- **Navigate To**: `Payment Types`
- **Observe**:
  - list of payment types
  - <valid payment type name>

**Expected Change**: The new payment type '<valid payment type name>' appears in the list of payment types.

---

### [TC-008] Add maximum allowed entries to Column Definitions
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter a valid Data Table Name in the Data_Table_Name field
2. 2. Select an Application Table Name from the dropdown
3. 3. Add exactly maximum allowed entries to the Column Definitions repeating group

**Original Expected Result:** Form submits successfully; custom data table is created with the maximum number of column definitions

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Bulk Import page`
- **Observe**:
  - import history table
  - total records count
  - success count
  - failure count

**Post-Check**
- **Navigate To**: `Bulk Import page`
- **Observe**:
  - import history table
  - total records count
  - success count
  - failure count

**Expected Change**: Total records count increased by the number of records in the uploaded file; success count reflects the number of successfully imported records.

---

### [TC-001] User logs out successfully from the user profile icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the User Profile Icon in the top-right corner
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User is redirected to the login page and the authenticated session is terminated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Manage Scheduler Jobs`
- **Observe**:
  - Is Active (toggle) for each job
  - Next Run Time for each job

**Post-Check**
- **Navigate To**: `Manage Scheduler Jobs`
- **Observe**:
  - Is Active (toggle) for each job

**Expected Change**: All scheduled jobs are now active and have their next run times updated accordingly.

---

### [TC-002] Attempt to log out without being authenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the User Profile Icon
2. 2. Select 'Log Out' from the dropdown

**Original Expected Result:** User remains on the current page; no session is terminated; user is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Manage Scheduler Jobs`
- **Observe**:
  - Job Name
  - Is Active
  - Next Run Time

**Post-Check**
- **Navigate To**: `Manage Scheduler Jobs`
- **Observe**:
  - Job Name
  - Is Active
  - Next Run Time

**Expected Change**: All scheduled jobs show 'Is Active' as inactive and 'Next Run Time' is no longer scheduled.

---

### [TC-003] Attempt to access an authenticated page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to an authenticated page

**Original Expected Result:** User is redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Manage Data Tables`
- **Observe**:
  - list of existing data tables

**Post-Check**
- **Navigate To**: `Manage Data Tables`
- **Observe**:
  - list of existing data tables
  - <Data Table Name>

**Expected Change**: The new custom data table named '<Data Table Name>' appears in the list of existing data tables.

---
