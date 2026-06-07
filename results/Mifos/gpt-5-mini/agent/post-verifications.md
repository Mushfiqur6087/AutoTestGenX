# Post-Verification Specifications

### [TC-002] Log Out via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Log Out' in the dropdown

**Original Expected Result:** terminates authenticated session; clears authentication token; redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Clients page`
- **Observe**:
  - Search field is visible
  - No existing client returned when searching for Document Key '<Document Key>'
  - No existing client (or note current count) when searching for name '<First Name> <Last Name>'

**Post-Check**
- **Navigate To**: `Clients page`
- **Observe**:
  - Use search to find '<Document Key>' or '<First Name> <Last Name>' and verify a result row is returned
  - In the result row observe columns: 'Name' (should show '<First Name> <Last Name>'), 'Account No.' (clickable link to detail), 'External ID' (if used), 'Status' (shown as a colored chip), 'Office'
  - Click the client's Name to open Client Detail page and verify header shows client name and status badge
  - On Client Detail page navigate to Identifiers tab and verify an identifier row with Document Type '<Document Type>' and Document Key '<Document Key>' exists

**Expected Change**: A new client with name '<First Name> <Last Name>' and identifier '<Document Key>' appears in the Clients listing for office '<Office>' with status 'Pending'; the Client Detail page shows a 'Pending' status badge and the Identifiers tab contains the Document Type '<Document Type>' and Document Key '<Document Key>'.

---

### [TC-005] Direct navigation to Profile Settings while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Profile Settings page URL

**Original Expected Result:** Auth Guard blocks access: browser is redirected to the Login page; Profile Settings content is not displayed and no profile settings UI elements are visible.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Clients -> Import Client (Bulk Import) -> Import History section`
- **Observe**:
  - import history entries (Name column)
  - Import Time
  - End Time
  - Completed indicator
  - Total Records, Success Count, Failure Count columns

**Post-Check**
- **Navigate To**: `Clients -> Import Client (Bulk Import) -> Import History section`
- **Observe**:
  - new import history entry with Name matching the uploaded file
  - Import Time populated (recent timestamp)
  - End Time blank or null while job running
  - Completed indicator = false OR status shows 'Processing'/'Queued'/'Running'
  - Total Records populated (expected > 0) and Success Count/Failure Count present (may be 0 while running)
  - Download/details action available for the new entry

**Expected Change**: A new row appears in the Import History with Name equal to the uploaded file and a recent Import Time; the job is marked as not completed (Completed = false or status 'Processing'/'Queued'/'Running'), Total Records is populated (> 0) and Success/Failure counts are present (initially may be zero). Over time the row may update End Time and Completed to true and show final Success/Failure counts.

---

### [TC-010] Log Out in one tab, then attempt Log Out in another tab (concurrent session edge)
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Tab A, click the Profile Icon
2. 2. In Tab A, click the "Log Out" button
3. 3. In Tab B, click the Profile Icon
4. 4. In Tab B, click the "Log Out" button

**Original Expected Result:** Logout in Tab A succeeds: Tab A is redirected to the login page and authentication token cleared. In Tab B, clicking "Log Out" succeeds in resulting in the login page (no error shown) but performs no additional session termination; Tab B is redirected to the login page as well.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Clients -> Client Detail page for <target client>`
- **Observe**:
  - status badge showing 'Pending' (yellow chip)
  - Submitted On date (recorded on the detail page)
  - Activation Date is blank or not set
  - Available actions include 'Activate'

**Post-Check**
- **Navigate To**: `Clients -> Client Detail page for <target client>`
- **Observe**:
  - status badge showing 'Active' (green chip)
  - Activation Date equals <Activation Date>
  - Available actions include 'Edit', 'Transfer Client', 'Close', 'New Loan', 'New Savings' and no longer include 'Activate'
  - Clients listing row for <target client> shows status 'Active' (green chip) when viewing Clients page or search results

**Expected Change**: Client's status changes from 'Pending' to 'Active'; the Activation Date field is set to the provided <Activation Date> (which must be on or after the Submitted On date); the 'Activate' action is removed and Active-state actions (Edit, Transfer Client, Close, New Loan, New Savings) become available; the Clients listing and client detail both reflect the Active status (green).

---

### [TC-011] Profile menu and Profile Settings access when user is unauthenticated
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is logged out (if not, perform Log Out)
2. 2. Observe whether the Profile Icon is visible in the top-right corner
3. 3. In the browser address bar, manually navigate to the Profile Settings page URL and press Enter

**Original Expected Result:** Profile Icon is not visible when unauthenticated (no dropdown available). Direct navigation to the Profile Settings URL is blocked: Auth_Guard redirects to the login page and the Profile Settings page is not displayed.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Clients page -> open Client Detail for <target client>`
- **Observe**:
  - Mobile Number (current value before edit)
  - Client Status badge (should be 'Pending')

**Post-Check**
- **Navigate To**: `Clients page -> open Client Detail for <target client>`
- **Observe**:
  - Mobile Number
  - Client Status badge

**Expected Change**: Mobile Number is updated to <new value> on the Client Detail page and the Client Status badge remains 'Pending'.

---

### [TC-012] Move a code value up in ordering
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the Code Values Editor for <Code List Name>, click Move Up on the row for <entry A>

**Original Expected Result:** moves entry up in ordering and <entry A> is now displayed above the previous item in the list ordering

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Clients page -> search for <target client> -> open Client Detail page for <target client>`
- **Observe**:
  - status badge showing 'Pending'
  - 'Reject' action/button is present on the Client Detail page
  - Client name and account number match <target client>

**Post-Check**
- **Navigate To**: `Clients page -> search for <target client> -> open Client Detail page for <target client>; then Admin -> Audit Trails (filter by Resource ID or Action Name if needed)`
- **Observe**:
  - status badge showing 'Rejected' on the Client Detail page
  - 'Reject' action/button is no longer present on the Client Detail page (no actions available for Rejected status)
  - Audit Trails contains an entry for the client with Action Name containing 'Reject' (or equivalent), Maker = current user, Processing Result = 'Approved' or 'Completed', and the recorded reason text equals <Reason>

**Expected Change**: Client status changed from 'Pending' to 'Rejected'; the Client Detail page displays a 'Rejected' status badge and no Reject action is available; an audit trail entry exists recording the rejection performed by the current user and containing the supplied <Reason>.

---

### [TC-013] Move a code value down in ordering
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the Code Values Editor for <Code List Name>, click Move Down on the row for <entry B>

**Original Expected Result:** moves entry down in ordering and <entry B> is now displayed below the previous item in the list ordering

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Clients -> <target client> detail page`
- **Observe**:
  - status badge (expected: 'Pending')
  - available action buttons (expected to include: 'Activate', 'Edit', 'Reject', 'Withdraw')

**Post-Check**
- **Navigate To**: `Clients -> <target client> detail page`
- **Observe**:
  - status badge
  - available action buttons

**Expected Change**: Client status badge changed from 'Pending' to 'Withdrawn'; status-changing action buttons such as 'Activate', 'Edit', 'Reject', and 'Withdraw' are no longer available (no actions shown for Withdrawn status).

---

### [TC-014] Open Create Data Table form from Manage Data Tables
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Manage Data Tables
2. 2. Click Create Data Table (Create_Data_Table action)

**Original Expected Result:** Create_Data_Table form opens and the Create Data Table form is displayed with fields Data Table Name, Application Table Name, Multi Row, and Column Definitions

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Clients page -> open Client Detail for <target client>`
- **Observe**:
  - client name
  - status badge (expect 'Active')
  - email address (current value shown on detail page)

**Post-Check**
- **Navigate To**: `Clients page -> open Client Detail for <target client>`
- **Observe**:
  - client name
  - status badge (expect 'Active')
  - email address (value shown on detail page)

**Expected Change**: The client's email address is updated to <new value> on the Client Detail page; client name and status remain unchanged (status remains Active).

---

### [TC-015] Open data table definition editor via Edit_Data_Table row action
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Manage Data Tables
2. 2. Click Edit for the <Data_Table_Name> row

**Original Expected Result:** opens data table definition editor and the data table definition editor for <Data_Table_Name> is displayed

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Detail page for <target client> (opened from Clients listing filtered by <Current Office>)`
- **Observe**:
  - Office (shows <Current Office>)
  - Status (shows Active)
  - Client Account No. / Identifier

**Post-Check**
- **Navigate To**: `1) Client Detail page for <target client>; 2) Clients page filtered by Office = <Current Office>; 3) Clients page filtered by Office = <Destination Office>`
- **Observe**:
  - On Client Detail: Office field
  - On Client Detail: Status
  - On Client Detail: Client Account No. / Identifier
  - On Clients listing filtered by <Current Office>: absence of <target client>
  - On Clients listing filtered by <Destination Office>: presence of <target client> (Name, Account No., Office column)

**Expected Change**: Client's Office changed from <Current Office> to <Destination Office> (Client Detail Office field shows <Destination Office>); Status remains Active; Client Account No./Identifier unchanged; client is no longer listed when filtering Clients by <Current Office> and is listed when filtering by <Destination Office>.

---

### [TC-016] Delete a custom data table with confirmation
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Manage Data Tables
2. 2. Click Delete for the <Data_Table_Name> row
3. 3. Click Confirm on the deletion confirmation dialog

**Original Expected Result:** deletes custom data table and the row for <Data_Table_Name> is no longer visible in the Manage Data Tables list

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Detail page for <target client>`
- **Observe**:
  - client name
  - status badge equals 'Active'
  - active accounts summary (Loans, Savings, Shares) shows zero active accounts
  - available action buttons include 'Close' (and other Active-state actions)

**Post-Check**
- **Navigate To**: `Client Detail page for <target client>`
- **Observe**:
  - client name
  - status badge equals 'Closed'
  - available action buttons reflect Closed state (e.g., 'Reactivate' visible; 'Close' not present)
  - accounts tabs/summary still show no active accounts
  - Client appears in Clients listing with status 'Closed' (optional cross-check via Clients page)

**Expected Change**: Client status changed from 'Active' to 'Closed'; status badge displays 'Closed' and the set of available action buttons updates to closed-state actions (for example, 'Reactivate' is available and 'Close' is removed).

---

### [TC-017] Submit Create Data Table form with columns (Create)
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Create Data Table form, enter Data Table Name = <data table name>
2. 2. Select Application Table Name = <application table> from the dropdown
3. 3. Optionally check Multi Row
4. 4. Click Add Row in Column Definitions, then for the new column enter Name = <column name>, Type = <column type>, set Length/Is Mandatory/Is Unique as needed
5. 5. Click Create

**Original Expected Result:** New row appears in Manage Data Tables with the entered Data Table Name and Application Table Name and the Create Data Table form closes

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Clients -> <target client> Detail page -> Charges tab`
- **Observe**:
  - charges table rows (list of existing charges)
  - Charge Name, Amount, Due Date, Paid/Waived/Outstanding status columns
  - Total outstanding charges / Charges summary

**Post-Check**
- **Navigate To**: `Clients -> <target client> Detail page -> Charges tab`
- **Observe**:
  - charges table rows (list of existing charges)
  - Charge Name, Amount, Due Date, Paid/Waived/Outstanding status columns
  - Total outstanding charges / Charges summary

**Expected Change**: A new charge row appears in the Charges tab matching the charge entered in the Add Charge dialog (Charge Name equals the entered name; Amount equals the entered amount; Due Date equals the entered due date if provided). The new charge shows an unpaid/outstanding status and the client's Total outstanding charges increases by the charge amount.

---

### [TC-021] Submit Create Data Table form with ALL required fields empty
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Create Data Table' action to open Create_Data_Table_Form
2. 2. Leave the Data Table Name field blank
3. 3. Leave the Application Table Name dropdown unselected
4. 4. Do not add any Column Definitions items
5. 5. Click the Create button

**Original Expected Result:** Form does not submit; Data table is not created. Inline validation errors appear: Data Table Name field displays an error indicating it is required; Application Table Name field displays an error indicating it is required.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Clients page -> open Client Detail page for <target client>`
- **Observe**:
  - status badge (expected 'Closed')
  - client name
  - account number

**Post-Check**
- **Navigate To**: `Clients page -> open Client Detail page for <target client>`
- **Observe**:
  - status badge
  - activation date
  - available action buttons (e.g., Edit, Transfer Client, New Loan, New Savings, New Share Account)

**Expected Change**: Client status changes from 'Closed' to 'Active' (status badge shows Active/green); Activation date is populated; action buttons appropriate for an Active client appear (for example: Edit, Transfer Client, New Loan, New Savings, New Share Account).

---

### [TC-022] Create Data Table: leave representative text field (Data Table Name) blank
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Leave the Data Table Name field blank
2. 2. Select <valid application table> in the Application Table Name dropdown
3. 3. Click the Create button

**Original Expected Result:** Form does not submit; Data table is not created. Inline validation error appears on the Data Table Name field indicating it is required.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Clients -> <target client> (Client Detail) -> Identifiers tab`
- **Observe**:
  - list of identifier rows showing Document Type and Document Key
  - count of identifier rows
  - verify absence of identifier with Document Type '<Document Type>' and Document Key '<Document Key>'

**Post-Check**
- **Navigate To**: `Clients -> <target client> (Client Detail) -> Identifiers tab`
- **Observe**:
  - list of identifier rows showing Document Type and Document Key
  - count of identifier rows
  - presence of identifier with Document Type '<Document Type>' and Document Key '<Document Key>'

**Expected Change**: A new identifier row appears with Document Type '<Document Type>' and Document Key '<Document Key>'; the total identifier count has increased by 1 compared to pre-check; duplicates are not added (no additional row with the same Document Type and Document Key exists).

---

### [TC-023] Create Data Table: leave representative dropdown (Application Table Name) blank
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <valid name> in the Data Table Name field
2. 2. Leave the Application Table Name dropdown unselected
3. 3. Click the Create button

**Original Expected Result:** Form does not submit; Data table is not created. Inline validation error appears on the Application Table Name field indicating it is required.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Clients -> <target client> -> Identifiers tab`
- **Observe**:
  - Identifiers list/table is visible
  - presence of the target identifier row with Document Type '<document_type>' and Document Key '<document_key>'
  - count of identifier rows (n)

**Post-Check**
- **Navigate To**: `Clients -> <target client> -> Identifiers tab`
- **Observe**:
  - Identifiers list/table is visible
  - absence of the target identifier row with Document Type '<document_type>' and Document Key '<document_key>'
  - count of identifier rows (n-1)

**Expected Change**: The target identifier (Document Type '<document_type>' and Document Key '<document_key>') is no longer listed in the Identifiers tab for <target client>; the total number of identifier rows has decreased by one.

---

### [TC-024] Create Data Table: Column Definitions item with missing required column Name
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <valid name> in the Data Table Name field
2. 2. Select <valid application table> in the Application Table Name dropdown
3. 3. Click Add to create a Column Definitions item
4. 4. Leave the Column 'Name' field blank in the new item
5. 5. Select <valid Type> in the new item's Type dropdown
6. 6. Click the Create button

**Original Expected Result:** Form does not submit; Data table is not created. Inline validation error appears on the Column Definitions item's Name field indicating it is required.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Clients page`
- **Observe**:
  - No client exists with name '<First Name> <Last Name>' in the Clients listing (search by name returns no results)
  - No client exists with the same External ID (if External ID was provided on Step 1)

**Post-Check**
- **Navigate To**: `Clients page -> search for '<First Name> <Last Name>' -> open the created Client Detail page`
- **Observe**:
  - Client Detail page 'Address' section displays 'Address line 1' with the value entered on Step 2 ('<Address line 1>')
  - Client Detail page 'Address' section displays 'City' with the value entered on Step 2 ('<City>')
  - Any other address fields entered on Step 2 (e.g., Address line 2, State, Postal Code) are displayed with the entered values

**Expected Change**: The newly created client appears in the Clients listing and the Client Detail page Address section shows the address fields entered on Step 2 (Address line 1: '<Address line 1>', City: '<City>', and any other provided address fields).

---

### [TC-025] Inline edit CRON expression with invalid CRON format
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the CRON Expression cell for a job to edit inline
2. 2. Enter <invalid CRON expression> into the CRON Expression field
3. 3. Save the inline edit

**Original Expected Result:** Inline validation error appears on the CRON Expression field stating it must be a valid CRON expression; the change is rejected and the job's CRON expression remains unchanged.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Clients page (use search to look for the client to be created)`
- **Observe**:
  - Search for client by name '<First Name> <Last Name>' returns no results (client does not already exist)
  - Clients listing does not contain an entry for '<First Name> <Last Name>'

**Post-Check**
- **Navigate To**: `Client Detail page for '<First Name> <Last Name>' (via Clients page -> search -> open client)`
- **Observe**:
  - Client header shows name '<First Name> <Last Name>' and account number
  - Family Members tab is present on the Client Detail page
  - Within Family Members tab, a row exists with Family Member Name = '<Family Member Name>' and Relationship = '<relationship>'

**Expected Change**: A new client '<First Name> <Last Name>' is present and, on their Client Detail page, the Family Members tab lists the added member with the specified name '<Family Member Name>' and relationship '<relationship>'.

---

### [TC-004] Profile icon/menu inaccessible when unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application home page while not logged in
2. 2. Click the top-right Profile Icon

**Original Expected Result:** Profile Icon and profile menu are not available: the Profile Icon is not visible in the top-right; no dropdown opens; 'Profile Settings' and 'Log Out' options are not present or accessible. The user remains on the public/unauthenticated page (no authenticated UI is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Groups page -> Groups List`
- **Observe**:
  - Groups list table is visible
  - record the count of rows with Name = <group name> (existing_count)

**Post-Check**
- **Navigate To**: `Groups page -> Groups List; locate the row with Name = <group name> and click it to open Group Detail`
- **Observe**:
  - Groups list contains a row with Name = <group name>
  - Office column for that row equals <office>
  - Status badge for that row (Active if Active checkbox was checked during creation; otherwise Pending)
  - In Group Detail -> Members tab, the member list includes <client>

**Expected Change**: A new row with Name '<group name>' and Office '<office>' appears in the Groups list (the count of rows with that name increased by 1 compared to pre_check); opening the group's detail shows <client> listed under Members; Status is 'Active' if the Active checkbox was checked during creation, otherwise the status is 'Pending'.

---

### [TC-006] Invoking Log Out endpoint while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Log Out endpoint/URL that the 'Log Out' button would call

**Original Expected Result:** Precondition prevents logout action: browser is redirected to the Login page; no logout success behavior occurs (no authenticated session existed and no session changes happen).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Groups -> Bulk Import Groups (Bulk Import page)`
- **Observe**:
  - Import History table rows (current count)
  - Most recent entry file name (if any)
  - Most recent entry Import Time and End Time
  - Most recent entry Completed status
  - Most recent entry Total Records, Success Count, Failure Count
  - Presence/absence of Download action/link on most recent entry

**Post-Check**
- **Navigate To**: `Groups -> Bulk Import Groups (Bulk Import page)`
- **Observe**:
  - Import History table rows (new count)
  - Top/most recent entry file name
  - Top entry Import Time and End Time
  - Top entry Completed status
  - Top entry Total Records, Success Count, Failure Count
  - Presence of Download action/link for the top entry
  - Success notification/toast message displayed after upload

**Expected Change**: A new row appears at the top of the Import History table for the uploaded file (file name matches the uploaded file); Import Time is recent, End Time is set, Completed shows a completed/processed status, Total Records equals Success Count plus Failure Count, a Download link is available for the import result, and a success notification/toast is displayed immediately after the upload.

---

### [TC-007] Using browser Back after Log Out does not return to authenticated pages
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the Login page
2. 2. Enter <valid credentials> in the Username/Email field
3. 3. Enter <valid password> in the Password field
4. 4. Click the Login button
5. 5. Navigate to a protected page (e.g., Dashboard) while logged in
6. 6. Click the Profile Icon
7. 7. Click the 'Log Out' button in the profile menu
8. 8. After the application redirects to the Login page, click the browser Back button to return to the previously viewed protected page

**Original Expected Result:** After logout the protected page remains inaccessible: Auth Guard immediately redirects to the Login page; protected page content is not displayed; the user remains logged out (authentication token/session cleared).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Group Detail page (for the target group)`
- **Observe**:
  - status badge showing 'Pending'
  - Activate action/button present in the action bar

**Post-Check**
- **Navigate To**: `1) Refresh Group Detail page; 2) Navigate to Groups page and locate the group row`
- **Observe**:
  - status badge on Group Detail page showing 'Active'
  - status chip color indicates Active (green) on detail page
  - Activate action/button is no longer present in the action bar on detail page
  - Groups listing row for the group shows Status = 'Active' with green chip

**Expected Change**: Group status changes from 'Pending' to 'Active' on the Group Detail page after confirmation; the Activate action is removed and the Groups listing reflects the group's status as 'Active'.

---

### [TC-009] Browser Back after Log Out should not return to protected page
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. From the protected page, click the Profile Icon
2. 2. Click the "Log Out" button
3. 3. Wait for redirect to the login page
4. 4. Press the browser Back button

**Original Expected Result:** Navigation back to the protected page is blocked: Auth_Guard redirects to the login page and the protected page is not displayed. The back navigation is effectively blocked and the login page is shown.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Group Detail page for the target group (same group used in the core test case)`
- **Observe**:
  - status badge (text and color) - expected 'Pending'
  - available action buttons in the action bar (e.g., Activate, Edit, Close)
  - group identifier (name or account number) shown in header/breadcrumb to confirm correct entity

**Post-Check**
- **Navigate To**: `Group Detail page for the same group, then optionally Groups listing (to cross-check row status)`
- **Observe**:
  - status badge (text and color) - expected 'Closed'
  - available action buttons in the action bar (expect 'Close' removed and 'Reactivate' or other Closed-state actions present)
  - Groups listing row for the group shows Status column = 'Closed' (optional cross-check)

**Expected Change**: The group's status changed from 'Pending' to 'Closed' on the Group Detail page; the action bar no longer shows the 'Close' action and now shows actions appropriate for a Closed group (e.g., 'Reactivate'); the Groups listing (if checked) reflects the group's Status as 'Closed'.

---

### [TC-010] Log Out in one tab, then attempt Log Out in another tab (concurrent session edge)
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Tab A, click the Profile Icon
2. 2. In Tab A, click the "Log Out" button
3. 3. In Tab B, click the Profile Icon
4. 4. In Tab B, click the "Log Out" button

**Original Expected Result:** Logout in Tab A succeeds: Tab A is redirected to the login page and authentication token cleared. In Tab B, clicking "Log Out" succeeds in resulting in the login page (no error shown) but performs no additional session termination; Tab B is redirected to the login page as well.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Group Detail page for the target group (open from Groups listing or via global search)`
- **Observe**:
  - Staff field value (e.g., 'Unassigned' or current staff)
  - Group status badge

**Post-Check**
- **Navigate To**: `Groups -> search for the target group -> open Group Detail (or refresh the Group Detail page)`
- **Observe**:
  - Staff field value
  - Group status badge

**Expected Change**: Staff field on the Group Detail page now displays '<staff>' instead of the pre-check value; the Group status remains 'Pending'.

---

### [TC-011] Profile menu and Profile Settings access when user is unauthenticated
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is logged out (if not, perform Log Out)
2. 2. Observe whether the Profile Icon is visible in the top-right corner
3. 3. In the browser address bar, manually navigate to the Profile Settings page URL and press Enter

**Original Expected Result:** Profile Icon is not visible when unauthenticated (no dropdown available). Direct navigation to the Profile Settings URL is blocked: Auth_Guard redirects to the login page and the Profile Settings page is not displayed.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Group Detail page - Source Group (Pending status)`
- **Observe**:
  - members list contains <clients> (identify by Name and Account No.)
  - members count (number of members shown)

**Post-Check**
- **Navigate To**: `Group Detail page - Source Group (Pending status) and Group Detail page - <target group>`
- **Observe**:
  - source group members list does NOT contain the transferred <clients> (by Name and Account No.)
  - source group members count decreased by the number of transferred <clients>
  - target group members list contains the transferred <clients> (by Name and Account No.)
  - target group members count increased by the number of transferred <clients>

**Expected Change**: The transferred clients are removed from the Source Group's members list (member count reduced accordingly) and appear in the Target Group's members list (member count increased by the same number).

---

### [TC-013] Move a code value down in ordering
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the Code Values Editor for <Code List Name>, click Move Down on the row for <entry B>

**Original Expected Result:** moves entry down in ordering and <entry B> is now displayed below the previous item in the list ordering

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Group Detail page for the target group (ensure you are on the group's detail view)`
- **Observe**:
  - status badge showing 'Active'
  - presence of 'Close' action button in the Group Action Bar
  - group name and account number displayed in the header (to confirm correct group)

**Post-Check**
- **Navigate To**: `Group Detail page for the same group; then go to Groups listing and search for the group by name or account number`
- **Observe**:
  - status badge showing 'Closed' on the Group Detail page
  - absence of 'Close' action button in the Group Action Bar on the Group Detail page
  - in Groups listing, the group's Status column shows a 'Closed' chip for the same group (matching name/account number)

**Expected Change**: The group's status has changed from 'Active' to 'Closed' — the Group Detail page displays a 'Closed' status badge and the 'Close' action is no longer available; the Groups listing shows the group with a 'Closed' status chip.

---

### [TC-014] Open Create Data Table form from Manage Data Tables
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Manage Data Tables
2. 2. Click Create Data Table (Create_Data_Table action)

**Original Expected Result:** Create_Data_Table form opens and the Create Data Table form is displayed with fields Data Table Name, Application Table Name, Multi Row, and Column Definitions

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Group Detail page for the target group (status: Active)`
- **Observe**:
  - status badge
  - assigned staff field (Staff) — current value (may be empty or a different staff)

**Post-Check**
- **Navigate To**: `Group Detail page for the target group`
- **Observe**:
  - assigned staff field (Staff)
  - status badge

**Expected Change**: Assigned staff field on the Group Detail page displays '<staff>' (previous value replaced or populated); group status remains 'Active'.

---

### [TC-015] Open data table definition editor via Edit_Data_Table row action
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Manage Data Tables
2. 2. Click Edit for the <Data_Table_Name> row

**Original Expected Result:** opens data table definition editor and the data table definition editor for <Data_Table_Name> is displayed

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Source Group Detail page -> Members tab`
- **Observe**:
  - presence of the selected client(s) to be transferred (by name and/or account number) in the members list
  - member count on the Source Group members tab

**Post-Check**
- **Navigate To**: `1) Source Group Detail page -> Members tab; 2) Target Group Detail page -> Members tab`
- **Observe**:
  - absence of the transferred client(s) in the Source Group members list (by name and/or account number)
  - updated member count on the Source Group members tab
  - presence of the transferred client(s) in the Target Group members list (by name and/or account number)
  - updated member count on the Target Group members tab

**Expected Change**: The selected client(s) no longer appear in the Source Group's members list and the Source Group's member count has decreased by the number of transferred clients; the same client(s) now appear in the Target Group's members list and the Target Group's member count has increased by that number.

---

### [TC-016] Delete a custom data table with confirmation
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Manage Data Tables
2. 2. Click Delete for the <Data_Table_Name> row
3. 3. Click Confirm on the deletion confirmation dialog

**Original Expected Result:** deletes custom data table and the row for <Data_Table_Name> is no longer visible in the Manage Data Tables list

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Group Detail page for the target group (page shows status 'Closed')`
- **Observe**:
  - status badge showing 'Closed' (gray chip)
  - presence of 'Activate' action button in the Group Action Bar
  - group name and account number to uniquely identify the group

**Post-Check**
- **Navigate To**: `Group Detail page for the same group (and optionally Groups listing with filter 'Active')`
- **Observe**:
  - status badge showing 'Active' (green chip)
  - absence of 'Activate' action in the Group Action Bar
  - presence of Active-state actions such as 'Assign Staff' or 'Close'
  - Groups listing (with 'Active' filter applied) shows the group row with status 'Active' and matching account number

**Expected Change**: The group's status is updated from 'Closed' to 'Active' on the Group Detail page; the 'Activate' action is removed and Active-specific actions appear; the group is visible under the Active filter in the Groups listing.

---

### [TC-018] Cancel Create Data Table form (Cancel)
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Create Data Table form, click Cancel

**Original Expected Result:** closes form without creating and the Create Data Table form is closed with no new row added to Manage Data Tables

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Groups -> [Group Name] Detail page (the Closed group under test)`
- **Observe**:
  - status badge (expect 'Closed')
  - staff field (current value or empty)
  - presence of 'Assign Staff' action in the Group Action Bar

**Post-Check**
- **Navigate To**: `Groups -> [Group Name] Detail page (refresh or reopen); then Groups listing page`
- **Observe**:
  - staff field on Group Detail page
  - status badge on Group Detail page
  - staff column for the group on the Groups listing

**Expected Change**: Staff field on the Group Detail page displays <staff>; the Groups listing shows <staff> in the Staff column for this group; the group's status remains 'Closed'.

---

### [TC-019] Approve an Audit Trail entry when maker-checker is enabled and Processing Result is Pending
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Audit Trails
2. 2. Locate the audit row for <Action_Name> with Processing Result = Pending
3. 3. Click Approve for that audit row

**Original Expected Result:** sets Processing Result to Approved and the Processing Result column for the selected audit row displays 'Approved'

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Source Group Detail page (Closed group) — the group from which clients will be transferred`
- **Observe**:
  - members list shows the selected client(s) by name and account number
  - members count includes the selected client(s)

**Post-Check**
- **Navigate To**: `Source Group Detail page (Closed group) and then navigate to Target Group Detail page (destination group)`
- **Observe**:
  - On Source Group: members list (names and account numbers) and members count
  - On Target Group: members list (names and account numbers) and members count

**Expected Change**: The selected client(s) no longer appear in the source group's members list and the source group's members count has decreased by the number of transferred clients; the same client(s) appear in the target group's members list and the target group's members count has increased by the same number.

---

### [TC-021] Submit Create Data Table form with ALL required fields empty
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Create Data Table' action to open Create_Data_Table_Form
2. 2. Leave the Data Table Name field blank
3. 3. Leave the Application Table Name dropdown unselected
4. 4. Do not add any Column Definitions items
5. 5. Click the Create button

**Original Expected Result:** Form does not submit; Data table is not created. Inline validation errors appear: Data Table Name field displays an error indicating it is required; Application Table Name field displays an error indicating it is required.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Group Detail -> Calendar/Meeting tab`
- **Observe**:
  - meeting list/calendar entries for the group (focus on <meeting date> or surrounding range)
  - verify there is no meeting with topic '<meeting topic>' scheduled on <meeting date> at <meeting time>

**Post-Check**
- **Navigate To**: `Group Detail -> Calendar/Meeting tab`
- **Observe**:
  - meeting list/calendar entries for the group (showing meetings on and around <meeting date>)
  - a meeting entry with topic '<meeting topic>'
  - meeting date displayed as <meeting date>
  - meeting time displayed as <meeting time>
  - meeting details (when opened) show the organizer as the current user and any saved notes/metadata

**Expected Change**: A new meeting appears in the group's meeting list/calendar with the entered topic, scheduled on <meeting date> at <meeting time>; the meeting count for that date increases by one and the meeting detail shows the creator as the current user.

---

### [TC-022] Create Data Table: leave representative text field (Data Table Name) blank
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Leave the Data Table Name field blank
2. 2. Select <valid application table> in the Application Table Name dropdown
3. 3. Click the Create button

**Original Expected Result:** Form does not submit; Data table is not created. Inline validation error appears on the Data Table Name field indicating it is required.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Group Detail -> Calendar/Meeting tab (Meeting history)`
- **Observe**:
  - number of meetings listed (meeting count)
  - most recent meeting's notes/description
  - most recent meeting's attendance list (names and statuses)
  - most recent meeting's date/time
  - most recent meeting's recorded by / creator

**Post-Check**
- **Navigate To**: `Group Detail -> Calendar/Meeting tab (Meeting history) and Group Detail -> Notes tab`
- **Observe**:
  - number of meetings listed (meeting count)
  - most recent meeting's notes/description
  - most recent meeting's attendance list (names and statuses)
  - most recent meeting's date/time
  - most recent meeting's recorded by / creator
  - most recent note entry in Notes tab (to verify meeting note is optionally recorded in notes)

**Expected Change**: Meeting count increased by 1 and a new top/most-recent meeting entry appears whose notes exactly match the entered <meeting notes>, whose attendance list includes the entered <attendance> with correct presence statuses, and whose date/time and 'recorded by' indicate the submitted meeting. The meeting details are also present as a corresponding entry in the Group's Notes tab (if the system records meeting notes there).

---

### [TC-004] Profile icon/menu inaccessible when unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application home page while not logged in
2. 2. Click the top-right Profile Icon

**Original Expected Result:** Profile Icon and profile menu are not available: the Profile Icon is not visible in the top-right; no dropdown opens; 'Profile Settings' and 'Log Out' options are not present or accessible. The user remains on the public/unauthenticated page (no authenticated UI is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Centers page (use the page search/filter to query Name = <center name>)`
- **Observe**:
  - absence or presence of a row with Name = <center name> and Office = <office> (record whether it exists before the test)
  - Centers table columns visible: Name, Account #, External Id, Status, Office Name

**Post-Check**
- **Navigate To**: `Centers page (use the page search/filter to query Name = <center name>)`
- **Observe**:
  - row with Name = <center name> and Office = <office>
  - Status badge for that row (e.g., Active if Active checkbox was checked during creation, otherwise Pending or default initial status)
  - Submitted On / Created Date column value for the row (should match or be consistent with the entered <date> if displayed)

**Expected Change**: A new row appears in the Centers table with Name = <center name> and Office = <office>. The Status column shows 'Active' if the Active checkbox was selected during creation (otherwise the initial pending/default status). The row's Submitted On/Created Date, if displayed, corresponds to the entered <date>.

---

### [TC-005] Direct navigation to Profile Settings while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Profile Settings page URL

**Original Expected Result:** Auth Guard blocks access: browser is redirected to the Login page; Profile Settings content is not displayed and no profile settings UI elements are visible.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin -> Organization -> Centers page`
- **Observe**:
  - Presence or absence of a row in the Centers table with Name = '<center name>'
  - If a row with Name = '<center name>' exists, note its Office column value and number of Member Groups listed on its detail page

**Post-Check**
- **Navigate To**: `Admin -> Organization -> Centers page; then open the created center's detail -> Groups tab`
- **Observe**:
  - Centers table contains a new row with Name = '<center name>'
  - The Office column for the '<center name>' row shows '<office>'
  - After opening the center detail and selecting the 'Groups' tab, the Member Groups table contains a row with the group name '<matching result>'

**Expected Change**: A new row appears in the Centers table with Name '<center name>' and Office '<office>'; when opening that Center's Detail and viewing the Groups tab, the added group '<matching result>' is listed in the Member Groups table.

---

### [TC-007] Using browser Back after Log Out does not return to authenticated pages
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the Login page
2. 2. Enter <valid credentials> in the Username/Email field
3. 3. Enter <valid password> in the Password field
4. 4. Click the Login button
5. 5. Navigate to a protected page (e.g., Dashboard) while logged in
6. 6. Click the Profile Icon
7. 7. Click the 'Log Out' button in the profile menu
8. 8. After the application redirects to the Login page, click the browser Back button to return to the previously viewed protected page

**Original Expected Result:** After logout the protected page remains inaccessible: Auth Guard immediately redirects to the Login page; protected page content is not displayed; the user remains logged out (authentication token/session cleared).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Centers page`
- **Observe**:
  - Centers table row count
  - Presence/absence of center names that will be in the import file (record which of those names are currently present before import)

**Post-Check**
- **Navigate To**: `Centers page`
- **Observe**:
  - Centers table row count
  - Presence of center names from the uploaded file as rows in the Centers table
  - Import History latest entry with fields: File Name, Import Time, Completed status, Total Records, Success Count, Failure Count

**Expected Change**: The Centers table contains new rows for each center in the uploaded file; the Centers table row count increases by the number of successfully imported centers; the Import History shows a completed import entry for the uploaded file where Success Count equals the number of centers imported (and Failure Count is zero or matches reported failures).

---

### [TC-008] Rapid double-click Log Out
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Log in as a valid user
2. 2. Click the Profile Icon in the top-right corner
3. 3. Click the "Log Out" button
4. 4. Immediately click the "Log Out" button again

**Original Expected Result:** First click succeeds: authenticated session is terminated and the user is redirected to the login page. The immediate second click is ignored (no additional navigation or error shown) and only a single logout action takes effect.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Center Detail page for the target center`
- **Observe**:
  - center name (to confirm correct entity)
  - status badge text (expected: 'Inactive')
  - available actions in action bar (expected: 'Activate' present)

**Post-Check**
- **Navigate To**: `Center Detail page for the same center (refresh or reopen if necessary); then optionally navigate to Centers listing`
- **Observe**:
  - status badge text on Center Detail page
  - available actions in action bar on Center Detail page
  - Centers listing row for the center (Status column)

**Expected Change**: Status badge on the Center Detail page changes from 'Inactive' to 'Active'; the 'Activate' action is no longer presented in the action bar (replaced by actions appropriate to an active center such as 'Edit' or 'Close'); the Centers listing row for the center shows Status 'Active'.

---

### [TC-010] Log Out in one tab, then attempt Log Out in another tab (concurrent session edge)
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Tab A, click the Profile Icon
2. 2. In Tab A, click the "Log Out" button
3. 3. In Tab B, click the Profile Icon
4. 4. In Tab B, click the "Log Out" button

**Original Expected Result:** Logout in Tab A succeeds: Tab A is redirected to the login page and authentication token cleared. In Tab B, clicking "Log Out" succeeds in resulting in the login page (no error shown) but performs no additional session termination; Tab B is redirected to the login page as well.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Center Detail page (for the target center)`
- **Observe**:
  - status badge (expected 'Active' or 'Open')
  - available actions in the action bar (should include 'Close')
  - center identifier (Name or Account #) to use for searching later

**Post-Check**
- **Navigate To**: `Centers listing -> search for the same center -> open Center Detail page (or refresh the Detail page)`
- **Observe**:
  - status badge (should show 'Closed')
  - available actions in the action bar (should NOT include 'Close')
  - Centers listing row for the center shows status 'Closed' when searched

**Expected Change**: The center's status changed from 'Active'/'Open' to 'Closed' on the persisted record: the Center Detail page now shows a 'Closed' status badge, the 'Close' action is no longer available in the action bar, and the Centers listing shows the center with status 'Closed'.

---

### [TC-006] Invoking Log Out endpoint while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Log Out endpoint/URL that the 'Log Out' button would call

**Original Expected Result:** Precondition prevents logout action: browser is redirected to the Login page; no logout success behavior occurs (no authenticated session existed and no session changes happen).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Products page`
- **Observe**:
  - absence of a product row with Name '<Product Name>' in the loan products listing (search for '<Product Name>' returns no results)
  - loan products listing is accessible and searchable

**Post-Check**
- **Navigate To**: `Loan Products page -> search for '<Product Name>'`
- **Observe**:
  - product row with Name '<Product Name>' and Short Name '<Short Name>' appears in the search results
  - click the product Name '<Product Name>' to open Product Detail page
  - Product Detail displays Product Name '<Product Name>'
  - Product Detail displays Short Name '<Short Name>'

**Expected Change**: A loan product with Product Name '<Product Name>' and Short Name '<Short Name>' is present in the Loan Products listing and its Product Detail page persists and displays those values.

---

### [TC-007] Using browser Back after Log Out does not return to authenticated pages
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the Login page
2. 2. Enter <valid credentials> in the Username/Email field
3. 3. Enter <valid password> in the Password field
4. 4. Click the Login button
5. 5. Navigate to a protected page (e.g., Dashboard) while logged in
6. 6. Click the Profile Icon
7. 7. Click the 'Log Out' button in the profile menu
8. 8. After the application redirects to the Login page, click the browser Back button to return to the previously viewed protected page

**Original Expected Result:** After logout the protected page remains inaccessible: Auth Guard immediately redirects to the Login page; protected page content is not displayed; the user remains logged out (authentication token/session cleared).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Products page`
- **Observe**:
  - Loan Products table does not contain a product with name '<Product Name>'

**Post-Check**
- **Navigate To**: `Loan Products page -> Open product detail for '<Product Name>'`
- **Observe**:
  - Product appears in Loan Products list with Name '<Product Name>'
  - On Product Detail page: 'Currency' field displays '<Currency>'
  - On Product Detail page: 'Principal Amount Default' (Principal Amount default) displays '<Principal Default>'

**Expected Change**: A new product named '<Product Name>' appears in the Loan Products list and its Product Detail page shows Currency '<Currency>' and Principal Amount Default '<Principal Default>', confirming the Currency step values were persisted after submit.

---

### [TC-008] Rapid double-click Log Out
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Log in as a valid user
2. 2. Click the Profile Icon in the top-right corner
3. 3. Click the "Log Out" button
4. 4. Immediately click the "Log Out" button again

**Original Expected Result:** First click succeeds: authenticated session is terminated and the user is redirected to the login page. The immediate second click is ignored (no additional navigation or error shown) and only a single logout action takes effect.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Products page`
- **Observe**:
  - Confirm no existing product with name '<Product Name>' (search/listing)
  - If needed, note current loan products count or listing page state before creation

**Post-Check**
- **Navigate To**: `Loan Products page -> search for '<Product Name>' -> open product detail`
- **Observe**:
  - Product name '<Product Name>' is present in the listing and detail page is accessible
  - Amortization Method displayed on product detail
  - Interest Method displayed on product detail
  - Days in Year displayed on product detail
  - Days in Month displayed on product detail

**Expected Change**: A new loan product named '<Product Name>' appears in Loan Products. Its product detail shows Amortization Method '<Amortization Method>', Interest Method '<Interest Method>', Days in Year set to '<Days in Year>' and Days in Month set to '<Days in Month>' as selected during the Settings step.

---

### [TC-009] Browser Back after Log Out should not return to protected page
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. From the protected page, click the Profile Icon
2. 2. Click the "Log Out" button
3. 3. Wait for redirect to the login page
4. 4. Press the browser Back button

**Original Expected Result:** Navigation back to the protected page is blocked: Auth_Guard redirects to the login page and the protected page is not displayed. The back navigation is effectively blocked and the login page is shown.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Products page`
- **Observe**:
  - products list (searchable)
  - absence of a product named '<Product Name>' in the list

**Post-Check**
- **Navigate To**: `Loan Products page -> click product '<Product Name>' to open Product Detail`
- **Observe**:
  - Number of Repayments (Default) value on product detail
  - Repaid Every display showing frequency and unit (e.g., '<Frequency> <Unit>')
  - Nominal Interest Rate (Default) value on product detail

**Expected Change**: Product detail displays Number of Repayments Default '<Number of Repayments Default>', Repaid Every '<Frequency> <Unit>', and Nominal Interest Rate Default '<Nominal Interest Rate Default>' as entered in the Create Loan Product wizard.

---

### [TC-010] Log Out in one tab, then attempt Log Out in another tab (concurrent session edge)
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Tab A, click the Profile Icon
2. 2. In Tab A, click the "Log Out" button
3. 3. In Tab B, click the Profile Icon
4. 4. In Tab B, click the "Log Out" button

**Original Expected Result:** Logout in Tab A succeeds: Tab A is redirected to the login page and authentication token cleared. In Tab B, clicking "Log Out" succeeds in resulting in the login page (no error shown) but performs no additional session termination; Tab B is redirected to the login page as well.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Products page`
- **Observe**:
  - Search for product by name '<Product Name>' (should not exist prior to creation)

**Post-Check**
- **Navigate To**: `Loan Products page -> Click the product named '<Product Name>' to open Product Detail`
- **Observe**:
  - Charges section is present on the Product Detail page
  - Charges section lists charge named '<selected charge>'

**Expected Change**: A new loan product named '<Product Name>' appears in the Loan Products list; on its Product Detail page the Charges section lists the added charge '<selected charge>' (persists after reload/navigation).

---

### [TC-011] Profile menu and Profile Settings access when user is unauthenticated
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is logged out (if not, perform Log Out)
2. 2. Observe whether the Profile Icon is visible in the top-right corner
3. 3. In the browser address bar, manually navigate to the Profile Settings page URL and press Enter

**Original Expected Result:** Profile Icon is not visible when unauthenticated (no dropdown available). Direct navigation to the Profile Settings URL is blocked: Auth_Guard redirects to the login page and the Profile Settings page is not displayed.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Products page (use search/filter for <Product Name>)`
- **Observe**:
  - No existing product with name '<Product Name>' in the listing (search results empty)
  - Create Loan Product button is present and enabled

**Post-Check**
- **Navigate To**: `Loan Products page -> search for '<Product Name>' -> open Product Detail page by clicking the product name`
- **Observe**:
  - Accounting Method field on the Product Detail page
  - Fund Source GL Account mapping value
  - Loan Portfolio GL Account mapping value
  - Interest on Loans GL Account mapping value
  - Income from Fees GL Account mapping value
  - Income from Penalties GL Account mapping value
  - Losses Written Off GL Account mapping value
  - Overpayment Liability GL Account mapping value

**Expected Change**: The created product appears in the Loan Products listing and its Product Detail page shows Accounting Method set to '<Accounting Method other than None>' and the GL account mappings persisted as: Fund Source '<Fund Source GL Account>', Loan Portfolio '<Loan Portfolio GL Account>', Interest on Loans '<Interest on Loans GL Account>', Income from Fees '<Income from Fees GL Account>', Income from Penalties '<Income from Penalties GL Account>', Losses Written Off '<Losses Written Off GL Account>', and Overpayment Liability '<Overpayment Liability GL Account>'.

---

### [TC-003] Unauthenticated navigation to a protected page redirects to login
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <authenticated page URL> in the browser address bar and navigate to it

**Original Expected Result:** redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Products page`
- **Observe**:
  - Use the page search/filter to search for the product name used in the test: '<valid product name>'
  - Verify that no product with name '<valid product name>' and short name '<short name>' exists prior to creation

**Post-Check**
- **Navigate To**: `Savings Products page`
- **Observe**:
  - Product appears in the listing with Name = '<valid product name>' and Short Name = '<short name>'
  - Click the product name to open the Product Detail view
  - In Details/General: Product Name equals '<valid product name>', Short Name equals '<short name>', Description (if provided) matches '<optional description>'
  - In Currency: Currency = '<currency>', Decimal Places = '<decimal places>', Currency In Multiples Of = '<currency multiple>'
  - In Terms: Nominal Annual Interest Rate = '<nominal annual interest rate>', Interest Compounding Period = '<compounding period>', Interest Posting Period = '<posting period>', Interest Calculated Using = '<calculation method>', Days in Year = '<days option>'
  - In Settings: Minimum Opening Balance = '<minimum opening balance>', Enforce Minimum Required Balance is enabled and Minimum Required Balance = '<minimum required balance>', Is Overdraft Allowed is enabled with Maximum Overdraft Amount = '<max overdraft amount>' and Overdraft Interest Rate = '<overdraft interest rate>'
  - In Charges tab: the added charge list contains the selected charge '<matching result>'
  - In Accounting: Accounting Method = 'Cash-based' and the configured GL account mappings match the values entered ('<valid GL account>' placeholders)

**Expected Change**: A new Savings Product with Name '<valid product name>' and Short Name '<short name>' is created and visible in the Savings Products listing; its detail view reflects the currency, terms, settings (including minimums and overdraft settings), added charge, and accounting method/GL mappings as submitted in the wizard.

---

### [TC-003] Unauthenticated navigation to a protected page redirects to login
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <authenticated page URL> in the browser address bar and navigate to it

**Original Expected Result:** redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Products -> Share Products table`
- **Observe**:
  - row for <target product> exists in the table
  - visible columns for that row include: Name, Short Name, Total Shares

**Post-Check**
- **Navigate To**: `Share Products -> Share Products table`
- **Observe**:
  - row for <target product> is not present in the table
  - list of product names in the table does not include <target product>

**Expected Change**: The row for <target product> is no longer present in the Share Products table and the total count of share products in the listing has decreased by one.

---

### [TC-005] Direct navigation to Profile Settings while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Profile Settings page URL

**Original Expected Result:** Auth Guard blocks access: browser is redirected to the Login page; Profile Settings content is not displayed and no profile settings UI elements are visible.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Products -> Share Products page (Share Products listing)`
- **Observe**:
  - table contains a row with Name = <target product>
  - Short Name and Total Shares columns are present for that row
  - record the number of rows (total products) in the Share Products table

**Post-Check**
- **Navigate To**: `Products -> Share Products page (Share Products listing)`
- **Observe**:
  - no row with Name = <target product> is present in the table
  - the number of rows (total products) in the Share Products table is one less than recorded in pre_check
  - searching for '<target product>' via the Share Products search field returns no results / shows 'No results found'

**Expected Change**: The row for <target product> is removed from the Share Products table; the total products count decreased by one; searching for <target product> returns no results.

---

### [TC-006] Invoking Log Out endpoint while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Log Out endpoint/URL that the 'Log Out' button would call

**Original Expected Result:** Precondition prevents logout action: browser is redirected to the Login page; no logout success behavior occurs (no authenticated session existed and no session changes happen).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Products page (Products -> Share Products)`
- **Observe**:
  - Share Products table rows with columns: Product Name, Short Name, Total Shares
  - There is no existing row with Product Name = <Product Name> and Short Name = <Short Name>

**Post-Check**
- **Navigate To**: `Share Products page -> Click the created product row to open the Share Product Detail page`
- **Observe**:
  - Share Products table contains a row with Product Name = <Product Name> and Short Name = <Short Name>
  - Share Products table row shows Total Shares equals <Total Number of Shares> (if displayed in list)
  - On the Share Product Detail page, Accounting Method is displayed as 'None'
  - On the Share Product Detail page Accounting section: no GL mapping fields (e.g., Share Reference, Share Suspense, Equity in Shares, Income from Fees) are visible
  - On the Terms section of the Detail page: Capital Value is displayed and equals <Total Number of Shares> × <Nominal/Unit Price> (shows computed numeric value)

**Expected Change**: A new share product row appears in the Share Products table with the provided Product Name and Short Name; opening the product's Detail page shows Accounting Method as 'None' with no GL mapping fields visible, and the Terms section displays Capital Value computed as Total Number of Shares multiplied by the Nominal/Unit Price.

---

### [TC-007] Using browser Back after Log Out does not return to authenticated pages
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the Login page
2. 2. Enter <valid credentials> in the Username/Email field
3. 3. Enter <valid password> in the Password field
4. 4. Click the Login button
5. 5. Navigate to a protected page (e.g., Dashboard) while logged in
6. 6. Click the Profile Icon
7. 7. Click the 'Log Out' button in the profile menu
8. 8. After the application redirects to the Login page, click the browser Back button to return to the previously viewed protected page

**Original Expected Result:** After logout the protected page remains inaccessible: Auth Guard immediately redirects to the Login page; protected page content is not displayed; the user remains logged out (authentication token/session cleared).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Products -> Share Products`
- **Observe**:
  - list of product names and short names in the Share Products table
  - verify that <Product Name> and <Short Name> are NOT present in the list (or record current count of rows for comparison)

**Post-Check**
- **Navigate To**: `Products -> Share Products`
- **Observe**:
  - presence of a row with Product Name = <Product Name> and Short Name = <Short Name> in the Share Products table
  - open the created product's detail view by clicking the product row
  - on the Share Product Detail page observe the Accounting Method field
  - on the Share Product Detail page observe GL mapping fields: GL Share Reference, GL Share Suspense, GL Equity in Shares, GL Income from Fees, GL Share Equity and their displayed account values

**Expected Change**: A new row exists in the Share Products table with Product Name = <Product Name> and Short Name = <Short Name>. The Share Product detail view shows Accounting Method set to 'Cash-based' and the GL mapping fields (GL Share Reference, GL Share Suspense, GL Equity in Shares, GL Income from Fees, GL Share Equity) populated with the GL accounts selected during creation.

---

### [TC-008] Rapid double-click Log Out
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Log in as a valid user
2. 2. Click the Profile Icon in the top-right corner
3. 3. Click the "Log Out" button
4. 4. Immediately click the "Log Out" button again

**Original Expected Result:** First click succeeds: authenticated session is terminated and the user is redirected to the login page. The immediate second click is ignored (no additional navigation or error shown) and only a single logout action takes effect.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Products`
- **Observe**:
  - no existing product with name <Product Name> in listing (or use a unique <Product Name> for this test)

**Post-Check**
- **Navigate To**: `Share Products -> click <Product Name> to open Product Detail page`
- **Observe**:
  - Currency
  - Decimal Places
  - Currency In Multiples Of

**Expected Change**: Product detail displays Currency set to <Currency>, Decimal Places set to <Decimal Places>, and Currency In Multiples Of set to <Currency In Multiples Of> as entered on the Currency (Step 2) of the Create Share Product wizard.

---

### [TC-009] Browser Back after Log Out should not return to protected page
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. From the protected page, click the Profile Icon
2. 2. Click the "Log Out" button
3. 3. Wait for redirect to the login page
4. 4. Press the browser Back button

**Original Expected Result:** Navigation back to the protected page is blocked: Auth_Guard redirects to the login page and the protected page is not displayed. The back navigation is effectively blocked and the login page is shown.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Products page (Products -> Share Products)`
- **Observe**:
  - list of share products (confirm <Product Name> is not present)

**Post-Check**
- **Navigate To**: `Share Products page -> click the created product <Product Name> to open its Detail view -> Terms tab/section`
- **Observe**:
  - Total Number of Shares (value equals <Total Number of Shares>)
  - Nominal/Unit Price (value equals <Nominal/Unit Price>)
  - Capital Value (displayed)

**Expected Change**: A Share Product named <Product Name> exists; in the Terms section Total Number of Shares and Nominal/Unit Price match the values entered during creation, and Capital Value equals Total Number of Shares × Nominal/Unit Price. The Capital Value displayed on the product detail page matches the Capital Value observed on Step 3 of the creation wizard.

---

### [TC-010] Log Out in one tab, then attempt Log Out in another tab (concurrent session edge)
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Tab A, click the Profile Icon
2. 2. In Tab A, click the "Log Out" button
3. 3. In Tab B, click the Profile Icon
4. 4. In Tab B, click the "Log Out" button

**Original Expected Result:** Logout in Tab A succeeds: Tab A is redirected to the login page and authentication token cleared. In Tab B, clicking "Log Out" succeeds in resulting in the login page (no error shown) but performs no additional session termination; Tab B is redirected to the login page as well.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Products page`
- **Observe**:
  - presence of a product with name '<Product Name>' (expectation: none exists prior to creation)
  - if a product with the same name exists, record its Settings values: 'Allow Dividends for Inactive Clients' state, Minimum Shares per Client, Maximum Shares per Client

**Post-Check**
- **Navigate To**: `Share Products page -> Open '<Product Name>' detail view`
- **Observe**:
  - Product Name (should be '<Product Name>')
  - Short Name (should be '<Short Name>')
  - Settings section: 'Allow Dividends for Inactive Clients' checkbox state
  - Settings section: Minimum Shares per Client value
  - Settings section: Maximum Shares per Client value

**Expected Change**: A Share Product named '<Product Name>' is present and on its detail page the Settings section shows 'Allow Dividends for Inactive Clients' checked and the Minimum Shares per Client and Maximum Shares per Client match the values entered during creation ('<Minimum_Shares_per_Client>' and '<Maximum_Shares_per_Client>').

---

### [TC-011] Profile menu and Profile Settings access when user is unauthenticated
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is logged out (if not, perform Log Out)
2. 2. Observe whether the Profile Icon is visible in the top-right corner
3. 3. In the browser address bar, manually navigate to the Profile Settings page URL and press Enter

**Original Expected Result:** Profile Icon is not visible when unauthenticated (no dropdown available). Direct navigation to the Profile Settings URL is blocked: Auth_Guard redirects to the login page and the Profile Settings page is not displayed.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Products page -> Search for <Product Name>`
- **Observe**:
  - No existing product named <Product Name> in the listing (or note existing product if re-using a name)
  - If product exists, note current number of Market Price rows for <Product Name> (to compare after test)

**Post-Check**
- **Navigate To**: `Share Products page -> Click product <Product Name> to open Detail page -> Market Price tab`
- **Observe**:
  - Market Price table lists rows with From Date and Share Value entries matching the values entered during creation (each row shows the entered From Date and corresponding Share Value)
  - The number of Market Price rows equals the number of rows added in the wizard

**Expected Change**: The created Share Product's Market Price table contains the same rows that were added in the wizard: each row's From Date and Share Value match the inputs supplied in Step 5 and the total row count matches the number of rows added during creation.

---

### [TC-012] Move a code value up in ordering
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the Code Values Editor for <Code List Name>, click Move Up on the row for <entry A>

**Original Expected Result:** moves entry up in ordering and <entry A> is now displayed above the previous item in the list ordering

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Products`
- **Observe**:
  - Search for product with name '<Product Name>' returns no results (product does not exist prior to test)

**Post-Check**
- **Navigate To**: `Share Products -> Click product '<Product Name>' to open Detail page -> Charges tab`
- **Observe**:
  - Charges table contains a row with Charge Name matching '<charge search term>'
  - Charge Amount shown for that row matches the amount selected when adding the charge in the wizard
  - Charge Applies To or applicability indicator reflects that the charge applies to the Share Product
  - The listed charge(s) count includes the charge(s) added during creation

**Expected Change**: The Share Product '<Product Name>' Charges tab lists the added charge(s) whose Charge Name matches '<charge search term>' and displays the same amount and applicability as selected during the Create Share Product wizard.

---

### [TC-002] Log Out via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Log Out' in the dropdown

**Original Expected Result:** terminates authenticated session; clears authentication token; redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Charges page`
- **Observe**:
  - Charges table (ensure no existing row with Name '<Charge Name>')
  - Ability to filter/search charges by Name and by 'Charge Applies To' = 'Loan' (verify '<Charge Name>' not present in filtered results)

**Post-Check**
- **Navigate To**: `Charges page`
- **Observe**:
  - Charges table row with Name '<Charge Name>' exists
  - Charge Applies To column for that row equals 'Loan'
  - Is Active indicator for that row reflects the selected toggle (Active/Inactive)
  - Open the newly created charge's detail view and observe: ['Charge Name', 'Charge Applies To', 'Charge Time Type', 'Charge Calculation Type', 'Amount', 'Is Penalty', 'Payment Mode']

**Expected Change**: A new charge record with Name '<Charge Name>' has been created: it appears in the Charges table and its Charge Applies To is 'Loan'. In the charge detail view, the Charge Time Type equals the selected loan-specific option, the Charge Calculation Type equals the selected value, the Amount equals the entered amount, the Is Penalty and Is Active flags reflect the chosen toggles, and the Payment Mode matches the selected payment mode.

---

### [TC-003] Unauthenticated navigation to a protected page redirects to login
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <authenticated page URL> in the browser address bar and navigate to it

**Original Expected Result:** redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Charges page`
- **Observe**:
  - Charges table rows
  - absence of a row with Name = '<Charge Name>' and Charge Applies To = 'Savings Account'

**Post-Check**
- **Navigate To**: `Charges page -> Click the row with Name = '<Charge Name>' to open its Detail view`
- **Observe**:
  - Charges table contains a row with Name = '<Charge Name>' and Charge Applies To = 'Savings Account'
  - Charge Detail: Charge Name
  - Charge Detail: Charge Applies To
  - Charge Detail: Charge Time Type
  - Charge Detail: Charge Calculation Type
  - Charge Detail: Amount
  - Charge Detail: Is Penalty
  - Charge Detail: Is Active
  - Charge Detail: Payment Mode

**Expected Change**: A new row appears in the Charges table with Name '<Charge Name>' and Charge Applies To 'Savings Account'. Opening the created charge's detail view shows Charge Time Type set to the selected savings-specific option (one of: Specified Due Date, Savings Activation, Withdrawal Fee, Annual Fee, Monthly Fee, Overdraft Fee), Charge Calculation Type equals the selected value, Amount equals the submitted amount, Payment Mode equals the selected payment mode, and the Is Penalty / Is Active flags reflect the chosen toggles.

---

### [TC-004] Profile icon/menu inaccessible when unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application home page while not logged in
2. 2. Click the top-right Profile Icon

**Original Expected Result:** Profile Icon and profile menu are not available: the Profile Icon is not visible in the top-right; no dropdown opens; 'Profile Settings' and 'Log Out' options are not present or accessible. The user remains on the public/unauthenticated page (no authenticated UI is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin -> Charges page (Charges listing)`
- **Observe**:
  - Charges table is visible with columns: Name, Charge Applies To, Charge Time Type, Charge Calculation Type, Amount, Currency, Payment Mode, Is Penalty, Is Active, Is Paid Derived
  - No existing row with Name '<Charge Name>'

**Post-Check**
- **Navigate To**: `Admin -> Charges page (Charges listing)`
- **Observe**:
  - Charges table rows including recently created entries
  - A row with Name '<Charge Name>' showing values for: Charge Applies To, Charge Time Type, Charge Calculation Type, Amount, Currency, Payment Mode, Is Penalty, Is Active

**Expected Change**: A new row with Name '<Charge Name>' appears in the Charges table with 'Charge Applies To' = 'Client', 'Charge Time Type' = '<Charge Time Type>', 'Charge Calculation Type' = '<Charge_Calculation_Type>', 'Currency' = '<Currency>', 'Amount' = '<Amount>', 'Payment Mode' = '<Payment_Mode>', and the 'Is Active' and 'Is Penalty' flags matching the selections made during creation.

---

### [TC-008] Rapid double-click Log Out
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Log in as a valid user
2. 2. Click the Profile Icon in the top-right corner
3. 3. Click the "Log Out" button
4. 4. Immediately click the "Log Out" button again

**Original Expected Result:** First click succeeds: authenticated session is terminated and the user is redirected to the login page. The immediate second click is ignored (no additional navigation or error shown) and only a single logout action takes effect.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin -> Charges (Charges listing page)`
- **Observe**:
  - Presence of the target charge row (identify by Name and at least one unique attribute such as Charge Applies To or Amount) — record the exact Name used for deletion
  - Total number of rows in the Charges table (or count of matching rows if a filter/search is applied)
  - If using pagination or filters, ensure filters are cleared or search for the recorded Name so the row is visible

**Post-Check**
- **Navigate To**: `Admin -> Charges (Charges listing page)`
- **Observe**:
  - Absence of the previously recorded charge Name/row in the Charges table
  - Total number of rows in the Charges table (or count of matching rows if a filter/search is applied)

**Expected Change**: The charge row identified by the recorded Name (and matching attributes) is no longer present in the Charges table. The total row count for Charges has decreased by one compared to the pre_check (or the count of matching rows is zero).

---

### [TC-009] Browser Back after Log Out should not return to protected page
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. From the protected page, click the Profile Icon
2. 2. Click the "Log Out" button
3. 3. Wait for redirect to the login page
4. 4. Press the browser Back button

**Original Expected Result:** Navigation back to the protected page is blocked: Auth_Guard redirects to the login page and the protected page is not displayed. The back navigation is effectively blocked and the login page is shown.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin -> Charges (Charges page / Charges table)`
- **Observe**:
  - Locate the charge row by Name (the charge to edit)
  - Charge Time Type column value for that charge
  - Amount column value for that charge
  - Is Penalty indicator/value for that charge
  - Is Active indicator/value for that charge

**Post-Check**
- **Navigate To**: `Admin -> Charges -> open the same Charge detail view (click the charge Name)`
- **Observe**:
  - Charge Name
  - Charge Time Type (on detail view)
  - Amount (on detail view)
  - Is Penalty (on detail view)
  - Is Active (on detail view)
  - Charges table row (verify reflected values in the listing)

**Expected Change**: The charge's Amount shows '<new Amount>' and Charge Time Type shows the selected '<Charge Time Type>' on the Charge detail view; any toggled Is Penalty and Is Active values reflect the changes. The updated Amount and Charge Time Type are also reflected in the Charges table listing for that charge, proving the change persisted.

---

### [TC-010] Log Out in one tab, then attempt Log Out in another tab (concurrent session edge)
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Tab A, click the Profile Icon
2. 2. In Tab A, click the "Log Out" button
3. 3. In Tab B, click the Profile Icon
4. 4. In Tab B, click the "Log Out" button

**Original Expected Result:** Logout in Tab A succeeds: Tab A is redirected to the login page and authentication token cleared. In Tab B, clicking "Log Out" succeeds in resulting in the login page (no error shown) but performs no additional session termination; Tab B is redirected to the login page as well.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Charges -> open the target Charge detail by clicking the Charge Name in the Charges table`
- **Observe**:
  - Charge Name
  - Charge Applies To
  - Charge Time Type
  - Amount
  - Is Penalty
  - Is Active

**Post-Check**
- **Navigate To**: `Charges -> open the same Charge detail by clicking the Charge Name in the Charges table (or refresh the detail view)`
- **Observe**:
  - Charge Name
  - Charge Applies To
  - Charge Time Type
  - Amount
  - Is Penalty
  - Is Active

**Expected Change**: On the Charge detail the Amount equals '<new Amount>' and Charge Time Type equals the selected Savings Account option '<Charge Time Type>'. The Is Penalty and Is Active flags reflect the toggles applied during edit. Charge Name and Charge Applies To remain unchanged.

---

### [TC-011] Profile menu and Profile Settings access when user is unauthenticated
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is logged out (if not, perform Log Out)
2. 2. Observe whether the Profile Icon is visible in the top-right corner
3. 3. In the browser address bar, manually navigate to the Profile Settings page URL and press Enter

**Original Expected Result:** Profile Icon is not visible when unauthenticated (no dropdown available). Direct navigation to the Profile Settings URL is blocked: Auth_Guard redirects to the login page and the Profile Settings page is not displayed.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Charges -> Charges table -> click the charge Name to open the Charge Detail view`
- **Observe**:
  - Charge Name
  - Charge Applies To
  - Amount
  - Payment Mode
  - Is Active
  - Last Modified Timestamp
  - Modified By

**Post-Check**
- **Navigate To**: `Charges -> Charges table -> (refresh listing) -> click the same charge Name to open the Charge Detail view`
- **Observe**:
  - Charge Name
  - Charge Applies To
  - Amount
  - Payment Mode
  - Is Active
  - Last Modified Timestamp
  - Modified By

**Expected Change**: Amount changed to <new Amount>; any other edited fields (e.g., Payment Mode) reflect the new selections; Charge Applies To remains 'Client'; Last Modified Timestamp is later than the pre_check timestamp and Modified By shows the acting user, indicating the edits were persisted in the backend.

---

### [TC-002] Log Out via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `partial`

**Coverage Note**: *Creation of the floating rate and its base-flag can be fully verified in-app. Automatic adjustment of linked loan products' effective interest rates can only be verified if one or more loan products are already linked to this floating rate (and their effective rates are recalculated/displayed). If no loan products are linked, that side-effect cannot be observed by this test and requires a separate cross-entity verification.*

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Log Out' in the dropdown

**Original Expected Result:** terminates authenticated session; clears authentication token; redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin -> Floating Rates page (Floating Rates listing)`
- **Observe**:
  - List of floating rates with columns: Floating Rate Name, Is Base Lending Rate, Is Active, Created By
  - Count of rows where Is Base Lending Rate = true (record current count)
  - Verify that no floating rate with the test name (<floating rate name>) exists prior to creation

**Post-Check**
- **Navigate To**: `Admin -> Floating Rates page (Floating Rates listing) and open the newly created floating rate detail`
- **Observe**:
  - Presence of a floating rate row with Floating Rate Name = <floating rate name>
  - Is Base Lending Rate flag set to true for that floating rate
  - Is Active flag value as set during creation (checked or unchecked)
  - In the floating rate detail, Rate Periods table contains a row with From Date = <from date>, Interest Rate = <interest rate percentage>, and Is Differential Rate = false
  - Count of rows where Is Base Lending Rate = true (should be 1 after creation)

**Expected Change**: A new floating rate with the specified name appears in the Floating Rates listing and in its detail view, the 'Is Base Lending Rate' flag is set. The Rate Periods table includes the specified From Date and Interest Rate with Is Differential Rate unchecked. There is at most one floating rate marked as base lending rate (any previously marked base is unset by the system). If loan products are linked to this floating rate, their effective interest rates should update per the new rate period (verification of linked loan product rate changes is conditional and may require navigating to those loan product details or loan accounts).

---

### [TC-003] Unauthenticated navigation to a protected page redirects to login
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <authenticated page URL> in the browser address bar and navigate to it

**Original Expected Result:** redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Floating Rates -> List; Loan Products -> Product Detail for product(s) expected to reference this floating rate`
- **Observe**:
  - Floating Rates list does NOT contain <floating rate name> (or note current presence if re-run)
  - For each loan product expected to be linked: current configured interest rate display and whether a Floating Rate linkage is shown (linked floating rate name or blank) — record the displayed interest rate value(s)

**Post-Check**
- **Navigate To**: `Floating Rates -> List -> Open the newly created <floating rate name> -> Rate Periods table; then Loan Products -> Product Detail for product(s) expected to reference this floating rate`
- **Observe**:
  - Floating Rates list contains <floating rate name>
  - Floating Rate detail shows Rate Periods table with two rows
  - Rate Period row 1 fields: From Date equals entered <from date>, Interest Rate equals entered <interest rate percentage>, Is Differential Rate is unchecked
  - Rate Period row 2 fields: From Date equals entered <from date>, Interest Rate equals entered <interest rate percentage>, Is Differential Rate is checked
  - For each linked loan product: the product detail shows the floating rate linkage to <floating rate name> (if product-level linkage exists) or the loan's effective interest rate calculation shows the floating rate as the source
  - For each linked loan product: the displayed effective interest rate (or the preview/calculated rate) matches the expected result based on the applicable Rate Period (absolute rate used for non-differential period; base lending rate ± differential percent applied for the differential period)

**Expected Change**: A new Floating Rate named <floating rate name> exists and its detail contains two Rate Period rows with the first row as an absolute rate (Is Differential Rate unchecked) and the second row as a differential rate (Is Differential Rate checked). Loan products that reference this floating rate reflect the floating rate linkage and their effective interest rates are updated according to the applicable Rate Period (absolute periods apply the listed rate; differential periods apply the base lending rate plus or minus the differential).

---

### [TC-005] Direct navigation to Profile Settings while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `partial`

**Coverage Note**: *The Floating Rate detail and its Rate Periods table are directly observable. Changes to already-approved/active loan accounts' calculated interest may be applied by scheduled background jobs (e.g., rate revaluation) and might not be immediate; verify product-level or loan-preview values if available. If linked loan recalculation is asynchronous, this verification confirms the rate period addition and immediate product-level linkage, not necessarily all downstream amortization recalculations.*

**Original Steps:**
1. 1. In the browser address bar, navigate to the Profile Settings page URL

**Original Expected Result:** Auth Guard blocks access: browser is redirected to the Login page; Profile Settings content is not displayed and no profile settings UI elements are visible.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Floating Rates -> <existing floating rate> (Detail view)`
- **Observe**:
  - rate periods table (each row shows From Date, Interest Rate, Is Differential Rate)
  - count of existing rate period rows
  - floating rate name
  - if shown: list of linked loan products or linked entities (product name, linkage indicator)
  - for one linked loan product (pick one if listed): displayed effective interest or note indicating floating rate is applied

**Post-Check**
- **Navigate To**: `Floating Rates -> <existing floating rate> (Detail view)`
- **Observe**:
  - rate periods table (each row shows From Date, Interest Rate, Is Differential Rate)
  - presence of a new Rate Period row with From Date = <from date>, Interest Rate = <interest rate percentage>, Is Differential Rate = <as set>
  - floating rate name (shows <updated floating rate name> if changed)
  - if shown: list of linked loan products (product name, linkage indicator)
  - for one linked loan product (same as pre-check): displayed effective interest or note indicating floating rate usage / updated effective rate for dates >= <from date>

**Expected Change**: The Floating Rate detail now includes a new Rate Period row with the specified From Date and Interest Rate and the configured Differential flag. If the floating rate name was edited, the detail header reflects the updated name. For loan products linked to this floating rate (if they are displayed), their effective interest metadata or preview reflects the application of the new rate period for applicable dates; full recalculation of active loans may be asynchronous and performed by scheduled jobs.

---

### [TC-002] Log Out via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Log Out' in the dropdown

**Original Expected Result:** terminates authenticated session; clears authentication token; redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin -> Delinquency Management -> Delinquency Ranges page`
- **Observe**:
  - current rows in Delinquency Ranges table (capture count)
  - presence of any row with Classification = <classification>
  - for any matching row, Minimum Age Days and Maximum Age Days values

**Post-Check**
- **Navigate To**: `Admin -> Delinquency Management -> Delinquency Ranges page`
- **Observe**:
  - rows in Delinquency Ranges table (capture count)
  - row with Classification = <classification>
  - Minimum Age Days cell value for that row
  - Maximum Age Days cell value for that row

**Expected Change**: A new row appears in the Delinquency Ranges table with Classification = <classification> and Minimum Age Days = <minimum age days>; the Maximum Age Days cell is blank indicating it applies to all days beyond the minimum.

---

### [TC-004] Profile icon/menu inaccessible when unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application home page while not logged in
2. 2. Click the top-right Profile Icon

**Original Expected Result:** Profile Icon and profile menu are not available: the Profile Icon is not visible in the top-right; no dropdown opens; 'Profile Settings' and 'Log Out' options are not present or accessible. The user remains on the public/unauthenticated page (no authenticated UI is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin -> Delinquency Management -> Delinquency Buckets page`
- **Observe**:
  - list of existing bucket names in the Delinquency Buckets table (confirm <bucket name> is not present)
  - availability of Linked Loan Products multi-select (shows loan products that can be linked)

**Post-Check**
- **Navigate To**: `Admin -> Delinquency Management -> Delinquency Buckets page`
- **Observe**:
  - a new row in the Delinquency Buckets table with Bucket Name = <bucket name>
  - the table row shows the configured ranges (first range: Minimum Age Days = <minimum age days 1>, Maximum Age Days = <maximum age days 1>; second range: Minimum Age Days = <minimum age days 2>, Maximum Age Days = blank/open-ended)
  - linked loan products are listed for the created bucket (matching the <linked loan products> selected during creation)
  - opening the created bucket's detail view shows the added ranges and the linked loan products in the detail

**Expected Change**: A new delinquency bucket named <bucket name> appears in the Delinquency Buckets table and in its detail view; it contains the two ranges entered (first with the specified min and max, second with the specified min and no max indicating open-ended) and lists the selected linked loan products exactly as chosen during creation.

---

### [TC-003] Unauthenticated navigation to a protected page redirects to login
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <authenticated page URL> in the browser address bar and navigate to it

**Original Expected Result:** redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Detail -> Accounts tab -> Loan Accounts sub-tab`
- **Observe**:
  - list of loan accounts rows with columns: Account No., Product Name, Status (and Principal if shown)
  - confirm there is no existing loan row with Product Name = <product> and Principal = <principal> in status 'Submitted and Pending Approval'

**Post-Check**
- **Navigate To**: `Client Detail -> Accounts tab -> Loan Accounts sub-tab; if Loan Detail page opened by the wizard, also verify from Loan Detail header`
- **Observe**:
  - a new loan row present in the Loan Accounts list with Product Name = <product>, Principal = <principal> (or matching account details), and Status = 'Submitted and Pending Approval'
  - open the new loan row to view the Loan Detail page and observe the header shows the generated Loan Account No., Client Name, and a status badge 'Submitted and Pending Approval' (yellow)

**Expected Change**: A new loan account for the client is created with Product = <product> and Principal = <principal> and appears in the client's Loan Accounts list with status 'Submitted and Pending Approval' (yellow). The Loan Detail page for that account shows the 'Submitted and Pending Approval' status badge and a generated loan account number.

---

### [TC-004] Profile icon/menu inaccessible when unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application home page while not logged in
2. 2. Click the top-right Profile Icon

**Original Expected Result:** Profile Icon and profile menu are not available: the Profile Icon is not visible in the top-right; no dropdown opens; 'Profile Settings' and 'Log Out' options are not present or accessible. The user remains on the public/unauthenticated page (no authenticated UI is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Detail -> Loans tab`
- **Observe**:
  - list of loan applications for the client (with statuses)
  - if any 'Submitted and Pending Approval' application exists, open the most recent and observe its Charges section (record current charge count and listed charge names/amounts)

**Post-Check**
- **Navigate To**: `Client Detail -> Loans tab -> Open the newly created loan application (the 'Submitted and Pending Approval' entry with the most recent Submitted On date) -> Charges section`
- **Observe**:
  - presence of a charge with name '<charge_name>'
  - presence of a charge amount equal to '<amount>' for that charge
  - displayed due date equals '<due_date>' (if a due date was entered)
  - charge status/paid indicator (e.g., 'Due' or 'Outstanding')
  - total number of charges on the application (should be pre-check count + 1)

**Expected Change**: A charge row with name '<charge_name>' and amount '<amount>' appears in the Charges section of the newly created loan application (status 'Submitted and Pending Approval' if the application was submitted). If a due date was provided it is shown on the charge. The total number of charges for the application has increased by one compared to the pre-check.

---

### [TC-005] Direct navigation to Profile Settings while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Profile Settings page URL

**Original Expected Result:** Auth Guard blocks access: browser is redirected to the Login page; Profile Settings content is not displayed and no profile settings UI elements are visible.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Detail page -> Loans tab`
- **Observe**:
  - count of loans listed for the client
  - most recent loan entry: loan account number (if present)
  - most recent loan entry: status (e.g., Submitted and Pending Approval, Approved, Active)
  - most recent loan entry: Terms shown (Repayment Strategy, Amortization) if available

**Post-Check**
- **Navigate To**: `Loan Detail page for the newly created loan (if the Loan Detail did not open automatically after submission, go to Client Detail page -> Loans tab and open the most recent loan)`
- **Observe**:
  - loan account number
  - loan status badge
  - Terms section: Repayment Strategy
  - Terms section: Amortization

**Expected Change**: A new loan record exists for the client (new loan account number present) with status 'Submitted and Pending Approval' (or the expected post-submission status). In the Terms section the Repayment Strategy is set to <repayment_strategy> and the Amortization is set to <amortization> (these values match what was selected in Step 2 of the wizard).

---

### [TC-006] Invoking Log Out endpoint while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Log Out endpoint/URL that the 'Log Out' button would call

**Original Expected Result:** Precondition prevents logout action: browser is redirected to the Login page; no logout success behavior occurs (no authenticated session existed and no session changes happen).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page for the loan in Submitted and Pending Approval state`
- **Observe**:
  - status badge shows 'Submitted and Pending Approval' (yellow)
  - Approved On Date field is empty or not set
  - Approved Amount field is empty or not set
  - Expected Disbursement Date field is empty or not set

**Post-Check**
- **Navigate To**: `Loans -> Approved / Loans Awaiting Disbursal listing and re-open the Loan Detail page for the same loan`
- **Observe**:
  - status badge shows 'Approved' (blue) on the Loan Detail page
  - Approved On Date displays the entered <approved_on_date>
  - Approved Amount displays the entered <approved_amount>
  - Expected Disbursement Date displays the entered <expected_disbursement_date> if provided
  - Loan no longer appears in the 'Pending Approval' or 'Loans Pending Approval' listing
  - Loan appears in 'Approved' or 'Loans Awaiting Disbursal' listing (if the application workflow places approved loans there)

**Expected Change**: The loan's status changed from 'Submitted and Pending Approval' (yellow) to 'Approved' (blue); the Approved On Date equals the entered <approved_on_date>; the Approved Amount equals the entered <approved_amount>; the Expected Disbursement Date (when provided) is recorded as <expected_disbursement_date>; the loan is removed from Pending Approval listings and appears in Approved/Awaiting Disbursal listings.

---

### [TC-007] Using browser Back after Log Out does not return to authenticated pages
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the Login page
2. 2. Enter <valid credentials> in the Username/Email field
3. 3. Enter <valid password> in the Password field
4. 4. Click the Login button
5. 5. Navigate to a protected page (e.g., Dashboard) while logged in
6. 6. Click the Profile Icon
7. 7. Click the 'Log Out' button in the profile menu
8. 8. After the application redirects to the Login page, click the browser Back button to return to the previously viewed protected page

**Original Expected Result:** After logout the protected page remains inaccessible: Auth Guard immediately redirects to the Login page; protected page content is not displayed; the user remains logged out (authentication token/session cleared).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page for the loan in Submitted and Pending Approval state`
- **Observe**:
  - loan account number and client name in header
  - status badge showing 'Submitted and Pending Approval' (yellow)
  - available state action buttons include: Approve, Reject, Withdraw, Delete
  - recent activity/audit trail does not yet contain a rejection entry for this loan

**Post-Check**
- **Navigate To**: `Loan Detail page for the same loan (refresh or reopen the page)`
- **Observe**:
  - loan account number and client name in header (same as pre-check)
  - status badge showing 'Rejected' (red or designated rejected color)
  - absence of the 'Submitted and Pending Approval' badge
  - state action buttons appropriate for Rejected status (Approve/Reject not present)
  - activity/audit trail contains a new entry indicating the loan was rejected with timestamp and acting user

**Expected Change**: The loan's status has changed from 'Submitted and Pending Approval' to 'Rejected'; the 'Submitted and Pending Approval' badge is no longer displayed; Pending-Approval actions (Approve/Reject) are no longer available; and a rejection entry is recorded in the activity/audit trail with the rejecting user and timestamp.

---

### [TC-008] Rapid double-click Log Out
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Log in as a valid user
2. 2. Click the Profile Icon in the top-right corner
3. 3. Click the "Log Out" button
4. 4. Immediately click the "Log Out" button again

**Original Expected Result:** First click succeeds: authenticated session is terminated and the user is redirected to the login page. The immediate second click is ignored (no additional navigation or error shown) and only a single logout action takes effect.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page for the target loan (use the loan account opened in preconditions)`
- **Observe**:
  - status badge text (expected: 'Submitted and Pending Approval' or equivalent pending status)
  - presence of 'Withdraw' action in the state action bar
  - loan account number and client name (to confirm correct loan)

**Post-Check**
- **Navigate To**: `Loan Detail page for the same loan (refresh or re-open the page to ensure backend state is loaded)`
- **Observe**:
  - status badge text (expected: 'Withdrawn' or equivalent withdrawn status)
  - absence of 'Submitted and Pending Approval' status badge
  - absence of 'Withdraw' action in the state action bar
  - Transactions or Audit Trails tab shows an entry indicating the withdrawal action (Withdrawal / Status change) or a maker/checker record if enabled

**Expected Change**: The loan's status changed from 'Submitted and Pending Approval' to 'Withdrawn' (or equivalent withdrawn status); the 'Withdraw' action is no longer available on the state action bar, and a corresponding withdrawal entry appears in Transactions/Audit Trails indicating the withdrawal was processed.

---

### [TC-009] Browser Back after Log Out should not return to protected page
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. From the protected page, click the Profile Icon
2. 2. Click the "Log Out" button
3. 3. Wait for redirect to the login page
4. 4. Press the browser Back button

**Original Expected Result:** Navigation back to the protected page is blocked: Auth_Guard redirects to the login page and the protected page is not displayed. The back navigation is effectively blocked and the login page is shown.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Detail page -> Accounts tab -> Loans sub-tab ( locate the specific loan entry )`
- **Observe**:
  - loan entry with Loan Account Number / Identifier (e.g., the target loan)
  - status column showing 'Submitted and Pending Approval' for that loan
  - client's loans count includes the target loan

**Post-Check**
- **Navigate To**: `Client Detail page -> Accounts tab -> Loans sub-tab; additionally, attempt direct access to the deleted loan's Loan Detail URL and use Global Search for the loan identifier`
- **Observe**:
  - the loan entry with the previously observed Loan Account Number / Identifier is absent from the loans list
  - client's loans count is reduced by one compared to pre_check
  - Global Search for the loan identifier returns 'No results found' or does not list the loan
  - direct navigation to the deleted loan's detail URL returns 'Not found', redirects to Client Detail, or shows an explicit 'Loan not found' message

**Expected Change**: The deleted loan no longer appears in the client's Loans list and the client's loan count decreased by one; attempts to search for or directly open the deleted loan's detail page return no results or a not-found/redirect response.

---

### [TC-010] Log Out in one tab, then attempt Log Out in another tab (concurrent session edge)
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Tab A, click the Profile Icon
2. 2. In Tab A, click the "Log Out" button
3. 3. In Tab B, click the Profile Icon
4. 4. In Tab B, click the "Log Out" button

**Original Expected Result:** Logout in Tab A succeeds: Tab A is redirected to the login page and authentication token cleared. In Tab B, clicking "Log Out" succeeds in resulting in the login page (no error shown) but performs no additional session termination; Tab B is redirected to the login page as well.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page for the Approved loan`
- **Observe**:
  - status badge (expected 'Approved')
  - loan balance / outstanding (should reflect pre-disbursement state)
  - Transactions tab: latest transaction (if any) and transaction list
  - Repayment Schedule tab: summary (total paid, total outstanding, total overdue) and schedule rows

**Post-Check**
- **Navigate To**: `Loan Detail page -> Header, Transactions tab, Repayment Schedule tab. If Disburse to Savings was selected: Linked Savings Account Detail page`
- **Observe**:
  - status badge
  - Transactions tab: presence of a new Disbursement transaction with Disbursed On Date = <disbursed_on_date>, Amount = <transaction_amount>, Payment Type = <payment_type>, and any provided payment details visible
  - loan balance / outstanding updated to reflect the disbursement (principal outstanding equals expected amount after disbursement)
  - Repayment Schedule: installments populated/updated with outstanding amounts and status indicators consistent with an Active loan
  - If Disburse to Savings selected: Linked Savings Account Transactions: a deposit/credit transaction for <transaction_amount> on <disbursed_on_date> and updated available balance

**Expected Change**: Status badge changes from 'Approved' to 'Active' (green). A Disbursement transaction is recorded dated <disbursed_on_date> for <transaction_amount> with the selected Payment Type and any provided payment details. The loan's outstanding/principal balance and repayment schedule reflect the disbursement (installments populated and total outstanding increased to include the disbursed principal as applicable). If 'Disburse to Savings' was toggled, the client's linked savings account shows a corresponding deposit/credit transaction for the disbursed amount and its available balance increases by that amount.

---

### [TC-011] Profile menu and Profile Settings access when user is unauthenticated
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is logged out (if not, perform Log Out)
2. 2. Observe whether the Profile Icon is visible in the top-right corner
3. 3. In the browser address bar, manually navigate to the Profile Settings page URL and press Enter

**Original Expected Result:** Profile Icon is not visible when unauthenticated (no dropdown available). Direct navigation to the Profile Settings URL is blocked: Auth_Guard redirects to the login page and the Profile Settings page is not displayed.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page for the target loan (currently in Approved state)`
- **Observe**:
  - status badge text and color (should read 'Approved' and be blue)
  - available action buttons in the state action bar (e.g., Disburse, Undo Approval)

**Post-Check**
- **Navigate To**: `Loan Detail page for the same loan (refresh if needed / reopen detail)`
- **Observe**:
  - status badge text and color
  - available action buttons in the state action bar

**Expected Change**: Status badge changes from 'Approved' (blue) to 'Submitted and Pending Approval' (yellow). Action bar updates to show Pending-Approval actions (e.g., Approve, Reject, Withdraw, Delete) and no longer shows Approved-only actions such as Disburse or Undo Approval.

---

### [TC-012] Move a code value up in ordering
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the Code Values Editor for <Code List Name>, click Move Up on the row for <entry A>

**Original Expected Result:** moves entry up in ordering and <entry A> is now displayed above the previous item in the list ordering

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page for the loan under test`
- **Observe**:
  - status badge (expected 'Active')
  - loan balance / total outstanding amount (greater than 0)
  - total paid amount
  - repayment schedule (installment rows showing principal/interest/fees/penalties due and paid status)
  - Transactions table - most recent entry (Date, Type, Amount, Payment Type) and transaction count

**Post-Check**
- **Navigate To**: `Loan Detail page for the same loan`
- **Observe**:
  - status badge
  - loan balance / total outstanding amount
  - total paid amount
  - repayment schedule (installment rows and their paid statuses)
  - Transactions table - most recent entry (Date, Type, Amount, Payment Type) and transaction count

**Expected Change**: After confirming the full repayment: the status badge is 'Closed obligations met' (was 'Active' in pre-check); loan balance and total outstanding become 0.00; Total Paid increases by the full settlement amount; all repayment schedule installments are marked as paid (no outstanding amounts); a new Transactions table entry exists with Type 'Repayment', Amount equal to <amount_due>, Transaction Date equal to <transaction_date>, and Payment Type equal to <payment_type>; Transactions table row count increased by one.

---

### [TC-013] Move a code value down in ordering
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the Code Values Editor for <Code List Name>, click Move Down on the row for <entry B>

**Original Expected Result:** moves entry down in ordering and <entry B> is now displayed below the previous item in the list ordering

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page -> Charges tab (and verify Summary tab totals)`
- **Observe**:
  - Charges table rows with columns: Charge Name, Amount, Due Date, Paid, Waived, Outstanding
  - The interest-related charge row(s) and their current Outstanding and Waived amounts
  - Loan Summary: total outstanding amount (principal + interest + fees + penalties)
  - Repayment Schedule: interest due for upcoming/installment rows (optional to note pre-change values)
  - Transactions tab: absence of a recent 'Waive Interest' transaction for the intended amount

**Post-Check**
- **Navigate To**: `Loan Detail page -> Charges tab, Summary tab, and Transactions tab`
- **Observe**:
  - Charges table interest row shows increased 'Waived' amount and reduced 'Outstanding' amount
  - Loan Summary shows total outstanding reduced by the waived interest amount
  - Repayment Schedule reflects reduced interest due (if waiver applied to scheduled installments)
  - Transactions tab (or Audit/Activity) shows an entry for 'Waive Interest' (or similar) with the waived amount and timestamp
  - Charge history/Notes (if present) documents the waiver action

**Expected Change**: The interest charge's 'Waived' column increases by the waived interest amount and its 'Outstanding' decreases by the same amount; the Loan Summary's total outstanding reduces by the waived interest amount; a 'Waive Interest' transaction or audit entry is present in Transactions/Activity documenting the waiver.

---

### [TC-014] Open Create Data Table form from Manage Data Tables
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Manage Data Tables
2. 2. Click Create Data Table (Create_Data_Table action)

**Original Expected Result:** Create_Data_Table form opens and the Create Data Table form is displayed with fields Data Table Name, Application Table Name, Multi Row, and Column Definitions

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page for the loan used in the test (open the same loan account)`
- **Observe**:
  - status badge (expected: 'Active')
  - loan outstanding balance (numeric value)
  - Transactions table - recent entries (no 'Write Off' entry yet)
  - Repayment Schedule - installment statuses and outstanding amounts (shows unpaid/overdue installments)

**Post-Check**
- **Navigate To**: `Loan Detail page for the same loan (refresh if necessary)`
- **Observe**:
  - status badge (expected: 'Written Off' and red)
  - loan outstanding balance (expected: cleared or clearly marked as written off)
  - Transactions table - recent entries (contains a 'Write Off' transaction with the write-off amount and correct date/user)
  - Repayment Schedule - installment statuses and outstanding amounts (previously outstanding installments are marked as waived/closed/written off)

**Expected Change**: The loan status changed from 'Active' to 'Written Off' (red); a 'Write Off' transaction exists matching the pre-check outstanding amount; the loan outstanding balance is cleared or marked as written-off and outstanding installments are updated to reflect the write-off.

---

### [TC-015] Open data table definition editor via Edit_Data_Table row action
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Manage Data Tables
2. 2. Click Edit for the <Data_Table_Name> row

**Original Expected Result:** opens data table definition editor and the data table definition editor for <Data_Table_Name> is displayed

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page for the loan in Active state (open the loan referenced in the core test case)`
- **Observe**:
  - status badge (text: 'Active', color: green)
  - loan account number
  - loan balance / total outstanding amount
  - available action buttons (e.g., Make Repayment, Waive Interest, Write Off) in the state action bar
  - Repayment Schedule tab -> outstanding installment rows and their statuses

**Post-Check**
- **Navigate To**: `Loan Detail page for the same loan (refresh or re-open the detail page)`
- **Observe**:
  - status badge (text: 'Closed', color: gray)
  - loan account number (same as pre-check)
  - loan balance / total outstanding amount
  - available action buttons (state actions) — verify Close/Active-only actions are no longer present or are disabled
  - Repayment Schedule tab -> outstanding installment rows (should show no outstanding amounts)
  - Transactions tab -> latest transaction(s) showing closing/settlement entry and Closure Date recorded in summary

**Expected Change**: The loan's status badge changes from 'Active' (green) to 'Closed' (gray). The loan account shows the same account number, total outstanding amount is zero (no remaining due) and repayment schedule shows no outstanding installments; Active-state actions (Make Repayment, Waive Interest, etc.) are no longer available and a closure/settlement transaction and closure date appear in the Transactions/summary.

---

### [TC-016] Delete a custom data table with confirmation
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Manage Data Tables
2. 2. Click Delete for the <Data_Table_Name> row
3. 3. Click Confirm on the deletion confirmation dialog

**Original Expected Result:** deletes custom data table and the row for <Data_Table_Name> is no longer visible in the Manage Data Tables list

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page for the loan in Active state (open the same loan used in the test)`
- **Observe**:
  - Loan status badge (e.g., 'Active')
  - Reschedule requests section / Requests list / Activity feed (verify there is no existing reschedule request matching the planned Reschedule From Date and Adjusted Due Date)
  - Repayment Schedule (note current due dates for reference)

**Post-Check**
- **Navigate To**: `Loan Detail page for the loan in Active state (refresh the page or navigate back to ensure backend state is loaded)`
- **Observe**:
  - Reschedule requests section / Requests list / Activity feed entry for the new reschedule request
  - Visible fields on the new request: 'Reschedule From Date', 'Adjusted Due Date', 'Reason', 'Requesting User' (or maker), and 'Requested On' timestamp
  - Request status badge or processing result showing 'Pending Approval' (or equivalent pending state)
  - Loan status badge remains 'Active' (reschedule request does not change loan operational status before approval)
  - Repayment Schedule still shows original due dates (optional: indicates change only after approval)

**Expected Change**: A new reschedule request entry appears in the loan's Reschedule requests / Requests list with the provided Reschedule From Date, Adjusted Due Date, and Reason; the entry shows the requesting user's name and a status of 'Pending Approval'. The loan's status remains 'Active' and repayment schedule changes are not applied until the reschedule request is approved.

---

### [TC-017] Submit Create Data Table form with columns (Create)
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Create Data Table form, enter Data Table Name = <data table name>
2. 2. Select Application Table Name = <application table> from the dropdown
3. 3. Optionally check Multi Row
4. 4. Click Add Row in Column Definitions, then for the new column enter Name = <column name>, Type = <column type>, set Length/Is Mandatory/Is Unique as needed
5. 5. Click Create

**Original Expected Result:** New row appears in Manage Data Tables with the entered Data Table Name and Application Table Name and the Create Data Table form closes

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page -> Transactions tab`
- **Observe**:
  - count of transaction rows
  - most recent transaction: {type, date, amount}
  - loan balance / total outstanding
  - repayment schedule summary (next due amount, total outstanding) and loan status badge

**Post-Check**
- **Navigate To**: `Loan Detail page -> Transactions tab`
- **Observe**:
  - count of transaction rows
  - new/latest transaction: {type, date, amount, payment type}
  - loan balance / total outstanding
  - repayment schedule summary (next due amount, total outstanding) and loan status badge

**Expected Change**: Transaction count increased by 1 and the Transactions table contains a new row for the prepayment with Type = 'Prepayment' (or labeled equivalent), Transaction Date = submitted date, and Amount = submitted prepayment amount. The loan balance / total outstanding decreased by the prepayment amount (or to zero if the prepayment fully settles the loan). The running balance shown on the new transaction row reflects the decreased outstanding. Loan status remains 'Active' unless the prepayment fully repays the loan, in which case the status changes to 'Closed'.

---

### [TC-018] Cancel Create Data Table form (Cancel)
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Create Data Table form, click Cancel

**Original Expected Result:** closes form without creating and the Create Data Table form is closed with no new row added to Manage Data Tables

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page for the target loan (Summary tab)`
- **Observe**:
  - status badge showing 'Active'
  - outstanding balance / loan balance
  - Repayment Schedule -> count of upcoming installments and their due dates
  - Transactions tab -> most recent transaction entries (type, date, amount)
  - Activity feed / Audit Trails for the loan -> ensure no existing 'Foreclosure' entry for this loan

**Post-Check**
- **Navigate To**: `Loan Detail page for the same loan (Summary tab), then Transactions tab and Activity feed / Audit Trails`
- **Observe**:
  - status badge (expect not to be 'Active')
  - outstanding balance / loan balance
  - Repayment Schedule -> future installments (expect cancelled/removed or marked as settled)
  - Transactions tab -> presence of a transaction entry with type 'Foreclosure' or 'Settlement' including date, amount and payment details
  - Activity feed / Audit Trails -> an entry recording the Foreclosure action with maker's username and timestamp

**Expected Change**: Loan status transitions from 'Active' to a non-active end state (e.g., 'Closed' or 'Foreclosed'); a foreclosure/settlement transaction appears in Transactions dated at the action time with the foreclosure amount; outstanding balance is reduced accordingly (typically to zero or to the post-foreclosure outstanding amount); future installments in the Repayment Schedule are cancelled or marked settled; Activity/Audit Trail contains a Foreclosure entry referencing the action and user.

---

### [TC-019] Approve an Audit Trail entry when maker-checker is enabled and Processing Result is Pending
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Audit Trails
2. 2. Locate the audit row for <Action_Name> with Processing Result = Pending
3. 3. Click Approve for that audit row

**Original Expected Result:** sets Processing Result to Approved and the Processing Result column for the selected audit row displays 'Approved'

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page for the loan (open the same loan used in the test case)`
- **Observe**:
  - status badge (expected 'Active')
  - outstanding principal balance (numeric value)
  - transactions table (most recent entries: date, type, amount)
  - loan activity log / recent activity entry
  - repayment schedule summary (total outstanding, number of unpaid installments)

**Post-Check**
- **Navigate To**: `Loan Detail page for the loan (reload or navigate back to ensure backend state is shown)`
- **Observe**:
  - status badge (new value indicating charge-off / written off state)
  - outstanding principal balance (numeric value)
  - transactions table (most recent entries: presence of a Charge Off / Write Off transaction)
  - loan activity log / recent activity entry (entry describing charge off with user and timestamp)
  - repayment schedule summary (total outstanding and statuses of remaining installments)

**Expected Change**: The loan status is no longer 'Active' and is displayed as a charge-off state (e.g., 'Written Off' or equivalent); the outstanding principal balance is reduced/adjusted to reflect the charge off (typically zeroed or moved to charged-off amount per product rules); a new transaction appears in the Transactions table recording the charge off (type 'Charge Off' or 'Write Off', amount, date); the Loan activity log contains an entry describing the charge off action (user, date, amount, reason); the repayment schedule and total outstanding reflect that remaining unpaid principal has been written off.

---

### [TC-020] Reject an Audit Trail entry with an optional rejection reason
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Audit Trails
2. 2. Locate the audit row for <Action_Name> with Processing Result = Pending
3. 3. Click Reject for that audit row
4. 4. Enter <rejection reason> in the Rejection_Reason field (optional) and click Confirm

**Original Expected Result:** sets Processing Result to Rejected and the Processing Result column for the selected audit row displays 'Rejected'

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail page for the loan in Active state`
- **Observe**:
  - loan account number
  - loan status badge
  - assigned loan officer (header)

**Post-Check**
- **Navigate To**: `Loan Detail page for the same loan (refresh or reopen the page)`
- **Observe**:
  - loan account number
  - loan status badge
  - assigned loan officer (header)

**Expected Change**: The assigned loan officer shown in the Loan Detail header is <loan_officer>. If a different officer was present before, it is replaced by <loan_officer>; the loan status remains Active.

---

### [TC-021] Submit Create Data Table form with ALL required fields empty
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Create Data Table' action to open Create_Data_Table_Form
2. 2. Leave the Data Table Name field blank
3. 3. Leave the Application Table Name dropdown unselected
4. 4. Do not add any Column Definitions items
5. 5. Click the Create button

**Original Expected Result:** Form does not submit; Data table is not created. Inline validation errors appear: Data Table Name field displays an error indicating it is required; Application Table Name field displays an error indicating it is required.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Loan Detail -> Transactions tab`
- **Observe**:
  - target transaction is present and identifiable (Transaction ID or unique combination of Date, Amount, Type)
  - Transactions table row for the target transaction shows Amount, Date, Type, and resulting Outstanding Balance
  - Loan Detail -> Summary: values for 'Total Paid', 'Total Outstanding', and 'Loan Balance'
  - Loan Detail -> Repayment Schedule: installment(s) affected by the target transaction showing Paid/Outstanding amounts and status

**Post-Check**
- **Navigate To**: `Loan Detail -> Transactions tab; then Loan Detail -> Summary; then Loan Detail -> Repayment Schedule`
- **Observe**:
  - target transaction identifier (Transaction ID or Date+Amount+Type) is not present in the Transactions table
  - Transactions table row count decreased by one OR shows a reversal entry indicating the undo
  - Loan Detail -> Summary: updated values for 'Total Paid', 'Total Outstanding', and 'Loan Balance'
  - Loan Detail -> Repayment Schedule: affected installment(s) reflect reverted payment (Paid amount decreased and Outstanding amount increased) or reflect the reversal

**Expected Change**: The selected transaction no longer appears as a posted transaction in the Transactions tab. Corresponding loan totals are updated: 'Total Paid' decreases by the transaction amount and 'Total Outstanding'/'Loan Balance' increase by the same amount. Affected repayment schedule installment(s) show amounts reverted (paid decreased, outstanding increased). If the system records a reversal entry instead of deleting the original, the original posted transaction will not be reflected as an active payment and the Summary/Repayment Schedule will reflect the reversal.

---

### [TC-001] Open Profile Settings via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Profile Settings' in the dropdown

**Original Expected Result:** navigates to Profile Settings page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Detail -> Savings Accounts tab`
- **Observe**:
  - List of savings accounts for the client (rows, with Product Name and Status columns)
  - Count of accounts with status 'Submitted and Pending Approval'
  - Absence of an account row with Product Name = <product> AND Submitted On = <Submitted On date> in status 'Submitted and Pending Approval'

**Post-Check**
- **Navigate To**: `Client Detail -> Savings Accounts tab; open the newly created savings account detail page`
- **Observe**:
  - A new row in the Savings Accounts list for Product Name = <product>
  - Status column shows 'Submitted and Pending Approval' (yellow badge) for this new row
  - Clickable account number link for the new savings account (opens detail page)
  - On the Savings Account detail page: Product Name = <product>
  - On the Savings Account detail page: Field Officer = <Field Officer>
  - On the Savings Account detail page: Submitted On = <Submitted On date>
  - On the Savings Account detail page: Minimum Opening Balance = <minimum opening amount>
  - On the Savings Account detail page: Allow Overdraft = <on|off>
  - On the Savings Account detail page: Charges section includes <charge> if it was added

**Expected Change**: A new savings account record is created and appears in the client's Savings Accounts list with status 'Submitted and Pending Approval'. The account detail page for that record shows Product Name = <product>, Field Officer = <Field Officer>, Submitted On = <Submitted On date>, Minimum Opening Balance = <minimum opening amount>, Allow Overdraft = <on|off>, and lists the added charge <charge> if provided.

---

### [TC-002] Log Out via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Log Out' in the dropdown

**Original Expected Result:** terminates authenticated session; clears authentication token; redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Account Detail page for the submitted account`
- **Observe**:
  - status badge text (expected: 'Submitted and Pending Approval')
  - available action buttons (expected to include 'Approve')
  - account number and client name (to ensure correct account)

**Post-Check**
- **Navigate To**: `Savings Account Detail page for the same account (or refresh the detail page)`
- **Observe**:
  - status badge text (expected: 'Approved')
  - available action buttons (expected to include 'Activate' and not include 'Approve')
  - account number and client name (unchanged)

**Expected Change**: Status badge changed from 'Submitted and Pending Approval' to 'Approved'. The 'Approve' action is no longer present and the 'Activate' action is available on the account detail page, confirming the backend status update.

---

### [TC-003] Unauthenticated navigation to a protected page redirects to login
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <authenticated page URL> in the browser address bar and navigate to it

**Original Expected Result:** redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Account Detail page for the submitted application`
- **Observe**:
  - status badge equals 'Submitted and Pending Approval'
  - action button 'Reject' is present
  - no rejection indicator or rejection reason displayed

**Post-Check**
- **Navigate To**: `Savings Account Detail page for the same account (refresh or reopen)`
- **Observe**:
  - status badge equals 'Rejected'
  - rejection indicator or rejection reason is displayed on the detail page
  - approval-related action buttons (e.g., 'Approve', 'Activate') are not available; 'Reject' action is no longer shown

**Expected Change**: The account status changed from 'Submitted and Pending Approval' to 'Rejected'; a visible rejection indicator/reason appears on the detail page; approval actions are removed from the UI, and an audit trail entry records the Reject action with Processing Result 'Rejected' attributed to the acting user.

---

### [TC-004] Profile icon/menu inaccessible when unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application home page while not logged in
2. 2. Click the top-right Profile Icon

**Original Expected Result:** Profile Icon and profile menu are not available: the Profile Icon is not visible in the top-right; no dropdown opens; 'Profile Settings' and 'Log Out' options are not present or accessible. The user remains on the public/unauthenticated page (no authenticated UI is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Account Detail page for the submitted application (from Client -> Accounts or Global Search)`
- **Observe**:
  - status badge showing 'Submitted and Pending Approval' (yellow)
  - presence of action buttons appropriate to Pending status (Approve, Reject, Withdraw Application)
  - account listed under the client's Accounts tab with status 'Submitted and Pending Approval'
  - no transactions present in Transactions tab (optional pre-condition)

**Post-Check**
- **Navigate To**: `Savings Account Detail page for the same application (from Client -> Accounts or Global Search)`
- **Observe**:
  - status badge showing 'Withdrawn' (orange/Withdrawn chip)
  - absence of action buttons for Pending status (Approve, Withdraw Application) — action buttons for Pending should no longer appear
  - account listed under the client's Accounts tab with status 'Withdrawn'
  - Transactions tab unchanged (no deposit transactions were posted as part of withdrawal)

**Expected Change**: The account's status changes from 'Submitted and Pending Approval' to 'Withdrawn'; pending-action buttons (Approve, Withdraw Application) are removed; the client's Accounts listing and the Savings Account Detail page reflect the 'Withdrawn' status.

---

### [TC-005] Direct navigation to Profile Settings while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Profile Settings page URL

**Original Expected Result:** Auth Guard blocks access: browser is redirected to the Login page; Profile Settings content is not displayed and no profile settings UI elements are visible.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Account Detail page for <the account>`
- **Observe**:
  - status badge
  - status text (should display 'Approved')
  - account number

**Post-Check**
- **Navigate To**: `Savings Account Detail page for <the account> and Client -> Savings Accounts tab (Accounts listing)`
- **Observe**:
  - status badge
  - status text (should display 'Active')
  - status column for the account in the Savings Accounts listing

**Expected Change**: The savings account status changes from 'Approved' to 'Active'; the detail page status badge displays 'Active'; the account's status in the client's Savings Accounts listing shows 'Active' (and the account appears under Active filters).

---

### [TC-006] Invoking Log Out endpoint while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Log Out endpoint/URL that the 'Log Out' button would call

**Original Expected Result:** Precondition prevents logout action: browser is redirected to the Login page; no logout success behavior occurs (no authenticated session existed and no session changes happen).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Account Detail page for the account (or Client Detail -> Savings Accounts tab -> open the savings account)`
- **Observe**:
  - status badge text (expected: 'Approved')
  - status badge color (expected: green or the UI's Approved color)
  - available action buttons (expected to include 'Activate' and 'Undo Approval')

**Post-Check**
- **Navigate To**: `Savings Account Detail page for the account (or Client Detail -> Savings Accounts tab -> open the savings account)`
- **Observe**:
  - status badge text
  - status badge color
  - available action buttons on the account detail page
  - account status as shown in the Client's Savings Accounts list/table

**Expected Change**: The status badge text changes from 'Approved' to 'Submitted and Pending Approval' and its color changes from the Approved color to the Submitted/Pending Approval color; the action buttons update from containing 'Undo Approval'/'Activate' to containing 'Approve' (and other Pending actions such as 'Reject' or 'Withdraw') and 'Undo Approval' is no longer present; the account's status in the Client's Savings Accounts list also updates to 'Submitted and Pending Approval'.

---

### [TC-007] Using browser Back after Log Out does not return to authenticated pages
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the Login page
2. 2. Enter <valid credentials> in the Username/Email field
3. 3. Enter <valid password> in the Password field
4. 4. Click the Login button
5. 5. Navigate to a protected page (e.g., Dashboard) while logged in
6. 6. Click the Profile Icon
7. 7. Click the 'Log Out' button in the profile menu
8. 8. After the application redirects to the Login page, click the browser Back button to return to the previously viewed protected page

**Original Expected Result:** After logout the protected page remains inaccessible: Auth Guard immediately redirects to the Login page; protected page content is not displayed; the user remains logged out (authentication token/session cleared).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Account Detail page -> Transactions tab (and Summary card)`
- **Observe**:
  - account balance on the Summary card (Account balance)
  - available balance on the Summary card (Available balance)
  - transactions table top row fields: Type, Amount, Transaction Date
  - transactions table row count

**Post-Check**
- **Navigate To**: `Savings Account Detail page -> Transactions tab (and Summary card)`
- **Observe**:
  - account balance on the Summary card (Account balance)
  - available balance on the Summary card (Available balance)
  - transactions table top row fields: Type, Amount, Transaction Date
  - transactions table row count

**Expected Change**: A new transaction appears as the top (most recent) row in the Transactions table with Type 'Deposit', Amount equal to <Transaction Amount>, and Transaction Date equal to <Transaction Date>; the Account balance and Available balance on the Summary card increase by <Transaction Amount>; and the transactions table row count increases by 1.

---

### [TC-008] Rapid double-click Log Out
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Log in as a valid user
2. 2. Click the Profile Icon in the top-right corner
3. 3. Click the "Log Out" button
4. 4. Immediately click the "Log Out" button again

**Original Expected Result:** First click succeeds: authenticated session is terminated and the user is redirected to the login page. The immediate second click is ignored (no additional navigation or error shown) and only a single logout action takes effect.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Account Detail page for the target account`
- **Observe**:
  - account balance
  - available balance
  - most recent transaction row (Date, Type, Amount) or transactions count

**Post-Check**
- **Navigate To**: `Savings Account Detail page for the target account -> Transactions tab`
- **Observe**:
  - account balance
  - available balance
  - transactions table top row (Date, Type, Amount, Status)
  - transactions count

**Expected Change**: A new transaction row appears in the Transactions table with Type 'Withdrawal', Transaction Date equal to the entered Transaction Date, and Amount equal to the entered Transaction Amount; the account balance and available balance on the detail page have decreased by the Transaction Amount (transactions count increased by one and the top-most transaction matches the new withdrawal).

---

### [TC-009] Browser Back after Log Out should not return to protected page
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. From the protected page, click the Profile Icon
2. 2. Click the "Log Out" button
3. 3. Wait for redirect to the login page
4. 4. Press the browser Back button

**Original Expected Result:** Navigation back to the protected page is blocked: Auth_Guard redirects to the login page and the protected page is not displayed. The back navigation is effectively blocked and the login page is shown.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Account Detail page -> Transactions tab (for the target account)`
- **Observe**:
  - account balance (displayed on Summary/header)
  - most recent transaction Type
  - most recent transaction Amount
  - total number of transactions (count or last row index)

**Post-Check**
- **Navigate To**: `Savings Account Detail page -> Transactions tab (refresh page if needed)`
- **Observe**:
  - account balance (displayed on Summary/header)
  - most recent transaction Type
  - most recent transaction Amount
  - total number of transactions (count or last row index)

**Expected Change**: A new transaction row is present at the top/end of the Transactions list with Type 'Interest Posting' and Amount equal to <calculated interest>; the account balance has increased by the same <calculated interest> amount compared to the pre_check balance; the total number of transactions has increased by one.

---

### [TC-011] Profile menu and Profile Settings access when user is unauthenticated
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is logged out (if not, perform Log Out)
2. 2. Observe whether the Profile Icon is visible in the top-right corner
3. 3. In the browser address bar, manually navigate to the Profile Settings page URL and press Enter

**Original Expected Result:** Profile Icon is not visible when unauthenticated (no dropdown available). Direct navigation to the Profile Settings URL is blocked: Auth_Guard redirects to the login page and the Profile Settings page is not displayed.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Account Detail page for the account under test`
- **Observe**:
  - status badge (expected 'Active')
  - account balance and available balance
  - available action buttons (Expect: Deposit, Withdraw, Post Interest, Calculate Interest, Close)
  - Transactions tab shows recent transactions (note last transaction id/amount for later comparison)

**Post-Check**
- **Navigate To**: `Savings Account Detail page for the account under test; additionally verify in Savings Accounts listing (Accounts -> Savings) filtered by account number`
- **Observe**:
  - status badge (expected 'Closed')
  - account balance and available balance (value should remain as before closure or reflect any automatic disposition performed during close)
  - available action buttons (Expect: Close button absent; actions for Deposit/Withdraw should be absent; may show Reopen/Reactivate depending on product)
  - Transactions tab shows the same historical transactions plus any close-related transaction (if closure triggered an automatic final transaction, it should be present and reconciled against balances)
  - Savings Accounts listing shows the account with Status column displaying 'Closed' (gray chip)

**Expected Change**: The account status has changed from 'Active' to 'Closed' (status badge displays 'Closed'); Deposit/Withdraw actions are no longer available on the detail page; the Savings Accounts listing shows the account with status 'Closed'. Any closure transaction (if performed by the system) appears in Transactions and balances reconcile with the presence of that transaction.

---

### [TC-012] Move a code value up in ordering
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the Code Values Editor for <Code List Name>, click Move Up on the row for <entry A>

**Original Expected Result:** moves entry up in ordering and <entry A> is now displayed above the previous item in the list ordering

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Account Detail page for <the account> (open via Client -> Accounts -> Savings or Global Search by account number)`
- **Observe**:
  - status badge (value) — expected 'Active'
  - available action buttons (should include 'Block Account')
  - account number / identifier (to confirm correct account)
  - current account balance

**Post-Check**
- **Navigate To**: `Savings Account Detail page for <the account> (refresh the page or re-open via Client -> Accounts -> Savings or Global Search)`
- **Observe**:
  - status badge (value)
  - available action buttons (verify 'Block Account' is no longer present or is disabled; verify presence of actions appropriate to Blocked state)
  - account number / identifier (to confirm same account)
  - current account balance

**Expected Change**: Status badge changed from 'Active' to 'Blocked'. The 'Block Account' action is no longer available (or is disabled) on the detail page. The account appears with status 'Blocked' on the savings account detail view (and will show as Blocked in listings/search). Account balance remains unchanged by the block action.

---

### [TC-013] Move a code value down in ordering
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the Code Values Editor for <Code List Name>, click Move Down on the row for <entry B>

**Original Expected Result:** moves entry down in ordering and <entry B> is now displayed below the previous item in the list ordering

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Account Detail page for the account`
- **Observe**:
  - status badge (expect 'Active')
  - absence of a 'Debit Blocked' indicator or badge
  - presence of debit-related action buttons (e.g., 'Withdraw') enabled
  - presence of 'Block Debit' action button

**Post-Check**
- **Navigate To**: `Savings Account Detail page for the account`
- **Observe**:
  - presence of a clear 'Debit Blocked' indicator (badge or status line) on the account detail header
  - status badge remains 'Active' (if applicable) but with an additional 'Debit Blocked' indicator visible
  - debit-related action buttons (e.g., 'Withdraw') are disabled or not available; 'Block Debit' action replaced by 'Unblock Debit' or similar
  - attempting to initiate a debit transaction (e.g., open Withdraw form and submit) is prevented and shows a validation/error message indicating debits are blocked

**Expected Change**: A 'Debit Blocked' indicator appears on the Savings Account detail page; debit actions that were previously enabled (such as Withdraw) are now disabled or removed and replaced by an unblock action; any attempt to perform a debit transaction is prevented and returns an appropriate error/validation message.

---

### [TC-014] Open Create Data Table form from Manage Data Tables
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Manage Data Tables
2. 2. Click Create Data Table (Create_Data_Table action)

**Original Expected Result:** Create_Data_Table form opens and the Create Data Table form is displayed with fields Data Table Name, Application Table Name, Multi Row, and Column Definitions

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Savings Account Detail page for <the account>`
- **Observe**:
  - account status badge (expected: 'Active')
  - presence and enabled state of 'Deposit' / 'Credit' action button
  - absence of any 'Credit Blocked' indicator (badge or status line)
  - Transactions tab: 'Deposit' flow can be initiated (Deposit button enabled)

**Post-Check**
- **Navigate To**: `Savings Account Detail page for <the account>`
- **Observe**:
  - presence of a clear 'Credit Blocked' indicator on the page (badge or status line)
  - state of action buttons: 'Deposit' / 'Credit' action is disabled or replaced by an 'Unblock Credit' action
  - Transactions tab: initiating a Deposit/credit transaction is blocked (shows validation/error) and no new credit transaction appears in the Transactions list

**Expected Change**: A 'Credit Blocked' indicator appears on the Savings Account Detail page; the 'Deposit' (credit) action is disabled or replaced by an 'Unblock Credit' action; attempts to submit a Deposit/credit transaction are rejected (error shown) and no credit transaction is recorded for the account.

---

### [TC-001] Open Profile Settings via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Profile Settings' in the dropdown

**Original Expected Result:** navigates to Profile Settings page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Detail -> Share Accounts tab (or Client Detail -> Accounts -> Shares)`
- **Observe**:
  - list of share account rows (each row shows: product name, requested shares, status badge, external ID if present)
  - count of share account rows matching Product = <share product> and External ID = <external id> (if provided) — expected to be 0 before test
  - if previously existing entries exist for the same product, note their requested shares and statuses for disambiguation

**Post-Check**
- **Navigate To**: `Client Detail -> Share Accounts tab (or Client Detail -> Accounts -> Shares)`
- **Observe**:
  - list of share account rows (each row shows: product name, requested shares, status badge, external ID if present)
  - newly created share account row matching Product = <share product> with Requested Shares = <valid number within product bounds>
  - status badge for that row showing 'Submitted and Pending Approval'
  - External ID column showing <external id> if it was supplied during submission
  - optionally: click the newly created row to open Share Account Detail and observe header status badge = 'Submitted and Pending Approval' and Requested/Approved shares details

**Expected Change**: A new Share Account row appears in the client's Share Accounts list for Product = <share product> with Requested Shares = <valid number within product bounds> and its status badge set to 'Submitted and Pending Approval'. If an External ID was provided during submission, the row shows that External ID. Opening the new account's detail page also shows the status badge 'Submitted and Pending Approval'.

---

### [TC-002] Log Out via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Log Out' in the dropdown

**Original Expected Result:** terminates authenticated session; clears authentication token; redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Account Detail page for <share account>`
- **Observe**:
  - status badge (expected: 'Submitted and Pending Approval')
  - total pending shares
  - total approved shares
  - unit price
  - Purchased Shares tab (presence of any existing entries)

**Post-Check**
- **Navigate To**: `Share Account Detail page for <share account>`
- **Observe**:
  - status badge (expected: 'Approved')
  - total approved shares
  - total pending shares
  - unit price
  - Purchased Shares tab (new entry for the approval with Date = Approved Date and Number of Shares = Approved Shares entered)

**Expected Change**: Status badge changes from 'Submitted and Pending Approval' to 'Approved'; 'Total Approved Shares' increases to equal the Approved Shares value entered in the approve dialog; 'Total Pending Shares' decreases by the same amount (typically to zero); the Purchased Shares tab contains a new entry reflecting the approved shares with the Approved Date.

---

### [TC-003] Unauthenticated navigation to a protected page redirects to login
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <authenticated page URL> in the browser address bar and navigate to it

**Original Expected Result:** redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Account Detail page for <share account>`
- **Observe**:
  - status badge (should read 'Submitted and Pending Approval')
  - available action buttons (should include 'Approve' and 'Reject')
  - Purchased Shares / Summary area showing pending shares or pending approval indicators

**Post-Check**
- **Navigate To**: `Share Account Detail page for <share account> (refresh or reopen)`
- **Observe**:
  - status badge
  - available action buttons (Approve/Reject/Activate etc)
  - Share Accounts listing (Client -> Share Accounts tab or global Share Accounts page) row for <share account> showing status

**Expected Change**: Status badge changes from 'Submitted and Pending Approval' to 'Rejected'; the 'Approve' and 'Reject' actions are no longer available on the detail page; the Share Accounts listing shows the account's status as 'Rejected'.

---

### [TC-004] Profile icon/menu inaccessible when unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application home page while not logged in
2. 2. Click the top-right Profile Icon

**Original Expected Result:** Profile Icon and profile menu are not available: the Profile Icon is not visible in the top-right; no dropdown opens; 'Profile Settings' and 'Log Out' options are not present or accessible. The user remains on the public/unauthenticated page (no authenticated UI is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client <client> -> Share Accounts -> <share account> Detail Page`
- **Observe**:
  - status badge (should show 'Approved')
  - action buttons (should include 'Activate')
  - total approved shares
  - total pending shares

**Post-Check**
- **Navigate To**: `Client <client> -> Share Accounts -> <share account> Detail Page (refresh or reopen to ensure backend state)`
- **Observe**:
  - status badge
  - action buttons
  - Purchased Shares tab or Purchased Shares summary (to verify account is active)
  - Audit trail / Activity log entry for activation (if available on detail page)

**Expected Change**: Status badge changes from 'Approved' to 'Active'; the 'Activate' action is no longer present; actions appropriate for an Active share account (for example 'Apply Additional Shares', 'Redeem Shares', 'Close') are available; Purchased Shares / account summaries reflect the account as active; an activation entry appears in the activity log/audit trail.

---

### [TC-005] Direct navigation to Profile Settings while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Profile Settings page URL

**Original Expected Result:** Auth Guard blocks access: browser is redirected to the Login page; Profile Settings content is not displayed and no profile settings UI elements are visible.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Account detail page for <share account>`
- **Observe**:
  - status badge (expected 'Approved')
  - presence of 'Undo Approval' action button
  - presence/absence of 'Approve' action button
  - total approved shares / total pending shares values

**Post-Check**
- **Navigate To**: `Share Account detail page for <share account>`
- **Observe**:
  - status badge
  - presence/absence of 'Undo Approval' action button
  - presence of 'Approve' action button
  - total approved shares / total pending shares values
  - audit trail / recent activity entry for the undo approval action (if available)

**Expected Change**: The status badge changes from 'Approved' to 'Submitted and Pending Approval'; the 'Undo Approval' action is no longer present and the 'Approve' action is available; share counts reflect that the account is now pending (approved/pending shares updated accordingly) and an audit trail entry records the undo approval action.

---

### [TC-006] Invoking Log Out endpoint while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Log Out endpoint/URL that the 'Log Out' button would call

**Original Expected Result:** Precondition prevents logout action: browser is redirected to the Login page; no logout success behavior occurs (no authenticated session existed and no session changes happen).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Account detail page for <share account>`
- **Observe**:
  - Purchased Shares table rows (each row: Date, Type, Number of Shares, Unit Price, Amount, Status)
  - count of rows with Type 'Purchase' and Status 'Pending'

**Post-Check**
- **Navigate To**: `Share Account detail page for <share account>`
- **Observe**:
  - Purchased Shares table rows (each row: Date, Type, Number of Shares, Unit Price, Amount, Status)
  - count of rows with Type 'Purchase' and Status 'Pending'

**Expected Change**: The Purchased Shares table shows one additional row with Type 'Purchase' and Status 'Pending' (i.e., the count of rows with Type 'Purchase' and Status 'Pending' increased by 1). The new row displays a positive Number of Shares and Amount, and Amount equals Unit Price multiplied by Number of Shares.

---

### [TC-007] Using browser Back after Log Out does not return to authenticated pages
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the Login page
2. 2. Enter <valid credentials> in the Username/Email field
3. 3. Enter <valid password> in the Password field
4. 4. Click the Login button
5. 5. Navigate to a protected page (e.g., Dashboard) while logged in
6. 6. Click the Profile Icon
7. 7. Click the 'Log Out' button in the profile menu
8. 8. After the application redirects to the Login page, click the browser Back button to return to the previously viewed protected page

**Original Expected Result:** After logout the protected page remains inaccessible: Auth Guard immediately redirects to the Login page; protected page content is not displayed; the user remains logged out (authentication token/session cleared).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client -> Share Accounts -> <share account> Detail page`
- **Observe**:
  - Purchased Shares table (existing rows and last row type/date/number of shares/unit price/amount)
  - Total Approved Shares value
  - Total Pending Shares value
  - Current Unit Price (displayed on the Share Account detail)
  - Available action 'Redeem Shares' present
  - Linked savings accounts list (to identify <linked_savings_account>)

**Post-Check**
- **Navigate To**: `1) Client -> Share Accounts -> <share account> Detail page; 2) Clients -> Savings Accounts -> <linked_savings_account> Detail page (or Accounts Overview -> <linked_savings_account>)`
- **Observe**:
  - Purchased Shares table (new latest row exists)
  - Latest Purchased Shares row columns: Date, Type, Number of Shares, Unit Price, Amount, Status
  - Total Approved Shares value
  - Share Account Transactions/Purchased Shares count (incremented)
  - Linked savings account balance
  - Linked savings account Transactions table (latest transaction referencing 'Redemption' or 'Redeem Shares' with credited Amount and description referencing <share account> or redemption)

**Expected Change**: A new 'Redemption' row appears in the Purchased Shares table with Number of Shares = <number of shares to redeem>, Unit Price = current unit price, and Amount = <number of shares to redeem> * Unit Price; Total Approved Shares decreased by <number of shares to redeem>; the selected <linked_savings_account> balance increased by the redemption Amount and its Transactions table contains a new credit transaction for that Amount referencing the share redemption.

---

### [TC-008] Rapid double-click Log Out
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Log in as a valid user
2. 2. Click the Profile Icon in the top-right corner
3. 3. Click the "Log Out" button
4. 4. Immediately click the "Log Out" button again

**Original Expected Result:** First click succeeds: authenticated session is terminated and the user is redirected to the login page. The immediate second click is ignored (no additional navigation or error shown) and only a single logout action takes effect.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Share Account Detail page for <share account> (via Client -> Share Accounts or Global Search)`
- **Observe**:
  - status badge (should be 'Active')
  - share account number / identifier
  - total approved shares
  - total pending shares
  - available action buttons (e.g., Apply Additional Shares, Redeem Shares, Close)

**Post-Check**
- **Navigate To**: `Share Account Detail page for <share account>`
- **Observe**:
  - status badge
  - share account number / identifier
  - available action buttons
  - Tabs: Purchased Shares and Transactions (for any closing transaction record)

**Expected Change**: Status badge changes from 'Active' to 'Closed'; actions valid only for Active accounts (Apply Additional Shares, Redeem Shares, Close) are no longer shown or are disabled; the account remains listed with the same account identifier and shows any closing transaction in Transactions/Purchased Shares as appropriate.

---

### [TC-002] Log Out via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Log Out' in the dropdown

**Original Expected Result:** terminates authenticated session; clears authentication token; redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Detail -> Fixed Deposits tab (for <target client>)`
- **Observe**:
  - list of Fixed Deposit accounts for <target client> (account numbers and deposit amounts)
  - absence of any Fixed Deposit account with Deposit Amount = <Deposit_Amount> and status 'Submitted and Pending Approval'

**Post-Check**
- **Navigate To**: `Client Detail -> Fixed Deposits tab (for <target client>) or Fixed Deposit Account detail page via newly created account link`
- **Observe**:
  - a new Fixed Deposit account row with Deposit Amount = <Deposit_Amount>
  - a status badge on that row or in the account detail indicating 'Submitted and Pending Approval' (or equivalent 'awaiting approval')
  - a clickable account number/link for the new Fixed Deposit account
  - on the Fixed Deposit Account detail page: Deposit Amount = <Deposit_Amount>
  - on the Fixed Deposit Account detail page: Maturity Date field is populated and visible
  - on the Fixed Deposit Account detail page: Interest Rate value is populated (calculated from the product's Interest Rate Chart)

**Expected Change**: A new Fixed Deposit account record for <target client> is created: it appears in the client's Fixed Deposits list (with a clickable account number), shows Deposit Amount = <Deposit_Amount>, has a populated Maturity Date and Interest Rate (calculated from the selected product), and displays a status badge indicating the account is awaiting approval ('Submitted and Pending Approval').

---

### [TC-004] Profile icon/menu inaccessible when unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application home page while not logged in
2. 2. Click the top-right Profile Icon

**Original Expected Result:** Profile Icon and profile menu are not available: the Profile Icon is not visible in the top-right; no dropdown opens; 'Profile Settings' and 'Log Out' options are not present or accessible. The user remains on the public/unauthenticated page (no authenticated UI is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Client Detail -> Accounts tab -> Recurring Deposits section`
- **Observe**:
  - number of recurring deposit accounts for the target client
  - whether an account exists with Product Name = <Recurring_Deposit_Product> and Expected First Deposit On = <Expected_First_Deposit_On>
  - for each listed recurring deposit account: [Account Number, Product Name, Status, Total Deposits Made, Maturity Date]

**Post-Check**
- **Navigate To**: `Client Detail -> Accounts tab -> Recurring Deposits section (open the newly created Recurring Deposit Account detail page if present)`
- **Observe**:
  - a recurring deposit account entry for Product Name = <Recurring_Deposit_Product>
  - status badge for the new account (expected 'Submitted and Pending Approval' / awaiting approval)
  - deposit schedule table (installment rows showing due dates and installment amounts)
  - Total deposits made (expected initially 0 or current total as per system state)
  - Maturity details (maturity date and maturity amount)
  - Interest Rate value shown on the account detail (calculated from the product's Interest Rate Chart)
  - Expected First Deposit On date reflected in the schedule or account summary

**Expected Change**: A new Recurring Deposit account for the target client and product <Recurring_Deposit_Product> exists (the recurring deposits list count increments by one or the new account row appears). The account detail shows the deposit schedule including the <Mandatory_Deposit_Amount_per_Installment> installments starting on <Expected_First_Deposit_On>, Total deposits made shown as 0 (or the current total if an initial deposit was recorded), maturity details populated (maturity date and amount), an Interest Rate value derived from the product's Interest Rate Chart, and a status badge indicating the account is awaiting approval (Submitted and Pending Approval).

---

### [TC-005] Direct navigation to Profile Settings while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Profile Settings page URL

**Original Expected Result:** Auth Guard blocks access: browser is redirected to the Login page; Profile Settings content is not displayed and no profile settings UI elements are visible.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Fixed Deposit Account detail page for the account under test`
- **Observe**:
  - status badge (expected 'Submitted and Pending Approval' or 'Pending Approval')
  - presence of 'Approve' action button on the detail action bar
  - account identifier (account number) to confirm correct record

**Post-Check**
- **Navigate To**: `Fixed Deposit Account detail page for the same account`
- **Observe**:
  - status badge
  - action buttons on the detail action bar
  - Approved / Approved On date or audit timestamp if displayed

**Expected Change**: The status badge updates from 'Submitted and Pending Approval' (Pending Approval) to 'Approved'; the 'Approve' action is removed from the action bar and subsequent actions such as 'Activate' become available; an Approved/Approved On date is recorded on the detail page if the UI shows approval timestamps.

---

### [TC-006] Invoking Log Out endpoint while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Log Out endpoint/URL that the 'Log Out' button would call

**Original Expected Result:** Precondition prevents logout action: browser is redirected to the Login page; no logout success behavior occurs (no authenticated session existed and no session changes happen).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Fixed Deposit Account detail page (the account in Approved status)`
- **Observe**:
  - status badge (value should be 'Approved')
  - account identifier / account number
  - presence of 'Activate' action button in the action bar
  - absence of Active-only actions (e.g., 'Premature Close', 'Close on Maturity')

**Post-Check**
- **Navigate To**: `Fixed Deposit Account detail page (refresh or return to the page after activation)`
- **Observe**:
  - status badge (value should be 'Active')
  - account identifier / account number (same as pre-check)
  - absence of 'Activate' action button in the action bar
  - presence of Active-only actions (e.g., 'Premature Close', 'Close on Maturity')
  - optionally, updated 'Activated On' or 'Activation Date' field if present

**Expected Change**: The status badge for the fixed deposit account changes from 'Approved' to 'Active'; the 'Activate' action is no longer present and Active-only actions (such as 'Premature Close' and 'Close on Maturity') are available. The account identifier remains unchanged.

---

### [TC-007] Using browser Back after Log Out does not return to authenticated pages
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the Login page
2. 2. Enter <valid credentials> in the Username/Email field
3. 3. Enter <valid password> in the Password field
4. 4. Click the Login button
5. 5. Navigate to a protected page (e.g., Dashboard) while logged in
6. 6. Click the Profile Icon
7. 7. Click the 'Log Out' button in the profile menu
8. 8. After the application redirects to the Login page, click the browser Back button to return to the previously viewed protected page

**Original Expected Result:** After logout the protected page remains inaccessible: Auth Guard immediately redirects to the Login page; protected page content is not displayed; the user remains logged out (authentication token/session cleared).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Fixed Deposit Account -> Detail page for the target account (page is open)`
- **Observe**:
  - status badge (expected 'Active')
  - account balance / maturity amount
  - transactions list (most recent transaction and types)

**Post-Check**
- **Navigate To**: `Fixed Deposit Account -> Detail page for the same account (or Client Detail -> Fixed Deposits tab to see listing)`
- **Observe**:
  - status badge
  - transactions list (presence of a transaction indicating premature closure)
  - account balance / maturity amount (updated to reflect premature closure settlement or transfer)

**Expected Change**: Status badge changed from 'Active' to 'Prematurely Closed'; a premature-closure transaction is recorded in the Transactions list; account balance and maturity amount updated to reflect the premature close (funds returned or transferred as per system handling).

---

### [TC-008] Rapid double-click Log Out
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Log in as a valid user
2. 2. Click the Profile Icon in the top-right corner
3. 3. Click the "Log Out" button
4. 4. Immediately click the "Log Out" button again

**Original Expected Result:** First click succeeds: authenticated session is terminated and the user is redirected to the login page. The immediate second click is ignored (no additional navigation or error shown) and only a single logout action takes effect.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Fixed Deposit Account Detail page (the account under test)`
- **Observe**:
  - status badge (expect 'Matured')
  - account number
  - maturity date
  - maturity instructions (e.g., Transfer to Savings / Re-Invest)
  - presence of 'Close on Maturity' action button in the action bar

**Post-Check**
- **Navigate To**: `Fixed Deposit Account Detail page (refresh or re-open to ensure backend state)`
- **Observe**:
  - status badge
  - available action buttons in the action bar
  - Transactions tab — most recent transaction entry (type and date)
  - account balance / maturity amount display

**Expected Change**: Status badge changed from 'Matured' to 'Closed on Maturity'; the 'Close on Maturity' action is no longer present in the action bar; a maturity/closure transaction appears in the Transactions tab dated on or after the confirmation, and the account balance reflects that the deposit was closed (e.g., zero balance or disbursed amount per maturity instructions).

---

### [TC-009] Browser Back after Log Out should not return to protected page
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. From the protected page, click the Profile Icon
2. 2. Click the "Log Out" button
3. 3. Wait for redirect to the login page
4. 4. Press the browser Back button

**Original Expected Result:** Navigation back to the protected page is blocked: Auth_Guard redirects to the login page and the protected page is not displayed. The back navigation is effectively blocked and the login page is shown.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Recurring Deposit Account Detail page (the account under test)`
- **Observe**:
  - status badge text (expected 'Submitted and Pending Approval' or 'Pending Approval')
  - available action buttons in the action bar (should include 'Approve')
  - account identifier (Account Number) to correlate with listing

**Post-Check**
- **Navigate To**: `1) Recurring Deposit Account Detail page (refresh); 2) Recurring Deposits listing (Accounts -> Recurring Deposits)`
- **Observe**:
  - status badge text on the detail page
  - available action buttons in the action bar on the detail page (e.g., 'Activate', 'Reject' should be present; 'Approve' should no longer be present)
  - in the Recurring Deposits listing row for the account: Status column text
  - in the Recurring Deposits listing row for the account: Account Number and Client Name to confirm same resource

**Expected Change**: The account's status badge on the detail page changes from 'Submitted and Pending Approval' (or 'Pending Approval') to 'Approved'; the 'Approve' action is no longer shown and post-approval actions such as 'Activate' are available. The Recurring Deposits listing shows the same account row with Status = 'Approved'.

---

### [TC-010] Log Out in one tab, then attempt Log Out in another tab (concurrent session edge)
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Tab A, click the Profile Icon
2. 2. In Tab A, click the "Log Out" button
3. 3. In Tab B, click the Profile Icon
4. 4. In Tab B, click the "Log Out" button

**Original Expected Result:** Logout in Tab A succeeds: Tab A is redirected to the login page and authentication token cleared. In Tab B, clicking "Log Out" succeeds in resulting in the login page (no error shown) but performs no additional session termination; Tab B is redirected to the login page as well.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Recurring Deposit Account detail page for the account in preconditions`
- **Observe**:
  - status badge (displays 'Approved')
  - action buttons on the detail action bar (includes 'Activate')
  - account identifier (Account number) to ensure correct account context

**Post-Check**
- **Navigate To**: `Recurring Deposit Account detail page for the same account (refresh if needed)`
- **Observe**:
  - status badge (displays 'Active')
  - action buttons on the detail action bar (no longer includes 'Activate'; includes actions available to Active accounts such as 'Deposit')
  - Activation date field on the detail header (populated / not blank)
  - Account identifier (Account number) matches pre-check to confirm same account

**Expected Change**: Status badge changes from 'Approved' to 'Active'; the 'Activate' action is removed from the action bar and actions appropriate to an Active recurring deposit account (e.g., 'Deposit') are present; the Activation date is populated on the account detail.

---

### [TC-011] Profile menu and Profile Settings access when user is unauthenticated
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is logged out (if not, perform Log Out)
2. 2. Observe whether the Profile Icon is visible in the top-right corner
3. 3. In the browser address bar, manually navigate to the Profile Settings page URL and press Enter

**Original Expected Result:** Profile Icon is not visible when unauthenticated (no dropdown available). Direct navigation to the Profile Settings URL is blocked: Auth_Guard redirects to the login page and the Profile Settings page is not displayed.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Recurring Deposit Account detail page -> Transactions tab and Summary/Details section`
- **Observe**:
  - Most recent transaction in Transactions table (Date, Type, Amount)
  - Total deposits made value on the Recurring Deposit detail page (Summary/Details)

**Post-Check**
- **Navigate To**: `Recurring Deposit Account detail page -> Transactions tab and Summary/Details section`
- **Observe**:
  - Most recent transaction in Transactions table (Date, Type, Amount, Status)
  - Total deposits made value on the Recurring Deposit detail page (Summary/Details)

**Expected Change**: A new transaction of type 'Deposit' appears at the top of the Transactions table with Amount equal to the deposit amount entered in the test and Transaction Date equal to the deposit date; the 'Total deposits made' value on the Recurring Deposit detail page has increased by the same deposit amount compared to the pre-check.

---

### [TC-012] Move a code value up in ordering
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the Code Values Editor for <Code List Name>, click Move Up on the row for <entry A>

**Original Expected Result:** moves entry up in ordering and <entry A> is now displayed above the previous item in the list ordering

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Recurring Deposit Account -> Detail page for the account under test`
- **Observe**:
  - status badge (should be 'Active')
  - account balance
  - available balance
  - Transactions tab -> most recent transaction type and date
  - Summary tab -> maturity date / next scheduled deposit information

**Post-Check**
- **Navigate To**: `Recurring Deposit Account -> Detail page for the same account (refresh or reopen to ensure backend state)`
- **Observe**:
  - status badge
  - account balance
  - available balance
  - Transactions tab -> most recent transaction type, date and amount
  - Summary tab -> closure date or 'Prematurely Closed' note

**Expected Change**: Status badge is updated to 'Prematurely Closed' (was 'Active' in pre-check); account balance and available balance reflect the closure (typically zero or the payout amount removed from the account); Transactions contains a new 'Premature Close' / closure payout transaction with the closure date and payout amount; Summary shows a closure date and the status 'Prematurely Closed'.

---

### [TC-013] Move a code value down in ordering
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the Code Values Editor for <Code List Name>, click Move Down on the row for <entry B>

**Original Expected Result:** moves entry down in ordering and <entry B> is now displayed below the previous item in the list ordering

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Recurring Deposit Account detail page (specific account under test)`
- **Observe**:
  - status badge (expect 'Matured')
  - 'Close on Maturity' action button visible and enabled on the action bar
  - account identifier / account number shown in header

**Post-Check**
- **Navigate To**: `Recurring Deposit Account detail page (refresh page or navigate away and re-open via Recurring Deposits listing)`
- **Observe**:
  - status badge
  - action buttons on the detail action bar
  - Transactions tab latest entry (to confirm maturity/closure posting)

**Expected Change**: Status badge changed from 'Matured' to 'Closed on Maturity'; the 'Close on Maturity' action is no longer present on the action bar; account is reflected as closed (i.e., shown in closed/closed-on-maturity state) and a final maturity/closure transaction is present in Transactions.

---

### [TC-002] Log Out via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Log Out' in the dropdown

**Original Expected Result:** terminates authenticated session; clears authentication token; redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounting -> Chart of Accounts`
- **Observe**:
  - Expand the '<Account_Type>' top-level node in the Chart of Accounts tree and locate the header account named '<existing header account>'
  - Record the current list of child accounts under the '<existing header account>' header (each entry's GL Code and Account Name)
  - Verify that GL Code '<unique GL Code>' is NOT present under the '<existing header account>' header

**Post-Check**
- **Navigate To**: `Accounting -> Chart of Accounts`
- **Observe**:
  - Expand the '<Account_Type>' top-level node and open the '<existing header account>' header node
  - List child accounts under the header showing GL Code, Account Name, Account Usage, Account Type, and Manual Entries Allowed indicator for each row
  - Locate the row with GL Code '<unique GL Code>' and observe its details

**Expected Change**: A new detail account row appears under '<Account_Type>' > '<existing header account>' with GL Code '<unique GL Code>' and Account Name '<Account Name>'; the row shows Account Usage = 'Detail', Account Type = '<Account_Type>', and Manual Entries Allowed = checked. The header's child list now includes this new row (child count increased by one) and previously-verified absence of '<unique GL Code>' is now false.

---

### [TC-006] Invoking Log Out endpoint while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Log Out endpoint/URL that the 'Log Out' button would call

**Original Expected Result:** Precondition prevents logout action: browser is redirected to the Login page; no logout success behavior occurs (no authenticated session existed and no session changes happen).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounting -> Chart of Accounts`
- **Observe**:
  - account row with GL Code <existing GL Code>
  - account name <existing Account Name>
  - parent/child position in the chart hierarchy (if visible)

**Post-Check**
- **Navigate To**: `Accounting -> Chart of Accounts`
- **Observe**:
  - absence of account row with GL Code <existing GL Code>
  - absence of account name <existing Account Name>
  - search for <existing GL Code> or <existing Account Name> returns no results or a 'not found' message

**Expected Change**: The account row for <existing Account Name> (GL Code <existing GL Code>) is no longer present in the Chart of Accounts tree; searching or attempting to open the deleted GL Code/account returns no result or 'not found'.

---

### [TC-007] Using browser Back after Log Out does not return to authenticated pages
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the Login page
2. 2. Enter <valid credentials> in the Username/Email field
3. 3. Enter <valid password> in the Password field
4. 4. Click the Login button
5. 5. Navigate to a protected page (e.g., Dashboard) while logged in
6. 6. Click the Profile Icon
7. 7. Click the 'Log Out' button in the profile menu
8. 8. After the application redirects to the Login page, click the browser Back button to return to the previously viewed protected page

**Original Expected Result:** After logout the protected page remains inaccessible: Auth Guard immediately redirects to the Login page; protected page content is not displayed; the user remains logged out (authentication token/session cleared).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounting -> Chart of Accounts`
- **Observe**:
  - tree row for GL Code <existing GL Code> displays Account Name '<existing Account Name>'
  - Account Detail view for GL Code <existing GL Code> (open by clicking the account name) shows Account Name field value '<existing Account Name>'

**Post-Check**
- **Navigate To**: `Accounting -> Chart of Accounts`
- **Observe**:
  - tree row for GL Code <existing GL Code> displays Account Name '<new Account Name>'
  - Account Detail view for GL Code <existing GL Code> (open by clicking the account name) shows Account Name field value '<new Account Name>'

**Expected Change**: The Account Name for GL Code <existing GL Code> is updated from '<existing Account Name>' to '<new Account Name>' in both the Account Detail view and the Chart of Accounts tree row.

---

### [TC-002] Log Out via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Log Out' in the dropdown

**Original Expected Result:** terminates authenticated session; clears authentication token; redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounting -> Journal Entries`
- **Observe**:
  - Filter by Office = <Office> and Transaction Date = <Transaction_Date> (or narrow Date Range covering <Transaction_Date>)
  - Initial count of journal entries matching the filter (e.g., displayed rows)
  - For visible entries: observe columns Entry ID, Office, Transaction Date, Debit Total, Credit Total, Difference, Reference Number, Created By

**Post-Check**
- **Navigate To**: `Accounting -> Journal Entries`
- **Observe**:
  - Apply same filter: Office = <Office> and Transaction Date = <Transaction_Date>
  - New/updated count of journal entries matching the filter
  - Locate a journal entry row with Office = <Office> and Transaction Date = <Transaction_Date>
  - From that row observe: Entry ID, Debit Total, Credit Total, Difference, Reference Number, Comments (if visible), Created By (should be <Accountant>)

**Expected Change**: A new journal entry row appears for the selected Office and Transaction Date (or the initial count increased by one); the entry's Debit Total equals its Credit Total, the Difference displays 0.00, and the Created By column shows the <Accountant>. Reference Number and Comments (if provided during submission) are visible on the entry row or detail view.

---

### [TC-005] Direct navigation to Profile Settings while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Profile Settings page URL

**Original Expected Result:** Auth Guard blocks access: browser is redirected to the Login page; Profile Settings content is not displayed and no profile settings UI elements are visible.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounting -> Journal Entries -> Closing Entries`
- **Observe**:
  - list of existing rows in the Closing Entries table (note count)
  - for the most recent row observe Office, Closing Date, Created Date, Created By, and Comments
  - verify that there is no existing row with Office = <Office> and Closing Date = <Closing_Date>

**Post-Check**
- **Navigate To**: `Accounting -> Journal Entries -> Closing Entries`
- **Observe**:
  - Closing Entries table contains a row with Office = <Office> and Closing Date = <Closing_Date>
  - the new row shows Created Date (recent) and Created By = current <Accountant> user
  - Comments column contains <Comments> if comments were provided on submission
  - attempt to create a Journal Entry with Transaction Date on or before <Closing_Date> and observe a validation/error message preventing the posting

**Expected Change**: A new row appears in the Closing Entries table with Office <Office> and Closing Date <Closing_Date>; the row shows a recent Created Date and Created By the acting Accountant, and Comments contains <Comments> if provided. Additionally, the system prevents posting Journal Entries with Transaction Dates on or before <Closing_Date> (attempts to create such entries should be blocked with a validation/error message).

---

### [TC-001] Open Profile Settings via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Profile Settings' in the dropdown

**Original Expected Result:** navigates to Profile Settings page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounting -> Accounting Rules page`
- **Observe**:
  - Search for '<Rule Name>' in the Accounting Rules table (use table search/filter)
  - Confirm no row exists with Rule Name = '<Rule Name>'
  - Confirm table displays columns: 'Rule Name', 'Office', 'Debit Account(s)', 'Credit Account(s)'

**Post-Check**
- **Navigate To**: `Accounting -> Accounting Rules page`
- **Observe**:
  - Search for '<Rule Name>' in the Accounting Rules table (use table search/filter)
  - A row exists with Rule Name = '<Rule Name>'
  - Office column shows the selected Office name, or is blank/indicates 'Applies to all offices' if left blank during creation
  - Debit Account(s) column lists the debit account(s) selected in the Create Rule form
  - Credit Account(s) column lists the credit account(s) selected in the Create Rule form

**Expected Change**: A new row appears in the Accounting Rules table with Rule Name equal to '<Rule Name>'; the Office column displays the chosen Office (or is blank/marked for all offices if left blank); the Debit Account(s) and Credit Account(s) columns list the configured accounts exactly as selected during rule creation.

---

### [TC-003] Unauthenticated navigation to a protected page redirects to login
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <authenticated page URL> in the browser address bar and navigate to it

**Original Expected Result:** redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin -> Accounting Rules -> Open the detail view for <existing rule>`
- **Observe**:
  - Rule Name
  - Debit Account(s) (listed GL accounts)
  - Allow Multiple Debit Entries (checkbox state)
  - Credit Account(s) (listed GL accounts)
  - Allow Multiple Credit Entries (checkbox state)

**Post-Check**
- **Navigate To**: `Admin -> Accounting Rules -> Refresh and open the detail view for the same rule (or return to Accounting Rules listing and re-open the rule)`
- **Observe**:
  - Rule Name
  - Debit Account(s) (listed GL accounts)
  - Allow Multiple Debit Entries (checkbox state)
  - Credit Account(s) (listed GL accounts)
  - Allow Multiple Credit Entries (checkbox state)

**Expected Change**: Rule Name equals <new Rule Name>; Debit Account(s) contains the newly selected GL account(s) and no longer shows removed selections; Allow Multiple Debit Entries reflects the new toggled state; Credit Account(s) contains the newly selected GL account(s) and no longer shows removed selections; Allow Multiple Credit Entries reflects the new toggled state.

---

### [TC-004] Profile icon/menu inaccessible when unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application home page while not logged in
2. 2. Click the top-right Profile Icon

**Original Expected Result:** Profile Icon and profile menu are not available: the Profile Icon is not visible in the top-right; no dropdown opens; 'Profile Settings' and 'Log Out' options are not present or accessible. The user remains on the public/unauthenticated page (no authenticated UI is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Accounting -> Accounting Rules (Listing)`
- **Observe**:
  - presence of a row with Rule Name = <existing rule>
  - Office column value for the row
  - Debit Account(s) and Credit Account(s) values for the row
  - total number of rows (or visible row count) in the Accounting Rules table

**Post-Check**
- **Navigate To**: `Accounting -> Accounting Rules (Listing)`
- **Observe**:
  - absence of any row with Rule Name = <existing rule>
  - searching/filtering by <existing rule> returns no results or 'No results found' message
  - total number of rows decreased by one compared to pre-check (or no longer includes the deleted rule)

**Expected Change**: The Accounting Rules table no longer contains a row for <existing rule>; the rule is removed from the listing (search/filter for <existing rule> returns no results) and the visible row count is reduced accordingly.

---

### [TC-005] Direct navigation to Profile Settings while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Profile Settings page URL

**Original Expected Result:** Auth Guard blocks access: browser is redirected to the Login page; Profile Settings content is not displayed and no profile settings UI elements are visible.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin -> Accounting -> Financial Activity Mappings`
- **Observe**:
  - Financial Activity Mappings table rows (columns: Financial Activity, GL Account)
  - absence of '<unmapped Financial Activity>' in the Financial Activity column
  - presence of '+ Create Mapping' button

**Post-Check**
- **Navigate To**: `Admin -> Accounting -> Financial Activity Mappings`
- **Observe**:
  - Financial Activity Mappings table rows (columns: Financial Activity, GL Account)
  - presence of a row with Financial Activity = '<unmapped Financial Activity>'
  - GL Account value for that row equals '<GL Account>'
  - total row count increased by 1 compared to pre_check (optional numeric check)

**Expected Change**: A new row appears in the Financial Activity Mappings table with Financial Activity set to '<unmapped Financial Activity>' and GL Account set to '<GL Account>'; the mapping that was previously absent is now present and will enable automatic posting for that activity.

---

### [TC-003] Unauthenticated navigation to a protected page redirects to login
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <authenticated page URL> in the browser address bar and navigate to it

**Original Expected Result:** redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Provisioning Criteria page`
- **Observe**:
  - list of Criteria Names in the Provisioning Criteria table
  - number of rows in the Provisioning Criteria table
  - for each existing row: Criteria Name, Created Date, Definitions count

**Post-Check**
- **Navigate To**: `Provisioning Criteria page`
- **Observe**:
  - row with Criteria Name = <criteria name>
  - Created Date for the new row
  - Definitions for the new row showing: Loan Product, Category, Minimum Age, Maximum Age, Provisioning Percentage, Liability Account, Expense Account

**Expected Change**: A new row appears in the Provisioning Criteria table with Criteria Name equal to <criteria name> and a non-empty Created Date. The new row contains one Definitions entry with Loan Product = <loan product>, Category = STANDARD, Minimum Age = <minimum overdue days>, Maximum Age = <maximum overdue days>, Provisioning Percentage = <provision percentage>, Liability Account = <liability account>, and Expense Account = <expense account>.

---

### [TC-004] Profile icon/menu inaccessible when unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application home page while not logged in
2. 2. Click the top-right Profile Icon

**Original Expected Result:** Profile Icon and profile menu are not available: the Profile Icon is not visible in the top-right; no dropdown opens; 'Profile Settings' and 'Log Out' options are not present or accessible. The user remains on the public/unauthenticated page (no authenticated UI is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Provisioning -> Entries page`
- **Observe**:
  - count of rows in Provisioning Entries table
  - most recent row: Entry Date
  - most recent row: Journal Entry Created column value (empty or journal entry id/link)

**Post-Check**
- **Navigate To**: `Provisioning -> Entries page, then navigate to Accounting -> Journal Entries page to follow the referenced journal entry`
- **Observe**:
  - count of rows in Provisioning Entries table
  - most recent row: Entry Date
  - most recent row: Journal Entry Created column value (non-empty and clickable to a Journal Entry)
  - Journal Entries page: presence of a Journal Entry matching the ID/link shown in the Provisioning Entries table (verify Transaction Date and amount present)

**Expected Change**: Provisioning Entries table row count increased by 1; the new most-recent row's Entry Date is the creation date and its 'Journal Entry Created' column shows a created journal entry (non-empty and clickable); the referenced Journal Entry exists in Journal Entries with a matching ID and has Transaction Date and amount details.

---

### [TC-006] Invoking Log Out endpoint while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Log Out endpoint/URL that the 'Log Out' button would call

**Original Expected Result:** Precondition prevents logout action: browser is redirected to the Login page; no logout success behavior occurs (no authenticated session existed and no session changes happen).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Provisioning > Entries page`
- **Observe**:
  - number of rows in the Provisioning Entries table
  - identify and note the target provisioning entry row (by Entry Date, Created By or other visible identifier)
  - record the target row's 'Entry Date' value and 'Journal Entry Created' column value

**Post-Check**
- **Navigate To**: `Provisioning > Entries page`
- **Observe**:
  - number of rows in the Provisioning Entries table
  - the most recent/newest row's 'Entry Date' value
  - the most recent/newest row's 'Journal Entry Created' column value
  - presence of a new row that corresponds to the recreated provisioning entry (e.g., same identifying fields as the original but with a new Entry Date/Created Date)

**Expected Change**: The Provisioning Entries table has one additional row compared to pre_check; a new row appears for the recreated provisioning entry whose 'Entry Date' reflects the recreation timestamp (i.e., same or later than the action time) and whose 'Journal Entry Created' column indicates that a journal entry was created (e.g., shows 'Created' / a journal entry link / yes).

---

### [TC-004] Profile icon/menu inaccessible when unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application home page while not logged in
2. 2. Click the top-right Profile Icon

**Original Expected Result:** Profile Icon and profile menu are not available: the Profile Icon is not visible in the top-right; no dropdown opens; 'Profile Settings' and 'Log Out' options are not present or accessible. The user remains on the public/unauthenticated page (no authenticated UI is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Offices page`
- **Observe**:
  - Presence or absence of an office with name '<Office Name>' in the Offices table
  - Parent Office value for any existing row with name '<Office Name>' (should be none)
  - Total number of rows in the Offices table

**Post-Check**
- **Navigate To**: `Offices page`
- **Observe**:
  - Offices table row with Office Name = '<Office Name>'
  - Parent Office column value for the '<Office Name>' row should equal '<Parent Office>'
  - Opened On Date column value for the '<Office Name>' row should equal '<Opened On Date>'
  - External ID column value for the '<Office Name>' row should equal '<External ID>' (if provided)
  - Total number of rows in the Offices table

**Expected Change**: A new row appears in the Offices table for '<Office Name>' with Parent Office = '<Parent Office>' and Opened On Date = '<Opened On Date>'; if an External ID was provided it is shown in the External ID column; the total number of offices increases by 1 compared to the pre-check.

---

### [TC-005] Direct navigation to Profile Settings while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Profile Settings page URL

**Original Expected Result:** Auth Guard blocks access: browser is redirected to the Login page; Profile Settings content is not displayed and no profile settings UI elements are visible.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Offices page -> Open the Detail page for the existing office (<existing office>)`
- **Observe**:
  - Office Name (current value)
  - Opened On Date (current value)
  - External ID (current value, if present)
  - Status/metadata displayed on the Office Detail header (to confirm correct office)

**Post-Check**
- **Navigate To**: `Offices page -> Open the Detail page for the same office (<existing office>) and also review the Offices listing row for that office`
- **Observe**:
  - Office Name (displayed on Office Detail header and in Offices listing)
  - Opened On Date (displayed on Office Detail and Offices listing if shown)
  - External ID (displayed on Office Detail)
  - Breadcrumbs or account identifier to ensure the same office record is being viewed

**Expected Change**: The Office Name on the Office Detail page and in the Offices listing matches the new <Office Name> entered in the Edit form; the Opened On Date on the Office Detail page matches the new <Opened On Date> entered; the External ID on the Office Detail matches the updated <External ID> if it was changed. Other identifying metadata (breadcrumb/office identifier) still references the same office record.

---

### [TC-001] Open Profile Settings via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Profile Settings' in the dropdown

**Original Expected Result:** navigates to Profile Settings page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Employees page`
- **Observe**:
  - Search for '<First Name> <Last Name>' returns no matching row
  - Employees table columns visible: Name, Office, Is Loan Officer, Status

**Post-Check**
- **Navigate To**: `Employees page (use search for '<First Name> <Last Name>')`
- **Observe**:
  - A row with Name '<First Name> <Last Name>' is present
  - Office column for that row shows '<Office>'
  - Is Loan Officer indicator for that row is unchecked / shows 'No'
  - Status column for that row shows 'Active'

**Expected Change**: A new employee row with Name '<First Name> <Last Name>' appears in the Employees table with Office '<Office>'; the Is Loan Officer indicator is unchecked and the Status displays 'Active'.

---

### [TC-002] Log Out via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Log Out' in the dropdown

**Original Expected Result:** terminates authenticated session; clears authentication token; redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Employees page`
- **Observe**:
  - search for the employee name '<First Name> <Last Name>' in the Employees table
  - verify there is no row with Name '<First Name> <Last Name>' and Office '<Office>'
  - note the current total employee count (optional)

**Post-Check**
- **Navigate To**: `Employees page`
- **Observe**:
  - row with Name '<First Name> <Last Name>'
  - Office column value for that row equals '<Office>'
  - Is Loan Officer column for that row shows checked/true
  - Status column for that row shows 'Active'
  - total employee count increased by 1 compared to pre-check (if noted)

**Expected Change**: A new row appears in the Employees table with Name '<First Name> <Last Name>' and Office '<Office>'; the Is Loan Officer column for that row is checked/true and the Status column displays 'Active'. If a total count was noted in pre_check, it has increased by one.

---

### [TC-005] Direct navigation to Profile Settings while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Profile Settings page URL

**Original Expected Result:** Auth Guard blocks access: browser is redirected to the Login page; Profile Settings content is not displayed and no profile settings UI elements are visible.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Employees -> Click the employee name '<First Name> <Last Name>' to open Staff Detail page`
- **Observe**:
  - Mobile Number (current value)
  - Is Loan Officer indicator (checkbox state or badge)

**Post-Check**
- **Navigate To**: `Employees -> Click the employee name '<First Name> <Last Name>' to open Staff Detail page`
- **Observe**:
  - Mobile Number
  - Is Loan Officer indicator (checkbox state or badge)

**Expected Change**: Mobile Number changed from the pre-check value to '<new mobile number>'; Is Loan Officer indicator is set to checked/true for the employee.

---

### [TC-001] Open Profile Settings via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Profile Settings' in the dropdown

**Original Expected Result:** navigates to Profile Settings page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Tellers page`
- **Observe**:
  - Tellers table rows (Teller Name column)
  - Count of rows in Tellers table
  - Presence or absence of a row with Teller Name '<Teller Name>'
  - Columns visible: Office, Status, Description

**Post-Check**
- **Navigate To**: `Tellers page`
- **Observe**:
  - Tellers table rows (Teller Name column)
  - Count of rows in Tellers table
  - Row with Teller Name '<Teller Name>'
  - Office value in that row
  - Status value in that row
  - Description value in that row
  - Start Date and End Date cells in that row (if visible)

**Expected Change**: Tellers table contains a new row with Teller Name '<Teller Name>' and Office '<Office>'; the Status column for that row shows the selected Status (e.g., 'Active'); the Description cell shows '<Description>' (or is empty if none was provided). The total row count in the Tellers table has increased by one compared to pre_check.

---

### [TC-003] Unauthenticated navigation to a protected page redirects to login
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <authenticated page URL> in the browser address bar and navigate to it

**Original Expected Result:** redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Tellers -> Click <existing teller> to open Teller Detail page -> Cashiers section`
- **Observe**:
  - count of rows in Cashiers table
  - presence or absence of a row with Staff = <Staff> and Start Date = <Start Date>
  - Start Date and End Date values for any existing assignments for <Staff>
  - Is Full Day column values for any existing assignments for <Staff>

**Post-Check**
- **Navigate To**: `Tellers -> Click <existing teller> to open Teller Detail page -> Cashiers section`
- **Observe**:
  - count of rows in Cashiers table
  - a row with Staff = <Staff>
  - Start Date column for the new row equals <Start Date>
  - End Date column for the new row equals <End Date> (if <End Date> was provided)
  - Is Full Day column for the new row reflects whether 'Is Full Day' was checked
  - the new assignment row is visible in the list (not hidden by pagination/filtering)

**Expected Change**: Cashiers table row count increased by one and there is a new row with Staff = <Staff> and Start Date = <Start Date>; End Date matches the provided value if entered; the 'Is Full Day' column reflects the submitted checkbox state; the new assignment is visible in the Cashiers list.

---

### [TC-004] Profile icon/menu inaccessible when unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application home page while not logged in
2. 2. Click the top-right Profile Icon

**Original Expected Result:** Profile Icon and profile menu are not available: the Profile Icon is not visible in the top-right; no dropdown opens; 'Profile Settings' and 'Log Out' options are not present or accessible. The user remains on the public/unauthenticated page (no authenticated UI is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Tellers -> Select <existing teller> -> Cashiers table -> Select <existing cashier> (Cashier Detail page)`
- **Observe**:
  - Cash In Hand value
  - Opening Balance value
  - Running Balance value (if displayed separately)
  - Cashier Transactions table: row count and last (most recent) row details {Date, Type, Amount, Running Balance}

**Post-Check**
- **Navigate To**: `Tellers -> Select <existing teller> -> Cashiers table -> Select <existing cashier> (Cashier Detail page)`
- **Observe**:
  - Cash In Hand value
  - Opening Balance value
  - Running Balance value (if displayed separately)
  - Cashier Transactions table: row count and top/most-recent row details {Date, Type, Amount, Running Balance}

**Expected Change**: Cashier Transactions table has one additional transaction row (new most-recent/top row) representing the allocation (Type indicates allocation/Allocate Cash) with Amount equal to the allocated amount; Cash In Hand and Running Balance values increased by the allocated amount; the new transaction's Running Balance equals the previous running balance plus the allocated amount.

---

### [TC-005] Direct navigation to Profile Settings while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Profile Settings page URL

**Original Expected Result:** Auth Guard blocks access: browser is redirected to the Login page; Profile Settings content is not displayed and no profile settings UI elements are visible.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Tellers page -> Teller Detail for <existing teller> -> Cashiers tab -> Cashier Detail for <existing cashier>`
- **Observe**:
  - Cash In Hand value on the Cashier Detail header/card
  - Running Balance value on the Cashier Detail or Cashier Transactions summary
  - Most recent row in the Cashier Transactions table: [Date, Type, Amount, Currency, Running Balance after transaction]

**Post-Check**
- **Navigate To**: `Tellers page -> Teller Detail for <existing teller> -> Cashiers tab -> Cashier Detail for <existing cashier>`
- **Observe**:
  - Cash In Hand value on the Cashier Detail header/card
  - Running Balance value on the Cashier Detail or Cashier Transactions summary
  - Top/newest row in the Cashier Transactions table: [Date, Type, Amount, Currency, Running Balance after transaction]

**Expected Change**: A new settlement transaction appears as the newest row in the Cashier Transactions table with Type 'Settle Cash' (or equivalent), Amount = <Amount>, Currency = <Currency>, and Transaction Date = <Transaction_Date>. The Cash In Hand value decreased by <Amount> compared to the pre_check value, and the Running Balance decreased by <Amount> (i.e., post-check running balance = pre-check running balance minus <Amount>).

---

### [TC-002] Log Out via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Log Out' in the dropdown

**Original Expected Result:** terminates authenticated session; clears authentication token; redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin -> Users (Users page)`
- **Observe**:
  - Users table loaded
  - no row with Username: <new username>
  - columns visible: Username, First Name, Last Name, Email, Office, Status

**Post-Check**
- **Navigate To**: `Admin -> Users (Users page)`
- **Observe**:
  - row with Username: <new username>
  - Email column for that row shows: <email address>
  - Office column for that row shows: <office> (if provided)
  - Staff column/link shows: <staff record> (if linked)
  - Roles column or roles indicator shows the selected role(s)
  - Status column shows Active (or the default status for newly created users)

**Expected Change**: A new row appears in the Users table with Username '<new username>' and Email '<email address>'; optional fields (Office, Staff, Roles) reflect the values entered during creation and the Username that was absent in pre_check is now present.

---

### [TC-003] Unauthenticated navigation to a protected page redirects to login
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <authenticated page URL> in the browser address bar and navigate to it

**Original Expected Result:** redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin -> Roles page (Roles listing)`
- **Observe**:
  - roles table rows (Name column)
  - search/filter input for roles
  - ensure '<role name>' is NOT present in the roles table prior to creation (optional)

**Post-Check**
- **Navigate To**: `Admin -> Roles page; click the newly created role '<role name>' to open the Role Permissions page`
- **Observe**:
  - roles table contains a row with Name = '<role name>'
  - roles table or role detail shows Description = '<description>'
  - clicking the '<role name>' row opens the Role Permissions page
  - Role Permissions page displays a permissions matrix with categories: 'User Management', 'Portfolio', 'Organization', 'Accounting', 'Reports', 'Other_Permissions'
  - each listed category shows its permission checkboxes (visible and interactable)

**Expected Change**: A new role named '<role name>' with description '<description>' appears in the Roles listing; clicking that role opens the Role Permissions page which displays the permissions matrix containing categories User Management, Portfolio, Organization, Accounting, Reports, and Other_Permissions with their permission checkboxes.

---

### [TC-004] Profile icon/menu inaccessible when unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application home page while not logged in
2. 2. Click the top-right Profile Icon

**Original Expected Result:** Profile Icon and profile menu are not available: the Profile Icon is not visible in the top-right; no dropdown opens; 'Profile Settings' and 'Log Out' options are not present or accessible. The user remains on the public/unauthenticated page (no authenticated UI is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin -> Roles -> Role Permissions page for <role name>`
- **Observe**:
  - <specific permission> checkbox state (expected: unchecked before action)
  - Role name displayed on the page

**Post-Check**
- **Navigate To**: `Admin -> Roles -> Role Permissions page for <role name> (perform the steps, then refresh the page or navigate away to Roles list and re-open the role permissions page)`
- **Observe**:
  - <specific permission> checkbox state (expected: checked)
  - Role name displayed on the page

**Expected Change**: The checkbox for <specific permission> is checked on the Role Permissions page for <role name> and remains checked after a page refresh or after navigating away and returning (indicating the permission change was persisted in the backend).

---

### [TC-001] Open Profile Settings via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Profile Settings' in the dropdown

**Original Expected Result:** navigates to Profile Settings page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `From Client -> Accounts -> <From_Account> (Account Detail) and To Client -> Accounts -> <To_Account> (Account Detail)`
- **Observe**:
  - From account: available balance
  - From account: account balance
  - From account: most recent transaction (date, amount, type, reference/description if present)
  - To account: available balance
  - To account: account balance
  - To account: most recent transaction (date, amount, type, reference/description if present)

**Post-Check**
- **Navigate To**: `From Client -> Accounts -> <From_Account> (Account Detail) and To Client -> Accounts -> <To_Account> (Account Detail)`
- **Observe**:
  - From account: available balance
  - From account: account balance
  - From account: transactions list (newest entry: date, amount, type = Debit, reference/description)
  - To account: available balance
  - To account: account balance
  - To account: transactions list (newest entry: date, amount, type = Credit, reference/description)

**Expected Change**: From account available and account balance decreased by <transfer amount> and a new debit transaction exists dated <transfer date> with amount = <transfer amount> and description matching the submitted description; To account available and account balance increased by <transfer amount> and a new credit transaction exists dated <transfer date> with amount = <transfer amount> and matching description; both transactions share the same transfer reference/transaction id (or show linked transfer reference) confirming the debit and credit are the same transfer.

---

### [TC-002] Log Out via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Log Out' in the dropdown

**Original Expected Result:** terminates authenticated session; clears authentication token; redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Administration -> Account Transfers & Standing Instructions -> Standing Instructions page`
- **Observe**:
  - presence of a table row with Name = <Name> (exists or not)
  - total number of rows in the Standing Instructions table
  - columns visible for each row: Name, From Client, From Account, To Client, To Account, Amount, Validity (From/Till), Recurrence Type, Recurrence Frequency/Interval, Status

**Post-Check**
- **Navigate To**: `Administration -> Account Transfers & Standing Instructions -> Standing Instructions page`
- **Observe**:
  - presence of a table row with Name = <Name>
  - the row's values for From Account, To Account, Amount, Validity From, Validity Till, Recurrence Type, Recurrence Frequency/Interval
  - Status column for the new row
  - total number of rows in the Standing Instructions table

**Expected Change**: A new row appears in the Standing Instructions table with Name = <Name>. The new row shows the From Account, To Account, Amount, Validity From/Till, Recurrence Type and Recurrence Frequency/Interval matching the values entered in the Create form. The Status column for the new row is 'Active'. If a pre-check recorded the table row count, the total number of rows has increased by 1.

---

### [TC-003] Unauthenticated navigation to a protected page redirects to login
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <authenticated page URL> in the browser address bar and navigate to it

**Original Expected Result:** redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin -> Standing Instructions page`
- **Observe**:
  - listing contains a row with Name = <Name>
  - Status column value for that row equals 'Disabled'
  - Actions column for that row includes an 'Enable' action

**Post-Check**
- **Navigate To**: `Admin -> Standing Instructions page`
- **Observe**:
  - listing contains a row with Name = <Name>
  - Status column value for that row equals 'Active'
  - Actions column for that row no longer shows an 'Enable' action (may show 'Disable' or 'Edit')

**Expected Change**: The Standing Instruction named <Name> has its Status changed from 'Disabled' to 'Active' in the listing, and the 'Enable' action is no longer available for that row.

---

### [TC-004] Profile icon/menu inaccessible when unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application home page while not logged in
2. 2. Click the top-right Profile Icon

**Original Expected Result:** Profile Icon and profile menu are not available: the Profile Icon is not visible in the top-right; no dropdown opens; 'Profile Settings' and 'Log Out' options are not present or accessible. The user remains on the public/unauthenticated page (no authenticated UI is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Standing Instructions page (Listing)`
- **Observe**:
  - Presence of a row with Name = <Name>
  - Status column for the row with Name = <Name> shows 'Active'
  - From Client and To Client values for the row (to uniquely identify the instruction)
  - Amount for the row (to uniquely identify the instruction)

**Post-Check**
- **Navigate To**: `Standing Instructions page (Listing) — refresh the listing or reopen the page`
- **Observe**:
  - Presence of a row with Name = <Name>
  - Status column for the row with Name = <Name>
  - From Client and To Client values for the row
  - Amount for the row

**Expected Change**: The Status column for the row with Name = <Name> changed from 'Active' to 'Disabled' (the listing reflects the updated status for the same instruction identified by Name, From Client, To Client, and Amount).

---

### [TC-005] Direct navigation to Profile Settings while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Profile Settings page URL

**Original Expected Result:** Auth Guard blocks access: browser is redirected to the Login page; Profile Settings content is not displayed and no profile settings UI elements are visible.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Standing Instructions page`
- **Observe**:
  - presence of a row with Name = <Name> in the Standing Instructions table
  - current count of rows matching Name = <Name> (expect >= 1)

**Post-Check**
- **Navigate To**: `Standing Instructions page (refresh the page and/or use the Name filter/search with Name = <Name>)`
- **Observe**:
  - absence of any row with Name = <Name> in the Standing Instructions table
  - search/filter for Name = <Name> returns zero results or 'No results found' message
  - success notification displayed after deletion with text containing: 'removes standing instruction from listing' (if notification is ephemeral, rely on listing/search absence as primary proof)

**Expected Change**: The standing instruction with Name = <Name> is no longer present in the Standing Instructions listing or search results; the count of entries matching that Name decreased by 1 from pre-check; a deletion success notification was shown immediately after the action.

---

### [TC-003] Unauthenticated navigation to a protected page redirects to login
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <authenticated page URL> in the browser address bar and navigate to it

**Original Expected Result:** redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin -> Tax Management -> Tax Components page`
- **Observe**:
  - count of rows in the Tax Components table
  - list of Tax Component names currently visible (to confirm the to-be-created Name is not already present)

**Post-Check**
- **Navigate To**: `Admin -> Tax Management -> Tax Components page (use table search/filter by Name if not on first page); optionally click the created Tax Component to open its detail view`
- **Observe**:
  - count of rows in the Tax Components table
  - a Tax Component row with Name equal to the Name entered in the test
  - Percentage column value for that row equals the Percentage entered in the test
  - Debit Account (or Debit Account Type + selected GL account) displayed for that row matches the Debit selection made in the test
  - Credit Account (or Credit Account Type + selected GL account) displayed for that row matches the Credit selection made in the test
  - Start Date column value for that row equals the Start Date entered in the test
  - optionally, opening the Tax Component detail view shows the same Name, Percentage, Debit Account, Credit Account, and Start Date values

**Expected Change**: Row count increased by 1 and the Tax Components table contains a new row matching the values entered during creation: the Name entered in the test appears, the Percentage matches the entered percentage, the selected Debit Account/Account Type and Credit Account/Account Type are shown, and the Start Date matches. If a detail view is opened, the same field values are present there.

---

### [TC-006] Invoking Log Out endpoint while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Log Out endpoint/URL that the 'Log Out' button would call

**Original Expected Result:** Precondition prevents logout action: browser is redirected to the Login page; no logout success behavior occurs (no authenticated session existed and no session changes happen).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin -> Tax Management -> Tax Groups`
- **Observe**:
  - Tax Groups table is visible
  - absence or presence of a row with Name = '<valid name>' (should be absent prior to creation)

**Post-Check**
- **Navigate To**: `Admin -> Tax Management -> Tax Groups`
- **Observe**:
  - Tax Groups table
  - a row with Name = '<valid name>'
  - Associated Components column for that row showing '<matching Tax Component>'
  - the Start Date and End Date displayed for the associated component row

**Expected Change**: A new Tax Group row with Name = '<valid name>' appears in the Tax Groups table; its Associated Components column lists the added component '<matching Tax Component>' and the component row shows the configured Start Date and End Date.

---

### [TC-001] Open Profile Settings via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Profile Settings' in the dropdown

**Original Expected Result:** navigates to Profile Settings page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin > Organization > Holidays`
- **Observe**:
  - Search for holiday by name: <holiday name> (expect: no results / row not present)
  - Holidays table columns visible: Name, Start Date, To Date, Status, Rescheduling Type, Applicable Offices
  - If possible, note current count of rows or last created holiday to detect changes

**Post-Check**
- **Navigate To**: `Admin > Organization > Holidays`
- **Observe**:
  - Presence of a row with Name = <holiday name>
  - Start Date column value for that row = <from date>
  - To Date column value for that row = <to date>
  - Rescheduling Type column value for that row = <rescheduling type>
  - Applicable Offices column shows the selected <applicable offices> (one or more)
  - A success notification/toast containing the text 'creates holiday; installments falling on holidays are rescheduled per configured type' is displayed immediately after submission

**Expected Change**: A new holiday row appears in the Holidays table with Name = <holiday name>, Start Date = <from date>, To Date = <to date>, Rescheduling Type = <rescheduling type>, and Applicable Offices including the selected offices; a success notification with the configured rescheduling message is shown after submission.

---

### [TC-002] Log Out via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Log Out' in the dropdown

**Original Expected Result:** terminates authenticated session; clears authentication token; redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin > Organization > Funds`
- **Observe**:
  - Funds table rows (visible list)
  - absence or presence of a row with Fund Name = <fund name> and External ID = <external id>
  - current total number of rows (record count or pagination indicator)

**Post-Check**
- **Navigate To**: `Admin > Organization > Funds`
- **Observe**:
  - Funds table rows (visible list)
  - row with Fund Name = <fund name> and External ID = <external id>
  - total number of rows (record count or pagination indicator)

**Expected Change**: A new row exists in the Funds table with Fund Name equal to <fund name> and External ID equal to <external id>. If the pre-check showed that such a row was absent, the post-check shows it present and the total number of rows has increased by one (or the new row appears on the first page of results according to current sort/filter).

---

### [TC-003] Unauthenticated navigation to a protected page redirects to login
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <authenticated page URL> in the browser address bar and navigate to it

**Original Expected Result:** redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin -> Organization -> Payment Types; then open a representative transaction form (e.g., Client -> Savings Account -> Deposit)`
- **Observe**:
  - Payment Types table does NOT contain <payment type name>
  - Payment Types table columns visible: Name, Is Cash Payment, Is Active (if present), Position
  - Payment Type dropdown in the transaction form does NOT list <payment type name>

**Post-Check**
- **Navigate To**: `Admin -> Organization -> Payment Types; then open a representative transaction form (e.g., Client -> Savings Account -> Deposit)`
- **Observe**:
  - Payment Types table contains a row with Name = <payment type name>
  - The Is Cash Payment column for that row reflects the chosen checkbox state (checked or unchecked)
  - The Position column for that row shows <position>
  - Payment Type dropdown in the transaction form lists <payment type name> as a selectable option

**Expected Change**: A new Payment Type named '<payment type name>' exists in the Payment Types table with the configured Is Cash Payment state and Position, and the same name appears as a selectable option in Payment Type dropdowns on transaction forms (e.g., Deposit, Withdrawal, Disbursement); a success notification confirming creation was displayed after submission.

---

### [TC-004] Profile icon/menu inaccessible when unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application home page while not logged in
2. 2. Click the top-right Profile Icon

**Original Expected Result:** Profile Icon and profile menu are not available: the Profile Icon is not visible in the top-right; no dropdown opens; 'Profile Settings' and 'Log Out' options are not present or accessible. The user remains on the public/unauthenticated page (no authenticated UI is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin > Organization > Currencies`
- **Observe**:
  - Identify and record the currency rows that will be selected by name and currency code (e.g., 'US Dollar - USD')
  - For each identified currency row, record the current 'Is Active' value (e.g., Active/Inactive or toggle state) shown in the table
  - Record the displayed total count of active currencies (if a summary/count is shown) or note the number of rows with Active = true in the current table/view

**Post-Check**
- **Navigate To**: `Admin > Organization > Currencies (refresh page or navigate away and return to ensure persisted state)`
- **Observe**:
  - For each previously identified currency row, check the 'Is Active' column/toggle and the row checkbox state
  - Confirm the table row visually indicates active/selected state (active badge, toggle ON, or similar) for each selected currency
  - Record the displayed total count of active currencies (if available) or count rows with Active = true

**Expected Change**: Each currency row that was selected in the test is now marked Active (Is Active = true / active badge or toggle ON) and shows the active/selected state in the Currencies table; the total number of active currencies has increased by the number of currencies selected. These changes persist after refreshing or navigating away and back to the Currencies page.

---

### [TC-006] Invoking Log Out endpoint while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Log Out endpoint/URL that the 'Log Out' button would call

**Original Expected Result:** Precondition prevents logout action: browser is redirected to the Login page; no logout success behavior occurs (no authenticated session existed and no session changes happen).

---

#### Verification Plan

**Actor A (Role: `user with Bulk Import permission (e.g., admin)`)**
- **Action**: Execute the steps from the core test case: navigate to Admin > Organization > Bulk Import, upload the valid Clients import file for the Clients import card and confirm upload.

**Actor B (Role: `different user with Clients view permission (e.g., data officer)`)**
- **Session**: `new_session`
- **Navigate To**: `Admin > Organization > Bulk Import -> Clients import history, then navigate to Clients page (Clients listing)`
- **Action**: 
- **Observe**:
  - Import history row for Clients with Import Time matching the recent upload (most recent entry)
  - Import history columns: Completed status (e.g., 'Completed' or completed indicator), Total Records, Success Count, Failure Count, and Download/Results link
  - Clients listing table rows for clients present in the uploaded file showing Name, External ID (or other unique identifier from the file), and Status
  - If available, client detail page for an imported client showing Submitted On/Creation Date matching import time and status (e.g., 'Pending')

**Expected Change**: A new Clients import history entry exists for the uploaded file with status 'Completed' (or completed indicator); Success Count equals the number of records successfully imported (and Failure Count reflects any failed rows). The Clients listing contains the imported client records (matching External ID or Name from the file) and their status is the expected post-import status (typically 'Pending' if imports create pending clients).

---

### [TC-008] Rapid double-click Log Out
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Log in as a valid user
2. 2. Click the Profile Icon in the top-right corner
3. 3. Click the "Log Out" button
4. 4. Immediately click the "Log Out" button again

**Original Expected Result:** First click succeeds: authenticated session is terminated and the user is redirected to the login page. The immediate second click is ignored (no additional navigation or error shown) and only a single logout action takes effect.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin > Organization > Bulk Import`
- **Observe**:
  - Groups import card/row is present with Upload control enabled
  - Groups import history table (columns: Name, Import Time, End Time, Completed, Total Records, Success Count, Failure Count, Download)
  - value of the most recent Groups import history row (record its Import Time and Completed status) or the current count of import history rows
  - for each group name included in the selected import file: whether a group with that exact name already exists in Groups listing (navigate to Clients/Groups -> Groups page if needed) — record presence/absence

**Post-Check**
- **Navigate To**: `Admin > Organization > Bulk Import; then navigate to Groups page (Admin > Organization > Groups) for entity verification`
- **Observe**:
  - Groups import history table: a new entry with Import Time roughly matching the test run time appears as the most recent row
  - most recent entry fields: Completed = true (or Completed status indicating finished), Total Records equals the number of rows in the uploaded file, Success Count equals Total Records (or equals expected successful imports), Failure Count equals 0 (or equals expected failures if any)
  - Download link for the new import entry is available (for error file or result details)
  - Groups listing contains entries for each group name present in the uploaded import file (each group row shows Name, Account Number, Office, Status)
  - Opening the detail page for at least one imported group shows data populated from the import file (Office matches, Status is as expected — e.g., Active or Pending per template)

**Expected Change**: A new Groups import history entry exists with Import Time matching the upload, Completed status indicating the import finished, and Success Count equal to the number of records in the uploaded file (Failure Count zero if all succeeded). The Groups listing now includes the groups from the uploaded file (their names appear and their detail pages reflect the imported data).

---

### [TC-010] Log Out in one tab, then attempt Log Out in another tab (concurrent session edge)
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Tab A, click the Profile Icon
2. 2. In Tab A, click the "Log Out" button
3. 3. In Tab B, click the Profile Icon
4. 4. In Tab B, click the "Log Out" button

**Original Expected Result:** Logout in Tab A succeeds: Tab A is redirected to the login page and authentication token cleared. In Tab B, clicking "Log Out" succeeds in resulting in the login page (no error shown) but performs no additional session termination; Tab B is redirected to the login page as well.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin > Organization > Bulk Import -> Centers import history; Organization > Centers`
- **Observe**:
  - Existing Centers import history rows (Filename, Import Time, End Time, Completed, Total Records, Success Count, Failure Count) — note the latest entry if any
  - Count of centers currently present that match the names/External IDs in <valid Centers import file> (expect 0 if importing new centers)
  - Presence of any Centers with External IDs listed in <valid Centers import file>

**Post-Check**
- **Navigate To**: `Admin > Organization > Bulk Import -> Centers import history; Organization > Centers`
- **Observe**:
  - A new import history row for <import filename> with Import Time and End Time populated
  - For that import history row: Completed status (Completed = true), Total Records equals the number of rows in <valid Centers import file>, Success Count equals Total Records, Failure Count = 0 (for a fully successful import)
  - Centers listing contains entries for each Center from <valid Centers import file> with matching Name and External Id and associated Office
  - Import history 'Download' link is available for the import entry and clicking it (optional) returns the import result file (success/failure details)

**Expected Change**: A new Centers import history entry for <import filename> appears and shows Completed = true with Success Count equal to Total Records and Failure Count = 0; all centers defined in <valid Centers import file> are now present in Organization > Centers listing with matching Name and External Id (and associated Office) as specified in the import file.

---

### [TC-012] Move a code value up in ordering
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the Code Values Editor for <Code List Name>, click Move Up on the row for <entry A>

**Original Expected Result:** moves entry up in ordering and <entry A> is now displayed above the previous item in the list ordering

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin > Organization > Bulk Import (Offices import card) AND Admin > Organization > Offices listing`
- **Observe**:
  - Bulk Import -> Offices card: most recent import history entry (filename, status, timestamp) — confirm it does NOT include the file about to be uploaded
  - Bulk Import -> Offices card: current Completed/Failed/Total counts for the most recent entry (if any)
  - Offices listing: total number of office rows
  - Offices listing: verify that office names (or External IDs) present in the import file are NOT present prior to import

**Post-Check**
- **Navigate To**: `Admin > Organization > Bulk Import -> Offices import history AND Admin > Organization > Offices listing`
- **Observe**:
  - Bulk Import -> Offices import history: a new entry for the uploaded filename with status 'Completed' or 'Completed with failures', timestamp and Success Count/Failure Count/Total Records shown
  - Bulk Import -> Offices import history: ability to view/import details or download failed-records file (if failures occurred)
  - Offices listing: presence of office rows matching the office names/External IDs from the imported file
  - Offices listing: total number of office rows increased by the number of successfully imported offices

**Expected Change**: A new import history entry appears for the uploaded Offices file showing a Completed status (or Completed with failures) with Success Count > 0; the Offices listing contains the offices from the import file and the total rows count has increased by the number of successfully imported offices.

---

### [TC-014] Open Create Data Table form from Manage Data Tables
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Manage Data Tables
2. 2. Click Create Data Table (Create_Data_Table action)

**Original Expected Result:** Create_Data_Table form opens and the Create Data Table form is displayed with fields Data Table Name, Application Table Name, Multi Row, and Column Definitions

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `1) Admin > Organization > Bulk Import -> Staff import card / Import History; 2) Admin > Organization > Employees (Staff listing) or Employees page`
- **Observe**:
  - Bulk Import - Staff import history: latest entry (if any) showing File Name, Import Time, End Time, Completed/Status, Total Records, Success Count, Failure Count
  - Employees listing: current presence or absence of the staff records that will be in the import file (searchable by Username, External ID, or Full Name) and current total staff count

**Post-Check**
- **Navigate To**: `1) Admin > Organization > Bulk Import -> Staff import history; 2) Admin > Organization > Employees (Staff listing) -- use search/filter by Username or External ID from the uploaded file`
- **Observe**:
  - Success notification message shown after upload (text: 'file uploaded; Staff imported per template' or equivalent)
  - Bulk Import - Staff import history: a new row for the uploaded file appears with Import Time and End Time populated, Status/Completed indicator showing completed/success
  - Bulk Import - Staff import history: Total Records equals the number of rows in the uploaded file, Success Count equals Total Records (or shows expected successes), Failure Count is 0 (or shows any failed rows with details available for download)
  - Employees listing: the staff records from the uploaded file appear (searchable by Username, External ID, or Full Name) with expected attributes visible (Office, Is Loan Officer flag if set, Status Active/Inactive as per import, and any External ID)

**Expected Change**: A new import history entry for the uploaded Staff file appears with a completed/success status and matching success count; the staff records contained in the file are present in the Employees listing (searchable by Username/External ID) with their expected attributes; a success notification 'file uploaded; Staff imported per template' is displayed.

---

### [TC-016] Delete a custom data table with confirmation
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Manage Data Tables
2. 2. Click Delete for the <Data_Table_Name> row
3. 3. Click Confirm on the deletion confirmation dialog

**Original Expected Result:** deletes custom data table and the row for <Data_Table_Name> is no longer visible in the Manage Data Tables list

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin > Organization > Bulk Import (Users import row) and Admin > Users (Users listing)`
- **Observe**:
  - Bulk Import history: latest Users import row showing Import Time, End Time, Completed flag, Total Records, Success Count, Failure Count
  - Users listing: current count of users (or presence/absence of usernames/emails that will be in the import file)

**Post-Check**
- **Navigate To**: `Admin > Organization > Bulk Import (Users import row) and Admin > Users (Users listing)`
- **Observe**:
  - Bulk Import history: new/updated Users import row with Import Time and End Time populated, Completed flag set (e.g., 'Completed' or Completed = true), Total Records matching uploaded file, Success Count showing number of imported users, Failure Count = 0
  - Users listing: rows for each user from the uploaded file present (matching Username, First/Last Name or Email), and overall user count increased by the Success Count

**Expected Change**: A Users import history entry appears/updates with Completed status and End Time; Total Records equals the uploaded file row count and Success Count equals those imported (Failure Count 0 for a valid file). The Users listing contains new user records matching the import file (usernames/emails present) and the total number of users increased by the Success Count.

---

### [TC-018] Cancel Create Data Table form (Cancel)
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Create Data Table form, click Cancel

**Original Expected Result:** closes form without creating and the Create Data Table form is closed with no new row added to Manage Data Tables

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin > Organization > Bulk Import -> Loans (Import History)`
- **Observe**:
  - Latest Loans import entry (presence/status)
  - Success Count for latest Loans import
  - Failure Count for latest Loans import
  - Timestamp of latest Loans import
  - Count of Loans in Loans listing matching identifiers from the import file (search by External ID or Account No.)

**Post-Check**
- **Navigate To**: `Admin > Organization > Bulk Import -> Loans (Import History) and Loans -> All Loans listing (use search)`
- **Observe**:
  - A new Loans import history entry for the uploaded file
  - Status of that import entry (Completed / Failed / Completed with Errors)
  - Success Count and Failure Count for that import entry
  - Import completion timestamp
  - Loans listing search results for identifiers from the uploaded file (External ID or Account No.)

**Expected Change**: A new import history entry appears for the uploaded file with status 'Completed' (or 'Completed with Errors' if some records failed). The Success Count equals the number of successfully imported loan records (and Failure Count equals zero for a fully successful import). The import entry shows a recent completion timestamp. Corresponding loan accounts are present in the Loans listing (searching by the External ID or Account No. from the import file returns the newly created loan records).

---

### [TC-020] Reject an Audit Trail entry with an optional rejection reason
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Audit Trails
2. 2. Locate the audit row for <Action_Name> with Processing Result = Pending
3. 3. Click Reject for that audit row
4. 4. Enter <rejection reason> in the Rejection_Reason field (optional) and click Confirm

**Original Expected Result:** sets Processing Result to Rejected and the Processing Result column for the selected audit row displays 'Rejected'

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin > Organization > Bulk Import -> Savings import history`
- **Observe**:
  - latest Savings import entry (Filename, Upload Time, Status/Completed flag, Success Count, Failure Count)
  - total count of Savings accounts in system (or count of Savings accounts matching identifiers present in the import file if known)

**Post-Check**
- **Navigate To**: `Admin > Organization > Bulk Import -> Savings import history; optionally navigate to Clients/Savings Accounts listing to spot-created accounts`
- **Observe**:
  - a new Savings import history entry for the uploaded <valid Savings import file> showing Filename and Upload Time
  - the new entry's Status/Completed flag and Completion Time
  - the new entry's Success Count and Failure Count
  - the Savings accounts listing contains sample account(s) or account numbers present in the import file (or the total Savings accounts count increased by the Success Count)

**Expected Change**: A new import history row for the uploaded <valid Savings import file> appears with Status = 'Completed' and Success Count equal to the number of records in the file and Failure Count = 0; the system's Savings accounts reflect the import (the total number of Savings accounts increased by the Success Count and sample account(s) from the file are present in the Savings accounts listing).

---

### [TC-001] Open Profile Settings via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Profile Settings' in the dropdown

**Original Expected Result:** navigates to Profile Settings page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `System Administration -> Manage Scheduler Jobs (Global Scheduler Control visible on this page)`
- **Observe**:
  - Scheduler Enabled checkbox state (checked or unchecked)
  - Global Start/Stop toggle label/value
  - Next Run Time for job 'Apply Annual Fee'
  - Currently Running indicator for job 'Apply Annual Fee' (true/false)
  - Previous Run Status for job 'Apply Annual Fee' (Success/Failed and timestamp)

**Post-Check**
- **Navigate To**: `System Administration -> Manage Scheduler Jobs (Global Scheduler Control visible on this page)`
- **Observe**:
  - Scheduler Enabled checkbox state (checked or unchecked)
  - Global Start/Stop toggle label/value
  - Next Run Time for job 'Apply Annual Fee'
  - Currently Running indicator for job 'Apply Annual Fee' (true/false)
  - Previous Run Status for job 'Apply Annual Fee' (Success/Failed and timestamp)

**Expected Change**: The 'Scheduler Enabled' checkbox value is the inverse of the pre_check value (i.e., toggled). Corresponding system behavior must reflect that change: if scheduler was turned OFF, scheduled jobs (e.g., 'Apply Annual Fee') should show no future Next Run Time (cleared or marked not scheduled) and 'Currently Running' should be false; if scheduler was turned ON, scheduled jobs should show populated Next Run Time values consistent with their CRON schedules (future timestamp) and may show 'Currently Running' true if a job is active. The global toggle state displayed on the Manage Scheduler Jobs page must match the new checkbox state.

---

### [TC-002] Log Out via Profile Icon
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Profile Icon in the top-right corner to open the User Profile Menu
2. 2. Click 'Log Out' in the dropdown

**Original Expected Result:** terminates authenticated session; clears authentication token; redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `System Administration -> Manage Scheduler Jobs`
- **Observe**:
  - Is Active toggle state for <Job Name>
  - Next Run Time for <Job Name>
  - Previous Run Status for <Job Name>

**Post-Check**
- **Navigate To**: `System Administration -> Manage Scheduler Jobs`
- **Observe**:
  - Is Active toggle state for <Job Name>
  - Next Run Time for <Job Name>
  - Previous Run Status for <Job Name>

**Expected Change**: The Is Active toggle state for <Job Name> is flipped compared to the pre_check state and remains persisted after navigation/refresh. If toggled to Active the table shows the Is Active toggle ON and the Next Run Time is populated; if toggled to Inactive the toggle shows OFF and the Next Run Time is cleared or blank.

---

### [TC-003] Unauthenticated navigation to a protected page redirects to login
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <authenticated page URL> in the browser address bar and navigate to it

**Original Expected Result:** redirects to login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `System Administration > Manage Scheduler Jobs`
- **Observe**:
  - presence of a job row for <Job Name>
  - current CRON Expression value for <Job Name> (record this as pre-edit value)

**Post-Check**
- **Navigate To**: `System Administration > Manage Scheduler Jobs (refresh the page or navigate away and return to ensure persisted backend state)`
- **Observe**:
  - CRON Expression value for <Job Name>
  - job row for <Job Name> still present

**Expected Change**: The CRON Expression for <Job Name> is updated from the pre-edit value to <valid CRON expression> and the new expression persists after page refresh/navigation.

---

### [TC-004] Profile icon/menu inaccessible when unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application home page while not logged in
2. 2. Click the top-right Profile Icon

**Original Expected Result:** Profile Icon and profile menu are not available: the Profile Icon is not visible in the top-right; no dropdown opens; 'Profile Settings' and 'Log Out' options are not present or accessible. The user remains on the public/unauthenticated page (no authenticated UI is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `System Administration > Manage Scheduler Jobs`
- **Observe**:
  - Locate the row for <Job Name>
  - CRON Expression column value for <Job Name> (record the current value)
  - Next Run Time column value for <Job Name> (record the current value)
  - Is Active / Currently Running indicators for <Job Name>

**Post-Check**
- **Navigate To**: `System Administration > Manage Scheduler Jobs (refresh the page or re-run search if necessary)`
- **Observe**:
  - Locate the row for <Job Name>
  - CRON Expression column value for <Job Name>
  - Next Run Time column value for <Job Name>
  - Is Active / Currently Running indicators for <Job Name>

**Expected Change**: The CRON Expression for <Job Name> is updated to <valid CRON expression>. The Next Run Time is recalculated and updated consistent with the new CRON expression. Active/Currently Running indicators remain appropriate (not unexpectedly changed) for the job.

---

### [TC-005] Direct navigation to Profile Settings while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Profile Settings page URL

**Original Expected Result:** Auth Guard blocks access: browser is redirected to the Login page; Profile Settings content is not displayed and no profile settings UI elements are visible.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `System Administration -> Global Configuration`
- **Observe**:
  - Enabled checkbox state for <Configuration_Name> (checked or unchecked)
  - Configuration row displays Configuration Name and current Value/Description

**Post-Check**
- **Navigate To**: `System Administration -> Global Configuration, then System Administration -> Audit Trails`
- **Observe**:
  - Enabled checkbox state for <Configuration_Name> (checked or unchecked) in the Global Configuration listing
  - Audit Trails table entry for the change with fields: Action Name (e.g., 'Update Global Configuration'), Entity Name ('Global Configuration'), Resource ID or Configuration Name matching <Configuration_Name>, Maker (current user), Made On Date/Timestamp, and a description showing previous and new enabled state

**Expected Change**: The Enabled checkbox state for <Configuration_Name> is inverted compared to the pre_check state (i.e., toggled). Additionally, an audit trail entry exists recording the toggle with the current user as the actor and showing the previous and new enabled states and a timestamp.

---

### [TC-006] Invoking Log Out endpoint while unauthenticated is blocked
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the browser address bar, navigate to the Log Out endpoint/URL that the 'Log Out' button would call

**Original Expected Result:** Precondition prevents logout action: browser is redirected to the Login page; no logout success behavior occurs (no authenticated session existed and no session changes happen).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `System Administration -> Global Configuration`
- **Observe**:
  - presence of row for <Configuration_Name>
  - current Value shown in the Value column for <Configuration_Name> (record this as pre_value)

**Post-Check**
- **Navigate To**: `System Administration -> Global Configuration`
- **Observe**:
  - presence of row for <Configuration_Name>
  - Value shown in the Value column for <Configuration_Name>

**Expected Change**: The Value column for <Configuration_Name> displays <valid configuration value>; this value should match the value entered during the inline edit and differ from pre_value if the pre-check recorded a different value.

---

### [TC-007] Using browser Back after Log Out does not return to authenticated pages
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the Login page
2. 2. Enter <valid credentials> in the Username/Email field
3. 3. Enter <valid password> in the Password field
4. 4. Click the Login button
5. 5. Navigate to a protected page (e.g., Dashboard) while logged in
6. 6. Click the Profile Icon
7. 7. Click the 'Log Out' button in the profile menu
8. 8. After the application redirects to the Login page, click the browser Back button to return to the previously viewed protected page

**Original Expected Result:** After logout the protected page remains inaccessible: Auth Guard immediately redirects to the Login page; protected page content is not displayed; the user remains logged out (authentication token/session cleared).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `System Administration > Global Configuration`
- **Observe**:
  - Enabled state of <Configuration_Name>
  - Value of <Configuration_Name>

**Post-Check**
- **Navigate To**: `System Administration > Global Configuration`
- **Observe**:
  - Enabled state of <Configuration_Name>
  - Value of <Configuration_Name>

**Expected Change**: Enabled state for <Configuration_Name> is now set to <enabled state> and Value is now set to <valid configuration value>; these should reflect the saved changes (i.e., Enabled changed from the pre_check value to <enabled state> and Value changed from the pre_check value to <valid configuration value>).

---

### [TC-009] Browser Back after Log Out should not return to protected page
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. From the protected page, click the Profile Icon
2. 2. Click the "Log Out" button
3. 3. Wait for redirect to the login page
4. 4. Press the browser Back button

**Original Expected Result:** Navigation back to the protected page is blocked: Auth_Guard redirects to the login page and the protected page is not displayed. The back navigation is effectively blocked and the login page is shown.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin -> Manage Codes -> Select <Code List Name> -> Open Code Values Editor`
- **Observe**:
  - list of rows in the Code Values Editor (count)
  - presence/absence of an entry with Value = <new entry value> (should be absent before test)
  - Is Active value for any existing row with Value = <new entry value> (should be absent)

**Post-Check**
- **Navigate To**: `Admin -> Manage Codes -> Select <Code List Name> -> Open Code Values Editor`
- **Observe**:
  - list of rows in the Code Values Editor (count)
  - row with Value = <new entry value>
  - Is Active column value for the row with Value = <new entry value>

**Expected Change**: A new row appears in the Code Values Editor for <Code List Name> with Value = <new entry value> and its Is Active column reflecting the chosen state; the total row count is increased by 1 compared to the pre-check.

---

### [TC-010] Log Out in one tab, then attempt Log Out in another tab (concurrent session edge)
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Tab A, click the Profile Icon
2. 2. In Tab A, click the "Log Out" button
3. 3. In Tab B, click the Profile Icon
4. 4. In Tab B, click the "Log Out" button

**Original Expected Result:** Logout in Tab A succeeds: Tab A is redirected to the login page and authentication token cleared. In Tab B, clicking "Log Out" succeeds in resulting in the login page (no error shown) but performs no additional session termination; Tab B is redirected to the login page as well.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin -> Manage Codes -> <Code List Name> -> Values Editor`
- **Observe**:
  - presence of a row with Value = <existing value>
  - Is Active status for that row (e.g., active/inactive chip or checkbox)
  - total number of rows in the Values Editor for <Code List Name>

**Post-Check**
- **Navigate To**: `Admin -> Manage Codes -> <Code List Name> -> Values Editor`
- **Observe**:
  - presence of a row with Value = <updated value>
  - Is Active status for that row (reflects the change made)
  - total number of rows in the Values Editor for <Code List Name> (should match pre-check unless a uniqueness conflict prevented the update)

**Expected Change**: The row that previously showed Value = <existing value> now shows Value = <updated value>; the Is Active column for that row reflects the new state. The total count of code values remains the same (no duplicate/new row created) unless the update was blocked due to uniqueness constraints.

---

### [TC-011] Profile menu and Profile Settings access when user is unauthenticated
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is logged out (if not, perform Log Out)
2. 2. Observe whether the Profile Icon is visible in the top-right corner
3. 3. In the browser address bar, manually navigate to the Profile Settings page URL and press Enter

**Original Expected Result:** Profile Icon is not visible when unauthenticated (no dropdown available). Direct navigation to the Profile Settings URL is blocked: Auth_Guard redirects to the login page and the Profile Settings page is not displayed.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin -> Manage Codes -> Open Code List: <Code List Name> -> Code Values Editor`
- **Observe**:
  - row with Value = <existing value> is present in the list
  - Is Active column / active indicator for the row with Value = <existing value> shows checked or 'Active'

**Post-Check**
- **Navigate To**: `Admin -> Manage Codes -> Open Code List: <Code List Name> -> Code Values Editor (refresh if necessary)`
- **Observe**:
  - row with Value = <existing value> is present in the list
  - Is Active column / active indicator for the row with Value = <existing value> shows unchecked or 'Inactive'

**Expected Change**: The code value row for Value = <existing value> is now marked inactive: the Is Active checkbox is unchecked or an inactive indicator is shown for that row (i.e., its active status changed from active to inactive).

---

### [TC-012] Move a code value up in ordering
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the Code Values Editor for <Code List Name>, click Move Up on the row for <entry A>

**Original Expected Result:** moves entry up in ordering and <entry A> is now displayed above the previous item in the list ordering

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin -> Manage Codes -> <Code List Name> -> Code Values Editor`
- **Observe**:
  - visible ordered list of code values for <Code List Name>
  - position/index of '<entry A>'
  - position/index of '<entry B>'
  - relative ordering showing '<entry A>' appears below '<entry B>'

**Post-Check**
- **Navigate To**: `Admin -> Manage Codes -> <Code List Name> -> Code Values Editor (refresh view if necessary)`
- **Observe**:
  - visible ordered list of code values for <Code List Name>
  - position/index of '<entry A>'
  - position/index of '<entry B>'
  - relative ordering showing '<entry A>' appears above '<entry B>'

**Expected Change**: '<entry A>' has moved up in the ordering so that it now appears immediately above '<entry B>' (its index/position decreased by one compared to the pre-check).

---

### [TC-013] Move a code value down in ordering
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In the Code Values Editor for <Code List Name>, click Move Down on the row for <entry B>

**Original Expected Result:** moves entry down in ordering and <entry B> is now displayed below the previous item in the list ordering

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin -> Manage Codes -> Open Code Values Editor for <Code List Name>`
- **Observe**:
  - visible ordering of code values in the list
  - row for <entry B> (capture current row index and the label of the row immediately above and below)
  - row for <entry C> (capture current row index and the label of the row immediately above and below)

**Post-Check**
- **Navigate To**: `Admin -> Manage Codes -> Open Code Values Editor for <Code List Name>`
- **Observe**:
  - visible ordering of code values in the list
  - row for <entry B> (capture current row index and the label of the row immediately above and below)
  - row for <entry C> (capture current row index and the label of the row immediately above and below)

**Expected Change**: <entry B> now appears immediately below <entry C> (i.e., <entry B> row index increased by one relative to pre_check and the adjacent neighbor ordering reflects that <entry B> moved down one position).

---

### [TC-016] Delete a custom data table with confirmation
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Manage Data Tables
2. 2. Click Delete for the <Data_Table_Name> row
3. 3. Click Confirm on the deletion confirmation dialog

**Original Expected Result:** deletes custom data table and the row for <Data_Table_Name> is no longer visible in the Manage Data Tables list

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `System Administration > Manage Data Tables`
- **Observe**:
  - presence of row with Data Table Name: <Data_Table_Name>
  - total number of custom data tables (count) shown in the list

**Post-Check**
- **Navigate To**: `System Administration > Manage Data Tables`
- **Observe**:
  - absence of row with Data Table Name: <Data_Table_Name>
  - total number of custom data tables (count) shown in the list

**Expected Change**: The row for <Data_Table_Name> is no longer present in the Manage Data Tables list and the total count of custom data tables has decreased by one compared to pre-check.

---

### [TC-017] Submit Create Data Table form with columns (Create)
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Create Data Table form, enter Data Table Name = <data table name>
2. 2. Select Application Table Name = <application table> from the dropdown
3. 3. Optionally check Multi Row
4. 4. Click Add Row in Column Definitions, then for the new column enter Name = <column name>, Type = <column type>, set Length/Is Mandatory/Is Unique as needed
5. 5. Click Create

**Original Expected Result:** New row appears in Manage Data Tables with the entered Data Table Name and Application Table Name and the Create Data Table form closes

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Admin -> Manage Data Tables`
- **Observe**:
  - Listing of existing data tables (rows visible)
  - No row exists with Data Table Name = <data table name> and Application Table Name = <application table>

**Post-Check**
- **Navigate To**: `Admin -> Manage Data Tables`
- **Observe**:
  - A row with Data Table Name = <data table name>
  - Application Table Name column for that row shows = <application table>
  - Multi Row indicator for that row matches the option selected during creation (checked if Multi Row was selected, unchecked otherwise)
  - Opening the new data table's detail displays Column Definitions and includes a column with Name = <column name>, Type = <column type>, and the configured Length / Is Mandatory / Is Unique attributes

**Expected Change**: A new row appears in the Manage Data Tables listing with Data Table Name set to <data table name> and Application Table Name set to <application table>; the Create Data Table form is closed; the row's Multi Row indicator reflects the selection made during creation; opening the created data table shows the defined column(s) including <column name> with type <column type> and the configured Length, Is Mandatory, and Is Unique attributes.

---

### [TC-019] Approve an Audit Trail entry when maker-checker is enabled and Processing Result is Pending
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Audit Trails
2. 2. Locate the audit row for <Action_Name> with Processing Result = Pending
3. 3. Click Approve for that audit row

**Original Expected Result:** sets Processing Result to Approved and the Processing Result column for the selected audit row displays 'Approved'

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `System Administration > Audit Trails`
- **Observe**:
  - row where Action Name = <Action_Name>
  - Processing Result column value for that row (expected 'Pending')
  - Checker column for that row (expected empty/null)
  - Checked On Date column for that row (expected empty/null)
  - Maker and Made On Date values for that row (record of who created the pending command)

**Post-Check**
- **Navigate To**: `System Administration > Audit Trails`
- **Observe**:
  - row where Action Name = <Action_Name>
  - Processing Result column value for that row
  - Checker column for that row
  - Checked On Date column for that row

**Expected Change**: The selected audit row's Processing Result changes from 'Pending' to 'Approved'; the Checker field is populated with the approver's username and the Checked On Date is populated with the approval timestamp (previously blank).

---

### [TC-020] Reject an Audit Trail entry with an optional rejection reason
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to System Administration > Audit Trails
2. 2. Locate the audit row for <Action_Name> with Processing Result = Pending
3. 3. Click Reject for that audit row
4. 4. Enter <rejection reason> in the Rejection_Reason field (optional) and click Confirm

**Original Expected Result:** sets Processing Result to Rejected and the Processing Result column for the selected audit row displays 'Rejected'

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `System Administration > Audit Trails`
- **Observe**:
  - presence of an audit row with Action Name = <Action_Name>
  - Processing Result column for that row shows 'Pending'
  - Checker column for that row is empty
  - Checked On Date column for that row is empty

**Post-Check**
- **Navigate To**: `System Administration > Audit Trails`
- **Observe**:
  - Processing Result column for the audit row with Action Name = <Action_Name> shows 'Rejected'
  - Checker column shows the rejecting user's username (the Administrator who performed the reject)
  - Checked On Date column is populated with a timestamp
  - Audit record/detail shows Rejection Reason = <rejection reason> if a reason was entered

**Expected Change**: Processing Result for the audit row with Action Name = <Action_Name> changes from 'Pending' to 'Rejected'; the Checker and Checked On Date fields are populated with the rejecting user's identity and timestamp; the Rejection Reason is recorded and visible in the audit record if provided.

---
