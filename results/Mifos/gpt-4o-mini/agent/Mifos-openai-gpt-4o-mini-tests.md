# Test Cases — Mifos

Generated: 2026-06-04T14:20:14.442705Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 31 | 497 | 153 | 179 | 165 | 245 | 186 | 58 |

## Login

Total: **9** (positive: 1, negative: 2, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful login with valid credentials | User logged in as <User> | 1. Enter <valid username> in the Username field<br>2. Enter <valid password> in the Password field<br>3. Click Login | User is redirected to Dashboard | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-002 | Attempt to login with empty Username and Password fields |  | 1. Leave the Username field blank<br>2. Leave the Password field blank<br>3. Click Login | Inline validation error appears on the Username and Password fields indicating 'Please fill in all required fields' | high |
| TC-003 | WF-003 | Attempt to login with invalid credentials |  | 1. Enter <invalid username> in the Username field<br>2. Enter <invalid password> in the Password field<br>3. Click Login | Page displays 'Invalid credentials' and the Password field is cleared | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (boundary) | WF-002 | Login attempt with empty Username and Password fields |  | 1. Leave the Username field empty<br>2. Leave the Password field empty<br>3. Click the Login button | Inline validation message 'Please fill in all required fields' is shown | medium |
| TC-005 (boundary) | WF-003 | Login attempt with valid Username but invalid Password |  | 1. Enter a valid Username in the Username field<br>2. Enter an invalid Password in the Password field<br>3. Click the Login button | Error message 'Invalid credentials' is shown | medium |
| TC-006 (boundary) | WF-003 | Login attempt with invalid Username and valid Password |  | 1. Enter an invalid Username in the Username field<br>2. Enter a valid Password in the Password field<br>3. Click the Login button | Error message 'Invalid credentials' is shown | medium |
| TC-007 (input_edge) |  | Login attempt with long Username and Password |  | 1. Enter a long string (200+ characters) in the Username field<br>2. Enter a long string (200+ characters) in the Password field<br>3. Click the Login button | The system handles the input without crashing, and appropriate error messages are shown if credentials are invalid | low |
| TC-008 (input_edge) |  | Login attempt with special characters in Username and Password |  | 1. Enter special characters in the Username field<br>2. Enter special characters in the Password field<br>3. Click the Login button | The system handles the input without crashing, and appropriate error messages are shown if credentials are invalid | low |
| TC-009 (input_edge) |  | Login attempt with leading/trailing whitespace in Username and Password |  | 1. Enter '   validUsername   ' in the Username field<br>2. Enter '   validPassword   ' in the Password field<br>3. Click the Login button | Leading/trailing whitespace is trimmed; if credentials are valid, user is redirected to the Dashboard | low |

---

## Home Page

Total: **5** (positive: 1, negative: 1, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Access the Dashboard from Home Page | User logged in as <Role> | 1. Click on the Dashboard button | redirects to dashboard | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to access the dashboard without being logged in | User is not authenticated | 1. Attempt to click the Dashboard button | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | Rapid re-submission after redirect | User is logged in successfully | 1. Click the Dashboard button | User is redirected to the dashboard; clicking the back button shows a blank home page. | medium |
| TC-004 (input_edge) |  | Long text input in Search Activity field | User is on the Home Page | 1. Enter a string of 200+ characters in the Search Activity input field | Input is accepted or truncated with a visible indicator. | low |
| TC-005 (input_edge) |  | Special characters in Search Activity field | User is on the Home Page | 1. Enter special characters (e.g., !@#$%^&*) in the Search Activity input field | Input is accepted or a specific error is shown. | low |

---

## Dashboard

Total: **14** (positive: 5, negative: 5, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Access the Dashboard | User logged in as <Role> | 1. Click the Dashboard button on the Home page | navigates to Dashboard | high |
| TC-002 | WF-002 | Search Activity on Dashboard | User logged in as <Role>, Dashboard is accessed | 1. Enter <search term> in the Search Activity field | Search results displayed | medium |
| TC-003 | WF-003 | View Client Trends Chart | User logged in as <Role>, Dashboard is accessed, data is available for selected office |  | Client trends visualized | medium |
| TC-004 | WF-004 | View Amount Pending Disbursed | User logged in as <Role>, Dashboard is accessed, data is available for selected office |  | Amount pending/disbursed displayed | medium |
| TC-005 | WF-005 | View Amount Collected | User logged in as <Role>, Dashboard is accessed, data is available for selected office |  | Amount collected displayed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-001 | Attempt to access Dashboard without data available |  | 1. Click the 'Dashboard' button on the Home page | Dashboard does not display; 'No Data' is shown for Client Trends Chart and Summary Cards | high |
| TC-007 | WF-002 | Attempt to search activity without accessing Dashboard |  | 1. Leave the Dashboard without clicking the 'Dashboard' button<br>2. Attempt to use the 'Search Activity' field | 'Search Activity' field is not visible; no search results displayed | high |
| TC-008 | WF-003 | Attempt to view Client Trends Chart without data available |  | 1. Click the 'Dashboard' button on the Home page | Client Trends Chart displays 'No Data' | high |
| TC-009 | WF-004 | Attempt to view Amount Pending Disbursed without data available |  | 1. Click the 'Dashboard' button on the Home page | Amount Pending / Disbursed card displays 'No Data' | high |
| TC-010 | WF-005 | Attempt to view Amount Collected without data available |  | 1. Click the 'Dashboard' button on the Home page | Amount Collected card displays 'No Data' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (input_edge) | WF-002 | Enter a very long search term in the Search Activity field | Dashboard is accessed | 1. Enter a string of 200+ characters in the Search Activity field | Search results displayed or input is truncated with an indicator | low |
| TC-012 (interaction_edge) | WF-003 | Access Dashboard and check Client Trends Chart without data | Dashboard is accessed | 1. Access the Dashboard<br>2. Verify the Client Trends Chart | Client Trends Chart displays 'No Data' message | medium |
| TC-013 (interaction_edge) | WF-004 | Access Dashboard and check Amount Pending Disbursed without data | Dashboard is accessed | 1. Access the Dashboard<br>2. Verify Amount Pending/Disbursed card | Amount Pending/Disbursed card displays 'No Data' message | medium |
| TC-014 (interaction_edge) | WF-005 | Access Dashboard and check Amount Collected without data | Dashboard is accessed | 1. Access the Dashboard<br>2. Verify Amount Collected card | Amount Collected card displays 'No Data' message | medium |

---

## Global Search

Total: **10** (positive: 3, negative: 3, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open search input field | User logged in as <Role> | 1. Click on the search icon in the top toolbar | Search input field is opened | high |
| TC-002 | WF-002 | Search across Clients, Groups, Loans, and Savings accounts | User logged in as <Role>, Search input field is opened | 1. Enter <valid search term> in the search input field | Searches across Clients, Groups, Loans, and Savings accounts | high |
| TC-003 | WF-003 | Display no results found message | User logged in as <Role>, Search input field is opened | 1. Enter <non-matching search term> in the search input field | No results found | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Unauthenticated user attempts to access search input |  | 1. Attempt to click on the Search Icon | User is redirected to the login page | high |
| TC-005 |  | Search input is left blank and submitted | user is logged in | 1. Click on the Search Icon<br>2. Leave the Search Input blank<br>3. Submit the search | No results found message is displayed | medium |
| TC-006 |  | Search with invalid input format | user is logged in | 1. Click on the Search Icon<br>2. Enter <invalid input format> in the Search Input<br>3. Submit the search | No results found message is displayed | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) | WF-002 | Search with a partial match at the edge of the input length | User is logged in | 1. Click on the Search Icon<br>2. Enter a partial string that matches the beginning of an entity name<br>3. Observe the search results | Search results display matching entities based on the partial input | medium |
| TC-008 (boundary) | WF-003 | Search with an input that has no matches | User is logged in | 1. Click on the Search Icon<br>2. Enter a string that does not match any entity<br>3. Observe the search results | No results found message is displayed | medium |
| TC-009 (input_edge) |  | Search with special characters | User is logged in | 1. Click on the Search Icon<br>2. Enter a string with special characters<br>3. Observe the search results | Search results display based on the input with special characters or an appropriate error message | low |
| TC-010 (input_edge) |  | Search with leading and trailing whitespace | User is logged in | 1. Click on the Search Icon<br>2. Enter a string with leading and trailing spaces<br>3. Observe the search results | Leading and trailing whitespace is trimmed; search results display correctly | low |

---

## Client Management

Total: **29** (positive: 14, negative: 9, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Bulk Import page | User logged in as <role> | 1. Click 'Import Client' button | Bulk Import page opens | high |
| TC-002 | WF-002 | Open Create Client wizard | User logged in as <role> | 1. Click 'Create Client' button | Create Client wizard opens | high |
| TC-003 | WF-003 | Submit Create Client wizard | User logged in as <role>, Create Client wizard is open | 1. Enter <valid office> in the Office field<br>2. Enter <valid first name> in the First Name field<br>3. Enter <valid last name> in the Last Name field<br>4. Enter <valid submission date> in the Submitted On field<br>5. Enter <unique external ID> in the External ID field<br>6. Click 'Submit' button | creates client in Pending status | high |
| TC-004 | WF-004 | Activate Pending Client | User logged in as <role>, Client is in Pending status | 1. Click 'Activate' button<br>2. Enter <valid activation date> in the Activation Date field<br>3. Click 'Confirm' on the Activation dialog | Client activated | high |
| TC-005 | WF-005 | Edit Pending Client | User logged in as <role>, Client is in Pending status | 1. Click 'Edit' button<br>2. Update <field> with <new value><br>3. Click 'Save' button | Client details updated | medium |
| TC-006 | WF-006 | Reject Pending Client | User logged in as <role>, Client is in Pending status | 1. Click 'Reject' button<br>2. Enter <valid reason> in the Reason field<br>3. Click 'Confirm' on the Reject dialog | Client rejected | medium |
| TC-007 | WF-007 | Withdraw Pending Client | User logged in as <role>, Client is in Pending status | 1. Click 'Withdraw' button<br>2. Enter <valid reason> in the Reason field<br>3. Click 'Confirm' on the Withdraw dialog | Client withdrawn | medium |
| TC-008 | WF-008 | Transfer Active Client | User logged in as <role>, Client is in Active status | 1. Click 'Transfer Client' button<br>2. Enter <valid destination office> in the Destination Office field<br>3. Click 'Confirm' on the Transfer dialog | Client transferred | medium |
| TC-009 | WF-009 | Close Active Client | User logged in as <role>, Client is in Active status | 1. Click 'Close' button<br>2. Enter <valid closure reason> in the Closure Reason field<br>3. Click 'Confirm' on the Close dialog | Client closed | medium |
| TC-010 | WF-010 | Add Charge to Active Client | User logged in as <role>, Client is in Active status | 1. Click 'Add Charge' button<br>2. Enter <valid charge details><br>3. Click 'Confirm' on the Add Charge dialog | Charge added to client | medium |
| TC-011 | WF-011 | Create New Loan for Active Client | User logged in as <role>, Client is in Active status | 1. Click 'New Loan' button<br>2. Enter <valid loan details><br>3. Click 'Confirm' on the New Loan dialog | New loan created for client | medium |
| TC-012 | WF-012 | Create New Savings for Active Client | User logged in as <role>, Client is in Active status | 1. Click 'New Savings' button<br>2. Enter <valid savings details><br>3. Click 'Confirm' on the New Savings dialog | New savings account created for client | medium |
| TC-013 | WF-013 | Create New Share Account for Active Client | User logged in as <role>, Client is in Active status | 1. Click 'New Share Account' button<br>2. Enter <valid share account details><br>3. Click 'Confirm' on the New Share Account dialog | New share account created for client | medium |
| TC-014 | WF-014 | Reactivate Closed Client | User logged in as <role>, Client is in Closed status | 1. Click 'Reactivate' button<br>2. Click 'Confirm' on the Reactivate dialog | Client reactivated | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 | WF-001 | Attempt to import client without uploading a file |  | 1. Navigate to the Bulk Import page<br>2. Leave the Upload File field blank<br>3. Click Import | Inline validation error appears on the Upload_File field indicating it is required | high |
| TC-016 | WF-003 | Submit Create Client Wizard without filling required fields |  | 1. Navigate to the Create Client wizard<br>2. Leave the Office field blank<br>3. Leave the First Name field blank<br>4. Leave the Last Name field blank<br>5. Leave the Submitted On field blank<br>6. Click Submit | Form does not submit; Client is not created; error shown on Office, First_Name, Last_Name, and Submitted_On fields indicating they are required | high |
| TC-017 | WF-003 | Submit Create Client Wizard with duplicate External ID |  | 1. Navigate to the Create Client wizard<br>2. Fill in the Office field with a valid value<br>3. Fill in the First Name field with a valid value<br>4. Fill in the Last Name field with a valid value<br>5. Fill in the Submitted On field with a valid date<br>6. Enter a value in the External ID field that already exists<br>7. Click Submit | Form does not submit; Client is not created; error shown on External_ID field indicating 'must be unique' | high |
| TC-018 | WF-004 | Attempt to activate a client with an Activation Date before submission date |  | 1. Navigate to the Client Detail page of a Pending client<br>2. Click Activate<br>3. Enter an Activation Date that is before the Submitted On date<br>4. Click Submit | Form does not submit; Client is not activated; error shown on Activation_Date field indicating it must not be before submission date | high |
| TC-019 | WF-009 | Attempt to close an Active client with active accounts |  | 1. Navigate to the Client Detail page of an Active client<br>2. Click Close<br>3. Enter a Closure Reason<br>4. Click Submit | Form does not submit; Client is not closed; error shown indicating cannot close with active accounts | high |
| TC-020 | WF-006 | Reject a Pending client without providing a reason |  | 1. Navigate to the Client Detail page of a Pending client<br>2. Click Reject<br>3. Leave the Reason field blank<br>4. Click Submit | Form does not submit; Client is not rejected; error shown on Reason field indicating it is required | high |
| TC-021 | WF-007 | Withdraw a Pending client without providing a reason |  | 1. Navigate to the Client Detail page of a Pending client<br>2. Click Withdraw<br>3. Leave the Reason field blank<br>4. Click Submit | Form does not submit; Client is not withdrawn; error shown on Reason field indicating it is required | high |
| TC-022 | WF-008 | Transfer an Active client to the same office |  | 1. Navigate to the Client Detail page of an Active client<br>2. Click Transfer Client<br>3. Select the same office as the current office<br>4. Click Submit | Form does not submit; Client is not transferred; error shown indicating cannot transfer to the same office | high |
| TC-023 | WF-014 | Reactivate a Closed client without any action |  | 1. Navigate to the Client Detail page of a Closed client<br>2. Click Reactivate | No action is taken; Client remains Closed; no reactivation occurs | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-024 (boundary) | WF-004 | Activate client with Activation Date equal to Submitted On date | Client is in Pending status, Submitted On date is set | 1. Navigate to Client Detail page<br>2. Click Activate button<br>3. Enter Activation Date equal to Submitted On date<br>4. Click Submit | Client is activated successfully | medium |
| TC-025 (boundary) | WF-004 | Activate client with Activation Date one day before Submitted On date | Client is in Pending status, Submitted On date is set | 1. Navigate to Client Detail page<br>2. Click Activate button<br>3. Enter Activation Date one day before Submitted On date<br>4. Click Submit | Activation is blocked; error shown indicating 'Activation Date must not be before submission date' | medium |
| TC-026 (input_edge) |  | Upload a file exactly at the size limit for client import | User is on Bulk Import page | 1. Click on Upload_File field<br>2. Select a file that is exactly at the size limit<br>3. Click Submit | File uploads successfully with a visible success indicator | low |
| TC-027 (input_edge) |  | Upload a file one byte over the size limit for client import | User is on Bulk Import page | 1. Click on Upload_File field<br>2. Select a file that is one byte over the size limit<br>3. Click Submit | File upload is blocked; error shown indicating size constraint | low |
| TC-028 (input_edge) |  | Enter a very long string in the External ID field | User is on Create Client wizard, step 1 | 1. Enter a string longer than the maximum allowed length in the External ID field<br>2. Fill all other required fields<br>3. Click Submit | Submission is blocked; error shown indicating the length constraint for External ID | low |
| TC-029 (input_edge) |  | Enter External ID with leading and trailing whitespace | User is on Create Client wizard, step 1 | 1. Enter '   uniqueID   ' in the External ID field<br>2. Fill all other required fields<br>3. Click Submit | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Group Management

Total: **22** (positive: 8, negative: 8, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new group successfully | User logged in as <Role> | 1. Click 'Create Group' button<br>2. Enter <valid group name> in the Name field<br>3. Select <valid office> from the Office dropdown<br>4. Enter <valid date> in the Submitted On field<br>5. Click Submit | The group is created | high |
| TC-002 | WF-002 | Upload groups via bulk import successfully | User logged in as <Role>, On the Bulk Import Groups page | 1. Click 'Choose File' on the File Picker<br>2. Select a <valid file> for upload<br>3. Click Upload_Button | Groups imported successfully | high |
| TC-003 | WF-003 | Activate a group successfully | User logged in as <Role>, Group is in 'Pending' status | 1. Click Activate button | Group activated | medium |
| TC-004 | WF-004 | Edit group details successfully | User logged in as <Role>, Group details are displayed | 1. Click Edit button<br>2. Update <valid field> in the group details<br>3. Click Submit | Group details updated | medium |
| TC-005 | WF-005 | Close a group successfully | User logged in as <Role>, Group is in 'Active' status | 1. Click Close button<br>2. Confirm closure | Group closed | medium |
| TC-006 | WF-006 | Assign staff to a group successfully | User logged in as <Role>, Group is displayed | 1. Click Assign Staff button<br>2. Select <valid staff> from the dropdown<br>3. Click Submit | Staff assigned to group | medium |
| TC-007 | WF-007 | Transfer clients from a group successfully | User logged in as <Role>, Group is displayed | 1. Click Transfer Clients button<br>2. Select <valid clients> to transfer<br>3. Click Submit | Clients transferred from group | medium |
| TC-008 | WF-008 | View group details successfully | User logged in as <Role>, On the Groups page | 1. Click on the Group Name link | Group details displayed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 | WF-001 | Leave the Name field blank and submit the Create Group form |  | 1. Leave the Name field blank<br>2. Fill in the Office field with a valid value<br>3. Fill in the Submitted On field with a valid value<br>4. Click Submit | Inline validation error appears on the Name field indicating it is required | high |
| TC-010 | WF-001 | Leave the Office field blank and submit the Create Group form |  | 1. Fill in the Name field with a valid value<br>2. Leave the Office field blank<br>3. Fill in the Submitted On field with a valid value<br>4. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-011 | WF-001 | Leave the Submitted On field blank and submit the Create Group form |  | 1. Fill in the Name field with a valid value<br>2. Fill in the Office field with a valid value<br>3. Leave the Submitted On field blank<br>4. Click Submit | Inline validation error appears on the Submitted On field indicating it is required | high |
| TC-012 | WF-001 | Submit the Create Group form with all required fields empty |  | 1. Leave the Name field blank<br>2. Leave the Office field blank<br>3. Leave the Submitted On field blank<br>4. Click Submit | Form does not submit; error shown on Name, Office, and Submitted On fields | high |
| TC-013 | WF-002 | Leave the File Picker blank and click Upload on the Bulk Import Groups page |  | 1. Leave the File Picker blank<br>2. Click Upload_Button | Inline validation error appears on the File Picker field indicating it is required | high |
| TC-014 | WF-003 | Attempt to activate a group that is already active |  | 1. Navigate to the Group Detail Page of an active group<br>2. Click Activate | Status remains Active; no transition occurs | medium |
| TC-015 | WF-005 | Attempt to close a group that is already closed |  | 1. Navigate to the Group Detail Page of a closed group<br>2. Click Close | Status remains Closed; no transition occurs | medium |
| TC-016 | WF-006 | Attempt to assign staff to a group that has no staff assigned |  | 1. Navigate to the Group Detail Page of a group with no staff assigned<br>2. Click Assign Staff | No staff can be assigned; action is blocked | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-017 (boundary) | WF-001 | Create group with minimum required fields |  | 1. Enter a valid value in the Name field<br>2. Enter a valid value in the Office field<br>3. Enter a valid value in the Submitted On field<br>4. Click Submit | Form submits successfully; entity is created with the minimum required fields | medium |
| TC-018 (boundary) | WF-001 | Create group with empty required fields |  | 1. Leave the Name field empty<br>2. Leave the Office field empty<br>3. Leave the Submitted On field empty<br>4. Click Submit | Form is blocked; error messages are shown for missing required fields | medium |
| TC-019 (boundary) | WF-002 | Upload file exactly at size limit |  | 1. Select a file exactly at the maximum size limit for upload<br>2. Click Upload_Button | File upload succeeds; confirmation message is displayed | medium |
| TC-020 (boundary) | WF-002 | Upload file exceeding size limit |  | 1. Select a file that exceeds the maximum size limit for upload<br>2. Click Upload_Button | File upload is blocked; error message indicates the file size limit | medium |
| TC-021 (input_edge) |  | Enter long text in Name field |  | 1. Enter a string longer than 200 characters in the Name field<br>2. Fill other required fields with valid values<br>3. Click Submit | Form submits successfully; saved value in detail page shows the long text correctly | low |
| TC-022 (input_edge) |  | Enter special characters in Office field |  | 1. Enter special characters in the Office field<br>2. Fill other required fields with valid values<br>3. Click Submit | Form submits successfully; saved value in detail page shows the special characters correctly | low |

---

## Center Management

Total: **20** (positive: 7, negative: 7, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new center successfully | User logged in as <Role> | 1. Click 'Create Center' button<br>2. Enter <valid center name> in the Name field<br>3. Enter <valid office name> in the Office field<br>4. Enter <valid date> in the Submitted On field<br>5. Click Submit | A success notification is displayed; the center is created | high |
| TC-002 | WF-002 | Bulk import centers successfully | User logged in as <Role> | 1. Click 'Import Center' button<br>2. Upload a valid centers file<br>3. Click Submit | A success notification is displayed; centers are imported | high |
| TC-003 | WF-003 | View center details | User logged in as <Role>, At least one center exists | 1. Click on the center name in the Centers table | Center details are displayed | medium |
| TC-004 | WF-004 | Activate a center | User logged in as <Role>, Center is in Active state | 1. Click Activate on the Center Detail page | A success notification is displayed; the center is activated | medium |
| TC-005 | WF-005 | Edit a center | User logged in as <Role>, Center is in Active state | 1. Click Edit on the Center Detail page<br>2. Modify <valid field> with <new value><br>3. Click Submit | A success notification is displayed; the center is edited | medium |
| TC-006 | WF-006 | Close a center | User logged in as <Role>, Center is in Active state | 1. Click Close on the Center Detail page<br>2. Confirm the closure | A success notification is displayed; the center is closed | medium |
| TC-007 | WF-007 | Assign staff to a center | User logged in as <Role>, Center is in Active state | 1. Click Assign Staff on the Center Detail page<br>2. Select <valid staff member> from the dropdown<br>3. Click Submit | A success notification is displayed; staff is assigned to the center | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 | WF-001 | Leave the Name field blank and submit the Create Center form |  | 1. Leave the Name field blank<br>2. Fill in the Office field with a valid value<br>3. Fill in the Submitted On field with a valid date<br>4. Click Submit | Inline validation error appears on the Name field indicating it is required | high |
| TC-009 | WF-001 | Leave the Office field blank and submit the Create Center form |  | 1. Fill in the Name field with a valid value<br>2. Leave the Office field blank<br>3. Fill in the Submitted On field with a valid date<br>4. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-010 | WF-001 | Leave the Submitted On field blank and submit the Create Center form |  | 1. Fill in the Name field with a valid value<br>2. Fill in the Office field with a valid value<br>3. Leave the Submitted On field blank<br>4. Click Submit | Inline validation error appears on the Submitted On field indicating it is required | high |
| TC-011 | WF-002 | Attempt to submit the Bulk Import Centers form without any file uploaded |  | 1. Leave the file upload field blank<br>2. Click Submit | Form does not submit; error shown indicating a file must be uploaded | high |
| TC-012 | WF-004 | Attempt to activate a center that is already Active |  | 1. Attempt to activate a center that is already in Active state | Status remains Active; no transition occurs; error shown indicating the center is already active | medium |
| TC-013 | WF-006 | Attempt to close a center that is already Active |  | 1. Attempt to close a center that is already in Active state | Status remains Active; no transition occurs; error shown indicating the center cannot be closed while active | medium |
| TC-014 | WF-007 | Attempt to assign staff to a center that is already Active |  | 1. Attempt to assign staff to a center that is already in Active state | Status remains Active; no transition occurs; error shown indicating staff cannot be assigned to an active center | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-015 (boundary) | WF-001 | Submit Create Center form with minimum required fields |  | 1. Enter a valid value in the Name field<br>2. Enter a valid value in the Office field<br>3. Enter a valid date in the Submitted On field<br>4. Click Submit | Form submits successfully; center is created | medium |
| TC-016 (boundary) | WF-001 | Submit Create Center form with empty required fields |  | 1. Leave the Name field empty<br>2. Leave the Office field empty<br>3. Leave the Submitted On field empty<br>4. Click Submit | Form submission is blocked; error messages are shown for required fields | medium |
| TC-017 (boundary) | WF-002 | Submit Bulk Import Centers form with valid file size limit |  | 1. Upload a file that meets the size requirements for bulk import<br>2. Click Submit | Form submits successfully; centers are imported | medium |
| TC-018 (boundary) | WF-002 | Submit Bulk Import Centers form with file exceeding size limit |  | 1. Upload a file that exceeds the size limit for bulk import<br>2. Click Submit | Form submission is blocked; error message indicates file size limit exceeded | medium |
| TC-019 (state_edge) | WF-004 | Rapidly transition center state from Active to Activate |  | 1. Activate a center<br>2. Immediately attempt to activate the same center again | Action is blocked; user is notified that the center is already active | medium |
| TC-020 (state_edge) | WF-006 | Rapidly transition center state from Active to Close |  | 1. Close a center<br>2. Immediately attempt to close the same center again | Action is blocked; user is notified that the center is already closed | medium |

---

## Loan Products

Total: **25** (positive: 8, negative: 11, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Loan Product Detail | User logged in as <Role> | 1. Click on the Name of an existing loan product in the data table | opens detail view | high |
| TC-002 | WF-002 | Edit Loan Product | User logged in as <Role> | 1. Click on the Edit option of an existing loan product in the data table | opens detail view | high |
| TC-003 | WF-003 | Create Loan Product - Step 1 Submit | User logged in as <Role>, User is on the Loan Products page | 1. Click '+ Create Loan Product' button<br>2. Enter <Product Name> in the Product Name field<br>3. Enter <Short Name> in the Short Name field<br>4. Click Next to proceed to Step 2 | proceeds to Step 2 | high |
| TC-004 | WF-004 | Create Loan Product - Step 2 Submit | User logged in as <Role>, User is on Step 2 of the Create Loan Product stepper | 1. Select <Currency> from the Currency Selection dropdown<br>2. Enter <Decimal Places> in the Decimal Places field<br>3. Enter <Multiples of Rounding> in the Multiples of Rounding field<br>4. Enter <Principal Amount> in the Principal Amount field<br>5. Click Next to proceed to Step 3 | proceeds to Step 3 | high |
| TC-005 | WF-005 | Create Loan Product - Step 3 Submit | User logged in as <Role>, User is on Step 3 of the Create Loan Product stepper | 1. Select <Repayment Strategy> from the Repayment Strategy dropdown<br>2. Enter <Grace Period> in the Grace Period field<br>3. Enter <Arrears Tolerance> in the Arrears Tolerance field<br>4. Click Next to proceed to Step 4 | proceeds to Step 4 | high |
| TC-006 | WF-006 | Create Loan Product - Step 4 Submit | User logged in as <Role>, User is on Step 4 of the Create Loan Product stepper | 1. Enter <Number of Repayments> in the Number of Repayments field<br>2. Select <Repaid Every> from the Repaid Every dropdown<br>3. Enter <Nominal Interest Rate> in the Nominal Interest Rate field<br>4. Click Next to proceed to Step 5 | proceeds to Step 5 | high |
| TC-007 | WF-007 | Create Loan Product - Step 5 Submit | User logged in as <Role>, User is on Step 5 of the Create Loan Product stepper | 1. Search for <Charge> in the Search and Add Charges field<br>2. Select <Charge> from the search results<br>3. Click Next to proceed to Step 6 | proceeds to Step 6 | high |
| TC-008 | WF-008 | Create Loan Product - Step 6 Submit | User logged in as <Role>, User is on Step 6 of the Create Loan Product stepper | 1. Select <Accounting Method> from the Accounting Method radio options<br>2. Click Submit to create the loan product | Loan product created; success message shown | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 | WF-003 | Leave Product Name blank and submit |  | 1. Leave the Product Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Product Name field indicating it is required | high |
| TC-010 | WF-003 | Leave Short Name blank and submit |  | 1. Leave the Short Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Short Name field indicating it is required | high |
| TC-011 | WF-004 | Leave Currency Selection blank and submit |  | 1. Fill all required fields in Step 1<br>2. Leave the Currency Selection field blank<br>3. Click Submit | Inline validation error appears on the Currency Selection field indicating it is required | high |
| TC-012 | WF-004 | Leave Decimal Places blank and submit |  | 1. Fill all required fields in Step 1<br>2. Fill Currency Selection<br>3. Leave the Decimal Places field blank<br>4. Click Submit | Inline validation error appears on the Decimal Places field indicating it is required | high |
| TC-013 | WF-004 | Leave Multiples of Rounding blank and submit |  | 1. Fill all required fields in Step 1<br>2. Fill Currency Selection<br>3. Fill Decimal Places<br>4. Leave the Multiples of Rounding field blank<br>5. Click Submit | Inline validation error appears on the Multiples of Rounding field indicating it is required | high |
| TC-014 | WF-006 | Leave Repaid Every blank and submit |  | 1. Fill all required fields in Steps 1-4<br>2. Leave the Repaid Every field blank<br>3. Click Submit | Inline validation error appears on the Repaid Every field indicating it is required | high |
| TC-015 | WF-008 | Attempt to create loan product without filling required fields |  | 1. Leave all required fields blank in Steps 1-6<br>2. Click Submit | Form does not submit; loan product is not created; inline validation errors shown on all required fields | high |
| TC-016 | WF-008 | Attempt to create loan product with invalid Principal Amount |  | 1. Fill all required fields in Steps 1-4<br>2. Enter <negative amount> in the Principal Amount field<br>3. Click Submit | Inline validation error appears on the Principal Amount field indicating it must be a positive number | medium |
| TC-017 | WF-008 | Attempt to create loan product with invalid Number of Repayments |  | 1. Fill all required fields in Steps 1-4<br>2. Enter <negative number> in the Number of Repayments field<br>3. Click Submit | Inline validation error appears on the Number of Repayments field indicating it must be a positive number | medium |
| TC-018 | WF-008 | Attempt to create loan product with invalid Grace Period |  | 1. Fill all required fields in Steps 1-4<br>2. Enter <negative number> in the Grace Period field<br>3. Click Submit | Inline validation error appears on the Grace Period field indicating it must be a positive number | medium |
| TC-019 | WF-008 | Attempt to create loan product with invalid Arrears Tolerance |  | 1. Fill all required fields in Steps 1-4<br>2. Enter <negative number> in the Arrears Tolerance field<br>3. Click Submit | Inline validation error appears on the Arrears Tolerance field indicating it must be a positive number | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-020 (boundary) | WF-003 | Submit Step 1 with minimum required Product Name length |  | 1. Enter minimum allowed value in the Product Name field<br>2. Enter minimum allowed value in the Short Name field<br>3. Click Submit | Form submits successfully; proceeds to Step 2 | medium |
| TC-021 (boundary) | WF-003 | Submit Step 1 with one character less than minimum required Product Name length |  | 1. Enter one character less than minimum allowed value in the Product Name field<br>2. Enter minimum allowed value in the Short Name field<br>3. Click Submit | Inline error shown for Product Name indicating it is required | medium |
| TC-022 (boundary) | WF-004 | Submit Step 2 with minimum allowed Principal Amount |  | 1. Select a currency in the Currency Selection field<br>2. Enter minimum allowed value in the Principal Amount field<br>3. Enter minimum allowed value in the Decimal Places field<br>4. Enter minimum allowed value in the Multiples of Rounding field<br>5. Click Submit | Form submits successfully; proceeds to Step 3 | medium |
| TC-023 (boundary) | WF-004 | Submit Step 2 with one unit below minimum allowed Principal Amount |  | 1. Select a currency in the Currency Selection field<br>2. Enter one unit below minimum allowed value in the Principal Amount field<br>3. Enter minimum allowed value in the Decimal Places field<br>4. Enter minimum allowed value in the Multiples of Rounding field<br>5. Click Submit | Inline error shown for Principal Amount indicating it is below the minimum allowed | medium |
| TC-024 (boundary) | WF-006 | Submit Step 4 with minimum allowed Number of Repayments |  | 1. Enter minimum allowed value in the Number of Repayments field<br>2. Select a frequency in the Repaid Every field<br>3. Enter minimum allowed value in the Nominal Interest Rate field<br>4. Click Submit | Form submits successfully; proceeds to Step 5 | medium |
| TC-025 (boundary) | WF-006 | Submit Step 4 with one unit below minimum allowed Number of Repayments |  | 1. Enter one unit below minimum allowed value in the Number of Repayments field<br>2. Select a frequency in the Repaid Every field<br>3. Enter minimum allowed value in the Nominal Interest Rate field<br>4. Click Submit | Inline error shown for Number of Repayments indicating it is below the minimum allowed | medium |

---

## Savings Products

Total: **16** (positive: 3, negative: 6, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create Savings Product successfully | User logged in as <Role> | 1. Click '+ Create Savings Product' button<br>2. Enter <valid product name> in the Product Name field<br>3. Enter <valid short name> in the Short Name field<br>4. Click Next to proceed to the Currency step<br>5. Click Next to proceed to the Terms step<br>6. Click Next to proceed to the Settings step<br>7. Click Next to proceed to the Charges step<br>8. Click Next to proceed to the Accounting step<br>9. Select 'None' for Accounting Method<br>10. Click Submit | Page shows 'Savings product created successfully' | high |
| TC-002 | WF-002 | Create Fixed Deposit Product successfully | User logged in as <Role> | 1. Click '+ Create Savings Product' button<br>2. Enter <valid product name> in the Product Name field<br>3. Enter <valid short name> in the Short Name field<br>4. Click Next to proceed to the Currency step<br>5. Click Next to proceed to the Terms step<br>6. Click Next to proceed to the Settings step<br>7. Click Next to proceed to the Pre-Closure step<br>8. Click Next to proceed to the Deposit Term step<br>9. Click Next to proceed to the Interest Rate Chart step<br>10. Click Submit | Page shows 'Fixed deposit product created successfully' | high |
| TC-003 | WF-003 | Create Recurring Deposit Product successfully | User logged in as <Role> | 1. Click '+ Create Savings Product' button<br>2. Enter <valid product name> in the Product Name field<br>3. Enter <valid short name> in the Short Name field<br>4. Click Next to proceed to the Currency step<br>5. Click Next to proceed to the Terms step<br>6. Click Next to proceed to the Settings step<br>7. Click Next to proceed to the Charges step<br>8. Click Next to proceed to the Accounting step<br>9. Select 'None' for Accounting Method<br>10. Click Next to proceed to the Mandatory Deposit step<br>11. Click Submit | Page shows 'Recurring deposit product created successfully' | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Leave Product Name blank and submit |  | 1. Leave the Product_Name field blank<br>2. Fill Short_Name with a valid value<br>3. Click Submit | Inline validation error appears on the Product_Name field indicating it is required | high |
| TC-005 | WF-001 | Leave Short Name blank and submit |  | 1. Leave the Short_Name field blank<br>2. Fill Product_Name with a valid value<br>3. Click Submit | Inline validation error appears on the Short_Name field indicating it is required | high |
| TC-006 | WF-001 | Submit with all required fields empty |  | 1. Leave the Product_Name field blank<br>2. Leave the Short_Name field blank<br>3. Click Submit | Form does not submit; error shown on Product_Name and Short_Name fields | high |
| TC-007 | WF-001 | Select Cash-based accounting without filling GL Account Mappings |  | 1. Select Accounting_Method as Cash-based<br>2. Click Submit | Inline validation error appears on the GL Account Mappings fields indicating they are required | high |
| TC-008 | WF-002 | Leave Product Name blank in Fixed Deposit Product wizard and submit |  | 1. Leave the Product_Name field blank<br>2. Fill Short_Name with a valid value<br>3. Click Submit | Inline validation error appears on the Product_Name field indicating it is required | high |
| TC-009 | WF-003 | Leave Product Name blank in Recurring Deposit Product wizard and submit |  | 1. Leave the Product_Name field blank<br>2. Fill Short_Name with a valid value<br>3. Click Submit | Inline validation error appears on the Product_Name field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) | WF-001 | Test Minimum Required Balance at the exact minimum value | User is on the Create Savings Product wizard | 1. Enter <minimum required balance> in the Minimum Required Balance field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; entity is created with the <minimum required balance> | medium |
| TC-011 (boundary) | WF-001 | Test Minimum Required Balance just below the minimum value | User is on the Create Savings Product wizard | 1. Enter <one unit below minimum required balance> in the Minimum Required Balance field<br>2. Fill all other required fields<br>3. Click Submit | Submission is blocked; error message indicates the value is below the minimum allowed | medium |
| TC-012 (boundary) | WF-001 | Test Maximum Deposit Amount at the exact maximum value | User is on the Create Savings Product wizard | 1. Enter <maximum deposit amount> in the Maximum Deposit Amount field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; entity is created with the <maximum deposit amount> | medium |
| TC-013 (boundary) | WF-001 | Test Maximum Deposit Amount just above the maximum value | User is on the Create Savings Product wizard | 1. Enter <one unit above maximum deposit amount> in the Maximum Deposit Amount field<br>2. Fill all other required fields<br>3. Click Submit | Submission is blocked; error message indicates the value exceeds the maximum allowed | medium |
| TC-014 (input_edge) | WF-001 | Enter a very long string in the Product Name field | User is on the Create Savings Product wizard | 1. Enter a string longer than 200 characters in the Product Name field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is either accepted or a visible error is shown indicating the length issue | low |
| TC-015 (input_edge) | WF-001 | Enter special characters in the Short Name field | User is on the Create Savings Product wizard | 1. Enter special characters in the Short Name field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is either accepted or a specific error is shown | low |
| TC-016 (interaction_edge) | WF-001 | Rapid re-submission after successful creation of Savings Product | User has successfully submitted the form and is redirected to the detail page | 1. Press the browser back button<br>2. Attempt to submit the form again | User is redirected to the detail page without a second entity being created | low |

---

## Share Products

Total: **23** (positive: 3, negative: 13, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new share product successfully | User logged in as <Role> | 1. Click '+ Create Share Product' button<br>2. Enter <valid product name> in the Product Name field<br>3. Enter <valid short name> in the Short Name field<br>4. Enter <valid description> in the Description field<br>5. Click Next to proceed to the Currency step<br>6. Click Next to proceed to the Terms step<br>7. Enter <valid total number of shares> in the Total Number of Shares field<br>8. Enter <valid nominal unit price> in the Nominal Unit Price field<br>9. Click Next to proceed to the Settings step<br>10. Enter <valid minimum shares per client> in the Minimum Shares per Client field<br>11. Enter <valid nominal shares per client> in the Nominal Shares per Client field<br>12. Enter <valid minimum active period frequency> in the Minimum Active Period Frequency field<br>13. Enter <valid lock-in period> in the Lock-in Period field<br>14. Click Next to proceed to the Market Price step<br>15. Click 'Add Row' in the Market Price section<br>16. Enter <valid from date> in the From Date field<br>17. Enter <valid share value> in the Share Value field<br>18. Click Next to proceed to the Charges step<br>19. Click Next to proceed to the Accounting step<br>20. Click Create to submit the share product | Share product created; success message shown | high |
| TC-002 | WF-002 | Edit an existing share product successfully | User logged in as <Role>, At least one share product exists | 1. Click on the Product Name of an existing share product<br>2. Click Edit<br>3. Update <valid product name> in the Product Name field<br>4. Update <valid short name> in the Short Name field<br>5. Update <valid description> in the Description field<br>6. Click Save | Product details updated; success message shown | high |
| TC-003 | WF-003 | Delete an existing share product successfully | User logged in as <Role>, At least one share product exists | 1. Click on the Product Name of an existing share product<br>2. Click Delete<br>3. Click Confirm on the Delete dialog | Product deleted; success message shown | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Leave Product Name blank and submit |  | 1. Click on '+ Create Share Product'<br>2. Leave the Product Name field blank<br>3. Fill in the Short Name and Description fields<br>4. Click Next | Inline validation error appears on the Product Name field indicating it is required | high |
| TC-005 | WF-001 | Leave Short Name blank and submit |  | 1. Click on '+ Create Share Product'<br>2. Fill in the Product Name and Description fields<br>3. Leave the Short Name field blank<br>4. Click Next | Inline validation error appears on the Short Name field indicating it is required | high |
| TC-006 | WF-001 | Leave Description blank and submit |  | 1. Click on '+ Create Share Product'<br>2. Fill in the Product Name and Short Name fields<br>3. Leave the Description field blank<br>4. Click Next | Inline validation error appears on the Description field indicating it is required | high |
| TC-007 | WF-001 | Leave Total Number of Shares blank and submit |  | 1. Click on '+ Create Share Product'<br>2. Fill in the Product Name, Short Name, Description<br>3. Leave the Total Number of Shares field blank<br>4. Fill in Nominal Unit Price<br>5. Click Next | Inline validation error appears on the Total Number of Shares field indicating it is required | high |
| TC-008 | WF-001 | Leave Nominal Unit Price blank and submit |  | 1. Click on '+ Create Share Product'<br>2. Fill in the Product Name, Short Name, Description<br>3. Fill in Total Number of Shares<br>4. Leave the Nominal Unit Price field blank<br>5. Click Next | Inline validation error appears on the Nominal Unit Price field indicating it is required | high |
| TC-009 | WF-001 | Leave Minimum Shares per Client blank and submit |  | 1. Click on '+ Create Share Product'<br>2. Fill in the Product Name, Short Name, Description<br>3. Fill in Total Number of Shares and Nominal Unit Price<br>4. Leave the Minimum Shares per Client field blank<br>5. Click Next | Inline validation error appears on the Minimum Shares per Client field indicating it is required | high |
| TC-010 | WF-001 | Leave Nominal Shares per Client blank and submit |  | 1. Click on '+ Create Share Product'<br>2. Fill in the Product Name, Short Name, Description<br>3. Fill in Total Number of Shares and Nominal Unit Price<br>4. Fill in Minimum Shares per Client<br>5. Leave the Nominal Shares per Client field blank<br>6. Click Next | Inline validation error appears on the Nominal Shares per Client field indicating it is required | high |
| TC-011 | WF-001 | Leave Minimum Active Period Frequency blank and submit |  | 1. Click on '+ Create Share Product'<br>2. Fill in the Product Name, Short Name, Description<br>3. Fill in Total Number of Shares and Nominal Unit Price<br>4. Fill in Minimum Shares per Client and Nominal Shares per Client<br>5. Leave the Minimum Active Period Frequency field blank<br>6. Click Next | Inline validation error appears on the Minimum Active Period Frequency field indicating it is required | high |
| TC-012 | WF-001 | Leave Lock-in Period blank and submit |  | 1. Click on '+ Create Share Product'<br>2. Fill in the Product Name, Short Name, Description<br>3. Fill in Total Number of Shares and Nominal Unit Price<br>4. Fill in Minimum Shares per Client and Nominal Shares per Client<br>5. Fill in Minimum Active Period Frequency<br>6. Leave the Lock-in Period field blank<br>7. Click Next | Inline validation error appears on the Lock-in Period field indicating it is required | high |
| TC-013 | WF-001 | Leave From Date blank in Market Price and submit |  | 1. Click on '+ Create Share Product'<br>2. Fill in the Product Name, Short Name, Description<br>3. Fill in Total Number of Shares and Nominal Unit Price<br>4. Fill in Minimum Shares per Client and Nominal Shares per Client<br>5. Fill in Minimum Active Period Frequency and Lock-in Period<br>6. Add a Market Price row and leave From Date blank<br>7. Fill in Share Value<br>8. Click Next | Inline validation error appears on the From Date field indicating it is required | high |
| TC-014 | WF-001 | Leave Share Value blank in Market Price and submit |  | 1. Click on '+ Create Share Product'<br>2. Fill in the Product Name, Short Name, Description<br>3. Fill in Total Number of Shares and Nominal Unit Price<br>4. Fill in Minimum Shares per Client and Nominal Shares per Client<br>5. Fill in Minimum Active Period Frequency and Lock-in Period<br>6. Add a Market Price row and fill in From Date<br>7. Leave Share Value blank<br>8. Click Next | Inline validation error appears on the Share Value field indicating it is required | high |
| TC-015 | WF-002 | Attempt to edit product without required fields filled |  | 1. Click on an existing product to edit<br>2. Leave all required fields blank<br>3. Click Save | Form does not submit; error shown on all required fields | high |
| TC-016 | WF-003 | Attempt to delete product without confirmation |  | 1. Click on an existing product<br>2. Click Delete<br>3. Attempt to delete without confirming | Product is not deleted; confirmation dialog remains open | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-017 (boundary) | WF-001 | Enter minimum allowed value for Total Number of Shares |  | 1. Click '+ Create Share Product' button<br>2. Enter <minimum allowed value> in the Total Number of Shares field<br>3. Fill all other required fields<br>4. Click Next | Form submits successfully; entity is created with the <minimum allowed value> | medium |
| TC-018 (boundary) | WF-001 | Enter one unit below minimum value for Total Number of Shares |  | 1. Click '+ Create Share Product' button<br>2. Enter <one unit below minimum> in the Total Number of Shares field<br>3. Fill all other required fields<br>4. Click Next | Total Number of Shares displays an error indicating the value is below the minimum allowed | medium |
| TC-019 (boundary) | WF-001 | Add maximum allowed entries to Market Price Rows |  | 1. Click '+ Create Share Product' button<br>2. Add exactly <maximum allowed entries> rows to the Market Price Rows<br>3. Fill all required fields in each row<br>4. Click Next | Form submits successfully; all entries are saved | medium |
| TC-020 (boundary) | WF-001 | Attempt to add one more entry to Market Price Rows than allowed |  | 1. Click '+ Create Share Product' button<br>2. Add <maximum allowed entries + 1> rows to the Market Price Rows<br>3. Fill all required fields in each row<br>4. Click Next | Adding one more entry is blocked; visible error shown indicating the maximum limit | medium |
| TC-021 (input_edge) |  | Enter a very long string in the Product Name field |  | 1. Click '+ Create Share Product' button<br>2. Enter a very long string (200+ characters) in the Product Name field<br>3. Fill all other required fields<br>4. Click Next | Product Name displays an error indicating the value exceeds the maximum allowed length or is accepted | low |
| TC-022 (input_edge) |  | Enter special characters in the Short Name field |  | 1. Click '+ Create Share Product' button<br>2. Enter special characters in the Short Name field<br>3. Fill all other required fields<br>4. Click Next | Short Name displays an error indicating invalid characters or is accepted | low |
| TC-023 (interaction_edge) |  | Rapidly navigate through wizard steps |  | 1. Click '+ Create Share Product' button<br>2. Fill all required fields in Step 1<br>3. Click Next<br>4. Immediately click Next again for Step 2<br>5. Click Next for Step 3 | Form submits successfully; user is taken to Step 3 without errors | medium |

---

## Charges

Total: **12** (positive: 3, negative: 5, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Charge Creation Form with valid data | User logged in as <Role> | 1. Click the '+ Create Charge' button<br>2. Enter <Charge Name> in the Charge Name field<br>3. Select 'Loan' from the Charge Applies To dropdown<br>4. Enter <Currency> in the Currency field<br>5. Select 'Disbursement' from the Charge Time Type dropdown<br>6. Select 'Flat' from the Charge Calculation Type dropdown<br>7. Enter <Amount> in the Amount field<br>8. Click Submit | A success notification is displayed; the charge definition is created. | high |
| TC-002 | WF-002 | Edit Charge from the Charges Table | User logged in as <Role>, At least one charge exists in the Charges Table | 1. Click the Name link of the existing charge in the Charges Table<br>2. Click the Edit button<br>3. Modify <Charge Name> in the Charge Name field<br>4. Click Submit | A success notification is displayed; the charge definition is updated. | medium |
| TC-003 | WF-003 | Delete Charge from the Charges Table | User logged in as <Role>, At least one charge exists in the Charges Table | 1. Click the Name link of the existing charge in the Charges Table<br>2. Click the Delete button<br>3. Confirm the deletion | The charge is deleted from the Charges Table. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Leave Charge Name blank and submit |  | 1. Click the '+ Create Charge' button<br>2. Leave the Charge Name field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Charge Name field indicating it is required | high |
| TC-005 | WF-001 | Leave Charge Applies To blank and submit |  | 1. Click the '+ Create Charge' button<br>2. Leave the Charge Applies To field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Charge Applies To field indicating it is required | high |
| TC-006 | WF-001 | Leave Currency blank and submit |  | 1. Click the '+ Create Charge' button<br>2. Leave the Currency field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Currency field indicating it is required | high |
| TC-007 | WF-001 | Leave Amount blank and submit |  | 1. Click the '+ Create Charge' button<br>2. Leave the Amount field blank<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Amount field indicating it is required | high |
| TC-008 | WF-001 | Submit with all required fields empty |  | 1. Click the '+ Create Charge' button<br>2. Leave all required fields blank<br>3. Click Submit | Form does not submit; Charge Name, Charge Applies To, Currency, and Amount fields display errors indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-001 | Submit Charge Creation Form with minimum amount | User is on the Charge Creation Form | 1. Enter a valid Charge Name in the Charge_Name field<br>2. Select 'Loan' from the Charge_Applies_To dropdown<br>3. Enter a valid Currency in the Currency field<br>4. Select a Charge Time Type from the dropdown<br>5. Select a Charge Calculation Type from the dropdown<br>6. Enter exactly <minimum allowed value> in the Amount field<br>7. Click Submit | Charge definition is created successfully. | medium |
| TC-010 (boundary) | WF-001 | Submit Charge Creation Form with amount below minimum | User is on the Charge Creation Form | 1. Enter a valid Charge Name in the Charge_Name field<br>2. Select 'Loan' from the Charge_Applies_To dropdown<br>3. Enter a valid Currency in the Currency field<br>4. Select a Charge Time Type from the dropdown<br>5. Select a Charge Calculation Type from the dropdown<br>6. Enter <one unit below minimum> in the Amount field<br>7. Click Submit | Form submission is blocked; an error message is displayed indicating the amount is below the minimum allowed. | medium |
| TC-011 (input_edge) | WF-001 | Submit Charge Creation Form with long Charge Name | User is on the Charge Creation Form | 1. Enter a very long string (200+ characters) in the Charge_Name field<br>2. Select 'Loan' from the Charge_Applies_To dropdown<br>3. Enter a valid Currency in the Currency field<br>4. Select a Charge Time Type from the dropdown<br>5. Select a Charge Calculation Type from the dropdown<br>6. Enter a valid amount in the Amount field<br>7. Click Submit | Form submission succeeds; the Charge Name is displayed correctly in the detail view. | low |
| TC-012 (input_edge) | WF-001 | Submit Charge Creation Form with special characters in Charge Name | User is on the Charge Creation Form | 1. Enter special characters in the Charge_Name field<br>2. Select 'Loan' from the Charge_Applies_To dropdown<br>3. Enter a valid Currency in the Currency field<br>4. Select a Charge Time Type from the dropdown<br>5. Select a Charge Calculation Type from the dropdown<br>6. Enter a valid amount in the Amount field<br>7. Click Submit | Form submission succeeds; the Charge Name is displayed correctly in the detail view. | low |

---

## Floating Rates

Total: **16** (positive: 3, negative: 5, edge: 8)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Floating Rate Details | User logged in as <Role> | 1. Click on the Floating Rate Name link in the Floating Rates Table | Floating rate details displayed | high |
| TC-002 | WF-002 | Create a New Floating Rate | User logged in as <Role> | 1. Click '+ Create Floating Rate' button<br>2. Enter <Floating Rate Name> in the Floating Rate Name field<br>3. Enter <From Date> in the Rate Periods table<br>4. Enter <Interest Rate> in the Rate Periods table<br>5. Click Submit | Floating rate created; success message shown | high |
| TC-003 | WF-003 | Edit Floating Rate | User logged in as <Role>, Floating rate details are displayed | 1. Click Edit on the Floating Rate Detail View<br>2. Modify <Floating Rate Name> in the Floating Rate Name field<br>3. Click Submit | Floating rate edited; success message shown | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-002 | Leave Floating Rate Name blank and submit |  | 1. Click on '+ Create Floating Rate' button<br>2. Leave the Floating Rate Name field blank<br>3. Fill all other required fields with valid data<br>4. Click Submit | Inline validation error appears on the Floating Rate Name field indicating it is required | high |
| TC-005 | WF-002 | Submit with all required fields empty |  | 1. Click on '+ Create Floating Rate' button<br>2. Leave all required fields empty<br>3. Click Submit | Form does not submit; Floating Rate Name field displays an error: 'Must be a valid value' | high |
| TC-006 | WF-002 | Enter invalid date in From Date field |  | 1. Click on '+ Create Floating Rate' button<br>2. Fill the Floating Rate Name with a valid value<br>3. Add a row in Rate Periods<br>4. Enter <invalid date format> in the From Date field<br>5. Enter a valid Interest Rate<br>6. Click Submit | Inline validation error appears on the From Date field indicating it must be a valid date | medium |
| TC-007 | WF-002 | Enter non-numeric value in Interest Rate field |  | 1. Click on '+ Create Floating Rate' button<br>2. Fill the Floating Rate Name with a valid value<br>3. Add a row in Rate Periods<br>4. Enter a valid From Date<br>5. Enter <non-numeric value> in the Interest Rate field<br>6. Click Submit | Inline validation error appears on the Interest Rate field indicating it must be a number | medium |
| TC-008 | WF-003 | Attempt to edit Floating Rate without proper permissions |  | 1. Navigate to the Floating Rates page<br>2. Click on the Edit button for a Floating Rate | User is blocked from editing; access denied message is displayed | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-002 | Add maximum allowed entries to Rate Periods | User is on the Create Floating Rate Form | 1. Add maximum allowed entries to the Rate Periods table | Form submits successfully; entity is created with the maximum allowed entries in Rate Periods | medium |
| TC-010 (boundary) | WF-002 | Attempt to add one more entry to Rate Periods | User is on the Create Floating Rate Form with maximum entries added | 1. Attempt to add one more entry to the Rate Periods table | Adding the entry is blocked; an error message is shown indicating the maximum limit has been reached | medium |
| TC-011 (boundary) | WF-002 | Enter today's date in From Date | User is on the Create Floating Rate Form | 1. Enter today's date in the From Date field of Rate Periods | Form submits successfully; today's date is accepted | medium |
| TC-012 (boundary) | WF-002 | Enter yesterday's date in From Date | User is on the Create Floating Rate Form | 1. Enter yesterday's date in the From Date field of Rate Periods | Form submits successfully; yesterday's date is accepted | medium |
| TC-013 (boundary) | WF-002 | Enter a negative Interest Rate | User is on the Create Floating Rate Form | 1. Enter a negative value in the Interest Rate field of Rate Periods | Form submission is blocked; an error message is shown indicating that the Interest Rate must be a positive value | medium |
| TC-014 (input_edge) |  | Enter a very long Floating Rate Name | User is on the Create Floating Rate Form | 1. Enter a very long string (200+ characters) in the Floating Rate Name field | Form submission is blocked; an error message is shown indicating the maximum length is exceeded | low |
| TC-015 (input_edge) |  | Enter special characters in Floating Rate Name | User is on the Create Floating Rate Form | 1. Enter special characters in the Floating Rate Name field | Form submission is blocked; an error message is shown indicating invalid characters | low |
| TC-016 (input_edge) |  | Enter leading/trailing whitespace in Floating Rate Name | User is on the Create Floating Rate Form | 1. Enter '  Rate Name  ' in the Floating Rate Name field | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Delinquency Management

Total: **14** (positive: 4, negative: 6, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Create Delinquency Range Form with valid data | User logged in as <Role> | 1. Open Create Delinquency Range Form<br>2. Enter <valid classification> in the Classification field<br>3. Enter <valid minimum age days> in the Minimum Age Days field<br>4. Enter <valid maximum age days> in the Maximum Age Days field<br>5. Click Submit | Delinquency range created; success message shown | high |
| TC-002 | WF-002 | Submit Create Delinquency Bucket Form with valid data | User logged in as <Role> | 1. Open Create Delinquency Bucket Form<br>2. Enter <valid bucket name> in the Bucket Name field<br>3. Click 'Add Range' to add a delinquency range<br>4. Enter <valid minimum age days> in the Minimum Age Days field of the new range<br>5. Enter <valid maximum age days> in the Maximum Age Days field of the new range<br>6. Click Submit | Delinquency bucket created; success message shown | high |
| TC-003 | WF-003 | View Classification details in Delinquency Ranges | User logged in as <Role> | 1. Navigate to Delinquency Ranges page<br>2. Click on the Classification link for a specific range | Classification details displayed | medium |
| TC-004 | WF-004 | View Bucket Name details in Delinquency Buckets | User logged in as <Role> | 1. Navigate to Delinquency Buckets page<br>2. Click on the Bucket Name link for a specific bucket | Bucket details displayed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Leave Classification field blank and submit Create Delinquency Range Form |  | 1. Leave the Classification field blank<br>2. Fill Minimum Age Days with a valid number<br>3. Click Submit | Inline validation error appears on the Classification field indicating it is required | high |
| TC-006 | WF-001 | Leave Minimum Age Days field blank and submit Create Delinquency Range Form |  | 1. Leave the Minimum Age Days field blank<br>2. Fill Classification with a valid value<br>3. Click Submit | Inline validation error appears on the Minimum Age Days field indicating it is required | high |
| TC-007 | WF-002 | Leave Bucket Name field blank and submit Create Delinquency Bucket Form |  | 1. Leave the Bucket Name field blank<br>2. Click Submit | Inline validation error appears on the Bucket Name field indicating it is required | high |
| TC-008 | WF-002 | Leave Minimum Age Days field blank in Delinquency Ranges and submit Create Delinquency Bucket Form |  | 1. Fill Bucket Name with a valid value<br>2. Leave Minimum Age Days field blank in Delinquency Ranges<br>3. Click Submit | Inline validation error appears on the Minimum Age Days field indicating it is required | high |
| TC-009 |  | Attempt to view Classification details without proper authentication |  | 1. Attempt to access the Classification link in Delinquency Ranges page | User is redirected to the login page | medium |
| TC-010 |  | Attempt to view Bucket Name details without proper authentication |  | 1. Attempt to access the Bucket Name link in Delinquency Buckets page | User is redirected to the login page | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) | WF-001 | Minimum Age Days boundary test |  | 1. Enter exactly 1 in the Minimum Age Days field<br>2. Fill in the Classification field with valid data<br>3. Click Submit | Form submits successfully; delinquency range is created with Minimum Age Days set to 1 | medium |
| TC-012 (boundary) | WF-001 | Minimum Age Days below boundary test |  | 1. Enter 0 in the Minimum Age Days field<br>2. Fill in the Classification field with valid data<br>3. Click Submit | Form submission is blocked; error shown indicating the value must be greater than 0 | medium |
| TC-013 (boundary) | WF-002 | Repeating group maximum entries test |  | 1. Fill in the Bucket Name field with valid data<br>2. Add exactly 5 delinquency ranges to the Delinquency Ranges repeating group<br>3. Click Submit | Form submits successfully; delinquency bucket is created with 5 delinquency ranges | medium |
| TC-014 (boundary) | WF-002 | Repeating group overflow test |  | 1. Fill in the Bucket Name field with valid data<br>2. Add 6 delinquency ranges to the Delinquency Ranges repeating group<br>3. Click Submit | Form submission is blocked; error shown indicating the maximum number of delinquency ranges has been exceeded | medium |

---

## Loan Account

Total: **27** (positive: 15, negative: 5, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Loan Application with valid details | User logged in as <Client>, Loan Application form is open | 1. Select <valid product> from the Product Name dropdown<br>2. Enter <Loan Officer> in the Loan Officer field<br>3. Enter <Loan Purpose> in the Loan Purpose field<br>4. Enter <Fund> in the Fund field<br>5. Enter <valid date> in the Submitted On field<br>6. Enter <valid date> in the Expected Disbursement Date field<br>7. Enter <valid principal amount> in the Principal field<br>8. Enter <valid number of repayments> in the Number of Repayments field<br>9. Enter <valid frequency> in the Repaid Every field<br>10. Enter <valid interest rate> in the Interest Rate field<br>11. Click Submit | Loan is created in Submitted and Pending Approval status | high |
| TC-002 | WF-002 | Approve Loan Application | User logged in as <Loan Officer>, Loan application is in Pending Approval status | 1. Click Approve on the Loan Detail page<br>2. Enter <valid date> in the Approved On Date field<br>3. Enter <valid amount> in the Approved Amount field<br>4. Enter <valid date> in the Expected Disbursement Date field<br>5. Click Confirm on the Approval dialog | Loan approved | high |
| TC-003 | WF-003 | Reject Loan Application | User logged in as <Loan Officer>, Loan application is in Pending Approval status | 1. Click Reject on the Loan Detail page<br>2. Click Confirm on the Reject dialog | Loan application rejected | high |
| TC-004 | WF-004 | Withdraw Loan Application | User logged in as <Client>, Loan application is in Pending Approval status | 1. Click Withdraw on the Loan Detail page<br>2. Click Confirm on the Withdraw dialog | Loan application withdrawn | high |
| TC-005 | WF-005 | Delete Loan Application | User logged in as <Loan Officer>, Loan application is in Pending Approval status | 1. Click Delete on the Loan Detail page<br>2. Click Confirm on the Delete dialog | Loan application deleted | high |
| TC-006 | WF-006 | Disburse Loan | User logged in as <Loan Officer>, Loan application is in Approved status | 1. Click Disburse on the Loan Detail page<br>2. Enter <valid date> in the Disbursed On Date field<br>3. Enter <valid amount> in the Transaction Amount field<br>4. Select <Payment Type> from the dropdown<br>5. Click Confirm on the Disburse dialog | Loan disbursed | high |
| TC-007 | WF-008 | Make Repayment | User logged in as <Client>, Loan application is in Active status | 1. Click Make Repayment on the Loan Detail page<br>2. Enter <valid date> in the Transaction Date field<br>3. Enter <valid amount> in the Transaction Amount field<br>4. Select <Payment Type> from the dropdown<br>5. Click Confirm on the Repayment dialog | Repayment made | high |
| TC-008 | WF-009 | Waive Interest | User logged in as <Loan Officer>, Loan application is in Active status | 1. Click Waive Interest on the Loan Detail page<br>2. Click Confirm on the Waive Interest dialog | Interest waived | high |
| TC-009 | WF-010 | Write Off Loan | User logged in as <Loan Officer>, Loan application is in Active status | 1. Click Write Off on the Loan Detail page<br>2. Click Confirm on the Write Off dialog | Loan written off | high |
| TC-010 | WF-011 | Close Loan | User logged in as <Loan Officer>, Loan application is in Active status | 1. Click Close on the Loan Detail page<br>2. Click Confirm on the Close dialog | Loan closed | high |
| TC-011 | WF-012 | Reschedule Loan | User logged in as <Loan Officer>, Loan application is in Active status | 1. Click Reschedule on the Loan Detail page<br>2. Enter <valid date> in the Reschedule From Date field<br>3. Enter <valid reason> in the Reason field<br>4. Enter <valid date> in the Adjusted Due Date field<br>5. Click Confirm on the Reschedule dialog | Loan rescheduled | high |
| TC-012 | WF-013 | Prepay Loan | User logged in as <Client>, Loan application is in Active status | 1. Click Prepay Loan on the Loan Detail page<br>2. Enter <valid amount> in the Transaction Amount field<br>3. Click Confirm on the Prepay Loan dialog | Loan prepayed | high |
| TC-013 | WF-014 | Foreclose Loan | User logged in as <Loan Officer>, Loan application is in Active status | 1. Click Foreclosure on the Loan Detail page<br>2. Click Confirm on the Foreclosure dialog | Loan foreclosed | high |
| TC-014 | WF-015 | Charge Off Loan | User logged in as <Loan Officer>, Loan application is in Active status | 1. Click Charge Off on the Loan Detail page<br>2. Click Confirm on the Charge Off dialog | Loan charged off | high |
| TC-015 | WF-016 | Assign Loan Officer | User logged in as <Loan Officer>, Loan application is in Active status | 1. Click Assign Loan Officer on the Loan Detail page<br>2. Select <new loan officer> from the dropdown<br>3. Click Confirm on the Assign Loan Officer dialog | Loan officer assigned | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-016 | WF-001 | Leave all required fields blank and submit the loan application |  | 1. Leave the Product Name dropdown blank<br>2. Leave the Loan Officer field blank<br>3. Leave the Loan Purpose field blank<br>4. Leave the Fund field blank<br>5. Leave the Submitted On date blank<br>6. Leave the Expected Disbursement Date blank<br>7. Leave the Principal field blank<br>8. Leave the Number of Repayments field blank<br>9. Leave the Repaid Every field blank<br>10. Leave the Interest Rate field blank | Form does not submit; error shown on Product Name, Loan Officer, Loan Purpose, Fund, Submitted On, Expected Disbursement Date, Principal, Number of Repayments, Repaid Every, and Interest Rate fields indicating they are required | high |
| TC-017 | WF-001 | Leave the Principal field below the minimum bound and submit the loan application |  | 1. Fill all required fields with valid data<br>2. Enter <amount below minimum> in the Principal field<br>3. Click Submit | Form does not submit; error shown on Principal field indicating it must be within product min/max | high |
| TC-018 | WF-001 | Leave the Interest Rate field above the maximum bound and submit the loan application |  | 1. Fill all required fields with valid data<br>2. Enter <amount above maximum> in the Interest Rate field<br>3. Click Submit | Form does not submit; error shown on Interest Rate field indicating it must be within product min/max | high |
| TC-019 | WF-002 | Attempt to approve a loan application when the loan is not in Pending Approval state | Loan is in Approved state | 1. Click on Approve button | Action is blocked; no approval occurs | high |
| TC-020 | WF-008 | Attempt to make a repayment when the loan is not in Active state | Loan is in Approved state | 1. Click on Make Repayment button | Action is blocked; no repayment occurs | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-021 (boundary) | WF-001 | Principal at minimum value | User is on the Loan Application form, Product with defined min/max for Principal is selected | 1. Enter exactly <minimum value> in the Principal field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; loan is created in Submitted and Pending Approval status | medium |
| TC-022 (boundary) | WF-001 | Principal just below minimum value | User is on the Loan Application form, Product with defined min/max for Principal is selected | 1. Enter <one unit below minimum> in the Principal field<br>2. Fill all other required fields<br>3. Click Submit | Form is blocked; error shown indicating the Principal is below the minimum allowed | medium |
| TC-023 (boundary) | WF-001 | Interest Rate at maximum value | User is on the Loan Application form, Product with defined min/max for Interest Rate is selected | 1. Enter exactly <maximum value> in the Interest Rate field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; loan is created in Submitted and Pending Approval status | medium |
| TC-024 (boundary) | WF-001 | Interest Rate just above maximum value | User is on the Loan Application form, Product with defined min/max for Interest Rate is selected | 1. Enter <one unit above maximum> in the Interest Rate field<br>2. Fill all other required fields<br>3. Click Submit | Form is blocked; error shown indicating the Interest Rate exceeds the maximum allowed | medium |
| TC-025 (interaction_edge) | WF-004 | Rapid withdrawal of loan application | Loan application is in Pending Approval status | 1. Click Withdraw<br>2. Immediately click Withdraw again | Second withdrawal attempt is blocked; only one application withdrawal is processed | low |
| TC-026 (input_edge) |  | Long text in Loan Purpose field | User is on the Loan Application form | 1. Enter a long string (200+ characters) in the Loan Purpose field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; loan is created with the Loan Purpose displayed correctly | low |
| TC-027 (input_edge) |  | Special characters in Loan Officer field | User is on the Loan Application form | 1. Enter special characters in the Loan Officer field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; loan is created with the Loan Officer displayed correctly | low |

---

## Savings Account

Total: **20** (positive: 6, negative: 6, edge: 8)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new savings account | User logged in as <Client Manager>, User is on the Client Detail page | 1. Select <Product Name> from the Product Name dropdown<br>2. Enter <valid date> in the Submitted On field<br>3. Enter <valid nominal annual interest rate> in the Nominal Annual Interest Rate field<br>4. Select <interest compounding period> from the Interest Compounding Period dropdown<br>5. Select <interest posting period> from the Interest Posting Period dropdown<br>6. Select <interest calculation method> from the Interest Calculated Using dropdown<br>7. Select <days in year> from the Days in Year dropdown<br>8. Enter <minimum opening balance> in the Minimum Opening Balance field<br>9. Enter <lock-in period> in the Lock-in Period field<br>10. Check the Allow Overdraft checkbox if applicable<br>11. Click 'Add' to add any charges if necessary<br>12. Click 'Submit' to create the account | The account is created in 'Submitted and Pending Approval' status | high |
| TC-002 | WF-007 | Deposit into an active savings account | User logged in as <Account Holder>, Savings account is in Active status | 1. Click on the Deposit action<br>2. Enter <valid transaction date> in the Transaction Date field<br>3. Enter <valid transaction amount> in the Transaction Amount field<br>4. Select <payment type> from the Payment Type dropdown<br>5. Click 'Submit' to complete the deposit | Deposit credited to savings account | high |
| TC-003 | WF-008 | Withdraw from an active savings account | User logged in as <Account Holder>, Savings account is in Active status | 1. Click on the Withdraw action<br>2. Enter <valid transaction date> in the Transaction Date field<br>3. Enter <valid transaction amount> in the Transaction Amount field<br>4. Select <payment type> from the Payment Type dropdown<br>5. Click 'Submit' to complete the withdrawal | Withdrawal processed from savings account | high |
| TC-004 | WF-009 | Post interest for an active savings account | User logged in as <Account Manager>, Savings account is in Active status | 1. Click on the Post Interest action<br>2. Click 'Confirm' on the Post Interest confirmation dialog | Interest posted to savings account | medium |
| TC-005 | WF-010 | Calculate interest for an active savings account | User logged in as <Account Manager>, Savings account is in Active status | 1. Click on the Calculate Interest action<br>2. Click 'Confirm' on the Calculate Interest confirmation dialog | Interest calculated for savings account | medium |
| TC-006 | WF-011 | Close an active savings account | User logged in as <Account Manager>, Savings account is in Active status | 1. Click on the Close action<br>2. Click 'Confirm' on the Close confirmation dialog | Savings account closed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 |  | Leave Nominal Annual Interest Rate blank and submit |  | 1. Leave the Nominal Annual Interest Rate field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Nominal Annual Interest Rate field indicating it is required | high |
| TC-008 |  | Leave Lock-in Period blank and submit |  | 1. Leave the Lock-in Period field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Lock-in Period field indicating it is required | high |
| TC-009 |  | Submit with all required fields empty |  | 1. Leave the Nominal Annual Interest Rate field blank<br>2. Leave the Lock-in Period field blank<br>3. Click Submit | Form does not submit; errors shown on Nominal Annual Interest Rate and Lock-in Period fields | high |
| TC-010 | WF-002 | Attempt to approve a savings account that is not in Pending state | entity_state != Pending | 1. Click on Approve button | Action is blocked; no change in savings account status | high |
| TC-011 | WF-008 | Withdraw from Active Savings Account exceeding available balance without overdraft | entity_state == Active | 1. Click on Withdraw button<br>2. Enter <amount exceeding available balance> in the Transaction Amount field<br>3. Click Submit | Form does not submit; error shown indicating withdrawal cannot exceed available balance unless overdraft is enabled | high |
| TC-012 | WF-008 | Withdraw from Active Savings Account breaching minimum balance | entity_state == Active | 1. Click on Withdraw button<br>2. Enter <amount breaching minimum balance> in the Transaction Amount field<br>3. Click Submit | Form does not submit; error shown indicating minimum balance must be enforced | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 (boundary) | WF-001 | Enter minimum allowed value for Lock-in Period |  | 1. Enter <minimum allowed value> in the <Lock-in Period> field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; account is created in Submitted and Pending Approval status | medium |
| TC-014 (boundary) | WF-001 | Enter one unit below minimum for Lock-in Period |  | 1. Enter <one unit below minimum> in the <Lock-in Period> field<br>2. Fill all other required fields<br>3. Click Submit | <Lock-in Period> displays an error indicating the value is below the minimum allowed | medium |
| TC-015 (boundary) | WF-008 | Withdraw amount equal to available balance | Account is in Active state, Available balance is set | 1. Click Withdraw<br>2. Enter <Transaction Date> as today<br>3. Enter <available balance> in the <Transaction Amount> field<br>4. Select <Payment Type><br>5. Click Submit | Withdrawal is processed from savings account; available balance is updated | medium |
| TC-016 (boundary) | WF-008 | Withdraw amount exceeding available balance without overdraft enabled | Account is in Active state, Available balance is set | 1. Click Withdraw<br>2. Enter <Transaction Date> as today<br>3. Enter <amount greater than available balance> in the <Transaction Amount> field<br>4. Select <Payment Type><br>5. Click Submit | Withdrawal is blocked; error shown indicating withdrawal exceeds available balance | medium |
| TC-017 (boundary) | WF-008 | Withdraw amount that breaches minimum balance requirement | Account is in Active state, Minimum balance is enforced, Available balance is set | 1. Click Withdraw<br>2. Enter <Transaction Date> as today<br>3. Enter <amount that breaches minimum balance> in the <Transaction Amount> field<br>4. Select <Payment Type><br>5. Click Submit | Withdrawal is blocked; error shown indicating minimum balance must be enforced | medium |
| TC-018 (input_edge) |  | Enter a very long string in Product Name dropdown |  | 1. Enter a string longer than 200 characters in the <Product Name> dropdown | Input is either truncated or an error is shown indicating the input exceeds maximum length | low |
| TC-019 (input_edge) |  | Enter special characters in Nominal Annual Interest Rate |  | 1. Enter special characters in the <Nominal Annual Interest Rate> field | Input is blocked; error shown indicating invalid character usage | low |
| TC-020 (input_edge) |  | Enter value with leading/trailing whitespace in Lock-in Period |  | 1. Enter '  <value>  ' in the <Lock-in Period> field<br>2. Click Submit | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Share Account

Total: **26** (positive: 8, negative: 13, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Share Account Application with valid data | User logged in as <Client> | 1. Select <valid share product> from the Share Product dropdown<br>2. Enter <valid date> in the Submitted On field<br>3. Enter <valid number of shares> in the Requested Shares field<br>4. Enter <valid date> in the Application Date field<br>5. Select <active savings account> from the Savings Account for Charges dropdown<br>6. Click Submit | Account is created in Submitted and Pending Approval status | high |
| TC-002 | WF-002 | Approve Share Account with valid data | User logged in as <Approver>, Share account is in Pending status | 1. Enter <valid number of approved shares> in the Approved Shares field<br>2. Enter <valid date> in the Approved Date field<br>3. Click Approve | Approved shares processed | high |
| TC-003 | WF-003 | Reject Share Account | User logged in as <Approver>, Share account is in Pending status | 1. Click Reject | Share account rejected | high |
| TC-004 | WF-004 | Activate Share Account | User logged in as <Admin>, Share account is in Approved status | 1. Click Activate | Share account activated | high |
| TC-005 | WF-005 | Undo Approval of Share Account | User logged in as <Admin>, Share account is in Approved status | 1. Click Undo Approval | Approval undone | high |
| TC-006 | WF-006 | Apply Additional Shares | User logged in as <Client>, Share account is in Active status | 1. Click Apply Additional Shares<br>2. Enter <valid number of additional shares><br>3. Click Submit | Additional shares applied | high |
| TC-007 | WF-007 | Redeem Shares | User logged in as <Client>, Share account is in Active status | 1. Click Redeem Shares | Redemption amount calculated as shares multiplied by current unit price and credited to the linked savings account | high |
| TC-008 | WF-008 | Close Share Account | User logged in as <Client>, Share account is in Active status | 1. Click Close | Share account closed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 | WF-001 | Leave the Share Product dropdown blank and submit |  | 1. Leave the Share Product dropdown blank<br>2. Fill in all other required fields<br>3. Click Submit | Inline validation error appears on the Share Product field indicating it is required | high |
| TC-010 | WF-001 | Leave the Submitted On date blank and submit |  | 1. Leave the Submitted On date blank<br>2. Fill in all other required fields<br>3. Click Submit | Inline validation error appears on the Submitted On field indicating it is required | high |
| TC-011 | WF-001 | Leave the Requested Shares field blank and submit |  | 1. Leave the Requested Shares field blank<br>2. Fill in all other required fields<br>3. Click Submit | Inline validation error appears on the Requested Shares field indicating it is required | high |
| TC-012 | WF-001 | Leave the Application Date blank and submit |  | 1. Leave the Application Date blank<br>2. Fill in all other required fields<br>3. Click Submit | Inline validation error appears on the Application Date field indicating it is required | high |
| TC-013 | WF-001 | Leave the Savings Account for Charges dropdown blank and submit |  | 1. Leave the Savings Account for Charges dropdown blank<br>2. Fill in all other required fields<br>3. Click Submit | Inline validation error appears on the Savings Account for Charges field indicating it is required | high |
| TC-014 | WF-002 | Attempt to approve a share account when the Approved Shares field is blank | entity_state == Pending | 1. Click Approve<br>2. Leave the Approved Shares field blank<br>3. Leave the Approved Date blank<br>4. Click Submit | Inline validation error appears on the Approved Shares field indicating it is required | high |
| TC-015 | WF-002 | Attempt to approve a share account when the Approved Date is blank | entity_state == Pending | 1. Click Approve<br>2. Fill in the Approved Shares field<br>3. Leave the Approved Date blank<br>4. Click Submit | Inline validation error appears on the Approved Date field indicating it is required | high |
| TC-016 | WF-003 | Attempt to reject a share account when in Pending state | entity_state == Pending | 1. Click Reject | No action occurs; the share account remains in Pending state | medium |
| TC-017 | WF-004 | Attempt to activate a share account when in Approved state | entity_state == Approved | 1. Click Activate | No action occurs; the share account remains in Approved state | medium |
| TC-018 | WF-005 | Attempt to undo approval of a share account when in Approved state | entity_state == Approved | 1. Click Undo Approval | No action occurs; the share account remains in Approved state | medium |
| TC-019 | WF-006 | Attempt to apply additional shares when in Active state | entity_state == Active | 1. Click Apply Additional Shares | No action occurs; the share account remains in Active state | medium |
| TC-020 | WF-007 | Attempt to redeem shares when in Active state | entity_state == Active | 1. Click Redeem Shares | No action occurs; the share account remains in Active state | medium |
| TC-021 | WF-008 | Attempt to close a share account when in Active state | entity_state == Active | 1. Click Close | No action occurs; the share account remains in Active state | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-022 (boundary) | WF-001 | Enter minimum requested shares | User is on the Share Account Application form | 1. Select a Share Product from the dropdown<br>2. Enter the minimum allowed value in the Requested Shares field<br>3. Fill in the Submitted On date<br>4. Fill in the Application Date<br>5. Select a Savings Account for Charges from the dropdown<br>6. Click Submit | Form submits successfully; account is created in Submitted and Pending Approval status | medium |
| TC-023 (boundary) | WF-001 | Enter one more than maximum requested shares | User is on the Share Account Application form | 1. Select a Share Product from the dropdown<br>2. Enter one unit above the maximum allowed value in the Requested Shares field<br>3. Fill in the Submitted On date<br>4. Fill in the Application Date<br>5. Select a Savings Account for Charges from the dropdown<br>6. Click Submit | Form submission is blocked; an error message is shown indicating the requested shares exceed the maximum allowed | medium |
| TC-024 (input_edge) |  | Enter a long string in External ID | User is on the Share Account Application form | 1. Select a Share Product from the dropdown<br>2. Fill in the Submitted On date<br>3. Fill in the Application Date<br>4. Enter a very long string (200+ characters) in the External ID field<br>5. Select a Savings Account for Charges from the dropdown<br>6. Click Submit | Form submission is blocked; an error message is shown indicating the External ID exceeds the maximum length | low |
| TC-025 (input_edge) |  | Enter special characters in External ID | User is on the Share Account Application form | 1. Select a Share Product from the dropdown<br>2. Fill in the Submitted On date<br>3. Fill in the Application Date<br>4. Enter special characters in the External ID field<br>5. Select a Savings Account for Charges from the dropdown<br>6. Click Submit | Form submission is blocked; an error message is shown indicating invalid characters in the External ID | low |
| TC-026 (state_edge) | WF-002 | Rapidly approve a share account twice | User is on the Share Account Detail page for a Pending account | 1. Click Approve<br>2. Enter valid values in Approved Shares and Approved Date fields<br>3. Click Approve again immediately after the first submission | Second submission attempt is blocked; only one approval is processed, and the status remains Pending | medium |

---

## Fixed & Recurring Deposit Accounts

Total: **27** (positive: 13, negative: 8, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit FD Account Creation without Maturity Instructions | User logged in as <Role> | 1. Open the FD Account Creation Form<br>2. Enter <valid deposit amount> in the Deposit Amount field<br>3. Enter <valid deposit period> in the Deposit Period field<br>4. Select 'Days' from the Deposit Period Unit dropdown<br>5. Click Submit | Fixed Deposit account created successfully | high |
| TC-002 | WF-002 | Submit RD Account Creation without Deposit Frequency | User logged in as <Role> | 1. Open the RD Account Creation Form<br>2. Enter <valid mandatory deposit amount> in the Mandatory Deposit Amount Per Installment field<br>3. Enter <valid deposit period> in the Deposit Period field<br>4. Enter <valid expected first deposit date> in the Expected First Deposit On field<br>5. Click Submit | Recurring Deposit account created successfully | high |
| TC-003 | WF-003 | Activate RD Account in Draft state | User logged in as <Role>, RD Account is in Draft state | 1. Open the RD Account Detail page<br>2. Click Activate | Recurring Deposit account activated successfully | high |
| TC-004 | WF-004 | Close RD Account on Maturity in Active state | User logged in as <Role>, RD Account is in Active state | 1. Open the RD Account Detail page<br>2. Click Close on Maturity | Recurring Deposit account closed on maturity successfully | high |
| TC-005 | WF-005 | Approve FD Account | User logged in as <Role> | 1. Open the FD Account Detail page<br>2. Click Approve | FD Account approved successfully | high |
| TC-006 | WF-006 | Activate FD Account | User logged in as <Role> | 1. Open the FD Account Detail page<br>2. Click Activate | FD Account activated successfully | high |
| TC-007 | WF-007 | Premature Close FD Account | User logged in as <Role> | 1. Open the FD Account Detail page<br>2. Click Premature Close | FD Account closed prematurely successfully | high |
| TC-008 | WF-008 | Close FD Account on Maturity | User logged in as <Role> | 1. Open the FD Account Detail page<br>2. Click Close on Maturity | FD Account closed on maturity successfully | high |
| TC-009 | WF-009 | Approve RD Account | User logged in as <Role> | 1. Open the RD Account Detail page<br>2. Click Approve | RD Account approved successfully | high |
| TC-010 | WF-010 | Activate RD Account | User logged in as <Role> | 1. Open the RD Account Detail page<br>2. Click Activate | RD Account activated successfully | high |
| TC-011 | WF-011 | Deposit to RD Account | User logged in as <Role> | 1. Open the RD Account Detail page<br>2. Click Deposit | Deposit made to RD Account successfully | high |
| TC-012 | WF-012 | Premature Close RD Account | User logged in as <Role> | 1. Open the RD Account Detail page<br>2. Click Premature Close | RD Account closed prematurely successfully | high |
| TC-013 | WF-013 | Close RD Account on Maturity | User logged in as <Role> | 1. Open the RD Account Detail page<br>2. Click Close on Maturity | RD Account closed on maturity successfully | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 | WF-001 | Submit FD Account Creation without Deposit Amount |  | 1. Leave the Deposit Amount field blank<br>2. Fill all other required fields<br>3. Click Submit | Form does not submit; Deposit Amount is required and highlighted |  |
| TC-015 | WF-001 | Submit FD Account Creation with negative Deposit Period |  | 1. Enter <negative integer> in the Deposit Period field<br>2. Fill all other required fields<br>3. Click Submit | Form does not submit; Deposit Period must be a positive integer error shown |  |
| TC-016 | WF-002 | Submit RD Account Creation without Mandatory Deposit Amount Per Installment |  | 1. Leave the Mandatory Deposit Amount Per Installment field blank<br>2. Fill all other required fields<br>3. Click Submit | Form does not submit; Mandatory Deposit Amount Per Installment is required and highlighted |  |
| TC-017 | WF-002 | Submit RD Account Creation with negative Deposit Period |  | 1. Enter <negative integer> in the Deposit Period field<br>2. Fill all other required fields<br>3. Click Submit | Form does not submit; Deposit Period must be a positive integer error shown |  |
| TC-018 | WF-003 | Activate RD Account in Draft state |  | 1. Attempt to activate an RD Account that is in Draft state | Action is blocked; cannot activate RD Account while in Draft state |  |
| TC-019 | WF-004 | Close RD Account on Maturity in Active state |  | 1. Attempt to close an RD Account that is in Active state | Action is blocked; cannot close RD Account on maturity while in Active state |  |
| TC-020 | WF-005 | Approve FD Account without required fields filled |  | 1. Leave all required fields blank<br>2. Click Approve | Action is blocked; required fields must be filled before approval |  |
| TC-021 | WF-006 | Activate FD Account without required fields filled |  | 1. Leave all required fields blank<br>2. Click Activate | Action is blocked; required fields must be filled before activation |  |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-022 (boundary) | WF-001 | Submit FD Account Creation with Deposit Period as 1 |  | 1. Select a Fixed Deposit Product from the dropdown<br>2. Enter '1000' in the Deposit Amount field<br>3. Enter '1' in the Deposit Period field<br>4. Select 'Days' from the Deposit Period Unit dropdown<br>5. Click Submit | FD Account created successfully with a Deposit Period of 1 day | medium |
| TC-023 (boundary) | WF-001 | Submit FD Account Creation with Deposit Period as 0 |  | 1. Select a Fixed Deposit Product from the dropdown<br>2. Enter '1000' in the Deposit Amount field<br>3. Enter '0' in the Deposit Period field<br>4. Select 'Days' from the Deposit Period Unit dropdown<br>5. Click Submit | Submission is blocked; error message displayed indicating Deposit Period must be a positive integer | medium |
| TC-024 (boundary) | WF-002 | Submit RD Account Creation with Deposit Period as 1 |  | 1. Select a Recurring Deposit Product from the dropdown<br>2. Enter '500' in the Mandatory Deposit Amount Per Installment field<br>3. Enter '1' in the Deposit Period field<br>4. Click Submit | Recurring Deposit account created successfully with a Deposit Period of 1 | medium |
| TC-025 (boundary) | WF-002 | Submit RD Account Creation with Deposit Period as 0 |  | 1. Select a Recurring Deposit Product from the dropdown<br>2. Enter '500' in the Mandatory Deposit Amount Per Installment field<br>3. Enter '0' in the Deposit Period field<br>4. Click Submit | Submission is blocked; error message displayed indicating Deposit Period must be a positive integer | medium |
| TC-026 (input_edge) |  | Submit FD Account Creation with a very large Deposit Amount |  | 1. Select a Fixed Deposit Product from the dropdown<br>2. Enter '9999999999' in the Deposit Amount field<br>3. Enter '1' in the Deposit Period field<br>4. Select 'Months' from the Deposit Period Unit dropdown<br>5. Click Submit | FD Account created successfully with a large Deposit Amount | low |
| TC-027 (input_edge) |  | Submit RD Account Creation with a very large Mandatory Deposit Amount |  | 1. Select a Recurring Deposit Product from the dropdown<br>2. Enter '9999999999' in the Mandatory Deposit Amount Per Installment field<br>3. Enter '1' in the Deposit Period field<br>4. Click Submit | Recurring Deposit account created successfully with a large Mandatory Deposit Amount | low |

---

## Accounting — Chart of Accounts

Total: **10** (positive: 3, negative: 3, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new GL Account successfully | User logged in as <Role> | 1. Click '+ Create GL Account' button<br>2. Select <account type> from the Account Type dropdown<br>3. Select <parent account> from the Parent Account dropdown<br>4. Enter <unique GL code> in the GL Code field<br>5. Enter <account name> in the Account Name field<br>6. Select <usage type> from the Account Usage dropdown<br>7. Click Submit | GL Account created successfully | high |
| TC-002 | WF-002 | Edit an existing GL Account successfully | User logged in as <Role>, An existing GL Account is displayed in the Chart of Accounts | 1. Click on the <account name> of the GL Account to view details<br>2. Click Edit<br>3. Modify <field> with <new value><br>4. Click Submit | GL Account details updated | high |
| TC-003 | WF-003 | Delete an existing GL Account successfully | User logged in as <Role>, An existing GL Account is displayed in the Chart of Accounts | 1. Click on the <account name> of the GL Account to view details<br>2. Click Delete<br>3. Confirm deletion | GL Account deleted successfully | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Attempt to create a GL Account with all required fields empty |  | 1. Leave the Account Type field blank<br>2. Leave the Parent Account field blank<br>3. Leave the GL Code field blank<br>4. Leave the Account Name field blank<br>5. Leave the Account Usage field blank<br>6. Click Submit | Form does not submit; Account Type, Parent Account, GL Code, Account Name, and Account Usage fields are highlighted with inline validation errors indicating they are required | high |
| TC-005 | WF-001 | Attempt to create a GL Account with a duplicate GL Code |  | 1. Enter <existing GL Code> in the GL Code field<br>2. Enter <valid Account Name> in the Account Name field<br>3. Select <valid Account Type> from the Account Type dropdown<br>4. Select <valid Parent Account> from the Parent Account dropdown<br>5. Select <valid Account Usage> from the Account Usage dropdown<br>6. Click Submit | Form does not submit; GL Code field displays an error: 'GL Code must be unique' | high |
| TC-006 |  | Attempt to create a GL Account with invalid Account Usage |  | 1. Select <valid Account Type> from the Account Type dropdown<br>2. Select <valid Parent Account> from the Parent Account dropdown<br>3. Enter <valid GL Code> in the GL Code field<br>4. Enter <valid Account Name> in the Account Name field<br>5. Select <invalid Account Usage> from the Account Usage dropdown<br>6. Click Submit | Form does not submit; Account Usage field displays an error: 'Must be a valid option' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) | WF-001 | Attempt to create GL Account with duplicate GL Code | A GL Account with the same GL Code already exists | 1. Open the Create GL Account form<br>2. Fill in all required fields with valid data<br>3. Enter the existing GL Code in the GL_Code field<br>4. Click Submit | An error message displays indicating that the GL Code must be unique | medium |
| TC-008 (input_edge) |  | Create GL Account with maximum length Account Name |  | 1. Open the Create GL Account form<br>2. Fill in all required fields with valid data<br>3. Enter a maximum length string in the Account_Name field<br>4. Click Submit | Form submits successfully; GL Account is created with the maximum length Account Name | low |
| TC-009 (input_edge) |  | Create GL Account with special characters in Account Name |  | 1. Open the Create GL Account form<br>2. Fill in all required fields with valid data<br>3. Enter special characters in the Account_Name field<br>4. Click Submit | Form submits successfully; GL Account is created with the Account Name containing special characters | low |
| TC-010 (input_edge) |  | Create GL Account with leading and trailing whitespace in Account Name |  | 1. Open the Create GL Account form<br>2. Fill in all required fields with valid data<br>3. Enter leading and trailing whitespace in the Account_Name field<br>4. Click Submit | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Accounting — Journal Entries & Closures

Total: **15** (positive: 2, negative: 9, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit a valid journal entry | User logged in as <Role> | 1. Click '+ Add Journal Entry' to open the creation form<br>2. Select <valid office> from the Office dropdown<br>3. Select <valid currency> from the Currency dropdown<br>4. Enter <valid transaction date> in the Transaction Date field<br>5. Click 'Add Row' to add an entry line<br>6. Select <valid GL Account> from the GL Account dropdown in the new row<br>7. Enter <valid amount> in the Amount field in the new row<br>8. Click 'Submit' to submit the journal entry | A success notification is displayed; total debits must equal total credits | high |
| TC-002 | WF-002 | Create a closure successfully | User logged in as <Role> | 1. Click '+ Create Closure' to open the closure form<br>2. Select <valid office> from the Office dropdown<br>3. Enter <valid closing date> in the Closing Date field<br>4. Click 'Create Closure' to create the closure | prevents journal entries from being posted for dates on or before the closing date | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Office field blank and submit journal entry |  | 1. Leave the Office field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Office field indicating it is required | high |
| TC-004 |  | Leave the Currency field blank and submit journal entry |  | 1. Leave the Currency field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Currency field indicating it is required | high |
| TC-005 |  | Leave the Transaction Date field blank and submit journal entry |  | 1. Leave the Transaction Date field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Transaction Date field indicating it is required | high |
| TC-006 |  | Leave the GL Account field blank in entry lines and submit journal entry |  | 1. Click 'Add Row' to add an entry line<br>2. Leave the GL Account field blank<br>3. Fill the Amount field<br>4. Click Submit | Inline validation error appears on the GL Account field indicating it is required | high |
| TC-007 |  | Leave the Amount field blank in entry lines and submit journal entry |  | 1. Click 'Add Row' to add an entry line<br>2. Fill the GL Account field<br>3. Leave the Amount field blank<br>4. Click Submit | Inline validation error appears on the Amount field indicating it is required | high |
| TC-008 |  | Submit journal entry with total debits not equal to total credits |  | 1. Fill all required fields with valid data<br>2. Add entry lines with total debits not equal to total credits<br>3. Click Submit | Form does not submit; total debits must equal total credits error is shown | high |
| TC-009 |  | Leave the Office field blank and create closure |  | 1. Leave the Office field blank<br>2. Fill the Closing Date field<br>3. Click Create Closure | Inline validation error appears on the Office field indicating it is required | high |
| TC-010 |  | Leave the Closing Date field blank and create closure |  | 1. Fill the Office field<br>2. Leave the Closing Date field blank<br>3. Click Create Closure | Inline validation error appears on the Closing Date field indicating it is required | high |
| TC-011 |  | Attempt to create closure for a date that is on or before the closing date |  | 1. Fill the Office field<br>2. Fill the Closing Date field with a past date<br>3. Click Create Closure | Form does not submit; prevents journal entries from being posted for dates on or before the closing date error is shown | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) | WF-001 | Total debits equal total credits | Add at least one entry line with a GL Account and Amount | 1. Enter a valid Office in the Add Journal Entry form<br>2. Enter a valid Currency in the Add Journal Entry form<br>3. Enter a valid Transaction Date in the Add Journal Entry form<br>4. Add an Entry Line with a GL Account and Amount<br>5. Add another Entry Line with a GL Account and the same Amount as the first line<br>6. Click Submit | Form submits successfully; journal entry is created with total debits equal to total credits | medium |
| TC-013 (boundary) | WF-001 | Total debits do not equal total credits | Add at least one entry line with a GL Account and Amount | 1. Enter a valid Office in the Add Journal Entry form<br>2. Enter a valid Currency in the Add Journal Entry form<br>3. Enter a valid Transaction Date in the Add Journal Entry form<br>4. Add an Entry Line with a GL Account and Amount<br>5. Add another Entry Line with a GL Account and a different Amount<br>6. Click Submit | Submission is blocked; error shown indicating 'total debits must equal total credits' | medium |
| TC-014 (boundary) | WF-002 | Create closure on the same day as journal entry date | Ensure there are journal entries with Transaction Dates today or earlier | 1. Enter a valid Office in the Create Closure form<br>2. Enter today's date in the Closing Date field<br>3. Click Create Closure | Closure is created successfully; journal entries cannot be posted for dates on or before today's date | medium |
| TC-015 (boundary) | WF-002 | Create closure on a date before existing journal entries | Ensure there are journal entries with Transaction Dates before today | 1. Enter a valid Office in the Create Closure form<br>2. Enter a date before today's date in the Closing Date field<br>3. Click Create Closure | Submission is blocked; error shown indicating that journal entries can still be posted for dates after the closing date | medium |

---

## Accounting Rules & Financial Activity Mappings

Total: **13** (positive: 4, negative: 5, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-003 | Create a new accounting rule successfully | User logged in as <Role> | 1. Click '+ Create Rule' to open the creation form<br>2. Enter <valid rule name> in the Rule Name field<br>3. Select 'All Offices' from the Office dropdown<br>4. Click 'Create Rule' | A success notification is displayed; the accounting rule is listed in the Accounting Rules Table | high |
| TC-002 | WF-004 | Create a new financial activity mapping successfully | User logged in as <Role> | 1. Click '+ Create Mapping' to open the mapping form<br>2. Select <valid financial activity> from the Financial Activity dropdown<br>3. Select <valid GL account> from the GL Account dropdown<br>4. Click 'Create Mapping' | A success notification is displayed; the financial activity mapping is listed in the Financial Activity Mappings Table | high |
| TC-003 | WF-001 | Edit an existing accounting rule | User logged in as <Role>, An accounting rule exists in the Accounting Rules Table | 1. Click on the Rule Name of the existing accounting rule to open its detail view<br>2. Click 'Edit'<br>3. Modify the Rule Name to <new valid rule name><br>4. Click 'Save' | The accounting rule details are updated; the Accounting Rules Table displays the new rule name | medium |
| TC-004 | WF-002 | Delete an existing accounting rule | User logged in as <Role>, An accounting rule exists in the Accounting Rules Table | 1. Click on the Rule Name of the existing accounting rule to open its detail view<br>2. Click 'Delete'<br>3. Confirm the deletion | The accounting rule is no longer present in the Accounting Rules Table | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-003 | Leave the Rule Name field blank and submit |  | 1. Open the Create Rule form<br>2. Leave the Rule Name field blank<br>3. Click Create Rule | Form does not submit; Rule Name field displays an error: 'This field is required' | high |
| TC-006 | WF-004 | Leave the Financial Activity field blank and submit |  | 1. Open the Create Mapping form<br>2. Leave the Financial Activity field blank<br>3. Select a GL Account<br>4. Click Create Mapping | Form does not submit; Financial Activity field displays an error: 'This field is required' | high |
| TC-007 | WF-004 | Leave the GL Account field blank and submit |  | 1. Open the Create Mapping form<br>2. Select a Financial Activity<br>3. Leave the GL Account field blank<br>4. Click Create Mapping | Form does not submit; GL Account field displays an error: 'This field is required' | high |
| TC-008 | WF-003 | Submit with all required fields empty in Create Rule form |  | 1. Open the Create Rule form<br>2. Leave all required fields empty<br>3. Click Create Rule | Form does not submit; Rule Name field displays an error: 'This field is required' | high |
| TC-009 | WF-004 | Submit with all required fields empty in Create Mapping form |  | 1. Open the Create Mapping form<br>2. Leave all required fields empty<br>3. Click Create Mapping | Form does not submit; Financial Activity field displays an error: 'This field is required' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) | WF-003 | Create Accounting Rule with valid Rule Name |  | 1. Open the Create Rule form<br>2. Enter a valid Rule Name in the Rule_Name field | Form submits successfully; accounting rule is created with the valid Rule Name | medium |
| TC-011 (boundary) | WF-003 | Create Accounting Rule with empty Rule Name |  | 1. Open the Create Rule form<br>2. Leave the Rule_Name field empty | Form submission is blocked; error message indicates Rule Name is required | medium |
| TC-012 (boundary) | WF-004 | Create Financial Activity Mapping with valid Financial Activity and GL Account |  | 1. Open the Create Mapping form<br>2. Select a valid Financial Activity from the dropdown<br>3. Select a valid GL Account from the dropdown | Form submits successfully; financial activity mapping is created with the selected Financial Activity and GL Account | medium |
| TC-013 (boundary) | WF-004 | Create Financial Activity Mapping with duplicate Financial Activity |  | 1. Open the Create Mapping form<br>2. Select a Financial Activity that is already mapped<br>3. Select a valid GL Account from the dropdown | Form submission is blocked; error message indicates that the Financial Activity can only be mapped once | medium |

---

## Provisioning

Total: **15** (positive: 5, negative: 3, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Creation Form from Provisioning Criteria page | User logged in as <Role> | 1. Click '+ Create' button on the Provisioning Criteria page | Creation form opens | high |
| TC-002 | WF-002 | Submit Creation Form with valid criteria | User logged in as <Role>, Creation form is open | 1. Enter <valid criteria name> in the Criteria Name field<br>2. Click 'Add Row' in the Definitions table<br>3. Select 'STANDARD' from the Category dropdown<br>4. Enter <valid number> in the Minimum Age field<br>5. Enter <valid number> in the Maximum Age field<br>6. Enter <valid percentage> in the Provisioning Percentage field<br>7. Click 'Submit' on the Creation form | Criteria created; success message shown | high |
| TC-003 | WF-003 | Create Provisioning Entry | User logged in as <Role>, Provisioning criteria are created | 1. Click '+ Create Provisioning Entry' button on the Provisioning Entries page | Generates new provisioning entries based on current loan portfolio status | high |
| TC-004 | WF-004 | Review Provisioning Entry | User logged in as <Role>, Provisioning entries are available | 1. Click 'Review' action for a provisioning entry | Shows detailed breakdown by loan product and category | medium |
| TC-005 | WF-005 | Recreate Provisioning Entry | User logged in as <Role>, Provisioning entries are available | 1. Click 'Recreate' action for a provisioning entry | Recreates the provisioning entry | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-002 | Leave the Criteria Name field blank and submit the creation form |  | 1. Click on the '+ Create' button to open the creation form<br>2. Leave the Criteria Name field blank<br>3. Click Submit | Inline validation error appears on the Criteria Name field indicating it is required | high |
| TC-007 | WF-002 | Submit the creation form with all fields empty |  | 1. Click on the '+ Create' button to open the creation form<br>2. Leave all fields empty<br>3. Click Submit | Inline validation error appears on the Criteria Name field indicating it is required | high |
| TC-008 | WF-003 | Attempt to create provisioning entries without configured criteria |  | 1. Click on the '+ Create Provisioning Entry' button<br>2. Observe the state of the form | Form does not submit; no provisioning entries are created; error shown indicating criteria must be configured | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-002 | Minimum age set to 0 | User is on the creation form | 1. Enter a valid Criteria Name in the Criteria_Name field<br>2. Add a row in the Definitions table<br>3. Enter 0 in the Minimum_Age field<br>4. Fill all other required fields<br>5. Click Submit | Form submits successfully; entity is created with Minimum Age set to 0 | medium |
| TC-010 (boundary) | WF-002 | Maximum age set to 1000 | User is on the creation form | 1. Enter a valid Criteria Name in the Criteria_Name field<br>2. Add a row in the Definitions table<br>3. Enter 1000 in the Maximum_Age field<br>4. Fill all other required fields<br>5. Click Submit | Form submits successfully; entity is created with Maximum Age set to 1000 | medium |
| TC-011 (boundary) | WF-002 | Adding maximum allowed definitions | User is on the creation form | 1. Enter a valid Criteria Name in the Criteria_Name field<br>2. Add 1 row in the Definitions table<br>3. Add 1 more row in the Definitions table<br>4. Click Submit | Form submits successfully; entity is created with 2 definitions | medium |
| TC-012 (boundary) | WF-002 | Exceeding maximum definitions | User is on the creation form | 1. Enter a valid Criteria Name in the Criteria_Name field<br>2. Add 1 row in the Definitions table<br>3. Add 1 more row in the Definitions table<br>4. Attempt to add a 3rd row in the Definitions table<br>5. Click Submit | Submission is blocked; visible error indicating maximum definitions exceeded | medium |
| TC-013 (input_edge) |  | Entering a very long Criteria Name | User is on the creation form | 1. Enter a string longer than 200 characters in the Criteria_Name field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is blocked; error shown indicating the name is too long | low |
| TC-014 (input_edge) |  | Entering special characters in Criteria Name | User is on the creation form | 1. Enter special characters in the Criteria_Name field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is blocked; error shown indicating invalid characters | low |
| TC-015 (input_edge) |  | Leading/trailing whitespace in Criteria Name | User is on the creation form | 1. Enter '   Valid Name   ' in the Criteria_Name field<br>2. Fill all other required fields<br>3. Click Submit | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |

---

## Offices

Total: **11** (positive: 3, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Office Detail | User logged in as <Role> | 1. Click on the Office Name link in the Offices table | The Office Detail page opens displaying the office information | high |
| TC-002 | WF-002 | Open Create Office Form | User logged in as <Role> | 1. Click on the '+ Create Office' button | The creation form opens | high |
| TC-003 | WF-002 | Create Office Successfully | User logged in as <Role>, The creation form is open | 1. Enter <valid office name> in the Office Name field<br>2. Select 'Head Office' from the Parent Office dropdown<br>3. Enter <valid date> in the Opened On Date field<br>4. Click Submit | A success message is displayed; the new office appears in the Offices table | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-002 | Attempt to create office with blank Office Name |  | 1. Click on the '+ Create Office' button<br>2. Leave the Office Name field blank<br>3. Fill in the Parent Office and Opened On Date fields<br>4. Click Submit | Inline validation error appears on the Office Name field indicating it is required | high |
| TC-005 | WF-002 | Attempt to create office with blank Parent Office |  | 1. Click on the '+ Create Office' button<br>2. Fill in the Office Name and Opened On Date fields<br>3. Leave the Parent Office field blank<br>4. Click Submit | Inline validation error appears on the Parent Office field indicating it is required | high |
| TC-006 | WF-002 | Attempt to create office with blank Opened On Date |  | 1. Click on the '+ Create Office' button<br>2. Fill in the Office Name and Parent Office fields<br>3. Leave the Opened On Date field blank<br>4. Click Submit | Inline validation error appears on the Opened On Date field indicating it is required | high |
| TC-007 | WF-002 | Attempt to create office with invalid Parent Office |  | 1. Click on the '+ Create Office' button<br>2. Fill in the Office Name field<br>3. Enter an invalid Parent Office value<br>4. Fill in the Opened On Date field<br>5. Click Submit | Inline validation error appears on the Parent Office field indicating 'Head Office is the root' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) | WF-002 | Enter a valid date for Opening Date field |  | 1. Click the '+ Create Office' button<br>2. Enter a valid date in the 'Opened On Date' field | Form submits successfully; office is created with the entered date | medium |
| TC-009 (boundary) | WF-002 | Enter an invalid date for Opening Date field (one day before today) |  | 1. Click the '+ Create Office' button<br>2. Enter a date that is one day before today's date in the 'Opened On Date' field | 'Opened On Date' displays an error indicating the date cannot be before today | medium |
| TC-010 (input_edge) | WF-002 | Enter a very long Office Name |  | 1. Click the '+ Create Office' button<br>2. Enter a string of 200+ characters in the 'Office Name' field | The form displays an error indicating the Office Name is too long | low |
| TC-011 (input_edge) | WF-002 | Enter special characters in the Office Name field |  | 1. Click the '+ Create Office' button<br>2. Enter special characters (e.g., @#$%^&*) in the 'Office Name' field | The form displays an error indicating invalid characters in the Office Name | low |

---

## Employees

Total: **11** (positive: 3, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View employee details | User logged in as <Role>, Employee exists in the Employees table | 1. Click on the Name link of the employee | Employee details displayed | high |
| TC-002 | WF-002 | Edit employee details | User logged in as <Role>, Employee exists in the Employees table | 1. Click on the Edit action for the employee | Employee edit form displayed | high |
| TC-003 | WF-003 | Create a new employee | User logged in as <Role> | 1. Click the '+ Create Employee' button<br>2. Enter <valid office> in the Office field<br>3. Enter <valid first name> in the First Name field<br>4. Enter <valid last name> in the Last Name field<br>5. Click Submit | opens creation form | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-003 | Attempt to create a new employee with required fields empty |  | 1. Click the '+ Create Employee' button<br>2. Leave the Office field blank<br>3. Leave the First Name field blank<br>4. Leave the Last Name field blank<br>5. Click Submit | Form does not submit; Office field displays an error: 'This field is required'; First Name field displays an error: 'This field is required'; Last Name field displays an error: 'This field is required' | high |
| TC-005 | WF-003 | Attempt to create a new employee with the Office field empty |  | 1. Click the '+ Create Employee' button<br>2. Leave the Office field blank<br>3. Fill in the First Name field with <valid first name><br>4. Fill in the Last Name field with <valid last name><br>5. Click Submit | Form does not submit; Office field displays an error: 'This field is required' | high |
| TC-006 | WF-003 | Attempt to create a new employee with the First Name field empty |  | 1. Click the '+ Create Employee' button<br>2. Fill in the Office field with <valid office><br>3. Leave the First Name field blank<br>4. Fill in the Last Name field with <valid last name><br>5. Click Submit | Form does not submit; First Name field displays an error: 'This field is required' | high |
| TC-007 | WF-003 | Attempt to create a new employee with the Last Name field empty |  | 1. Click the '+ Create Employee' button<br>2. Fill in the Office field with <valid office><br>3. Fill in the First Name field with <valid first name><br>4. Leave the Last Name field blank<br>5. Click Submit | Form does not submit; Last Name field displays an error: 'This field is required' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) | WF-003 | Submit creation form with valid minimum values |  | 1. Click the '+ Create Employee' button<br>2. Enter a valid value in the Office field<br>3. Enter a valid value in the First Name field<br>4. Enter a valid value in the Last Name field<br>5. Click Submit | Form submits successfully; employee is created with the minimum required values | medium |
| TC-009 (boundary) | WF-003 | Submit creation form with empty required fields |  | 1. Click the '+ Create Employee' button<br>2. Leave the Office field empty<br>3. Leave the First Name field empty<br>4. Leave the Last Name field empty<br>5. Click Submit | Form submission is blocked; error messages indicate that Office, First Name, and Last Name are required | medium |
| TC-010 (input_edge) | WF-003 | Enter long text in the First Name field |  | 1. Click the '+ Create Employee' button<br>2. Enter a very long string (200+ characters) in the First Name field<br>3. Enter a valid value in the Office field<br>4. Enter a valid value in the Last Name field<br>5. Click Submit | Form submission is blocked; error message indicates the First Name exceeds the maximum length allowed | low |
| TC-011 (input_edge) | WF-003 | Enter special characters in the Last Name field |  | 1. Click the '+ Create Employee' button<br>2. Enter special characters in the Last Name field<br>3. Enter a valid value in the Office field<br>4. Enter a valid value in the First Name field<br>5. Click Submit | Form submission is blocked; error message indicates invalid characters in the Last Name field | low |

---

## Teller & Cashier Management

Total: **18** (positive: 5, negative: 6, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new teller successfully | User logged in as <role> | 1. Click '+ Create Teller' button<br>2. Enter <valid office> in the Office field<br>3. Enter <valid teller name> in the Teller Name field<br>4. Enter <valid start date> in the Start Date field<br>5. Click Submit | Teller created; success message shown | high |
| TC-002 | WF-002 | Allocate a cashier successfully | User logged in as <role>, A teller exists | 1. Click '+ Allocate Cashier' button<br>2. Enter <valid staff> in the Staff field<br>3. Enter <valid start date> in the Start Date field<br>4. Click Submit | Cashier allocated; success message shown | high |
| TC-003 | WF-003 | Edit teller details successfully | User logged in as <role>, A teller exists | 1. Click on the Teller Name link for the teller to edit<br>2. Click Edit<br>3. Update <valid office> in the Office field<br>4. Click Submit | Teller details updated; success message shown | high |
| TC-004 | WF-004 | Allocate cash successfully | User logged in as <role>, A cashier exists | 1. Click Allocate Cash on the Cashier Detail page<br>2. Enter <valid amount> in the Amount field<br>3. Enter <valid currency> in the Currency field<br>4. Enter <valid transaction date> in the Transaction Date field<br>5. Click Submit | Cash allocated; success message shown | high |
| TC-005 | WF-005 | Settle cash successfully | User logged in as <role>, A cashier exists | 1. Click Settle Cash on the Cashier Detail page<br>2. Enter <valid amount> in the Amount field<br>3. Enter <valid currency> in the Currency field<br>4. Enter <valid transaction date> in the Transaction Date field<br>5. Click Submit | Cash settled; success message shown | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-001 | Attempt to create a teller with required fields empty |  | 1. Leave the Office field blank<br>2. Leave the Teller Name field blank<br>3. Leave the Start Date field blank<br>4. Click Submit | Form does not submit; Office, Teller Name, and Start Date fields display errors indicating they are required | high |
| TC-007 | WF-001 | Attempt to create a teller with all required fields empty |  | 1. Leave all required fields (Office, Teller Name, Start Date) blank<br>2. Click Submit | Form does not submit; Office, Teller Name, and Start Date fields display errors indicating they are required | high |
| TC-008 | WF-002 | Attempt to allocate a cashier with required fields empty |  | 1. Leave the Staff field blank<br>2. Leave the Start Date field blank<br>3. Click Submit | Form does not submit; Staff and Start Date fields display errors indicating they are required | high |
| TC-009 | WF-005 | Attempt to settle cash with required fields empty |  | 1. Leave the Amount field blank<br>2. Leave the Currency field blank<br>3. Leave the Transaction Date field blank<br>4. Click Settle Cash | Form does not submit; Amount, Currency, and Transaction Date fields display errors indicating they are required | high |
| TC-010 |  | Attempt to access the Create Teller form without authentication |  | 1. Navigate to the Create Teller page | User is redirected to the login page | high |
| TC-011 | WF-003 | Attempt to edit a teller without sufficient permissions |  | 1. Attempt to click the Edit button on a teller entry | User is blocked from editing; Edit option is not visible | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) | WF-001 | Create Teller with Start Date equal to End Date | User is on the Create Teller form | 1. Enter a valid value in the Office field<br>2. Enter a valid value in the Teller_Name field<br>3. Enter a valid value in the Start_Date field as today's date<br>4. Enter the same value in the End_Date field as today's date<br>5. Click Submit | Form submits successfully; teller is created with Start_Date and End_Date set to today | medium |
| TC-013 (boundary) | WF-001 | Create Teller with Start Date one day before End Date | User is on the Create Teller form | 1. Enter a valid value in the Office field<br>2. Enter a valid value in the Teller_Name field<br>3. Enter a valid value in the Start_Date field as today's date<br>4. Enter the date one day in the future in the End_Date field<br>5. Click Submit | Form submits successfully; teller is created with Start_Date as today and End_Date as tomorrow | medium |
| TC-014 (boundary) | WF-005 | Settle Cash with Amount at zero | User is on the Cashier Detail page and clicks Settle Cash | 1. Enter '0' in the Amount field<br>2. Enter a valid value in the Currency field<br>3. Enter a valid date in the Transaction_Date field<br>4. Click Settle Cash | Form submits successfully; cash is settled with an Amount of 0 | medium |
| TC-015 (boundary) | WF-005 | Settle Cash with Amount just above maximum allowed | User is on the Cashier Detail page and clicks Settle Cash | 1. Enter an amount just above the maximum allowed in the Amount field<br>2. Enter a valid value in the Currency field<br>3. Enter a valid date in the Transaction_Date field<br>4. Click Settle Cash | Submission is blocked; error shown indicating the amount exceeds the maximum allowed | medium |
| TC-016 (boundary) | WF-002 | Allocate Cashier with Start Date equal to End Date | User is on the Allocate Cashier form | 1. Enter a valid value in the Staff field<br>2. Enter a valid value in the Start_Date field as today's date<br>3. Enter the same value in the End_Date field as today's date<br>4. Click Submit | Form submits successfully; cashier is allocated with Start_Date and End_Date set to today | medium |
| TC-017 (input_edge) |  | Enter long text in Description field | User is on the Create Teller form | 1. Enter a valid value in the Office field<br>2. Enter a valid value in the Teller_Name field<br>3. Enter a very long string (200+ characters) in the Description field<br>4. Enter a valid date in the Start_Date field<br>5. Click Submit | Form submits successfully; the Description field displays the long text as entered | low |
| TC-018 (input_edge) |  | Enter special characters in Staff field | User is on the Allocate Cashier form | 1. Enter a valid value in the Start_Date field<br>2. Enter a valid value in the End_Date field<br>3. Enter special characters in the Staff field<br>4. Click Submit | Submission is blocked; error shown indicating invalid characters in the Staff field | low |

---

## Users & Roles

Total: **16** (positive: 5, negative: 6, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new user successfully | User logged in as <Role> | 1. Click '+ Create User' button<br>2. Enter <unique username> in the Username field<br>3. Enter <first name> in the First Name field<br>4. Enter <last name> in the Last Name field<br>5. Enter <valid email> in the Email field<br>6. Enter <office> in the Office field<br>7. Enter <valid password> in the Password field<br>8. Enter <same valid password> in the Repeat Password field<br>9. Select <roles> from the Roles checkboxes<br>10. Click Submit | User created successfully; success message shown | high |
| TC-002 | WF-005 | Open user creation form via bulk action | User logged in as <Role> | 1. Click '+ Create User' button in the Users table<br>2. Verify the user creation form is displayed | User creation form opened | medium |
| TC-003 | WF-002 | Create a new role successfully | User logged in as <Role> | 1. Click '+ Create Role' button<br>2. Enter <role name> in the Role Name field<br>3. Enter <description> in the Description field<br>4. Click Submit | Role created successfully; success message shown | high |
| TC-004 | WF-004 | Open role creation form via bulk action | User logged in as <Role> | 1. Click '+ Create Role' button in the Roles table<br>2. Verify the role creation form is displayed | Role creation form opened | medium |
| TC-005 | WF-003 | View user details | User logged in as <Role> | 1. Click on the Username link for a specific user<br>2. Verify the user details are displayed | User details displayed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-001 | Attempt to create a user with all required fields empty |  | 1. Click on '+ Create User' button<br>2. Leave all required fields blank<br>3. Click Submit | Form does not submit; Username, First Name, Last Name, Email, Office, Password, and Roles fields are highlighted with errors indicating they are required | high |
| TC-007 | WF-001 | Attempt to create a user with invalid email format |  | 1. Click on '+ Create User' button<br>2. Fill in Username, First Name, Last Name, Office, Password, Repeat Password, and Roles<br>3. Enter <invalid email format> in the Email field<br>4. Click Submit | Form does not submit; Email field displays an error: 'Must be a valid email address' | high |
| TC-008 | WF-001 | Attempt to create a user with a non-unique username |  | 1. Click on '+ Create User' button<br>2. Fill in Username with an existing username, First Name, Last Name, Email, Office, Password, Repeat Password, and Roles<br>3. Click Submit | Form does not submit; Username field displays an error: 'Must be unique' | high |
| TC-009 | WF-001 | Attempt to create a user with mismatched passwords |  | 1. Click on '+ Create User' button<br>2. Fill in Username, First Name, Last Name, Email, Office, Password, and Roles<br>3. Enter different values in Password and Repeat Password fields<br>4. Click Submit | Form does not submit; Repeat Password field displays an error: 'Passwords must match' | high |
| TC-010 | WF-002 | Attempt to create a role with the description field empty |  | 1. Click on '+ Create Role' button<br>2. Leave the Description field blank<br>3. Click Submit | Form does not submit; Description field is highlighted with an error indicating it is required | high |
| TC-011 |  | Attempt to access the Users page without authentication |  | 1. Navigate to the Users page | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) | WF-001 | Username uniqueness check | User with the same Username already exists | 1. Enter the existing Username in the Username field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is blocked; error message 'Username must be unique' is displayed. | medium |
| TC-013 (boundary) | WF-001 | Email format validation |  | 1. Enter an invalid email format in the Email field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is blocked; error message 'Email is not valid' is displayed. | medium |
| TC-014 (boundary) | WF-001 | Password policy validation |  | 1. Enter a password that does not meet the password policy in the Password field<br>2. Enter the same password in the Repeat Password field<br>3. Fill all other required fields<br>4. Click Submit | Form submission is blocked; error message indicating password does not meet policy is displayed. | medium |
| TC-015 (input_edge) | WF-001 | Long text input for Username |  | 1. Enter a very long string (200+ characters) in the Username field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is blocked; error message indicating the Username is too long is displayed. | low |
| TC-016 (input_edge) | WF-001 | Special characters in Username |  | 1. Enter special characters in the Username field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is blocked; error message indicating invalid characters in Username is displayed. | low |

---

## Reports

Total: **5** (positive: 1, negative: 1, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Parameters and Run Report | User logged in as <Role> | 1. Click on the report named <Report Name><br>2. Fill in the parameters form with valid values for the fields<br>3. Click Run Report | Generates report as a data table with sorting and pagination; output options include viewing on screen, exporting to Excel, CSV, or PDF | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to run report without selecting any parameters |  | 1. Click on a report name to open the Parameters Form<br>2. Leave all fields blank<br>3. Click Run Report | Form does not submit; no report is generated; error shown indicating that parameters are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (boundary) | WF-001 | Test report generation with all parameters filled with long text |  | 1. Open the Reports page<br>2. Click on a report to view parameters<br>3. Fill the Office field with a very long string (200+ characters)<br>4. Fill the Branch field with a very long string (200+ characters)<br>5. Fill the Currency field with a very long string (200+ characters)<br>6. Fill the Loan Product field with a very long string (200+ characters)<br>7. Fill the Date Range field with a very long string (200+ characters)<br>8. Fill the Loan Officer field with a very long string (200+ characters)<br>9. Select an option from the Fund dropdown<br>10. Click Run Report | Report is generated successfully; visible output shows the report data table | low |
| TC-004 (input_edge) | WF-001 | Test report generation with special characters in parameters |  | 1. Open the Reports page<br>2. Click on a report to view parameters<br>3. Fill the Office field with special characters (e.g., @#$%^&*)<br>4. Fill the Branch field with special characters (e.g., @#$%^&*)<br>5. Fill the Currency field with special characters (e.g., @#$%^&*)<br>6. Fill the Loan Product field with special characters (e.g., @#$%^&*)<br>7. Fill the Date Range field with special characters (e.g., @#$%^&*)<br>8. Fill the Loan Officer field with special characters (e.g., @#$%^&*)<br>9. Select an option from the Fund dropdown<br>10. Click Run Report | Report is generated successfully; visible output shows the report data table | low |
| TC-005 (input_edge) | WF-001 | Test report generation with leading/trailing whitespace in parameters |  | 1. Open the Reports page<br>2. Click on a report to view parameters<br>3. Fill the Office field with leading and trailing spaces<br>4. Fill the Branch field with leading and trailing spaces<br>5. Fill the Currency field with leading and trailing spaces<br>6. Fill the Loan Product field with leading and trailing spaces<br>7. Fill the Date Range field with leading and trailing spaces<br>8. Fill the Loan Officer field with leading and trailing spaces<br>9. Select an option from the Fund dropdown<br>10. Click Run Report | Leading/trailing whitespace is trimmed; report is generated successfully and displayed correctly | low |

---

## Account Transfers & Standing Instructions

Total: **15** (positive: 1, negative: 8, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit a valid account transfer | User logged in as <Role>, Available balance is sufficient for the transfer amount | 1. Navigate to the Account Transfers form<br>2. Select <From Account Type> from the From Account Type dropdown<br>3. Enter <valid From Account> in the From Account field<br>4. Select <To Account Type> from the To Account Type dropdown<br>5. Enter <valid To Account> in the To Account field<br>6. Enter <valid Transfer Amount> in the Transfer Amount field<br>7. Enter <valid Transfer Date> in the Transfer Date field<br>8. Enter <Description> in the Description field (optional)<br>9. Click Submit | The transfer processes the transfer, debiting the source and crediting the destination | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to submit account transfer with Transfer Amount exceeding available balance |  | 1. Enter <amount exceeding available balance> in the Transfer Amount field<br>2. Enter a valid date in the Transfer Date field<br>3. Click Submit | Form does not submit; error shown on Transfer Amount field indicating 'Transfer amount exceeds available balance' | high |
| TC-003 |  | Leave Transfer Amount field blank and submit |  | 1. Leave the Transfer Amount field blank<br>2. Enter a valid date in the Transfer Date field<br>3. Click Submit | Inline validation error appears on the Transfer Amount field indicating it is required | high |
| TC-004 |  | Leave Transfer Date field blank and submit |  | 1. Enter a valid amount in the Transfer Amount field<br>2. Leave the Transfer Date field blank<br>3. Click Submit | Inline validation error appears on the Transfer Date field indicating it is required | high |
| TC-005 |  | Attempt to submit standing instruction creation form with Name field blank |  | 1. Leave the Name field blank<br>2. Enter a valid value in the Transfer Type field<br>3. Enter a valid value in the Priority field<br>4. Enter a valid value in the Recurrence Frequency field<br>5. Enter a valid value in the Recurrence Interval field<br>6. Click Submit | Inline validation error appears on the Name field indicating it is required | high |
| TC-006 |  | Attempt to submit standing instruction creation form with Transfer Type field blank |  | 1. Enter a valid value in the Name field<br>2. Leave the Transfer Type field blank<br>3. Enter a valid value in the Priority field<br>4. Enter a valid value in the Recurrence Frequency field<br>5. Enter a valid value in the Recurrence Interval field<br>6. Click Submit | Inline validation error appears on the Transfer Type field indicating it is required | high |
| TC-007 |  | Attempt to submit standing instruction creation form with Priority field blank |  | 1. Enter a valid value in the Name field<br>2. Enter a valid value in the Transfer Type field<br>3. Leave the Priority field blank<br>4. Enter a valid value in the Recurrence Frequency field<br>5. Enter a valid value in the Recurrence Interval field<br>6. Click Submit | Inline validation error appears on the Priority field indicating it is required | high |
| TC-008 |  | Attempt to submit standing instruction creation form with Recurrence Frequency field blank |  | 1. Enter a valid value in the Name field<br>2. Enter a valid value in the Transfer Type field<br>3. Enter a valid value in the Priority field<br>4. Leave the Recurrence Frequency field blank<br>5. Enter a valid value in the Recurrence Interval field<br>6. Click Submit | Inline validation error appears on the Recurrence Frequency field indicating it is required | high |
| TC-009 |  | Attempt to submit standing instruction creation form with Recurrence Interval field blank |  | 1. Enter a valid value in the Name field<br>2. Enter a valid value in the Transfer Type field<br>3. Enter a valid value in the Priority field<br>4. Enter a valid value in the Recurrence Frequency field<br>5. Leave the Recurrence Interval field blank<br>6. Click Submit | Inline validation error appears on the Recurrence Interval field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) | WF-001 | Transfer amount equals available balance | User has sufficient balance in the account | 1. Enter the available balance in the Transfer Amount field<br>2. Fill all other required fields<br>3. Click Submit | Transfer processes successfully, debiting the source and crediting the destination | medium |
| TC-011 (boundary) | WF-001 | Transfer amount exceeds available balance | User has insufficient balance in the account | 1. Enter an amount greater than the available balance in the Transfer Amount field<br>2. Fill all other required fields<br>3. Click Submit | Error is shown indicating the transfer amount exceeds available balance | medium |
| TC-012 (data_edge) |  | Enter a future date for Transfer Date |  | 1. Enter a date that is far in the future in the Transfer Date field<br>2. Fill all other required fields<br>3. Click Submit | Transfer processes successfully, debiting the source and crediting the destination | medium |
| TC-013 (data_edge) |  | Enter today's date for Transfer Date |  | 1. Enter today's date in the Transfer Date field<br>2. Fill all other required fields<br>3. Click Submit | Transfer processes successfully, debiting the source and crediting the destination | medium |
| TC-014 (input_edge) |  | Enter a very long description |  | 1. Enter a string of 200+ characters in the Description field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; the saved value in the detail page shows the entire description | low |
| TC-015 (input_edge) |  | Enter special characters in the Name field for Standing Instructions |  | 1. Enter special characters in the Name field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; the saved value displays the special characters correctly | low |

---

## Tax Management

Total: **16** (positive: 4, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new tax component successfully | User logged in as <Role> | 1. Click '+ Create Tax Component'<br>2. Enter <valid name> in the Name field<br>3. Enter <valid percentage> in the Percentage field<br>4. Select 'Asset' from the Debit Account Type dropdown<br>5. Enter <valid debit account> in the Debit Account field<br>6. Select 'Liability' from the Credit Account Type dropdown<br>7. Enter <valid credit account> in the Credit Account field<br>8. Enter <valid start date> in the Start Date field<br>9. Click '+ Create Tax Component' | A success notification is displayed; the Tax component details show the entered values. | high |
| TC-002 | WF-002 | Create a new tax group successfully | User logged in as <Role> | 1. Click '+ Create Tax Group'<br>2. Enter <valid name> in the Name field<br>3. Click 'Add Tax Component'<br>4. Enter <valid start date> in the Start Date field for the component<br>5. Enter <valid end date> in the End Date field for the component<br>6. Select 'Equity' from the Credit Account Type dropdown for the component<br>7. Enter <valid credit account> in the Credit Account field for the component<br>8. Click '+ Create Tax Group' | A success notification is displayed; the Tax group details show the entered values. | high |
| TC-003 | WF-003 | View tax component details | User logged in as <Role> | 1. Click on the Name link of an existing tax component | Tax component details displayed | medium |
| TC-004 | WF-004 | View tax group details | User logged in as <Role> | 1. Click on the Name link of an existing tax group | Tax group details displayed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Leave the Name field blank when creating a Tax Component |  | 1. Open the Create Tax Component form<br>2. Leave the Name field blank<br>3. Fill in a valid Percentage<br>4. Fill in a valid Start Date<br>5. Click + Create Tax Component | Inline validation error appears on the Name field indicating it is required | high |
| TC-006 | WF-001 | Leave the Percentage field blank when creating a Tax Component |  | 1. Open the Create Tax Component form<br>2. Fill in a valid Name<br>3. Leave the Percentage field blank<br>4. Fill in a valid Start Date<br>5. Click + Create Tax Component | Inline validation error appears on the Percentage field indicating it is required | high |
| TC-007 | WF-001 | Leave the Start Date field blank when creating a Tax Component |  | 1. Open the Create Tax Component form<br>2. Fill in a valid Name<br>3. Fill in a valid Percentage<br>4. Leave the Start Date field blank<br>5. Click + Create Tax Component | Inline validation error appears on the Start Date field indicating it is required | high |
| TC-008 | WF-002 | Leave the Name field blank when creating a Tax Group |  | 1. Open the Create Tax Group form<br>2. Leave the Name field blank<br>3. Add a Tax Component with valid fields<br>4. Click + Create Tax Group | Inline validation error appears on the Name field indicating it is required | high |
| TC-009 | WF-002 | Leave the Start Date field blank in Tax Components when creating a Tax Group |  | 1. Open the Create Tax Group form<br>2. Fill in a valid Name<br>3. Add a Tax Component with Start Date blank<br>4. Click + Create Tax Group | Inline validation error appears on the Start Date field indicating it is required | high |
| TC-010 | WF-002 | Attempt to create a Tax Group without adding any Tax Components |  | 1. Open the Create Tax Group form<br>2. Fill in a valid Name<br>3. Click + Create Tax Group | Inline validation error appears indicating at least one Tax Component is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) | WF-001 | Enter minimum percentage value in the Percentage field |  | 1. Open the Create Tax Component form<br>2. Enter the minimum allowed percentage in the Percentage field<br>3. Fill all other required fields<br>4. Click + Create Tax Component | Form submits successfully; entity is created with the minimum percentage value | medium |
| TC-012 (boundary) | WF-001 | Enter one unit below minimum percentage value in the Percentage field |  | 1. Open the Create Tax Component form<br>2. Enter one unit below the minimum allowed percentage in the Percentage field<br>3. Fill all other required fields<br>4. Click + Create Tax Component | Percentage field displays an error indicating the value is below the minimum allowed | medium |
| TC-013 (boundary) | WF-001 | Enter today's date in the Start Date field |  | 1. Open the Create Tax Component form<br>2. Enter today's date in the Start Date field<br>3. Fill all other required fields<br>4. Click + Create Tax Component | Form submits successfully; entity is created with today's date | medium |
| TC-014 (boundary) | WF-001 | Enter yesterday's date in the Start Date field |  | 1. Open the Create Tax Component form<br>2. Enter yesterday's date in the Start Date field<br>3. Fill all other required fields<br>4. Click + Create Tax Component | Form submits successfully; entity is created with yesterday's date | medium |
| TC-015 (boundary) | WF-002 | Add maximum allowed entries to the Tax Components section in Create Tax Group form |  | 1. Open the Create Tax Group form<br>2. Add the maximum allowed entries to the Tax Components section<br>3. Fill all other required fields<br>4. Click + Create Tax Group | Form submits successfully; tax group is created with maximum allowed entries | medium |
| TC-016 (boundary) | WF-002 | Attempt to add one more entry beyond maximum allowed in the Tax Components section |  | 1. Open the Create Tax Group form<br>2. Add the maximum allowed entries to the Tax Components section<br>3. Attempt to add one more entry<br>4. Fill all other required fields<br>5. Click + Create Tax Group | Adding the extra entry is blocked; visible error shown indicating the limit has been reached | medium |

---

## Organization Settings

Total: **18** (positive: 8, negative: 5, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Holiday Creation Form | User logged in as <Role> | 1. Click '+ Create Holiday' button | opens holiday creation form | high |
| TC-002 | WF-002 | Submit Holiday Creation Form | User logged in as <Role>, Holiday creation form is open | 1. Enter <valid holiday name> in the Name field<br>2. Enter <valid start date> in the From Date field<br>3. Enter <valid end date> in the To Date field<br>4. Click Submit | Holidays affect loan repayment schedules | high |
| TC-003 | WF-003 | Configure Working Days | User logged in as <Role>, Working Days page is open | 1. Check the checkbox for Monday<br>2. Check the checkbox for Tuesday<br>3. Click Submit | Working days updated | medium |
| TC-004 | WF-004 | Open Fund Creation Form | User logged in as <Role> | 1. Click 'Create Fund' button | opens fund creation form | high |
| TC-005 | WF-005 | Submit Fund Creation Form | User logged in as <Role>, Fund creation form is open | 1. Enter <valid fund name> in the Fund Name field<br>2. Enter <valid external ID> in the External ID field<br>3. Click Submit | Fund created | high |
| TC-006 | WF-006 | Add New Payment Type | User logged in as <Role>, Payment Types page is open | 1. Click '+ Create' button<br>2. Enter <valid payment type name> in the Name field<br>3. Enter <valid description> in the Description field<br>4. Click Submit | adds new payment type | medium |
| TC-007 | WF-007 | Download Import Template | User logged in as <Role>, Bulk Import page is open | 1. Click 'Download template' button | downloads import template | medium |
| TC-008 | WF-008 | Upload Data for Import | User logged in as <Role>, Bulk Import page is open | 1. Click 'Upload' button<br>2. Select <valid import file> from the file dialog<br>3. Click Confirm on the upload dialog | uploads data for import | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 | WF-001 | Leave the Name field blank when creating a holiday |  | 1. Click on '+ Create Holiday'<br>2. Leave the Name field blank<br>3. Fill in the From Date and To Date fields<br>4. Click Submit | Inline validation error appears on the Name field indicating it is required | high |
| TC-010 | WF-001 | Leave all required fields blank when creating a holiday |  | 1. Click on '+ Create Holiday'<br>2. Leave the Name, From Date, and To Date fields blank<br>3. Click Submit | Inline validation error appears on the Name field indicating it is required; Inline validation error appears on the From Date field indicating it is required; Inline validation error appears on the To Date field indicating it is required | high |
| TC-011 | WF-002 | Submit holiday creation form with invalid From Date |  | 1. Click on '+ Create Holiday'<br>2. Fill in the Name field<br>3. Enter <invalid date format> in the From Date field<br>4. Enter a valid date in the To Date field<br>5. Click Submit | Inline validation error appears on the From Date field indicating it must be a valid date | medium |
| TC-012 | WF-002 | Submit holiday creation form with From Date after To Date |  | 1. Click on '+ Create Holiday'<br>2. Fill in the Name field<br>3. Enter a valid date in the From Date field<br>4. Enter a date earlier than the From Date in the To Date field<br>5. Click Submit | Inline validation error appears on the To Date field indicating it must be after the From Date | medium |
| TC-013 | WF-003 | Submit working days configuration without selecting any days |  | 1. Navigate to Working Days page<br>2. Leave all checkboxes for days of the week unchecked<br>3. Click Submit | No changes occur; the working days remain unchanged | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 (boundary) | WF-002 | Create Holiday with From_Date and To_Date as the same day |  | 1. Click + Create Holiday<br>2. Enter a valid Name in the Name field<br>3. Enter today's date in the From_Date field<br>4. Enter today's date in the To_Date field<br>5. Click Submit | Holiday is created successfully with From_Date and To_Date set to today | medium |
| TC-015 (boundary) | WF-002 | Create Holiday with From_Date one day before To_Date |  | 1. Click + Create Holiday<br>2. Enter a valid Name in the Name field<br>3. Enter today's date in the From_Date field<br>4. Enter tomorrow's date in the To_Date field<br>5. Click Submit | Holiday is created successfully; From_Date is today and To_Date is tomorrow | medium |
| TC-016 (boundary) | WF-002 | Create Holiday with From_Date after To_Date |  | 1. Click + Create Holiday<br>2. Enter a valid Name in the Name field<br>3. Enter tomorrow's date in the From_Date field<br>4. Enter today's date in the To_Date field<br>5. Click Submit | Submission is blocked; error shown indicating 'From_Date must be before To_Date' | medium |
| TC-017 (input_edge) | WF-007 | Download Import Template with long entity type name |  | 1. Click Download template<br>2. Check the download folder | Template downloads successfully without errors | low |
| TC-018 (input_edge) | WF-008 | Upload data with special characters in entity types |  | 1. Prepare a data file with special characters in entity types<br>2. Click Upload<br>3. Select the prepared file<br>4. Click Confirm Upload | Upload is successful; data is imported without errors | low |

---

## System Administration

Total: **14** (positive: 3, negative: 4, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Start all scheduled jobs | User logged in as <Admin>, All scheduled jobs are inactive | 1. Click 'Start All' button | All scheduled jobs started | high |
| TC-002 | WF-002 | Stop all scheduled jobs | User logged in as <Admin>, All scheduled jobs are active | 1. Click 'Stop All' button | All scheduled jobs stopped | high |
| TC-003 | WF-003 | Submit new custom data table | User logged in as <Admin> | 1. Navigate to Manage Data Tables<br>2. Enter <Data Table Name> in the Data Table Name field<br>3. Select 'm_client' from the Application Table Name dropdown<br>4. Check the Multi Row checkbox<br>5. Click 'Add Row' in Column Definitions<br>6. Enter <Column Name> in the Name field of the new row<br>7. Select 'string' from the Type dropdown<br>8. Click 'Submit' button | Custom data table created | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave Data Table Name blank and submit |  | 1. Leave the Data Table Name field blank<br>2. Select an Application Table Name<br>3. Click Submit | Inline validation error appears on the Data Table Name field indicating it is required | high |
| TC-005 |  | Leave Name field in Column Definitions blank and submit |  | 1. Click to add a new column definition<br>2. Leave the Name field blank<br>3. Select a Type<br>4. Click Submit | Inline validation error appears on the Name field indicating it is required | high |
| TC-006 |  | Attempt to start all jobs when none are scheduled |  | 1. Click Start All | No jobs started; error message displayed indicating there are no scheduled jobs to start | medium |
| TC-007 |  | Attempt to stop all jobs when none are running |  | 1. Click Stop All | No jobs stopped; error message displayed indicating there are no jobs currently running | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) | WF-003 | Add maximum allowed entries to Column Definitions | User is on Manage Data Tables form | 1. Enter a valid Data Table Name in the Data_Table_Name field<br>2. Select an Application Table Name from the dropdown<br>3. Add exactly maximum allowed entries to the Column Definitions repeating group | Form submits successfully; custom data table is created with the maximum number of column definitions | medium |
| TC-009 (boundary) | WF-003 | Attempt to add one more entry to Column Definitions | User is on Manage Data Tables form | 1. Enter a valid Data Table Name in the Data_Table_Name field<br>2. Select an Application Table Name from the dropdown<br>3. Add maximum allowed entries to the Column Definitions repeating group<br>4. Attempt to add one more entry to the Column Definitions | Attempt to add entry is blocked; visible error shown indicating maximum entries reached | medium |
| TC-010 (boundary) | WF-003 | Enter maximum length for Name in Column Definitions | User is on Manage Data Tables form | 1. Enter a valid Data Table Name in the Data_Table_Name field<br>2. Select an Application Table Name from the dropdown<br>3. Add an entry to the Column Definitions repeating group<br>4. Enter exactly maximum length for the Name field | Form submits successfully; custom data table is created with the maximum length Name | medium |
| TC-011 (boundary) | WF-003 | Enter one character less than maximum length for Name in Column Definitions | User is on Manage Data Tables form | 1. Enter a valid Data Table Name in the Data_Table_Name field<br>2. Select an Application Table Name from the dropdown<br>3. Add an entry to the Column Definitions repeating group<br>4. Enter one character less than the maximum length for the Name field | Form submits successfully; custom data table is created with the Name field accepted | medium |
| TC-012 (input_edge) |  | Enter long text in Data Table Name | User is on Manage Data Tables form | 1. Enter a very long string (200+ characters) in the Data_Table_Name field | Form submission is either accepted or truncated with a visible indicator | low |
| TC-013 (input_edge) |  | Enter special characters in Data Table Name | User is on Manage Data Tables form | 1. Enter special characters in the Data_Table_Name field | Form submission is either accepted or a specific error shown | low |
| TC-014 (input_edge) |  | Enter leading/trailing whitespace in Data Table Name | User is on Manage Data Tables form | 1. Enter a value with leading/trailing spaces in the Data_Table_Name field | Leading/trailing whitespace is trimmed; saved value shown on detail page has no extra spaces | low |

---

## Logout

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | User logs out successfully from the user profile icon | User logged in as <Role> | 1. Click the User Profile Icon in the top-right corner<br>2. Select 'Log Out' from the dropdown | User is redirected to the login page and the authenticated session is terminated | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to log out without being authenticated | User is not authenticated | 1. Click on the User Profile Icon<br>2. Select 'Log Out' from the dropdown | User remains on the current page; no session is terminated; user is not redirected to the login page | high |
| TC-003 |  | Attempt to access an authenticated page after logout | User is logged out | 1. Attempt to navigate to an authenticated page | User is redirected to the login page | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (interaction_edge) | WF-001 | Rapid logout attempts | User is logged in | 1. Click on the User Profile Icon<br>2. Click on 'Log Out'<br>3. Immediately click on the User Profile Icon again<br>4. Click on 'Log Out' again | Second logout attempt is blocked; user remains on the login page without a second session being created. | medium |
| TC-005 (interaction_edge) |  | Navigate to authenticated page after logout | User is logged in, User has logged out | 1. Attempt to navigate to an authenticated page | User is redirected to the login page. | medium |

---
