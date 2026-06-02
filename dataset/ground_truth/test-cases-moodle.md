# Moodle Test Cases

**Legacy status:** this combined Moodle file is retained for historical reference only. Use `MoodleTeacher.md` and `MoodleStudent.md` as the authoritative role-separated ground truth files for scoring generated Moodle test cases.

**Website URL:** http://localhost:8080
**Test Suite Version:** 1.0

---

## Table of Contents
1. [Login](#1-login)
2. [Dashboard](#2-dashboard)
3. [My Courses](#3-my-courses)
4. [Course Page](#4-course-page)
5. [Participants](#5-participants)
6. [Adding Activities](#6-adding-activities)
7. [Course Settings](#7-course-settings)
8. [Assignment Submission](#8-assignment-submission)
9. [Assignment Review And Grading](#9-assignment-review-and-grading)
10. [Grades](#10-grades)
11. [Activities](#11-activities)
12. [Profile](#12-profile)
13. [Logout](#13-logout)

---

## 1. Login

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGIN-001 | Valid student login | Student account exists | 1. Navigate to the Moodle login page<br>2. Enter valid student username<br>3. Enter valid password<br>4. Click "Log in" | Student is redirected to the Dashboard | High |
| LOGIN-002 | Valid teacher login | Teacher account exists | 1. Navigate to the Moodle login page<br>2. Enter valid teacher username<br>3. Enter valid password<br>4. Click "Log in" | Teacher is redirected to the Dashboard | High |
| LOGIN-003 | Guest access | Guest access is enabled | 1. Navigate to the Moodle login page<br>2. Click "Access as a guest" | Guest user enters the site without authenticated dashboard access | Medium |
| LOGIN-004 | Login page elements displayed | None | 1. Navigate to the Moodle login page | Username field, Password field, "Log in" button, "Lost password?" link, "Access as a guest" button, and cookies notice control are visible | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGIN-005 | Invalid username and password | None | 1. Navigate to login page<br>2. Enter invalid username<br>3. Enter invalid password<br>4. Click "Log in" | Error message is displayed and user remains on the login page | High |
| LOGIN-006 | Empty username | None | 1. Leave username empty<br>2. Enter password<br>3. Click "Log in" | Validation or login error is displayed | High |
| LOGIN-007 | Empty password | None | 1. Enter username<br>2. Leave password empty<br>3. Click "Log in" | Validation or login error is displayed | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGIN-008 | Username remains populated after failed login | None | 1. Enter invalid username<br>2. Enter invalid password<br>3. Click "Log in" | Error appears and the username field remains populated for correction | Medium |
| LOGIN-009 | Cookies notice dismissal | Cookies notice is visible | 1. Click the cookies notice control | Cookies notice is accepted or dismissed without breaking the login form | Low |

---

## 2. Dashboard

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| DASH-001 | Personalized greeting displayed | User is logged in | 1. Navigate to Dashboard | Greeting with the logged-in user's name is displayed | High |
| DASH-002 | Timeline block visible | User is logged in | 1. Navigate to Dashboard | Timeline block is visible in the main content area | High |
| DASH-003 | Calendar block visible | User is logged in | 1. Navigate to Dashboard | Calendar block is visible in the main content area | High |
| DASH-004 | Full calendar link opens calendar view | User is logged in | 1. Click "Full calendar" | Full calendar page is displayed | Medium |
| DASH-005 | New event button opens event creation flow | User is logged in | 1. Click "New event" | Event creation form or modal is displayed | Medium |
| DASH-006 | Teacher add-a-block opens modal | Logged in as teacher and edit mode is enabled | 1. Click "+ Add a block" | Add-a-block modal is displayed for the teacher view | Medium |
| DASH-007 | Student add-a-block opens page | Logged in as student and edit mode is enabled | 1. Click "+ Add a block" | Add-a-block page is displayed for the student view | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| DASH-008 | Dashboard search with no matching activity | User is logged in | 1. Enter a non-matching term in the Timeline search field | Empty-state or no-results feedback is displayed | Medium |
| DASH-009 | Add-a-block action unavailable outside edit mode | User is logged in and edit mode is disabled | 1. Observe the dashboard controls | Personalization controls are hidden or inactive until edit mode is enabled | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| DASH-010 | Reset page to default after dashboard customization | User is logged in and edit mode is enabled | 1. Reorder or customize dashboard blocks<br>2. Click "Reset page to default" | Dashboard returns to the default layout | Medium |
| DASH-011 | Dashboard with no upcoming work | User is logged in and has no pending activities | 1. Navigate to Dashboard | "No activities require action" state is shown without layout issues | Low |

---

## 3. My Courses

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| COURSES-001 | My Courses headings displayed | User is logged in and enrolled in at least one course | 1. Navigate to "My courses" | "My courses" heading and "Course overview" subheading are displayed | High |
| COURSES-002 | Course cards displayed | User is logged in and enrolled in multiple courses | 1. Navigate to "My courses" | Each enrolled course is shown as a card with image, course name, and category | High |
| COURSES-003 | Search for enrolled course | User is logged in and enrolled in multiple courses | 1. Enter part of a course name in the search field | Matching course cards are displayed | High |
| COURSES-004 | Sort courses | User is logged in and enrolled in multiple courses | 1. Open "Sort by course name"<br>2. Choose a sort option | Course list is reordered according to the selected sort | Medium |
| COURSES-005 | Star a course from three-dot menu | User is logged in and enrolled in courses | 1. Open a course card menu<br>2. Click "Star this course" | Course is marked as starred | Medium |
| COURSES-006 | Switch course overview layout | User is logged in and enrolled in courses | 1. Open the layout dropdown<br>2. Select another layout | Course overview changes to the selected layout | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| COURSES-007 | Search for non-existent course | User is logged in | 1. Enter a non-matching course name in the search field | No matching course cards are displayed | Medium |
| COURSES-008 | Remove course from current view | User is logged in and enrolled in courses | 1. Open a course card menu<br>2. Click "Remove from view" | Selected course disappears from the current overview layout | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| COURSES-009 | Filter by "All" dropdown when many courses exist | User is logged in and enrolled in courses with different statuses | 1. Open the "All" dropdown<br>2. Choose another filter | Only courses matching the selected filter remain visible | Low |

---

## 4. Course Page

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| COURSE-001 | Teacher course navigation tabs displayed | Logged in as teacher and enrolled in a course | 1. Open a course page | Course, Settings, Participants, Grades, Activities, and More are displayed | High |
| COURSE-002 | Student course navigation tabs displayed | Logged in as student and enrolled in a course | 1. Open a course page | Course, Participants, Grades, Activities, and Competencies are displayed | High |
| COURSE-003 | Course sections and activities displayed | User is logged in and on a course page | 1. Open a course page | Sections, activity icons, and activity names are visible | High |
| COURSE-004 | Collapse all sections | User is logged in and on a course page | 1. Click "Collapse all" | All course sections collapse | Medium |
| COURSE-005 | Course Index navigation works | User is logged in and on a course page | 1. Click an item in the Course Index | Page navigates to the selected section or activity | Medium |
| COURSE-006 | Activity link opens activity page | User is logged in and on a course page | 1. Click an assignment, forum, or page activity | Corresponding activity page opens | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| COURSE-007 | Student cannot access teacher settings controls | Logged in as student | 1. Open a course page | Settings tab and editing controls are not available to the student | High |
| COURSE-008 | Student cannot enable edit mode on course page | Logged in as student | 1. Open a course page | Edit mode toggle is absent or inaccessible | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| COURSE-009 | Hide Course Index sidebar | User is logged in and on a course page | 1. Click the Course Index close button (X) | Course Index sidebar closes without affecting course content rendering | Low |

---

## 5. Participants

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| PART-001 | Teacher participants page management controls displayed | Logged in as teacher and on a course Participants page | 1. Open Participants tab | Enrolled users dropdown, "Enrol users" button, filters, and participants table are visible | High |
| PART-002 | Student participants page view displayed | Logged in as student and on a course Participants page | 1. Open Participants tab | Participants table and filters are visible | High |
| PART-003 | Filter participants by role or name | Logged in as teacher | 1. Add a filter condition<br>2. Apply filters | Participants list updates to match the selected criteria | High |
| PART-004 | Participant profile link opens profile | User is logged in and on Participants page | 1. Click a participant name | Participant profile page opens | Medium |
| PART-005 | Alphabetical filter works | User is logged in and on Participants page | 1. Click an alphabetical filter<br>2. Apply filters | Participants list is filtered by the selected initial | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| PART-006 | Student cannot enroll users | Logged in as student | 1. Open Participants tab | Enrolment management controls are not available | High |
| PART-007 | Student cannot edit or remove participant roles | Logged in as student | 1. Open Participants tab | Role edit and participant removal controls are not available | High |
| PART-008 | Filter with no matches | User is logged in and on Participants page | 1. Apply a filter that matches no users | Empty or zero-results state is displayed | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| PART-009 | Multiple filter conditions combined | Logged in as teacher | 1. Add two filter conditions<br>2. Click "Apply filters" | Results satisfy both filter conditions | Medium |

---

## 6. Adding Activities

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ACT-001 | Enable edit mode | Logged in as teacher and on a course page | 1. Toggle edit mode on | Editing controls become visible on the course page | High |
| ACT-002 | Open Activity Chooser | Edit mode is enabled | 1. Click "+" in a course section<br>2. Select "Activity or resource" | Activity Chooser is displayed | High |
| ACT-003 | Search or filter Activity Chooser | Activity Chooser is open | 1. Enter a search term or choose a category filter | Matching activities and resources are displayed | Medium |
| ACT-004 | Create assignment with "Save and return to course" | Logged in as teacher and edit mode is enabled | 1. Open Activity Chooser<br>2. Select Assignment<br>3. Fill required fields<br>4. Click "Save and return to course" | Assignment is created and teacher returns to the course page | High |
| ACT-005 | Create assignment with "Save and display" | Logged in as teacher and edit mode is enabled | 1. Open Activity Chooser<br>2. Select Assignment<br>3. Fill required fields<br>4. Click "Save and display" | Assignment is created and its activity page opens | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ACT-006 | Assignment name empty | Logged in as teacher and on new assignment form | 1. Leave assignment name empty<br>2. Fill other required inputs<br>3. Save | Validation error indicates assignment name is required | High |
| ACT-007 | Add action with no activity selected | Activity Chooser is open | 1. Click "Add" without selecting an activity or resource | No activity is created and user is prompted to select an option | Medium |
| ACT-008 | Additional file exceeds upload limit | Logged in as teacher and on new assignment form | 1. Upload an oversized file in Additional files<br>2. Save | Upload is rejected and file-size error is shown | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ACT-009 | Same submission start and due date | Logged in as teacher and on new assignment form | 1. Enable "Allow submissions from"<br>2. Set Due date to the same date/time<br>3. Save | Assignment is created or validated consistently for the same boundary date | Low |
| ACT-010 | Maximum submission size selected | Logged in as teacher and on new assignment form | 1. Enable file submissions<br>2. Choose the maximum allowed submission size<br>3. Save | Assignment saves with the selected maximum size | Low |

---

## 7. Course Settings

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| CSET-001 | Save course settings with valid required fields | Logged in as teacher and on Course Settings page | 1. Enter valid course full name<br>2. Enter valid short name<br>3. Choose a valid category<br>4. Click "Save and display" | Course settings are saved successfully | High |
| CSET-002 | Course image upload controls displayed | Logged in as teacher and on Course Settings page | 1. Expand Description section | Course summary editor and course image upload area are visible | Medium |
| CSET-003 | Configuration dropdowns displayed | Logged in as teacher and on Course Settings page | 1. Expand each settings section | Visibility, format, appearance, upload, completion, and groups controls are present | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| CSET-004 | Course full name empty | Logged in as teacher and on Course Settings page | 1. Clear Course full name<br>2. Save | Validation error indicates full name is required | High |
| CSET-005 | Course short name empty | Logged in as teacher and on Course Settings page | 1. Clear Course short name<br>2. Save | Validation error indicates short name is required | High |
| CSET-006 | Course category empty | Logged in as teacher and on Course Settings page | 1. Remove category selection<br>2. Save | Validation error indicates category is required | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| CSET-007 | Same start and end date | Logged in as teacher and on Course Settings page | 1. Enable end date<br>2. Set course start date and end date to the same date<br>3. Save | System saves or validates the same-date boundary consistently | Low |
| CSET-008 | End date in the past | Logged in as teacher and on Course Settings page | 1. Enable end date<br>2. Set end date in the past<br>3. Save | System rejects invalid configuration or clearly indicates the accepted behavior | Low |
| CSET-009 | Maximum upload size selection | Logged in as teacher and on Course Settings page | 1. Select the maximum upload size<br>2. Save | Value is preserved after save | Low |

---

## 8. Assignment Submission

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ASUB-001 | Assignment page details displayed | Logged in as student and assignment is available | 1. Open an assignment | Opened date, due date, description, and submission status are visible | High |
| ASUB-002 | Submit assignment with online text | Logged in as student and assignment accepts online text | 1. Click "Add submission"<br>2. Enter valid online text<br>3. Submit | Submission is accepted and status changes to "Submitted for grading" | High |
| ASUB-003 | Submit assignment with file upload | Logged in as student and assignment accepts files | 1. Click "Add submission"<br>2. Upload valid file<br>3. Submit | Submission is accepted and status changes to "Submitted for grading" | High |
| ASUB-004 | Edit submitted assignment before deadline | Logged in as student and editable submission already exists | 1. Click "Edit submission"<br>2. Update submission<br>3. Save | Updated submission is stored successfully | Medium |
| ASUB-005 | Remove submitted assignment when allowed | Logged in as student and removable submission already exists | 1. Click "Remove submission"<br>2. Confirm removal | Submission status returns to not submitted | Medium |
| ASUB-006 | View grade and teacher feedback after grading | Student submission has been graded | 1. Open assignment page | Grade and feedback are displayed on the assignment page | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ASUB-007 | Submit with required online text missing | Logged in as student and assignment requires online text | 1. Click "Add submission"<br>2. Leave online text empty<br>3. Submit | Submission is blocked and validation feedback is shown | High |
| ASUB-008 | Submit with required file missing | Logged in as student and assignment requires file upload | 1. Click "Add submission"<br>2. Do not attach a file<br>3. Submit | Submission is blocked and validation feedback is shown | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ASUB-009 | Maximum allowed online text length | Logged in as student and assignment accepts online text | 1. Enter content at the maximum allowed size<br>2. Submit | Submission is handled correctly at the boundary | Low |
| ASUB-010 | File at allowed upload limit | Logged in as student and assignment accepts files | 1. Upload a file at the configured upload limit<br>2. Submit | Submission is accepted at the allowed file-size boundary | Low |

---

## 9. Assignment Review And Grading

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| AGRD-001 | Teacher assignment summary displayed | Logged in as teacher and on an assignment page | 1. Open assignment page | Grade button and grading summary are visible | High |
| AGRD-002 | Submissions tab elements displayed | Logged in as teacher and on assignment Submissions tab | 1. Open Submissions tab | Search, filter, status, quick grading, actions, grade, and feedback columns are visible | High |
| AGRD-003 | Search submissions by student | Logged in as teacher and on assignment Submissions tab | 1. Search by student name or email | Submission table is filtered to matching entries | Medium |
| AGRD-004 | Grade a submission | Logged in as teacher and at least one submission exists | 1. Click "Grade"<br>2. Enter a valid grade<br>3. Save | Grade is stored and shown in the submissions table | High |
| AGRD-005 | Save feedback comments | Logged in as teacher and grading form is open | 1. Enter feedback comments<br>2. Save | Feedback comments are stored successfully | Medium |
| AGRD-006 | Upload feedback file | Logged in as teacher and grading form is open | 1. Upload valid feedback file<br>2. Save | Feedback file is stored successfully | Medium |
| AGRD-007 | Advanced grading options visible | Logged in as teacher and on Advanced grading tab | 1. Open Advanced grading tab | Rubric-based grading options and template choices are displayed | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| AGRD-008 | Search with no matching submission | Logged in as teacher and on Submissions tab | 1. Search for a non-existent student | Empty or zero-results state is displayed | Medium |
| AGRD-009 | Invalid advanced grading form fallback | Logged in as teacher and invalid grading form exists | 1. Attempt to use an invalid advanced grading form | System falls back to simple grading or clearly signals invalid form status | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| AGRD-010 | Quick grading toggle | Logged in as teacher and on Submissions tab | 1. Enable Quick grading | Interface changes consistently to support quick grading | Low |
| AGRD-011 | Final grade reflects latest saved grade | Logged in as teacher and a submission was just graded | 1. Save a grade<br>2. Review Final grade column | Final grade column reflects the latest saved value | Low |

---

## 10. Grades

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| GRADE-001 | Student sees only own grades in user report | Logged in as student and enrolled in graded course | 1. Open Grades tab | User report shows only the logged-in student's grades | High |
| GRADE-002 | Ungraded items display empty state | Logged in as student and some activities are not graded | 1. Open Grades tab | Unsubmitted or ungraded items display "(Empty)" where applicable | Medium |
| GRADE-003 | Course total row visible in student report | Logged in as student and enrolled in graded course | 1. Open Grades tab<br>2. Scroll to bottom | Aggregation row for course total is displayed | Medium |
| GRADE-004 | Teacher gradebook columns displayed | Logged in as teacher and on Grades tab | 1. Open Grades tab | Gradebook shows student rows, assignment columns, and course total column | High |
| GRADE-005 | Teacher searches gradebook by user | Logged in as teacher and on Grades tab | 1. Enter a user name in search<br>2. Submit search | Gradebook filters to matching user rows | Medium |
| GRADE-006 | Save valid grade changes in gradebook | Logged in as teacher and gradebook is editable | 1. Enter valid grade values<br>2. Click "Save changes" | Updated grades are saved successfully | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| GRADE-007 | Student cannot access grader report controls | Logged in as student | 1. Open Grades tab | Grader report editing controls are not available to the student | High |
| GRADE-008 | Invalid or empty teacher grade entry | Logged in as teacher and gradebook is editable | 1. Enter invalid or empty grade value where not allowed<br>2. Save changes | Save is blocked or validation feedback is displayed | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| GRADE-009 | Overall averages update after valid save | Logged in as teacher and grade changes were saved | 1. Save grade changes<br>2. Review average row | Overall averages reflect the latest saved data | Low |
| GRADE-010 | Course total recalculation boundary | Logged in as teacher and one grade is updated to a high or low limit | 1. Update grade at a boundary value<br>2. Save changes | Course total recalculates correctly | Low |

---

## 11. Activities

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ACTIV-001 | Activities page heading displayed | Logged in as student and enrolled in a course | 1. Open the Activities tab in a course | "Activities" heading and overview description are visible | High |
| ACTIV-002 | Assignment activities section displayed | Logged in as student and enrolled in a course with assignments | 1. Open the Activities tab | Assignments section is visible with activity names, due dates, and submission statuses | High |
| ACTIV-003 | Forums and resources sections displayed | Logged in as student and enrolled in a course | 1. Open the Activities tab | Forums and Resources sections are visible | Medium |
| ACTIV-004 | Activity link navigation works | Logged in as student and Activities page is open | 1. Click an activity name from the Activities page | Corresponding activity page opens | Medium |
| ACTIV-005 | Expand or collapse activity groups | Logged in as student and Activities page is open | 1. Click the arrow icon for an activity group | Selected group expands or collapses | Low |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ACTIV-006 | Activities page with no matching activity type content | Logged in as student and selected activity group has no items | 1. Open an empty activity group | Empty-state behavior is displayed without breaking the page layout | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ACTIV-007 | Activities page displays long activity names cleanly | Logged in as student and course contains long activity names | 1. Open the Activities tab | Long activity names remain visible and readable without breaking table layout | Low |

---

## 12. Profile

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| PROF-001 | Profile information cards displayed | User is logged in | 1. Open user Profile | User details, course details, reports, and login activity sections are visible | High |
| PROF-002 | Update profile with valid information | User is logged in and on Edit profile page | 1. Enter valid first name, last name, and email<br>2. Update optional profile fields<br>3. Click "Update profile" | Profile updates successfully | High |
| PROF-003 | Upload valid profile picture | User is logged in and on Edit profile page | 1. Upload valid image file<br>2. Click "Update profile" | Profile picture is updated successfully | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| PROF-004 | First name empty | User is logged in and on Edit profile page | 1. Clear first name<br>2. Save profile | Validation error is displayed | Medium |
| PROF-005 | Email empty | User is logged in and on Edit profile page | 1. Clear email address<br>2. Save profile | Validation error is displayed | Medium |
| PROF-006 | Unsupported image type upload | User is logged in and on Edit profile page | 1. Upload unsupported file type as picture<br>2. Save profile | Upload is rejected with error feedback | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| PROF-007 | Maximum description length | User is logged in and on Edit profile page | 1. Enter description at the maximum allowed size<br>2. Save profile | Profile is saved or validated consistently at the text boundary | Low |
| PROF-008 | Image exceeds size limit | User is logged in and on Edit profile page | 1. Upload an oversized image<br>2. Save profile | Upload is rejected with file-size error | Low |

---

## 13. Logout

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGOUT-001 | Logout from user menu | User is logged in | 1. Open user menu<br>2. Click "Log out" | Session ends and user is returned to the login page | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGOUT-002 | Access protected page after logout | User logged out in current session | 1. Attempt to open a protected dashboard or course URL | User is redirected to login page or prompted to authenticate again | High |
