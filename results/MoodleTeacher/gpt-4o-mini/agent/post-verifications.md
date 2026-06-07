# Post-Verification Specifications

### [TC-001] User logs out successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the Logout button

**Original Expected Result:** terminates the current authenticated session and redirects to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard`
- **Observe**:
  - Calendar block
  - current date highlighted
  - events listed for the current month

**Post-Check**
- **Navigate To**: `Dashboard`
- **Observe**:
  - Calendar block
  - current date highlighted
  - events listed for the current month

**Expected Change**: A new event appears in the Calendar block for the selected date.

---

### [TC-005] Leave the Email Address field blank and submit
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Leave the Email Address field blank
2. 2. Fill all other required fields with valid data
3. 3. Click Update Profile

**Original Expected Result:** Inline validation error appears on the Email_Address field indicating it is required

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard`
- **Observe**:
  - position of existing blocks

**Post-Check**
- **Navigate To**: `Dashboard`
- **Observe**:
  - position of existing blocks

**Expected Change**: The moved block appears in a new position on the Dashboard.

---

### [TC-006] Upload a file that does not meet the upload constraints
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Select a file that does not meet the upload constraints
2. 2. Fill all other required fields with valid data
3. 3. Click Update Profile

**Original Expected Result:** Inline validation error appears indicating the file does not meet the upload constraints

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard`
- **Observe**:
  - existing block displayed

**Post-Check**
- **Navigate To**: `Dashboard`
- **Observe**:
  - no existing block displayed

**Expected Change**: The existing block is no longer displayed on the Dashboard.

---

### [TC-001] User logs out successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the Logout button

**Original Expected Result:** terminates the current authenticated session and redirects to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `My Courses`
- **Observe**:
  - list of courses
  - course order

**Post-Check**
- **Navigate To**: `My Courses`
- **Observe**:
  - list of courses
  - course order

**Expected Change**: The starred course appears at the top of the course list.

---

### [TC-002] Attempt to log out while unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is not authenticated
2. 2. Click the Logout button

**Original Expected Result:** Logout action is blocked; user remains on the current page and is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `My Courses page`
- **Observe**:
  - list of course cards

**Post-Check**
- **Navigate To**: `My Courses page`
- **Observe**:
  - list of course cards

**Expected Change**: The course card for the removed course is no longer visible in the list of course cards.

---

### [TC-001] User logs out successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the Logout button

**Original Expected Result:** terminates the current authenticated session and redirects to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Page`
- **Observe**:
  - list of sections
  - subsection names

**Post-Check**
- **Navigate To**: `Course Page`
- **Observe**:
  - list of sections
  - new subsection name

**Expected Change**: A new subsection appears in the list of sections on the course page.

---

### [TC-004] User attempts to log out when not authenticated
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button

**Original Expected Result:** Logout action is blocked; user remains on the current page with no session termination.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Page`
- **Observe**:
  - activity settings
  - activity name
  - activity description

**Post-Check**
- **Navigate To**: `Course Page`
- **Observe**:
  - activity settings
  - activity name
  - activity description

**Expected Change**: Activity settings reflect the changes made during the edit process.

---

### [TC-005] Leave the Email Address field blank and submit
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Leave the Email Address field blank
2. 2. Fill all other required fields with valid data
3. 3. Click Update Profile

**Original Expected Result:** Inline validation error appears on the Email_Address field indicating it is required

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Page`
- **Observe**:
  - activity position in the list

**Post-Check**
- **Navigate To**: `Course Page`
- **Observe**:
  - activity position in the list

**Expected Change**: The activity is now located in the new position as per the move action.

---

### [TC-006] Upload a file that does not meet the upload constraints
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Select a file that does not meet the upload constraints
2. 2. Fill all other required fields with valid data
3. 3. Click Update Profile

**Original Expected Result:** Inline validation error appears indicating the file does not meet the upload constraints

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Page`
- **Observe**:
  - list of activities
  - activity name of the original activity

**Post-Check**
- **Navigate To**: `Course Page`
- **Observe**:
  - list of activities
  - activity name of the duplicated activity

**Expected Change**: A new activity appears in the list with the same name as the original activity, indicating it has been duplicated.

---

### [TC-007] Submit with all required fields empty
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Leave all required fields blank
2. 2. Click Update Profile

**Original Expected Result:** Inline validation error appears on the First_Name, Last_Name, and Email_Address fields indicating they are required

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Page`
- **Observe**:
  - list of activities
  - visibility status of the activity

**Post-Check**
- **Navigate To**: `Course Page`
- **Observe**:
  - list of activities

**Expected Change**: The activity is no longer visible in the list of activities.

---

### [TC-008] Upload a file exactly at the size limit for New Picture Upload
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Drag and drop a file that is exactly at the size limit into the New Picture Upload area
2. 2. Fill in all required fields with valid data
3. 3. Click Update Profile

**Original Expected Result:** Profile is updated successfully; the profile page refreshes.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Page`
- **Observe**:
  - access restrictions settings for the activity

**Post-Check**
- **Navigate To**: `Course Page`
- **Observe**:
  - access restrictions settings for the activity

**Expected Change**: Access restrictions settings are updated to reflect the new restrictions applied.

---

### [TC-009] Upload a file one byte over the size limit for New Picture Upload
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Drag and drop a file that is one byte over the size limit into the New Picture Upload area
2. 2. Fill in all required fields with valid data
3. 3. Click Update Profile

**Original Expected Result:** Upload is blocked; an error message is displayed indicating the file exceeds the size limit.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Page`
- **Observe**:
  - list of activities
  - activity name

**Post-Check**
- **Navigate To**: `Course Page`
- **Observe**:
  - list of activities

**Expected Change**: The activity is no longer listed in the activities section.

---

### [TC-001] User logs out successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the Logout button

**Original Expected Result:** terminates the current authenticated session and redirects to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Page`
- **Observe**:
  - list of assignments
  - assignment name

**Post-Check**
- **Navigate To**: `Course Page`
- **Observe**:
  - list of assignments
  - assignment name

**Expected Change**: The new assignment appears in the list of assignments with the correct name.

---

### [TC-002] Attempt to log out while unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is not authenticated
2. 2. Click the Logout button

**Original Expected Result:** Logout action is blocked; user remains on the current page and is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Page`
- **Observe**:
  - list of assignments

**Post-Check**
- **Navigate To**: `Course Page`
- **Observe**:
  - new assignment name
  - due date
  - submission status

**Expected Change**: New assignment appears in the list of assignments with the correct name and default submission status.

---

### [TC-001] User logs out successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the Logout button

**Original Expected Result:** terminates the current authenticated session and redirects to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Settings`
- **Observe**:
  - Course full name
  - Course short name
  - Course category
  - Course visibility
  - Course start date

**Post-Check**
- **Navigate To**: `Course Page`
- **Observe**:
  - Course full name
  - Course short name
  - Course category
  - Course visibility
  - Course start date

**Expected Change**: Course settings are updated to reflect the new values entered in the Course Settings form.

---

### [TC-004] User attempts to log out when not authenticated
**Category**: `edge` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button

**Original Expected Result:** Logout action is blocked; user remains on the current page with no session termination.

---

#### Verification Plan

**Actor A (Role: `teacher`)**
- **Action**: Execute the steps from the core test case.

**Actor B (Role: `student`)**
- **Session**: `new_session`
- **Navigate To**: `Course Page -> Participants section`
- **Action**: 
- **Observe**:
  - list of enrolled students
  - newly added student's name
  - student's role

**Expected Change**: The newly added student appears in the Participants section with the correct role.

---

### [TC-006] Upload a file that does not meet the upload constraints
**Category**: `negative` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Select a file that does not meet the upload constraints
2. 2. Fill all other required fields with valid data
3. 3. Click Update Profile

**Original Expected Result:** Inline validation error appears indicating the file does not meet the upload constraints

---

#### Verification Plan

**Actor A (Role: `teacher`)**
- **Action**: Edit the role of a user in the Participants Table.

**Actor B (Role: `student`)**
- **Session**: `new_session`
- **Navigate To**: `Course Page -> Participants`
- **Action**: 
- **Observe**:
  - user's role in the Participants table

**Expected Change**: The user's role is updated to the new role selected by the teacher.

---

### [TC-007] Submit with all required fields empty
**Category**: `negative` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Leave all required fields blank
2. 2. Click Update Profile

**Original Expected Result:** Inline validation error appears on the First_Name, Last_Name, and Email_Address fields indicating they are required

---

#### Verification Plan

**Actor A (Role: `teacher`)**
- **Action**: Send message to a user.

**Actor B (Role: `student`)**
- **Session**: `new_session`
- **Navigate To**: `Messaging section`
- **Action**: 
- **Observe**:
  - message from teacher
  - timestamp of message
  - message content

**Expected Change**: The message appears in the messaging section with the correct content and timestamp.

---

### [TC-008] Upload a file exactly at the size limit for New Picture Upload
**Category**: `edge` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Drag and drop a file that is exactly at the size limit into the New Picture Upload area
2. 2. Fill in all required fields with valid data
3. 3. Click Update Profile

**Original Expected Result:** Profile is updated successfully; the profile page refreshes.

---

#### Verification Plan

**Actor A (Role: `teacher`)**
- **Action**: Execute the steps from the core test case.

**Actor B (Role: `student`)**
- **Session**: `new_session`
- **Navigate To**: `Course Page -> Participants`
- **Action**: 
- **Observe**:
  - list of enrolled users
  - newly enrolled user's name
  - user's role

**Expected Change**: The newly enrolled users appear in the Participants list with the correct role assigned.

---

### [TC-004] User attempts to log out when not authenticated
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button

**Original Expected Result:** Logout action is blocked; user remains on the current page with no session termination.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Grades -> Submissions`
- **Observe**:
  - Final grade column for the corresponding submission

**Post-Check**
- **Navigate To**: `Grades -> Submissions`
- **Observe**:
  - Final grade column for the corresponding submission

**Expected Change**: Final grade column updates to reflect the entered grade.

---

### [TC-001] User logs out successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the Logout button

**Original Expected Result:** terminates the current authenticated session and redirects to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Grades -> Grader Report`
- **Observe**:
  - grade cell for <valid student name>
  - overall average row

**Post-Check**
- **Navigate To**: `Grades -> Grader Report`
- **Observe**:
  - grade cell for <valid student name>
  - overall average row

**Expected Change**: The grade cell for <valid student name> reflects the updated value; the overall average row is adjusted accordingly.

---

### [TC-002] Attempt to log out while unauthenticated
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is not authenticated
2. 2. Click the Logout button

**Original Expected Result:** Logout action is blocked; user remains on the current page and is not redirected to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Gradebook Grader Report`
- **Observe**:
  - grade cell for the specific student
  - overall average row

**Post-Check**
- **Navigate To**: `Gradebook Grader Report`
- **Observe**:
  - grade cell for the specific student
  - overall average row

**Expected Change**: The grade cell for the specific student reflects the updated grade value, and the overall average row is adjusted accordingly.

---

### [TC-001] User logs out successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the Logout button

**Original Expected Result:** terminates the current authenticated session and redirects to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Profile`
- **Observe**:
  - full name
  - email address
  - timezone

**Post-Check**
- **Navigate To**: `Profile`
- **Observe**:
  - full name
  - email address
  - timezone

**Expected Change**: Profile details reflect the updated information after editing.

---

### [TC-013] Send a message
**Category**: `positive` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Message' button

**Original Expected Result:** Message sent successfully

---

#### Verification Plan

**Actor A (Role: `teacher`)**
- **Action**: Send a message by clicking the 'Message' button.

**Actor B (Role: `student`)**
- **Session**: `new_session`
- **Navigate To**: `Messages`
- **Action**: 
- **Observe**:
  - new message notification
  - message content

**Expected Change**: The student sees the new message in their messages list with the correct content.

---

### [TC-001] User logs out successfully
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click on the Logout button

**Original Expected Result:** terminates the current authenticated session and redirects to the login page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Profile`
- **Observe**:
  - full name
  - email address
  - profile picture

**Post-Check**
- **Navigate To**: `Profile`
- **Observe**:
  - full name
  - email address
  - profile picture

**Expected Change**: Full name updated to <valid first name> <valid last name>; email address updated to <valid email>; profile picture updated to the uploaded image.

---
