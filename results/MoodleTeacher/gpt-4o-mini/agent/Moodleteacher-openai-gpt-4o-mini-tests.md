# Test Cases — Moodleteacher

Generated: 2026-06-04T14:33:52.568351Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 15 | 207 | 66 | 73 | 68 | 83 | 89 | 20 |

## Login

Total: **13** (positive: 3, negative: 4, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Log in with valid credentials | User logged in as <Teacher> | 1. Enter <valid username> in the Username field<br>2. Enter <valid password> in the Password field<br>3. Click Log in | redirects to Dashboard | high |
| TC-002 | WF-002 | Access as Guest | User logged in as <Guest> | 1. Click Access as a guest | unauthenticated browsing | medium |
| TC-003 | WF-003 | View Cookies Notice | User logged in as <User> | 1. Click Cookies notice | provides cookie usage information | low |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave the Username field blank and submit |  | 1. Leave the Username field blank<br>2. Fill the Password field with <valid password><br>3. Click Log in | Inline validation error appears on the Username field indicating it is required | high |
| TC-005 |  | Leave the Password field blank and submit |  | 1. Fill the Username field with <valid username><br>2. Leave the Password field blank<br>3. Click Log in | Inline validation error appears on the Password field indicating it is required | high |
| TC-006 |  | Submit with invalid credentials |  | 1. Fill the Username field with <valid username><br>2. Fill the Password field with <invalid password><br>3. Click Log in | Form does not submit; Password field is cleared; error shown: 'Invalid or empty credentials' | high |
| TC-007 | WF-002 | Attempt to access as guest without authentication |  | 1. Click Access as a guest | User is redirected to the login page | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (input_edge) |  | Enter a very long username |  | 1. Enter a string of 200+ characters in the Username field<br>2. Enter a valid password in the Password field<br>3. Click Log in | Form submits successfully; user is redirected to Dashboard or an error indicates the username is too long | low |
| TC-009 (input_edge) |  | Enter special characters in the Username field |  | 1. Enter '@!#$%^&*()' in the Username field<br>2. Enter a valid password in the Password field<br>3. Click Log in | Form submits successfully; user is redirected to Dashboard or an error indicates invalid characters in the Username | low |
| TC-010 (input_edge) |  | Enter leading and trailing whitespace in the Username field |  | 1. Enter '   user123   ' in the Username field<br>2. Enter a valid password in the Password field<br>3. Click Log in | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |
| TC-011 (boundary) |  | Enter empty credentials |  | 1. Leave the Username field empty<br>2. Leave the Password field empty<br>3. Click Log in | Inline error message shows 'Invalid or empty credentials'; Password field is cleared, Username field retains input | medium |
| TC-012 (boundary) |  | Enter valid username and empty password |  | 1. Enter a valid username in the Username field<br>2. Leave the Password field empty<br>3. Click Log in | Inline error message shows 'Invalid or empty credentials'; Password field is cleared, Username field retains input | medium |
| TC-013 (boundary) |  | Enter valid credentials |  | 1. Enter a valid username in the Username field<br>2. Enter a valid password in the Password field<br>3. Click Log in | Form submits successfully; user is redirected to Dashboard | medium |

---

## Dashboard

Total: **15** (positive: 5, negative: 5, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create a new calendar event | User logged in as <Role> | 1. Click the 'New Event' button | A new calendar entry is created | high |
| TC-002 | WF-002 | Navigate to the previous month | User logged in as <Role> | 1. Click the 'Previous Month' button | Navigates to the previous month | medium |
| TC-003 | WF-003 | Navigate to the next month | User logged in as <Role> | 1. Click the 'Next Month' button | Navigates to the next month | medium |
| TC-004 | WF-004 | Open full calendar view | User logged in as <Role> | 1. Click the 'Full calendar' link | Opens dedicated calendar view | medium |
| TC-005 | WF-005 | Open calendar data management | User logged in as <Role> | 1. Click the 'Import or export calendars' link | Opens calendar data management | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 | WF-001 | Attempt to create a new calendar event without filling required fields |  | 1. Click on the 'New event' button | Form does not submit; no calendar entry is created; error shown on required fields |  |
| TC-007 | WF-002 | Attempt to navigate to the previous month without any events |  | 1. Click on the 'Previous Month' button | Calendar view updates to the previous month; no error shown |  |
| TC-008 | WF-003 | Attempt to navigate to the next month without any events |  | 1. Click on the 'Next Month' button | Calendar view updates to the next month; no error shown |  |
| TC-009 | WF-004 | Attempt to open full calendar view without authentication |  | 1. Click on the 'Full calendar' link | User is redirected to the login page |  |
| TC-010 | WF-005 | Attempt to open calendar data management without authentication |  | 1. Click on the 'Import or export calendars' link | User is redirected to the login page |  |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (interaction_edge) | WF-001 | Rapid submission of new calendar event | User is on the Dashboard | 1. Click the 'New Event' button<br>2. Immediately click the 'New Event' button again | Second submission attempt is blocked; only one calendar entry is created | medium |
| TC-012 (interaction_edge) | WF-002 | Navigate to previous month rapidly | User is on the Calendar block | 1. Click the 'Previous Month' button<br>2. Immediately click the 'Previous Month' button again | Navigation to previous month is blocked; the calendar remains on the current month | medium |
| TC-013 (interaction_edge) | WF-003 | Navigate to next month rapidly | User is on the Calendar block | 1. Click the 'Next Month' button<br>2. Immediately click the 'Next Month' button again | Navigation to next month is blocked; the calendar remains on the current month | medium |
| TC-014 (input_edge) |  | Enter long text in search activities field | User is on the Dashboard | 1. Enter a very long string (200+ characters) in the 'Search Activities' field | Search field displays an error indicating the input exceeds the maximum allowed length | low |
| TC-015 (input_edge) |  | Enter special characters in search activities field | User is on the Dashboard | 1. Enter special characters (e.g., @#$%^&*) in the 'Search Activities' field | Search field displays an error indicating invalid characters | low |

---

## Dashboard — Edit Mode

Total: **16** (positive: 6, negative: 6, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Reset the dashboard page to default | User logged in as <Role>, Edit mode is enabled | 1. Click 'Reset page to default' button | The page resets to default | high |
| TC-002 | WF-002 | Open Add a block page | User logged in as <Role>, Edit mode is enabled | 1. Click '+ Add a block' button | opens Add a block page | high |
| TC-003 | WF-003 | Cancel adding a block | User logged in as <Role>, Edit mode is enabled, Add a block page is open | 1. Click 'Cancel' | returns to Dashboard without adding a block | medium |
| TC-004 | WF-004 | Configure an existing block | User logged in as <Role>, Edit mode is enabled, At least one existing block is present | 1. Click the options menu of an existing block<br>2. Select 'configure' | Configuration options displayed for the block | medium |
| TC-005 | WF-005 | Move an existing block | User logged in as <Role>, Edit mode is enabled, At least one existing block is present | 1. Click the options menu of an existing block<br>2. Select 'move' | Block is moved to a new position | medium |
| TC-006 | WF-006 | Delete an existing block | User logged in as <Role>, Edit mode is enabled, At least one existing block is present | 1. Click the options menu of an existing block<br>2. Select 'delete' | Block is deleted from the Dashboard | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 | WF-001 | Attempt to reset page to default while in Edit mode |  | 1. Click the 'Reset page to default' button | Page does not reset; layout remains unchanged |  |
| TC-008 | WF-002 | Attempt to add a block without valid input |  | 1. Click the '+ Add a block' button | Add a block page opens; no block is added |  |
| TC-009 | WF-003 | Cancel adding a block and verify no block is added |  | 1. Click the '+ Add a block' button<br>2. Click the 'Cancel' button | Returns to Dashboard without adding a block |  |
| TC-010 | WF-004 | Attempt to configure an existing block without selecting it |  | 1. Click the 'configure' button without selecting a block | Configuration options are not displayed; no action occurs |  |
| TC-011 | WF-005 | Attempt to move an existing block without selecting it |  | 1. Click the 'move' button without selecting a block | Block is not moved; no action occurs |  |
| TC-012 | WF-006 | Attempt to delete an existing block without selecting it |  | 1. Click the 'delete' button without selecting a block | Block is not deleted; no action occurs |  |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-013 (interaction_edge) | WF-001 | Rapidly click the Reset page to default button | Edit mode is toggled on | 1. Click the 'Reset page to default' button<br>2. Immediately click the 'Reset page to default' button again | Second click is ignored; the page remains reset to default | medium |
| TC-014 (interaction_edge) | WF-002 | Rapidly click the Add a block button | Edit mode is toggled on | 1. Click the '+ Add a block' button<br>2. Immediately click the '+ Add a block' button again | Second click is ignored; the Add a block page opens only once | medium |
| TC-015 (interaction_edge) | WF-003 | Click Cancel after opening Add a block page | Edit mode is toggled on, Add a block page is opened | 1. Click the 'Cancel' link | Returns to Dashboard without adding a block; no new block is created | medium |
| TC-016 (interaction_edge) | WF-006 | Delete existing block after rapid clicks | Edit mode is toggled on, At least one block exists | 1. Click the 'delete' option from the options menu of an existing block<br>2. Immediately click the 'delete' option again | Only one block is deleted; the second click is ignored | medium |

---

## My Courses

Total: **10** (positive: 2, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Star a course | User logged in as <Teacher>, Courses are displayed on the My Courses page | 1. Click the three-dot menu on a course card<br>2. Select 'Star this course' from the menu | Course starred; pinned to the top | high |
| TC-002 | WF-002 | Remove a course from view | User logged in as <Teacher>, Courses are displayed on the My Courses page | 1. Click the three-dot menu on a course card<br>2. Select 'Remove from view' from the menu | Course removed from view; hidden | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Search field blank and submit |  | 1. Leave the Search field blank<br>2. Click the search button | No courses are displayed; the Search field remains empty |  |
| TC-004 |  | Select an invalid option in the Status dropdown |  | 1. Select 'Invalid Status' in the Status dropdown<br>2. Click the search button | No courses are displayed; the Status dropdown shows 'Invalid Status' as selected |  |
| TC-005 | WF-001 | Attempt to star a course without selecting a course |  | 1. Click on the 'Star this course' action without selecting any course | No course is starred; the action is not performed |  |
| TC-006 | WF-002 | Attempt to remove a course from view without selecting a course |  | 1. Click on the 'Remove from view' action without selecting any course | No course is removed from view; the action is not performed |  |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (interaction_edge) | WF-001 | Rapidly star a course after starring another | User is on the My Courses page with multiple courses displayed | 1. Click the three-dot menu on the first course card<br>2. Select 'Star this course'<br>3. Immediately click the three-dot menu on the second course card<br>4. Select 'Star this course' | Both courses are starred; the first course remains pinned at the top and the second course is also pinned above others. | medium |
| TC-008 (interaction_edge) | WF-002 | Rapidly remove a course from view after removing another | User is on the My Courses page with multiple courses displayed | 1. Click the three-dot menu on the first course card<br>2. Select 'Remove from view'<br>3. Immediately click the three-dot menu on the second course card<br>4. Select 'Remove from view' | Both courses are removed from view; they no longer appear in the course list. | medium |
| TC-009 (input_edge) |  | Search with leading and trailing whitespace | User is on the My Courses page | 1. Enter '   Course Name   ' in the Search field<br>2. Press Enter | Search results display courses matching 'Course Name' without leading or trailing whitespace. | low |
| TC-010 (input_edge) |  | Search with special characters | User is on the My Courses page | 1. Enter '@Course#Name!' in the Search field<br>2. Press Enter | Search results display courses matching '@Course#Name!' or show a message indicating no matches found. | low |

---

## Course Page

Total: **15** (positive: 5, negative: 5, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Access Activity 1 | User logged in as <Role> | 1. Click on 'Activity 1' link | Navigated to Activity 1 | high |
| TC-002 | WF-002 | Access Resource 1 | User logged in as <Role> | 1. Click on 'Resource 1' link | Navigated to Resource 1 | high |
| TC-003 | WF-003 | Access Activity 2 | User logged in as <Role> | 1. Click on 'Activity 2' link | Navigated to Activity 2 | high |
| TC-004 | WF-004 | Access Resource 2 | User logged in as <Role> | 1. Click on 'Resource 2' link | Navigated to Resource 2 | high |
| TC-005 | WF-005 | Collapse all sections | User logged in as <Role> | 1. Click on 'Collapse All' link | All sections collapsed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Attempt to access Activity 1 without being logged in | User is not authenticated | 1. Click on Activity 1 | Page redirects to login page | high |
| TC-007 |  | Attempt to access Resource 1 without being logged in | User is not authenticated | 1. Click on Resource 1 | Page redirects to login page | high |
| TC-008 |  | Attempt to access Activity 2 without being logged in | User is not authenticated | 1. Click on Activity 2 | Page redirects to login page | high |
| TC-009 |  | Attempt to access Resource 2 without being logged in | User is not authenticated | 1. Click on Resource 2 | Page redirects to login page | high |
| TC-010 |  | Click Collapse All when no sections are expanded | All sections are already collapsed | 1. Click on Collapse All link | No sections are collapsed; all sections remain hidden | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (interaction_edge) | WF-005 | Collapse all sections after expanding one | User has accessed the course page and expanded Section 1 | 1. Click the 'Collapse All' link | All sections are collapsed; Section 1 is not expanded anymore. | medium |
| TC-012 (interaction_edge) | WF-001 | Access Activity 1 after collapsing all sections | User has collapsed all sections | 1. Click on 'Activity 1' link | Navigated to Activity 1. | medium |
| TC-013 (interaction_edge) | WF-002 | Access Resource 1 after collapsing all sections | User has collapsed all sections | 1. Click on 'Resource 1' link | Navigated to Resource 1. | medium |
| TC-014 (interaction_edge) | WF-003 | Access Activity 2 after collapsing all sections | User has collapsed all sections | 1. Click on 'Activity 2' link | Navigated to Activity 2. | medium |
| TC-015 (interaction_edge) | WF-004 | Access Resource 2 after collapsing all sections | User has collapsed all sections | 1. Click on 'Resource 2' link | Navigated to Resource 2. | medium |

---

## Course Edit Mode and Activity Chooser

Total: **26** (positive: 9, negative: 9, edge: 8)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Add a subsection to the course | User logged in as <Role>, Edit mode is enabled | 1. Click '+ Add a subsection' | Subsection added to the course | high |
| TC-002 | WF-002 | Open the Activity Chooser modal | User logged in as <Role>, Edit mode is enabled | 1. Click '+ Add an activity or resource' | Activity chooser modal opens | high |
| TC-003 | WF-003 | Select and add an activity from the chooser | User logged in as <Role>, Edit mode is enabled, Activity chooser modal is open | 1. Select 'Assignment' from the activity/resource tiles<br>2. Click 'Add' | Activity creation form opens | high |
| TC-004 | WF-004 | Edit settings of an activity | User logged in as <Role>, Edit mode is enabled, At least one activity exists | 1. Click the three-dot menu on the activity row<br>2. Select 'Edit Settings' | Activity settings edited successfully | high |
| TC-005 | WF-005 | Move an activity | User logged in as <Role>, Edit mode is enabled, At least one activity exists | 1. Click the three-dot menu on the activity row<br>2. Select 'Move' | Activity moved successfully | high |
| TC-006 | WF-006 | Duplicate an activity | User logged in as <Role>, Edit mode is enabled, At least one activity exists | 1. Click the three-dot menu on the activity row<br>2. Select 'Duplicate' | Activity duplicated successfully | high |
| TC-007 | WF-007 | Hide an activity | User logged in as <Role>, Edit mode is enabled, At least one activity exists | 1. Click the three-dot menu on the activity row<br>2. Select 'Hide' | Activity hidden successfully | high |
| TC-008 | WF-008 | Set access restrictions on an activity | User logged in as <Role>, Edit mode is enabled, At least one activity exists | 1. Click the three-dot menu on the activity row<br>2. Select 'Set Access Restrictions' | Access restrictions set successfully | high |
| TC-009 | WF-009 | Delete an activity | User logged in as <Role>, Edit mode is enabled, At least one activity exists | 1. Click the three-dot menu on the activity row<br>2. Select 'Delete' | Activity deleted successfully | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 | WF-001 | Attempt to add a subsection without any sections present |  | 1. Click on '+ Add a subsection' | No action occurs; error shown indicating that a section must be present to add a subsection | high |
| TC-011 | WF-002 | Attempt to open the Activity Chooser modal without any sections present |  | 1. Click on '+ Add an activity or resource' | No action occurs; error shown indicating that a section must be present to add an activity | high |
| TC-012 | WF-003 | Attempt to add an activity without selecting any tile |  | 1. Click on '+ Add an activity or resource'<br>2. Open the Activity Chooser modal<br>3. Click 'Add' without selecting any activity tile | No action occurs; error shown indicating that an activity must be selected to add | high |
| TC-013 | WF-004 | Attempt to edit settings of an activity that does not exist |  | 1. Click on 'Edit Settings' for an activity that is not present | No action occurs; error shown indicating that the activity does not exist | medium |
| TC-014 | WF-005 | Attempt to move an activity that does not exist |  | 1. Click on 'Move' for an activity that is not present | No action occurs; error shown indicating that the activity does not exist | medium |
| TC-015 | WF-006 | Attempt to duplicate an activity that does not exist |  | 1. Click on 'Duplicate' for an activity that is not present | No action occurs; error shown indicating that the activity does not exist | medium |
| TC-016 | WF-007 | Attempt to hide an activity that does not exist |  | 1. Click on 'Hide' for an activity that is not present | No action occurs; error shown indicating that the activity does not exist | medium |
| TC-017 | WF-008 | Attempt to set access restrictions on an activity that does not exist |  | 1. Click on 'Set Access Restrictions' for an activity that is not present | No action occurs; error shown indicating that the activity does not exist | medium |
| TC-018 | WF-009 | Attempt to delete an activity that does not exist |  | 1. Click on 'Delete' for an activity that is not present | No action occurs; error shown indicating that the activity does not exist | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-019 (boundary) | WF-001 | Add maximum allowed subsections | User is in Course Edit Mode | 1. Add maximum allowed subsections to the course<br>2. Attempt to add one more subsection | Adding maximum allowed subsections succeeds; adding one more is blocked with a visible error indicating the maximum limit reached. | medium |
| TC-020 (boundary) | WF-002 | Open Activity Chooser modal | User is in Course Edit Mode | 1. Click on '+ Add an activity or resource' | Activity chooser modal opens successfully. | medium |
| TC-021 (boundary) | WF-003 | Select and add an activity from the chooser | Activity chooser modal is open | 1. Select a tile from the Activity Resource Tiles<br>2. Click 'Add' | Activity creation form opens successfully. | medium |
| TC-022 (boundary) | WF-004 | Edit settings of an activity | User is in Course Edit Mode, At least one activity exists | 1. Click on 'Edit Settings' for an existing activity | Activity settings edited successfully. | medium |
| TC-023 (boundary) | WF-009 | Delete an activity | User is in Course Edit Mode, At least one activity exists | 1. Click on 'Delete' for an existing activity | Activity deleted successfully. | medium |
| TC-024 (input_edge) |  | Enter long text in Activity Title | User is in Course Edit Mode, Activity creation form is open | 1. Enter a very long string (200+ characters) in the 'Activity_Title' field | Form submission is either accepted or shows a visible error indicating the title is too long. | low |
| TC-025 (input_edge) |  | Enter special characters in Activity Title | User is in Course Edit Mode, Activity creation form is open | 1. Enter special characters in the 'Activity_Title' field | Form submission is either accepted or shows a specific error indicating invalid characters. | low |
| TC-026 (input_edge) |  | Trim leading/trailing whitespace in Activity Title | User is in Course Edit Mode, Activity creation form is open | 1. Enter a value with leading and trailing spaces in the 'Activity_Title' field<br>2. Submit the form | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces. | low |

---

## Assignment Creation

Total: **12** (positive: 3, negative: 4, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Create assignment and redirect to course page | User logged in as <Role> | 1. Open the Assignment Creation form<br>2. Enter <valid assignment name> in the Assignment Name field<br>3. Click 'Save and return to course' | Assignment is created and redirects to the course page | high |
| TC-002 | WF-002 | Create assignment and open new assignment's page | User logged in as <Role> | 1. Open the Assignment Creation form<br>2. Enter <valid assignment name> in the Assignment Name field<br>3. Click 'Save and display' | Assignment is created and opens new assignment's page | high |
| TC-003 | WF-003 | Discard changes and cancel assignment creation | User logged in as <Role> | 1. Open the Assignment Creation form<br>2. Click 'Cancel' | All changes are discarded | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Attempt to save assignment with blank Assignment Name |  | 1. Leave the Assignment Name field blank<br>2. Fill all other fields as desired<br>3. Click 'Save and return to course' | Inline validation error appears on the Assignment Name field indicating it is required | high |
| TC-005 | WF-002 | Attempt to save assignment with blank Assignment Name |  | 1. Leave the Assignment Name field blank<br>2. Fill all other fields as desired<br>3. Click 'Save and display' | Inline validation error appears on the Assignment Name field indicating it is required | high |
| TC-006 |  | Attempt to save assignment with all required fields empty |  | 1. Leave the Assignment Name field blank<br>2. Leave all other fields blank<br>3. Click 'Save and return to course' | Inline validation error appears on the Assignment Name field indicating it is required | high |
| TC-007 |  | Attempt to save assignment with all required fields empty |  | 1. Leave the Assignment Name field blank<br>2. Leave all other fields blank<br>3. Click 'Save and display' | Inline validation error appears on the Assignment Name field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) | WF-002 | Enter maximum length for Assignment Name | Assignment Creation form is open | 1. Enter maximum allowed length in the Assignment_Name field<br>2. Fill all other required fields<br>3. Click 'Save and display' | Form submits successfully; entity is created with the maximum length value in the Assignment_Name field | medium |
| TC-009 (boundary) | WF-002 | Enter one character less than maximum length for Assignment Name | Assignment Creation form is open | 1. Enter one character less than maximum allowed length in the Assignment_Name field<br>2. Fill all other required fields<br>3. Click 'Save and display' | Form submits successfully; entity is created with the value in the Assignment_Name field | medium |
| TC-010 (input_edge) |  | Enter a long string in the Description field | Assignment Creation form is open | 1. Enter a long string (200+ characters) in the Description field<br>2. Fill all other required fields<br>3. Click 'Save and display' | Form submits successfully; Description field displays the long string correctly | low |
| TC-011 (data_edge) |  | Upload a file at the exact maximum size limit | Assignment Creation form is open, File_Submissions checkbox is checked | 1. Upload a file that is exactly at the maximum submission size limit in the Additional_Files field<br>2. Fill all other required fields<br>3. Click 'Save and display' | Form submits successfully; file is accepted and displayed in the Additional_Files field | medium |
| TC-012 (data_edge) |  | Upload a file exceeding the maximum size limit | Assignment Creation form is open, File_Submissions checkbox is checked | 1. Upload a file that is one byte over the maximum submission size limit in the Additional_Files field<br>2. Fill all other required fields<br>3. Click 'Save and display' | Form submission is blocked; an error message indicates that the file exceeds the maximum submission size | medium |

---

## Course Settings

Total: **12** (positive: 2, negative: 4, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successfully save and display course settings | User logged in as <Role> | 1. Enter <valid course full name> in the Course Full Name field<br>2. Enter <valid course short name> in the Course Short Name field<br>3. Select <valid course category> from the Course Category dropdown<br>4. Select <visibility option> from the Course Visibility dropdown<br>5. Enter <valid start date> in the Course Start Date field<br>6. Click 'Save and display' | persists the configuration and returns to the course page | high |
| TC-002 | WF-002 | Successfully cancel course settings | User logged in as <Role> | 1. Enter <valid course full name> in the Course Full Name field<br>2. Enter <valid course short name> in the Course Short Name field<br>3. Select <valid course category> from the Course Category dropdown<br>4. Click 'Cancel' | leaves existing settings unchanged | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Leave the Course Full Name field blank and submit |  | 1. Leave the Course Full Name field blank<br>2. Fill all other required fields<br>3. Click Save and display | Inline validation error appears on the Course Full Name field indicating it is required | high |
| TC-004 | WF-001 | Leave the Course Short Name field blank and submit |  | 1. Leave the Course Short Name field blank<br>2. Fill all other required fields<br>3. Click Save and display | Inline validation error appears on the Course Short Name field indicating it is required | high |
| TC-005 | WF-001 | Leave the Course Category field blank and submit |  | 1. Leave the Course Category field blank<br>2. Fill all other required fields<br>3. Click Save and display | Inline validation error appears on the Course Category field indicating it is required | high |
| TC-006 | WF-001 | Submit with all required fields empty |  | 1. Leave the Course Full Name field blank<br>2. Leave the Course Short Name field blank<br>3. Leave the Course Category field blank<br>4. Click Save and display | Form does not submit; Course Full Name, Course Short Name, and Course Category fields display errors indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) |  | Test Course Start Date with today's date |  | 1. Enter today's date in the Course Start Date field<br>2. Fill all other required fields<br>3. Click Save and display | Configuration persists successfully and returns to the course page | medium |
| TC-008 (boundary) |  | Test Course End Date with today's date |  | 1. Enter today's date in the Course End Date field<br>2. Fill all other required fields<br>3. Click Save and display | Configuration persists successfully and returns to the course page | medium |
| TC-009 (boundary) |  | Test Course End Date with yesterday's date |  | 1. Enable Course End Date toggle<br>2. Enter yesterday's date in the Course End Date field<br>3. Fill all other required fields<br>4. Click Save and display | Error shown indicating that the Course End Date cannot be before the Course Start Date | medium |
| TC-010 (input_edge) |  | Test Course Full Name with a long string |  | 1. Enter a string of 200+ characters in the Course Full Name field<br>2. Fill all other required fields<br>3. Click Save and display | Configuration persists successfully and returns to the course page | low |
| TC-011 (input_edge) |  | Test Course Summary with special characters |  | 1. Enter special characters in the Course Summary field<br>2. Fill all other required fields<br>3. Click Save and display | Configuration persists successfully and returns to the course page | low |
| TC-012 (interaction_edge) |  | Test rapid submission after redirect |  | 1. Click Save and display<br>2. Press the browser back button immediately after submission | Course Settings form is shown blank without pre-filled data | low |

---

## Participants Management

Total: **21** (positive: 8, negative: 7, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Apply filters using the filter system | User logged in as <Role> | 1. Select 'Role' from the Select Attribute dropdown<br>2. Click 'Apply Filters' | The system applies selected filters | high |
| TC-002 | WF-002 | Clear all filters | User logged in as <Role> | 1. Click 'Clear Filters' | The system clears all filters | high |
| TC-003 | WF-003 | Open enrollment dialog | User logged in as <Role> | 1. Click 'Enrol Users' | The system opens enrollment dialog | high |
| TC-004 | WF-004 | Confirm enrollment of a user | User logged in as <Role>, Enrollment dialog is open | 1. Enter <valid user> in the User Search field<br>2. Select 'Student' from the Role dropdown<br>3. Click 'Confirm Enrollment' | The system adds user to course at specified role | high |
| TC-005 | WF-005 | View user profile | User logged in as <Role> | 1. Click on the profile link of a user in the Participants Table<br>2. Observe the profile page | The system displays user profile | medium |
| TC-006 | WF-006 | Edit user role | User logged in as <Role> | 1. Click on the three-dot action menu of a user in the Participants Table<br>2. Select 'Edit Role'<br>3. Choose a new role from the dropdown<br>4. Click 'Save' | The system updates user role | medium |
| TC-007 | WF-007 | Send message to a user | User logged in as <Role> | 1. Click on the three-dot action menu of a user in the Participants Table<br>2. Select 'Send Message'<br>3. Enter <message> in the message field<br>4. Click 'Send' | The system sends message to user | medium |
| TC-008 | WF-008 | Bulk enroll selected users | User logged in as <Role> | 1. Check the checkbox for multiple users in the Participants Table<br>2. Select 'Enroll' from the 'With selected users...' dropdown<br>3. Click 'Confirm' | The system applies bulk action to checked participants | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 |  | Leave the Select Attribute dropdown blank and submit filters |  | 1. Open the Filter System<br>2. Leave the Select Attribute dropdown blank<br>3. Click Apply Filters | Inline validation error appears on the Select Attribute field indicating it is required | high |
| TC-010 |  | Leave all filter fields blank and submit filters |  | 1. Open the Filter System<br>2. Leave all filter fields blank<br>3. Click Apply Filters | Form does not submit; error shown on Select Attribute field indicating it is required | high |
| TC-011 |  | Attempt to enroll a user without entering a user search term |  | 1. Click on Enrol Users<br>2. Leave the User Search field blank<br>3. Click Confirm Enrollment | Inline validation error appears on the User Search field indicating it is required | high |
| TC-012 | WF-004 | Attempt to confirm enrollment without selecting a role |  | 1. Click on Enrol Users<br>2. Enter a valid user in the User Search field<br>3. Leave the Role dropdown blank<br>4. Click Confirm Enrollment | Inline validation error appears on the Role field indicating it is required | high |
| TC-013 | WF-008 | Attempt to apply bulk action without selecting any users |  | 1. Check the bulk action dropdown<br>2. Select 'Enroll' from the dropdown<br>3. Click Apply | Form does not submit; error shown indicating no users selected for bulk action | high |
| TC-014 | WF-001 | Attempt to apply filters without selecting any attribute |  | 1. Open the Filter System<br>2. Leave the Select Attribute dropdown blank<br>3. Click Apply Filters | Inline validation error appears on the Select Attribute field indicating it is required | high |
| TC-015 |  | Attempt to clear filters when no filters are applied |  | 1. Open the Filter System<br>2. Click Clear Filters | No action occurs; message shown indicating no filters to clear | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-016 (boundary) | WF-001 | Apply filters with valid selection | User is on the Participants page | 1. Select 'Current' from the Enrolled Users Scope dropdown<br>2. Select 'Role' from the Select Attribute dropdown<br>3. Click Apply Filters | Filters are applied successfully; the participants list updates to show only current users | medium |
| TC-017 (boundary) | WF-002 | Clear filters after applying | User has applied filters | 1. Click Clear Filters | All filters are cleared successfully; the participants list shows all users | medium |
| TC-018 (interaction_edge) | WF-003 | Rapid enrollment dialog opening | User is on the Participants page | 1. Click Enrol Users<br>2. Immediately click Enrol Users again | Enrollment dialog opens without error; user can proceed with enrollment | low |
| TC-019 (boundary) | WF-004 | Confirm enrollment with valid role | User is in the enrollment dialog | 1. Enter a user in the User Search field<br>2. Select 'Instructor' from the Role dropdown<br>3. Click Confirm Enrollment | User is added to the course as an Instructor; confirmation message is displayed | medium |
| TC-020 (boundary) | WF-008 | Bulk enroll with selected users | User has selected multiple users in the Participants Table | 1. Click the checkbox for multiple users<br>2. Select 'Enroll' from the With selected users… dropdown<br>3. Click Apply | Selected users are enrolled successfully; confirmation message is displayed | medium |
| TC-021 (input_edge) |  | User search with special characters | User is in the enrollment dialog | 1. Enter '@user!' in the User Search field | Search results are displayed correctly or an error message indicates no users found | low |

---

## Assignment — Teacher View

Total: **3** (positive: 1, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open grading interface for individual students | User logged in as <Teacher> | 1. Navigate to the Assignment tab<br>2. Click on the Grade button | opens grading interface for individual students | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to open grading interface without any prior action |  | 1. Navigate to the Assignment page<br>2. Click the Grade button | No grading interface opens; the page remains unchanged | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | Rapidly click the Grade button multiple times | User is on the Assignment page | 1. Click the Grade button<br>2. Immediately click the Grade button again | Grading interface opens successfully without duplication of instances | medium |

---

## Assignment Submissions

Total: **11** (positive: 4, negative: 3, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Grading Workflow for a submission | User logged in as <Role> | 1. Search for a student by entering <valid student name> in the Student_Name search field<br>2. Click the action menu for the corresponding submission<br>3. Select 'Open Grading Workflow' from the action menu | Grading workflow opened for the selected submission | high |
| TC-002 |  | Filter submissions by Submission Status | User logged in as <Role> | 1. Select 'Submitted for grading' from the Submission_Status dropdown<br>2. Observe the submissions table | Only submissions with the status 'Submitted for grading' are displayed; unrelated submissions are no longer visible | medium |
| TC-003 |  | Filter submissions by Grading Status | User logged in as <Role> | 1. Select 'Graded' from the Grading_Status dropdown<br>2. Observe the submissions table | Only submissions with the grading status 'Graded' are displayed; unrelated submissions are no longer visible | medium |
| TC-004 |  | Inline grading entry for a submission | User logged in as <Role>, Quick grading mode is enabled | 1. Enter <valid grade> in the Grade field for the corresponding submission<br>2. Observe the submissions table | The Final grade column updates to reflect the entered grade | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Attempt to open grading workflow without selecting a submission |  | 1. Navigate to the Assignment Submissions page<br>2. Click on 'Open Grading Workflow' without selecting any submission | No grading workflow opens; an error message indicates 'Please select a submission first.' | high |
| TC-006 |  | Leave the Grade field blank in inline grading |  | 1. Navigate to the Assignment Submissions page<br>2. Enable Quick grading mode<br>3. Leave the Grade field blank<br>4. Attempt to submit the grade | Inline validation error appears on the Grade field indicating it is required; form does not submit. | high |
| TC-007 |  | Enter a non-numeric value in the Grade field |  | 1. Navigate to the Assignment Submissions page<br>2. Enable Quick grading mode<br>3. Enter <non-numeric value> in the Grade field<br>4. Attempt to submit the grade | Inline validation error appears on the Grade field indicating 'Must be a number'; form does not submit. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) |  | Enter minimum grade value in the Grade field | User is in Quick grading mode | 1. Enter 0 in the Grade field<br>2. Click Save | Grade is saved successfully; table reflects the new grade of 0 | medium |
| TC-009 (boundary) |  | Enter maximum grade value in the Grade field | User is in Quick grading mode | 1. Enter 100 in the Grade field<br>2. Click Save | Grade is saved successfully; table reflects the new grade of 100 | medium |
| TC-010 (boundary) |  | Enter a grade value above maximum in the Grade field | User is in Quick grading mode | 1. Enter 101 in the Grade field<br>2. Click Save | Saving is blocked; inline error shows 'Grade must be between 0 and 100' | medium |
| TC-011 (input_edge) |  | Enter a very long student name in the search field |  | 1. Enter a string of 200+ characters in the Student_Name search field<br>2. Click Search | Search is processed; either results are shown or an error indicates the input is too long | low |

---

## Gradebook — Grader Report

Total: **8** (positive: 2, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Grader Report with valid inputs | User logged in as <Role>, Edit mode is enabled | 1. Select 'Grader report' from the Report_Type_Selector dropdown<br>2. Enter <valid student name> in the User_Search field<br>3. Select 'Group 1' from the User_Filter dropdown<br>4. Edit a grade cell to a valid value within the configured grade range<br>5. Click 'Save Changes' | The changes are applied; the grade table reflects the updated values | high |
| TC-002 | WF-002 | Edit Grade with valid input | User logged in as <Role>, Edit mode is enabled | 1. Click the three-dot menu on a grade cell<br>2. Select 'Edit Grade' from the menu<br>3. Enter a valid grade value within the configured grade range<br>4. Click 'Save' | Grade updated successfully | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Attempt to save changes with a grade value outside the configured grade range | Edit mode is enabled | 1. Open the grade cell for a student<br>2. Enter a <grade value outside the configured grade range><br>3. Click 'Save Changes' | Inline validation error appears on the Grade_Value field indicating it must be within configured grade range; form does not submit; no changes are saved. | high |
| TC-004 | WF-002 | Attempt to edit a grade with an invalid grade value | User selects a grade to edit | 1. Enter a <grade value outside the configured grade range><br>2. Click 'Edit_Grade' | Inline validation error appears on the Grade_Value field indicating it must be within configured grade range; grade is not updated. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (boundary) | WF-002 | Edit grade value at the lower boundary of the configured grade range | Edit mode is enabled, Configured grade range is known | 1. Navigate to the Grade Table<br>2. Click the three-dot menu on a grade cell<br>3. Select Edit Grade<br>4. Enter the minimum grade value in the Grade_Value field<br>5. Click Save Changes | Grade is updated successfully; the new grade value is displayed in the table | medium |
| TC-006 (boundary) | WF-002 | Edit grade value just below the lower boundary of the configured grade range | Edit mode is enabled, Configured grade range is known | 1. Navigate to the Grade Table<br>2. Click the three-dot menu on a grade cell<br>3. Select Edit Grade<br>4. Enter a value just below the minimum grade value in the Grade_Value field<br>5. Click Save Changes | Saving is blocked; inline error message indicates the value is outside the configured grade range | medium |
| TC-007 (boundary) | WF-002 | Edit grade value at the upper boundary of the configured grade range | Edit mode is enabled, Configured grade range is known | 1. Navigate to the Grade Table<br>2. Click the three-dot menu on a grade cell<br>3. Select Edit Grade<br>4. Enter the maximum grade value in the Grade_Value field<br>5. Click Save Changes | Grade is updated successfully; the new grade value is displayed in the table | medium |
| TC-008 (boundary) | WF-002 | Edit grade value just above the upper boundary of the configured grade range | Edit mode is enabled, Configured grade range is known | 1. Navigate to the Grade Table<br>2. Click the three-dot menu on a grade cell<br>3. Select Edit Grade<br>4. Enter a value just above the maximum grade value in the Grade_Value field<br>5. Click Save Changes | Saving is blocked; inline error message indicates the value is outside the configured grade range | medium |

---

## Profile

Total: **30** (positive: 13, negative: 13, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Edit profile | User logged in as <Teacher> | 1. Click the 'Edit profile' link | Profile updated successfully | high |
| TC-002 | WF-002 | View Data retention summary | User logged in as <Teacher> | 1. Click the 'Data retention summary' link | Data retention details displayed | medium |
| TC-003 | WF-003 | View Course profiles | User logged in as <Teacher> | 1. Click the 'Course_profiles' link | Course profiles displayed | medium |
| TC-004 | WF-004 | View Blog entries | User logged in as <Teacher> | 1. Click the 'Blog_entries' link | Blog entries displayed | medium |
| TC-005 | WF-005 | View Forum posts | User logged in as <Teacher> | 1. Click the 'Forum_posts' link | Forum posts displayed | medium |
| TC-006 | WF-006 | View Forum discussions | User logged in as <Teacher> | 1. Click the 'Forum_discussions' link | Forum discussions displayed | medium |
| TC-007 | WF-007 | View Learning plans | User logged in as <Teacher> | 1. Click the 'Learning_plans' link | Learning plans displayed | medium |
| TC-008 | WF-008 | View Browser sessions | User logged in as <Teacher> | 1. Click the 'Browser_sessions' link | Browser sessions displayed | medium |
| TC-009 | WF-009 | View Grades overview | User logged in as <Teacher> | 1. Click the 'Grades_overview' link | Grades overview displayed | medium |
| TC-010 | WF-010 | View First access | User logged in as <Teacher> | 1. Click the 'First_access' link | First access details displayed | medium |
| TC-011 | WF-011 | View Last access | User logged in as <Teacher> | 1. Click the 'Last_access' link | Last access details displayed | medium |
| TC-012 | WF-012 | View relative time indicators | User logged in as <Teacher> | 1. Click the 'relative_time_indicators' link | Relative time indicators displayed | medium |
| TC-013 | WF-013 | Send a message | User logged in as <Teacher> | 1. Click the 'Message' button | Message sent successfully | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 | WF-001 | Attempt to edit profile without any changes |  | 1. Click on the 'Edit profile' link<br>2. Leave all fields unchanged<br>3. Click Save | Form does not submit; no changes are made to the profile; error shown indicating no changes were detected. | high |
| TC-015 | WF-002 | Attempt to view Data retention summary without proper access |  | 1. Click on the 'Data retention summary' link | User is redirected to the login page; access denied. | high |
| TC-016 | WF-003 | Attempt to view Course profiles without proper access |  | 1. Click on the 'Course profiles' link | User is redirected to the login page; access denied. | high |
| TC-017 | WF-004 | Attempt to view Blog entries without proper access |  | 1. Click on the 'Blog entries' link | User is redirected to the login page; access denied. | high |
| TC-018 | WF-005 | Attempt to view Forum posts without proper access |  | 1. Click on the 'Forum posts' link | User is redirected to the login page; access denied. | high |
| TC-019 | WF-006 | Attempt to view Forum discussions without proper access |  | 1. Click on the 'Forum discussions' link | User is redirected to the login page; access denied. | high |
| TC-020 | WF-007 | Attempt to view Learning plans without proper access |  | 1. Click on the 'Learning plans' link | User is redirected to the login page; access denied. | high |
| TC-021 | WF-008 | Attempt to view Browser sessions without proper access |  | 1. Click on the 'Browser sessions' link | User is redirected to the login page; access denied. | high |
| TC-022 | WF-009 | Attempt to view Grades overview without proper access |  | 1. Click on the 'Grades overview' link | User is redirected to the login page; access denied. | high |
| TC-023 | WF-010 | Attempt to view First access without proper access |  | 1. Click on the 'First access' link | User is redirected to the login page; access denied. | high |
| TC-024 | WF-011 | Attempt to view Last access without proper access |  | 1. Click on the 'Last access' link | User is redirected to the login page; access denied. | high |
| TC-025 | WF-012 | Attempt to view relative time indicators without proper access |  | 1. Click on the 'relative time indicators' link | User is redirected to the login page; access denied. | high |
| TC-026 | WF-013 | Attempt to send a message without proper access |  | 1. Click on the 'Message' button | User is redirected to the login page; access denied. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-027 (interaction_edge) | WF-001 | Rapid re-submission after profile edit | User has successfully updated the profile | 1. Click the 'Edit profile' link<br>2. Make changes to the profile fields<br>3. Click 'Save' to submit changes<br>4. Immediately click 'Edit profile' again after the success message | Profile edit form is shown blank; no pre-filled data appears | medium |
| TC-028 (interaction_edge) | WF-002 | View Data retention summary |  | 1. Click the 'Data retention summary' link | Data retention details displayed | medium |
| TC-029 (state_edge) | WF-010 | View First access date |  | 1. Click the 'First_access' link | First access details displayed | medium |
| TC-030 (state_edge) | WF-011 | View Last access date |  | 1. Click the 'Last_access' link | Last access details displayed | medium |

---

## Profile Edit

Total: **11** (positive: 2, negative: 5, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Update profile with valid data | User logged in as <Role> | 1. Open the Edit Profile form<br>2. Enter <valid first name> in the First Name field<br>3. Enter <valid last name> in the Last Name field<br>4. Enter <valid email> in the Email Address field<br>5. Upload a <valid image file> in the New Picture Upload area<br>6. Click Update Profile | The profile page refreshes to show the updated information. | high |
| TC-002 | WF-002 | Cancel profile edit | User logged in as <Role> | 1. Open the Edit Profile form<br>2. Click Cancel | Exits without making changes. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the First Name field blank and submit |  | 1. Leave the First Name field blank<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the First_Name field indicating it is required | high |
| TC-004 |  | Leave the Last Name field blank and submit |  | 1. Leave the Last Name field blank<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the Last_Name field indicating it is required | high |
| TC-005 |  | Leave the Email Address field blank and submit |  | 1. Leave the Email Address field blank<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears on the Email_Address field indicating it is required | high |
| TC-006 |  | Upload a file that does not meet the upload constraints |  | 1. Select a file that does not meet the upload constraints<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Inline validation error appears indicating the file does not meet the upload constraints | high |
| TC-007 |  | Submit with all required fields empty |  | 1. Leave all required fields blank<br>2. Click Update Profile | Inline validation error appears on the First_Name, Last_Name, and Email_Address fields indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) | WF-001 | Upload a file exactly at the size limit for New Picture Upload | User is logged in and on the profile edit page | 1. Drag and drop a file that is exactly at the size limit into the New Picture Upload area<br>2. Fill in all required fields with valid data<br>3. Click Update Profile | Profile is updated successfully; the profile page refreshes. | medium |
| TC-009 (boundary) | WF-001 | Upload a file one byte over the size limit for New Picture Upload | User is logged in and on the profile edit page | 1. Drag and drop a file that is one byte over the size limit into the New Picture Upload area<br>2. Fill in all required fields with valid data<br>3. Click Update Profile | Upload is blocked; an error message is displayed indicating the file exceeds the size limit. | medium |
| TC-010 (input_edge) |  | Enter a very long string in the Description field | User is logged in and on the profile edit page | 1. Expand the General section<br>2. Enter a string longer than 200 characters in the Description field<br>3. Fill in all other required fields with valid data<br>4. Click Update Profile | Profile is updated successfully; the profile page refreshes, and the description is saved correctly. | low |
| TC-011 (input_edge) |  | Enter special characters in the First Name field | User is logged in and on the profile edit page | 1. Enter special characters (e.g., @, #, $, %) in the First Name field<br>2. Fill in all other required fields with valid data<br>3. Click Update Profile | Profile is updated successfully; the profile page refreshes, and the special characters are saved correctly. | low |

---

## Logout

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | User logs out successfully | User logged in as <Role> | 1. Click on the Logout button | terminates the current authenticated session and redirects to the login page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to log out while unauthenticated | user must be authenticated | 1. Ensure the user is not authenticated<br>2. Click the Logout button | Logout action is blocked; user remains on the current page and is not redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | User attempts to log out after being authenticated | User is authenticated | 1. Click the Logout button | User is redirected to the login page; session is terminated successfully. | medium |
| TC-004 (interaction_edge) | WF-001 | User attempts to log out when not authenticated | User is not authenticated | 1. Click the Logout button | Logout action is blocked; user remains on the current page with no session termination. | medium |

---
