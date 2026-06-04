# Test Cases — Moodlestudent

Generated: 2026-06-04T14:37:59.748233Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 10 | 106 | 31 | 37 | 38 | 44 | 47 | 15 |

## Login

Total: **14** (positive: 3, negative: 7, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Log in with valid credentials | User logged in as <Student> | 1. Enter <valid username> in the Username field<br>2. Enter <valid password> in the Password field<br>3. Click Log in | User is redirected to Dashboard | high |
| TC-002 | WF-003 | Access the application as a guest | User logged in as <Guest> | 1. Click Access as a guest | User accesses the application as a guest | medium |
| TC-003 | WF-004 | View cookie usage information | User logged in as <Student> | 1. Click Cookies notice | Displays cookie usage information | low |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Leave the Username field blank and submit |  | 1. Leave the Username field blank<br>2. Fill the Password field with <valid password><br>3. Click Log in | Inline validation error appears on the Username field indicating it is required | high |
| TC-005 |  | Leave the Password field blank and submit |  | 1. Fill the Username field with <valid username><br>2. Leave the Password field blank<br>3. Click Log in | Inline validation error appears on the Password field indicating it is required | high |
| TC-006 |  | Submit with both fields empty |  | 1. Leave the Username field blank<br>2. Leave the Password field blank<br>3. Click Log in | Inline validation error appears on the Username field indicating it is required; Inline validation error appears on the Password field indicating it is required | high |
| TC-007 |  | Submit with invalid Username format |  | 1. Enter <invalid username format> in the Username field<br>2. Fill the Password field with <valid password><br>3. Click Log in | Inline error message is shown; Password field is cleared and Username is retained for correction | medium |
| TC-008 |  | Submit with invalid Password format |  | 1. Fill the Username field with <valid username><br>2. Enter <invalid password format> in the Password field<br>3. Click Log in | Inline error message is shown; Password field is cleared and Username is retained for correction | medium |
| TC-009 |  | Access the disabled Lost Password link |  | 1. Click on the Lost password? link | No action occurs; the link is disabled | medium |
| TC-010 |  | Attempt to log in with incorrect credentials |  | 1. Fill the Username field with <invalid username><br>2. Fill the Password field with <invalid password><br>3. Click Log in | Inline error message is shown; Password field is cleared and Username is retained for correction | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (input_edge) |  | Enter a very long username |  | 1. Enter a string of 200+ characters in the Username field<br>2. Enter a valid password in the Password field<br>3. Click Log in | Inline error message is shown indicating the username is too long or the form submits successfully with the username truncated | low |
| TC-012 (input_edge) |  | Enter special characters in the Username field |  | 1. Enter a username with special characters (e.g., !@#$%^&*) in the Username field<br>2. Enter a valid password in the Password field<br>3. Click Log in | Inline error message is shown indicating invalid characters in the Username field or the form submits successfully | low |
| TC-013 (input_edge) |  | Enter leading/trailing whitespace in the Username field |  | 1. Enter a username with leading and trailing spaces in the Username field<br>2. Enter a valid password in the Password field<br>3. Click Log in | Username is trimmed; saved value shown on the Dashboard has no extra spaces | low |
| TC-014 (state_edge) | WF-002 | Rapid submission of invalid credentials |  | 1. Enter an invalid username in the Username field<br>2. Enter an invalid password in the Password field<br>3. Click Log in<br>4. Immediately click Log in again | Inline error message is shown for the first submission; second submission is blocked until the fields are corrected | medium |

---

## Dashboard

Total: **21** (positive: 9, negative: 8, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Search activities in Timeline block | User logged in as <Role> | 1. Select 'Next 7 days' from the Time Range dropdown<br>2. Enter <valid activity name> in the Search Field<br>3. Press Enter | Filtered activities displayed based on search criteria | high |
| TC-002 | WF-002 | View empty state in Timeline block | User logged in as <Role>, Select a time range with no activities | 1. Select 'Next 7 days' from the Time Range dropdown | Empty state message shown indicating no activities | high |
| TC-003 | WF-003 | Filter events by course in Calendar block | User logged in as <Role> | 1. Select <valid course> from the All Courses dropdown | Events filtered based on selected course | high |
| TC-004 | WF-004 | Create new event in Calendar block | User logged in as <Role> | 1. Click the New Event Button | New event creation interface opened | high |
| TC-005 | WF-005 | Navigate months in Calendar block | User logged in as <Role> | 1. Click the Left_Right_Arrows to navigate to the next month | Calendar updated to show events for the selected month | medium |
| TC-006 | WF-006 | Reset page to default in Edit mode | User logged in as <Role>, Edit mode is enabled | 1. Click the Reset_Page_Button | Page reset to default settings | medium |
| TC-007 | WF-007 | Add a block in Edit mode | User logged in as <Role>, Edit mode is enabled | 1. Click the Add_Block_Button | Block addition interface opened | medium |
| TC-008 | WF-008 | Open full calendar link | User logged in as <Role> | 1. Click on the Full calendar link | Full calendar view opened | medium |
| TC-009 | WF-009 | Open import/export calendars link | User logged in as <Role> | 1. Click on the Import or export calendars link | Calendar data management interface opened | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 |  | Leave Sort Order dropdown blank and submit |  | 1. Leave the Sort Order dropdown blank<br>2. Select a value in the Time Range dropdown<br>3. Enter a search term in the Search Field<br>4. Click Search | Inline validation error appears on the Sort Order field indicating it is required | high |
| TC-011 |  | Leave Search Field blank and submit |  | 1. Leave the Search Field blank<br>2. Select a value in the Sort Order dropdown<br>3. Select a value in the Time Range dropdown<br>4. Click Search | Inline validation error appears on the Search Field indicating it is required | high |
| TC-012 |  | Attempt to filter events without selecting a course |  | 1. Leave the All Courses dropdown blank<br>2. Click the filter button | Inline validation error appears on the All Courses field indicating it is required | high |
| TC-013 |  | Attempt to create a new event without entering required details |  | 1. Click the New Event button | New event creation interface does not open; error shown indicating required fields must be filled | high |
| TC-014 |  | Attempt to navigate months without any events |  | 1. Click the left/right arrows to navigate months | Calendar remains unchanged; no events displayed for the selected month | medium |
| TC-015 |  | Attempt to reset page in Edit mode without making changes |  | 1. Toggle Edit mode on<br>2. Click Reset Page to default | Page remains unchanged; no reset occurs | medium |
| TC-016 |  | Open full calendar link without being logged in |  | 1. Click on the Full calendar link | User is redirected to the login page | high |
| TC-017 |  | Open import/export calendars link without being logged in |  | 1. Click on the Import or export calendars link | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-018 (boundary) | WF-001 | Search with minimum and maximum character lengths | User is on the Dashboard | 1. Enter exactly 1 character in the Search_Field<br>2. Press Enter<br>3. Observe the results | Filtered activities displayed based on search criteria; search with 1 character succeeds | medium |
| TC-019 (boundary) | WF-001 | Search with one character over maximum length | User is on the Dashboard | 1. Enter a string longer than the maximum allowed length in the Search_Field<br>2. Press Enter<br>3. Observe the results | Search is blocked; inline error message shown indicating the input exceeds the maximum length | medium |
| TC-020 (boundary) | WF-002 | View empty state when no activities exist | User is on the Dashboard, No activities are available in the selected time range | 1. Select 'Next 7 days' in the Time_Range dropdown<br>2. Observe the Timeline block | Empty state message shown indicating no activities | medium |
| TC-021 (boundary) | WF-003 | Filter events in Calendar block with no courses available | User is on the Dashboard, No courses are available in the All_Courses dropdown | 1. Select an option from the All_Courses dropdown<br>2. Observe the Calendar block | Calendar updates to show no events; appropriate message shown indicating no events for the selected course | medium |

---

## My Courses

Total: **10** (positive: 2, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Star a course | User logged in as <Student>, At least one course is displayed in the course grid | 1. Click the three-dot menu on a course card<br>2. Select 'Star this course' from the menu | The course is pinned to the top | high |
| TC-002 | WF-002 | Remove a course from view | User logged in as <Student>, At least one course is displayed in the course grid | 1. Click the three-dot menu on a course card<br>2. Select 'Remove from view' from the menu | The course is hidden without unenrolling | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Attempt to star a course when no course is selected |  | 1. Navigate to the My Courses page<br>2. Click 'Star this course' without selecting a course | No course is starred; an error message is displayed indicating that a course must be selected first | high |
| TC-004 | WF-002 | Attempt to remove a course from view when no course is selected |  | 1. Navigate to the My Courses page<br>2. Click 'Remove from view' without selecting a course | No course is removed; an error message is displayed indicating that a course must be selected first | high |
| TC-005 |  | Leave the search field blank and submit |  | 1. Navigate to the My Courses page<br>2. Leave the Search field blank<br>3. Click the search button | The course grid displays all courses; no error is shown | medium |
| TC-006 |  | Select an invalid option in the Status dropdown |  | 1. Navigate to the My Courses page<br>2. Select an invalid option in the Status dropdown<br>3. Click the apply button | No courses are filtered; an error message is displayed indicating the selection is invalid | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (interaction_edge) | WF-001 | Rapidly star the same course multiple times | User is on the My Courses page, At least one course is displayed | 1. Click the three-dot menu on a course card<br>2. Click 'Star this course'<br>3. Immediately repeat steps 1 and 2 | Course is pinned to the top; no duplicate entries are created | medium |
| TC-008 (interaction_edge) | WF-002 | Rapidly remove the same course from view | User is on the My Courses page, At least one course is displayed | 1. Click the three-dot menu on a course card<br>2. Click 'Remove from view'<br>3. Immediately repeat steps 1 and 2 | Course is hidden from view; no error occurs and the course does not reappear | medium |
| TC-009 (input_edge) |  | Search with leading and trailing whitespace | User is on the My Courses page, At least one course is displayed | 1. Enter '   Course Name   ' in the Search field<br>2. Press Enter | Search results display correctly; leading/trailing whitespace is trimmed | low |
| TC-010 (input_edge) |  | Search using special characters | User is on the My Courses page, At least one course is displayed | 1. Enter '@#$%^&*()' in the Search field<br>2. Press Enter | Search results display correctly; no error is shown | low |

---

## Course Page

Total: **10** (positive: 2, negative: 3, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Collapse all sections | User logged in as <Student> | 1. Click 'Collapse all' link | All sections collapsed | high |
| TC-002 | WF-002 | View Activities and Resources in Sections | User logged in as <Student> | 1. Expand a section to view activities and resources<br>2. Click on an activity or resource name | Activity or resource details displayed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Section Name blank and submit |  | 1. Leave the Section Name field blank<br>2. Click to add the section | Inline validation error appears on the Section Name field indicating it is required | high |
| TC-004 |  | Leave the Activity Resource Name blank and submit |  | 1. Add a new section<br>2. Leave the Activity Resource Name field blank<br>3. Click to add the activity/resource | Inline validation error appears on the Activity Resource Name field indicating it is required | high |
| TC-005 | WF-001 | Attempt to collapse all sections when none are expanded |  | 1. Ensure all sections are collapsed<br>2. Click the Collapse All link | All sections remain collapsed; no action occurs | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (interaction_edge) | WF-001 | Collapse all sections | User is on the Course Page | 1. Click the 'Collapse All' link | All sections are collapsed; no section names are visible. | medium |
| TC-007 (boundary) |  | Add maximum number of sections | User is in edit mode (if applicable) | 1. Add maximum allowed sections to the course | All sections are added successfully; they appear in the list. | medium |
| TC-008 (boundary) |  | Add one more section than allowed | User is in edit mode (if applicable) | 1. Attempt to add one more section than the maximum allowed | Attempt to add section is blocked; error message is displayed. | medium |
| TC-009 (input_edge) |  | Enter long section name | User is adding a new section | 1. Enter a string of 200+ characters in the Section Name field | Section name is accepted or truncated with a visible indicator. | low |
| TC-010 (input_edge) |  | Enter special characters in section name | User is adding a new section | 1. Enter special characters in the Section Name field | Section name is accepted or an error message is shown. | low |

---

## Participants

Total: **9** (positive: 3, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Apply filters to the participants list | User logged in as <Student> | 1. Select <attribute> from the Select Attribute dropdown<br>2. Click Apply Filters | Filters applied; participants list updated | high |
| TC-002 | WF-002 | Clear filters on the participants list | User logged in as <Student>, Filters are currently applied | 1. Click Clear Filters | Filters cleared; participants list reset | high |
| TC-003 | WF-003 | View a participant's profile | User logged in as <Student> | 1. Click on the First name link of a participant in the Participants Table | Profile displayed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Attempt to apply filters without any selections |  | 1. Leave all filter fields blank<br>2. Click Apply filters | Form does not submit; no filters applied; participants list remains unchanged | high |
| TC-005 | WF-002 | Attempt to clear filters when no filters are applied |  | 1. Click Clear filters | No action taken; filters remain unchanged; participants list remains unchanged | medium |
| TC-006 | WF-003 | Attempt to view participant profile without selecting a participant |  | 1. Click View Profile without selecting any participant | No profile displayed; action is blocked; no change in the participants list | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (interaction_edge) | WF-001 | Rapidly apply filters multiple times | User is on the Participants page | 1. Set a filter condition using the Select Attribute dropdown<br>2. Click Apply Filters<br>3. Immediately set another filter condition<br>4. Click Apply Filters again | Filters applied; participants list updated with the latest filter conditions | medium |
| TC-008 (interaction_edge) | WF-002 | Clear filters after applying them | User has applied filters | 1. Click Clear Filters | Filters cleared; participants list reset to show all participants | medium |
| TC-009 (interaction_edge) | WF-003 | View participant profile rapidly | User is on the Participants page with visible participants | 1. Click on the First name link of a participant<br>2. Press the browser back button<br>3. Click on the First name link of another participant | Profile displayed for the second participant without issues | medium |

---

## Grades

Total: **9** (positive: 3, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Course Name 1 grade details | User logged in as <Student>, User has grades for Course Name 1 | 1. Navigate to the Grades page<br>2. Expand the Grade item for Course Name 1 | Grade details displayed for Course Name 1 including 'Calculated weight', 'Grade', 'Range', 'Percentage', 'Feedback', and 'Contribution to course total' | high |
| TC-002 | WF-002 | View Course Name 2 grade details | User logged in as <Student>, User has grades for Course Name 2 | 1. Navigate to the Grades page<br>2. Expand the Grade item for Course Name 2 | Grade details displayed for Course Name 2 including 'Not graded yet' in the Grade column | high |
| TC-003 | WF-003 | View AGGREGATION Course total grade details | User logged in as <Student>, User has grades for multiple courses | 1. Navigate to the Grades page<br>2. View the AGGREGATION Course total row | Grade details displayed for AGGREGATION Course total including 'Calculated weight', 'Grade', 'Percentage', and 'Contribution to course total' | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Attempt to view grade details for Course Name 1 without proper authentication | User is not authenticated | 1. Navigate to the Grades page<br>2. Attempt to view Course Name 1 grade details | User is redirected to the login page | high |
| TC-005 | WF-002 | Attempt to view grade details for Course Name 2 without proper authentication | User is not authenticated | 1. Navigate to the Grades page<br>2. Attempt to view Course Name 2 grade details | User is redirected to the login page | high |
| TC-006 | WF-003 | Attempt to view AGGREGATION Course total grade details without proper authentication | User is not authenticated | 1. Navigate to the Grades page<br>2. Attempt to view AGGREGATION Course total grade details | User is redirected to the login page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) | WF-001 | View grade details for Course Name 1 with exact grade value |  | 1. Navigate to the Grades page<br>2. Click on Course Name 1 to view grade details | Grade details displayed for Course Name 1 with Grade value of 85 | medium |
| TC-008 (boundary) | WF-002 | View grade details for Course Name 2 which is not graded yet |  | 1. Navigate to the Grades page<br>2. Click on Course Name 2 to view grade details | Grade details displayed for Course Name 2 with Grade value of '–' and feedback 'Not graded yet' | medium |
| TC-009 (boundary) | WF-003 | View AGGREGATION Course total grade details |  | 1. Navigate to the Grades page<br>2. Click on AGGREGATION Course total to view grade details | Grade details displayed for AGGREGATION Course total with Grade value of 85 | medium |

---

## Assignment

Total: **13** (positive: 4, negative: 4, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit assignment using online text editor | User logged in as <Student>, Assignment is open for submission | 1. Click 'Add submission' button<br>2. Enter <valid text> in the Online Text Editor<br>3. Click 'Submit' | Submission created; success message shown | high |
| TC-002 | WF-002 | Submit assignment using file upload | User logged in as <Student>, Assignment is open for submission | 1. Click 'Add submission' button<br>2. Upload a <valid file type> in the File Upload Area<br>3. Click 'Submit' | Submission created; success message shown | high |
| TC-003 | WF-003 | View submission after submission is made | User logged in as <Student>, Submission status is 'Submitted for grading' | 1. Click 'View Submission' action | Submission details displayed | medium |
| TC-004 | WF-004 | Edit submission before due date | User logged in as <Student>, Submission status is 'Submitted for grading', Due date has not passed | 1. Click 'Edit Submission' action | Submission edit form displayed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Attempt to submit assignment without any input in the online text editor |  | 1. Open the submission form<br>2. Leave the Online Text Editor blank<br>3. Click Submit | Form does not submit; error shown on Online Text Editor field indicating it is required | high |
| TC-006 | WF-002 | Attempt to submit assignment without uploading a file |  | 1. Open the submission form<br>2. Leave the File Upload Area empty<br>3. Click Submit | Form does not submit; error shown on File Upload Area field indicating it is required | high |
| TC-007 |  | Attempt to edit submission when the submission is graded |  | 1. Attempt to edit a submission that has been graded | No action buttons are visible; user cannot edit submission | medium |
| TC-008 |  | Attempt to view submission when there are no submissions made |  | 1. Attempt to view submission when no submissions have been made | No submission details displayed; user is informed that no submissions exist | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-001 | Submit with maximum file size limit | User has a file that meets the size limit | 1. Open the submission form<br>2. Upload a file that is exactly at the size limit in the File Upload Area<br>3. Click Submit | Submission is created; success message is shown | medium |
| TC-010 (boundary) | WF-001 | Submit with file size over limit | User has a file that exceeds the size limit | 1. Open the submission form<br>2. Upload a file that is one byte over the size limit in the File Upload Area<br>3. Click Submit | Submission is blocked; error shown indicating file size exceeds limit | medium |
| TC-011 (input_edge) | WF-002 | Submit with long text in online text editor | User has a long text to submit | 1. Open the submission form<br>2. Enter a long text (200+ characters) in the Online Text Editor<br>3. Click Submit | Submission is created; success message is shown | low |
| TC-012 (input_edge) | WF-002 | Submit with special characters in online text editor | User has special characters to submit | 1. Open the submission form<br>2. Enter special characters (e.g., emojis, unicode) in the Online Text Editor<br>3. Click Submit | Submission is created; success message is shown | low |
| TC-013 (interaction_edge) | WF-001 | Rapid submission after redirect | Submission has been successfully created | 1. Submit the assignment<br>2. Press the browser back button | Submission form is shown blank; no pre-filled data from previous submission | low |

---

## Activities

Total: **5** (positive: 1, negative: 1, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Navigate to Activity from Assignments Section | User logged in as <Role> | 1. Click on the activity name in the Assignments section | redirects to activity page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to navigate to an activity without any activities listed |  | 1. Ensure no activities are present in the Assignments section<br>2. Click on any activity name | No navigation occurs; the Activities page remains unchanged | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | Rapid navigation to activity page | User is on the Activities page | 1. Click on an activity name in the Assignments section.<br>2. Immediately click the back button in the browser.<br>3. Click on the same activity name again. | Redirects to the activity page without any duplication of navigation. | medium |
| TC-004 (input_edge) |  | Expand Forums section | User is on the Activities page | 1. Click on the arrow to expand the Forums section. | Forums section expands and displays any available content. | low |
| TC-005 (input_edge) |  | Expand Resources section | User is on the Activities page | 1. Click on the arrow to expand the Resources section. | Resources section expands and displays any available content. | low |

---

## Profile

Total: **11** (positive: 3, negative: 3, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open profile form | User logged in as <Student>, students can only modify their own profile | 1. Click the 'Edit profile' link | opens profile form | high |
| TC-002 | WF-002 | Update profile with all required fields filled | User logged in as <Student>, students can only modify their own profile | 1. Click the 'Edit profile' link<br>2. Enter <valid first name> in the First Name field<br>3. Enter <valid last name> in the Last Name field<br>4. Enter <valid email> in the Email Address field<br>5. Click 'Update Profile' | saves profile changes | high |
| TC-003 | WF-003 | Cancel profile update | User logged in as <Student>, students can only modify their own profile | 1. Click the 'Edit profile' link<br>2. Click 'Cancel' | exits without changes | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-002 | Attempt to update profile with required fields left blank |  | 1. Click on 'Edit profile' link<br>2. Leave the First Name, Last Name, and Email Address fields blank<br>3. Click 'Update Profile' | Form does not submit; error shown on First Name, Last Name, and Email Address fields indicating they are required | high |
| TC-005 | WF-002 | Attempt to update profile with only required fields empty |  | 1. Click on 'Edit profile' link<br>2. Leave all required fields empty<br>3. Click 'Update Profile' | Form does not submit; error shown on First Name, Last Name, and Email Address fields indicating they are required | high |
| TC-006 |  | Attempt to access profile form without being a student |  | 1. Attempt to click on 'Edit profile' link as a non-student | Access denied; user is not allowed to modify profile | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) | WF-002 | Fill all required fields with valid data and submit | User is on the profile form | 1. Enter a valid First Name in the First_Name field<br>2. Enter a valid Last Name in the Last_Name field<br>3. Enter a valid Email Address in the Email_Address field<br>4. Click Update Profile | Profile updates successfully; confirmation message is displayed. | medium |
| TC-008 (boundary) | WF-002 | Submit the profile form with one required field empty | User is on the profile form | 1. Enter a valid First Name in the First_Name field<br>2. Leave Last Name field empty<br>3. Enter a valid Email Address in the Email_Address field<br>4. Click Update Profile | Form submission is blocked; inline error message shows 'Last Name is required'. | medium |
| TC-009 (input_edge) |  | Enter a very long string in the Description field | User is on the profile form | 1. Enter a long string of 200+ characters in the Description field<br>2. Fill all other required fields<br>3. Click Update Profile | Form submits successfully; saved value in the Description field reflects the long input. | low |
| TC-010 (input_edge) |  | Enter special characters in the First Name field | User is on the profile form | 1. Enter special characters in the First_Name field<br>2. Fill all other required fields with valid data<br>3. Click Update Profile | Form submission is blocked; inline error message shows 'First Name contains invalid characters'. | low |
| TC-011 (interaction_edge) |  | Rapidly submit the profile form after a successful update | User has just updated their profile successfully | 1. Click Update Profile<br>2. Immediately click Update Profile again | Second submission attempt is blocked; only one record appears in the profile details. | medium |

---

## Logout

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | User logs out successfully | User logged in as <Role> | 1. Click the Logout button | User is redirected to the login page; access to all protected pages requires re-authentication after logout. | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Unauthenticated user attempts to log out | user must be authenticated | 1. Ensure user is not authenticated<br>2. Click Logout_Button | Logout action is blocked; user remains on the current page; no session is terminated. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | Attempt to log out without being authenticated | user is not authenticated | 1. Click on the Logout button | Logout action is blocked; user remains on the current page without session termination | medium |
| TC-004 (interaction_edge) | WF-001 | Rapid consecutive logout attempts | user is authenticated | 1. Click on the Logout button<br>2. Immediately click the Logout button again | Second logout attempt is ignored; user is redirected to the login page only once | medium |

---
