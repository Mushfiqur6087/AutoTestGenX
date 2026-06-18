# Moodle Student Test Cases

**Website URL:** http://localhost:8080
**Test Suite Version:** 2.1 (Moodle gold oracle)
**Role Scope:** Student learner workflows only

---

## Table of Contents
1. [Login](#1-login)
2. [Dashboard](#2-dashboard)
3. [My Courses](#3-my-courses)
4. [Course Page](#4-course-page)
5. [Participants](#5-participants)
6. [Grades](#6-grades)
7. [Assignment](#7-assignment)
8. [Activities](#8-activities)
9. [Profile](#9-profile)
10. [Logout](#10-logout)

---

## Test Credentials

| Field | Value |
|-------|-------|
| Student account | `student1`, seeded student enrolled in the test course |
| Teacher account | `teacher1`, seeded teacher for setup/grading preconditions |
| Test course | `QA Automation 101`, containing participants, grades, activities, and an assignment |
| Reference assignment | `Essay Draft`, online text and file submission enabled, open for submission, no separate submit-button confirmation |
| Boundary grade range | 0 to 100 points for `Essay Draft` |
| Boundary upload limit | 10 MB maximum upload size for assignment/profile upload checks |
| Boundary files | `essay-draft.pdf` under 1 MB, `essay-limit-10mb.pdf` exactly at limit, `oversize-11mb.pdf` over limit |
| Boundary text | `GT-LONG-TEXT-START` + 10,000 characters + `GT-LONG-TEXT-END` |

## Moodle Gold Oracle Contract

| Rule | Requirement |
|------|-------------|
| Source anchoring | Every module below maps to `dataset/raw_specifications/Moodle/MoodleStudent.md`; inferred Moodle behavior is allowed only when the expected result names observable UI evidence. |
| Student-only scope | Student ground truth must not include teacher authoring, enrollment administration, or full-gradebook administration workflows. |
| Observable result | Expected results must name visible UI state, persisted submission/grade state, redirect, access denial, validation feedback, or absence of privileged controls. |
| Deterministic oracle | Avoid generic success words, conditional applicability, ambiguous alternatives, and implementation-variable outcomes. A reviewer should be able to mark pass/fail without guessing. |
| Fixture stability | Use seeded student, teacher, course, assignment, file, grade, and activity fixtures rather than unspecified users or courses. |
| Permission boundary | Student tests should explicitly verify absence of teacher-only controls where relevant. |
| Persistence check | Submission, profile, dashboard layout, and course-card preference tests should verify state after save and refresh when practical. |
| Data cleanup | Tests that mutate data must restore the named fixture or create disposable records with the `Ground Truth` suffix for cleanup. |

## Quality and Traceability Rules

| Rule | Requirement |
|------|-------------|
| `MS-NAV` | Shared navigation, user menu, breadcrumbs, course tabs, Course Index, notifications, and messaging. |
| `MS-LOGIN` | Authentication form, guest entry, cookies notice, and login validation. |
| `MS-DASH` | Student Dashboard timeline, calendar, personal event entry, edit mode, and empty states. |
| `MS-COURSES` | My Courses filtering, searching, sorting, layout, starring, and hidden-course behavior. |
| `MS-COURSE` | Course page content, tabs, section collapse, Course Index navigation, and no-authoring permission boundary. |
| `MS-PART` | Participants viewing, filtering, profile navigation, and enrollment/role-management denial. |
| `MS-GRADE` | Student User report, own-grade visibility, course total, ungraded placeholders, and full-gradebook denial. |
| `MS-ASGN` | Assignment details, online text/file submission, edit/remove submission, feedback, late/required-field boundaries. |
| `MS-ACT` | Activities overview, grouped activity tables, activity navigation, hidden activity denial, and empty course state. |
| `MS-PROFILE` | Student profile display, own profile edit, picture upload, validation, and other-user edit denial. |
| `MS-LOGOUT` | Logout, protected-route reauthentication, browser-back protection, and timeout behavior. |

---

## 1. Login

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-LOGIN-001 | Valid student login | `student1` account exists and is active | 1. Navigate to the Moodle login page<br>2. Enter `student1` username<br>3. Enter the student password<br>4. Click "Log in" | Student is redirected to Dashboard and the user menu shows the student initials/name | High |
| MS-LOGIN-002 | Guest access from login page | Guest access is enabled | 1. Open login page<br>2. Click "Access as a guest" | Guest browsing opens without authenticating as student | Medium |
| MS-LOGIN-003 | Login page elements displayed | None | 1. Open login page | Username, Password, Log in, Lost password, Access as guest, and Cookies notice controls are visible | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-LOGIN-004 | Invalid student credentials | Login page is visible | 1. Enter `student1` username<br>2. Enter `WrongPass#2026`<br>3. Click "Log in" | Login error is shown, password is cleared, username remains populated, and Dashboard is not opened | High |
| MS-LOGIN-005 | Empty username | Login page is visible | 1. Leave Username empty<br>2. Enter the student password<br>3. Click "Log in" | Login is rejected, username field is identified as missing, and no authenticated page is opened | High |
| MS-LOGIN-006 | Empty password | Login page is visible | 1. Enter `student1` username<br>2. Leave Password empty<br>3. Click "Log in" | Login is rejected, password field is identified as missing, and no authenticated page is opened | High |
| MS-LOGIN-007 | Disabled lost-password link | Lost-password feature is disabled | 1. Click "Lost password?" | Recovery flow does not open | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-LOGIN-008 | Failed login retains username | Login page is visible | 1. Enter invalid credentials<br>2. Submit login | Username remains populated and password is cleared | Medium |
| MS-LOGIN-009 | Long username failure handling | Login page is visible | 1. Enter 200+ character username and invalid password<br>2. Submit | Login error is shown, password is cleared, the long username remains in the username field, and Log in remains clickable | Low |
| MS-LOGIN-010 | Both fields empty — all validation errors shown simultaneously | Login page is visible | 1. Leave Username and Password both empty<br>2. Click "Log in" | Both username and password fields are flagged with validation errors simultaneously; no authenticated page opens | High |
| MS-LOGIN-011 | Username with leading/trailing whitespace retained after failed login | Login page is visible | 1. Enter `  student1  ` (with leading and trailing spaces) as the username<br>2. Enter `WrongPass#2026`<br>3. Click "Log in" | Login is rejected with error; username field retains the entered string including the surrounding whitespace | Low |
| MS-LOGIN-012 | Rapid double submission of Log in results in single failure response | Login page is visible; invalid credentials ready | 1. Enter invalid credentials<br>2. Double-click "Log in" rapidly | Exactly one login-error response is displayed; the form is not submitted twice and no duplicate error message is stacked | Medium |

---

## 2. Dashboard

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-DASH-001 | Personalized dashboard greeting | Student is logged in | 1. Open Dashboard | Greeting for the logged-in student is displayed | High |
| MS-DASH-002 | Timeline shows upcoming activities | `Essay Draft` has a due date within the selected timeline range | 1. Log in as `student1`<br>2. Open Dashboard<br>3. Inspect Timeline block | Timeline lists `Essay Draft` with course name, due date, and direct activity link | High |
| MS-DASH-003 | Timeline controls update content | Timeline contains `Essay Draft` and at least one non-matching activity | 1. Select a range containing `Essay Draft`<br>2. Sort by date<br>3. Search for `Essay` | Timeline shows `Essay Draft`, hides non-matching activities, and preserves the selected controls | High |
| MS-DASH-004 | Calendar block supports personal event flow | Calendar block is visible | 1. Click "New event" | Personal calendar event form or modal opens with event title, date, and save/cancel controls | Medium |
| MS-DASH-005 | Calendar navigation and links | Calendar block is visible | 1. Select `QA Automation 101` in the course filter<br>2. Navigate to next month and back<br>3. Click Full calendar | Calendar heading changes then returns to the original month; Full calendar opens with `QA Automation 101` filter context visible | Medium |
| MS-DASH-006 | Add student dashboard block | Student is on Dashboard and Edit mode is enabled | 1. Click "+ Add a block"<br>2. Add `Latest announcements`<br>3. Refresh Dashboard | `Latest announcements` appears on `student1` Dashboard after refresh and is not added to `teacher1` Dashboard | Medium |
| MS-DASH-013 | Delete student dashboard block | `Latest announcements` is visible on `student1` Dashboard in Edit mode | 1. Open the block menu<br>2. Delete `Latest announcements`<br>3. Refresh Dashboard | `Latest announcements` is removed from `student1` Dashboard after refresh | Medium |
| MS-DASH-016 | Reset dashboard to default in edit mode reverts layout | `student1` is on Dashboard with Edit mode enabled and at least one block repositioned or added | 1. Click the "Reset page to default" option in Edit mode<br>2. Confirm the reset | Dashboard layout reverts to the default block arrangement and any added or repositioned blocks return to their original positions | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-DASH-007 | Dashboard blocked while unauthenticated | User is logged out | 1. Navigate directly to Dashboard URL | User is redirected to login | High |
| MS-DASH-008 | Add block unavailable outside edit mode | Edit mode is off | 1. Inspect Dashboard controls | "+ Add a block", configure, move, and delete controls are not rendered on the Dashboard | High |
| MS-DASH-009 | Timeline search with no matches | Student is logged in | 1. Search for non-existent activity | Empty/no-results state is displayed | Medium |
| MS-DASH-017 | Delete Timeline block via block menu removes it from dashboard | `student1` is on Dashboard with Edit mode enabled and Timeline block visible | 1. Open the block action menu on the Timeline block<br>2. Click "Delete Timeline" and confirm<br>3. Refresh Dashboard | Timeline block is absent from the Dashboard after refresh; no error message is shown | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-DASH-010 | Dashboard with no upcoming work | Student has no pending activities | 1. Open Dashboard | Timeline shows its no-activity empty state and Calendar block remains visible | Low |
| MS-DASH-011 | Calendar year boundary | Calendar displays January | 1. Click previous-month arrow | Calendar shows December of previous year | Medium |
| MS-DASH-012 | Rapid edit-mode toggle | Dashboard is visible | 1. Toggle Edit mode repeatedly | Final UI state matches final toggle | Medium |
| MS-DASH-014 | Timeline empty state when selected range has zero activities | `student1` is on Dashboard; a date range with no activities is known | 1. Select the date range that contains no scheduled activities | Timeline block displays its empty-state message and no activity rows are rendered | Low |
| MS-DASH-015 | Timeline search with special characters and emoji accepted | `student1` is on Dashboard | 1. Type `@@##🎓` into the Timeline search field | Search field accepts the input without error; timeline shows empty-results state or matching items; no crash or validation dialog appears | Low |
| MS-DASH-018 | Navigate calendar to previous month removes current-date highlight | Calendar block is visible and shows the current month | 1. Click the previous-month arrow on the Calendar block | Calendar advances to the previous month; the current-date highlight is absent on the previous month view | Low |

---

## 3. My Courses

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-COURSES-001 | Student course cards displayed | Student is enrolled in courses | 1. Open My Courses | Course cards show image, course name, and category | High |
| MS-COURSES-002 | Filter, search, sort, and layout controls | `student1` is enrolled in `QA Automation 101` and at least one other course | 1. Select All status filter<br>2. Search for `QA Automation`<br>3. Sort by course name<br>4. Switch to list layout | Only matching course cards/rows remain visible, order follows the sort selection, and list layout persists after refresh | High |
| MS-COURSES-003 | Open course from course card | At least one course is visible | 1. Click course name | Student opens course main page | High |
| MS-COURSES-004 | Star course from course card | `QA Automation 101` course card menu is visible | 1. Open card menu<br>2. Click "Star this course"<br>3. Refresh My Courses | `QA Automation 101` appears in the Starred filter and `student1` remains enrolled | Medium |
| MS-COURSES-009 | Remove course from view without unenrolling | `QA Automation 101` course card menu is visible | 1. Open card menu<br>2. Click "Remove from view"<br>3. Select Hidden filter<br>4. Open the hidden course card | `QA Automation 101` appears under Hidden, opens successfully, and `student1` remains enrolled as student | Medium |
| MS-COURSES-013 | Remove from view then immediately verify course appears in Hidden filter | `QA Automation 101` course card is visible | 1. Open card menu<br>2. Click "Remove from view"<br>3. Immediately switch to the Hidden filter without refreshing | `QA Automation 101` appears in the Hidden filter list immediately after the action; no page refresh is required | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-COURSES-005 | My Courses blocked while unauthenticated | User is logged out | 1. Navigate directly to My Courses URL | User is redirected to login | High |
| MS-COURSES-006 | Search no matching course | Student is logged in | 1. Search for non-existent course | Empty/no-results state is shown | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-COURSES-007 | Hidden-course filter | `QA Automation 101` was removed from view | 1. Select Hidden filter<br>2. Search for `QA Automation` | `QA Automation 101` is listed in Hidden with its course name and category; non-hidden courses are absent from the filtered list | Medium |
| MS-COURSES-008 | Long symbol search | My Courses is visible | 1. Search with `QA Automation @@@ ### 1234567890 long-search-token` | Search field retains the entered string, no matching-error dialog appears, and the course list shows matching or no-results content in the same layout | Low |
| MS-COURSES-010 | Very long search query (200+ chars) accepted without error | My Courses is visible | 1. Enter a 200+ character string into the course search field<br>2. Submit the search | Search field accepts and retains the long string; no error dialog appears; a matching or empty-results list is displayed without page crash | Low |
| MS-COURSES-011 | Search with special characters and emoji accepted | My Courses is visible | 1. Enter `@@##🎓 courses` into the search field<br>2. Submit the search | Search field accepts the input; no crash or validation error appears; list shows matching or empty-results content | Low |
| MS-COURSES-012 | Rapid star action on same course card is idempotent | `QA Automation 101` course card is visible and not starred | 1. Click "Star this course" on the `QA Automation 101` card menu<br>2. Immediately repeat the star action | Course is starred once; the Starred filter shows `QA Automation 101` exactly once with no duplicate entries | Medium |

---

## 4. Course Page

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-COURSE-001 | Student course tabs displayed | `student1` is enrolled in `QA Automation 101` | 1. Open the `QA Automation 101` course page | Course, Participants, Grades, Activities, and Competencies tabs are visible; Settings tab and edit controls are not visible | High |
| MS-COURSE-002 | Course sections and activities displayed | Course contains sections | 1. Inspect course content | Sections, activity icons, and activity/resource names are visible | High |
| MS-COURSE-003 | Collapse all sections | Sections are expanded | 1. Click "Collapse all" | Sections collapse | Medium |
| MS-COURSE-004 | Course Index navigation | Course Index is visible | 1. Click a section or activity in Course Index | Page navigates to selected content | Medium |
| MS-COURSE-005 | Open activity from course page | Activity link is visible | 1. Click assignment, forum, page, or resource link | Activity/resource page opens | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-COURSE-006 | Student cannot access Settings tab | Student is on course page | 1. Inspect course tabs | Settings tab and teacher settings controls are absent | High |
| MS-COURSE-007 | Student cannot enable course edit mode | Student is on course page | 1. Inspect page controls<br>2. Navigate directly to the edit-mode course URL | Edit toggle is absent; direct edit-mode URL returns to read-only course view or access denied without authoring controls | High |
| MS-COURSE-008 | Course page blocked while unauthenticated | User is logged out | 1. Navigate directly to course URL | User is redirected to the login page before course sections render | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-COURSE-009 | Hide Course Index sidebar | Course Index is open | 1. Click close button | Sidebar closes without affecting course content | Low |
| MS-COURSE-010 | Rapid section toggles | Section `Week 1` is visible | 1. Expand/collapse `Week 1` three times | `Week 1` ends in the final clicked state and each activity row appears once | Medium |
| MS-COURSE-011 | Collapse all when course has zero sections — no error | Course page for a course with no sections is open | 1. Click "Collapse all" when no sections exist | No error message or JavaScript alert appears; the page remains stable and the course page is still rendered | Low |
| MS-COURSE-012 | Collapse all when some sections already collapsed — all end collapsed | `QA Automation 101` course page shows a mix of expanded and collapsed sections | 1. Click "Collapse all" | All sections are collapsed regardless of their prior state; no section headers show expanded content | Medium |
| MS-COURSE-013 | Rapid single-section toggle ends in final clicked state | Section `Week 1` is visible | 1. Click the `Week 1` toggle arrow rapidly three times in quick succession | `Week 1` ends in the state corresponding to the final click (expanded or collapsed); no intermediate state is permanently locked | Medium |
| MS-COURSE-014 | Collapse all after adding then removing all sections succeeds silently | Course page is open; all sections were added then removed so the course has zero sections | 1. Click "Collapse all" | Collapse all completes silently; no error is displayed and the empty course page remains rendered | Low |

---

## 5. Participants

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-PART-001 | Participants table displayed | Student opens Participants tab | 1. Open Participants | Filters, alphabetical filters, and participant table are visible | High |
| MS-PART-002 | Filter participants by teacher name | Participants include `teacher1` | 1. Add a First name filter for the seeded teacher<br>2. Apply filters | Participants table shows `teacher1` and hides unrelated participant rows | High |
| MS-PART-003 | Alphabetical filters | Participants exist | 1. Select first-name or last-name initial | Table filters by selected initial | Medium |
| MS-PART-004 | Open participant profile | Participant row exists | 1. Click participant name | Participant profile page opens | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-PART-005 | Student cannot enrol users | Student is on Participants page | 1. Inspect page toolbar | Enrol users button, role dropdown, and enrollment duration controls are not rendered | High |
| MS-PART-006 | Student cannot edit/remove roles | Student is on Participants page | 1. Inspect row menus<br>2. Navigate directly to a role-management URL | Role edit and remove actions are not rendered; direct role-management URL shows access denied before any role form renders | High |
| MS-PART-007 | Participants blocked while unauthenticated | User is logged out | 1. Navigate directly to Participants URL | User is redirected to the login page before the participants table renders | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-PART-008 | Filter no matching users | Participants page is visible | 1. Apply filter with no matches | Empty/no-results state is displayed | Medium |
| MS-PART-009 | Multiple filter conditions | Participants include `student1` and `teacher1` | 1. Add a Role filter for Teacher<br>2. Add a name filter for `teacher1`<br>3. Apply filters | Table shows `teacher1`; `student1` and non-matching users are absent from the filtered table | Medium |
| MS-PART-010 | Apply filters with empty condition row — participants list updates without error | Participants page is visible with the filter panel open | 1. Add a filter condition row but leave its value empty<br>2. Click "Apply filters" | Participants list updates or shows all participants without a JavaScript error; no page crash occurs | Low |
| MS-PART-011 | Rapid First Name initial changes resolve to final selection only | Participants page is visible | 1. Click alphabetical initial "A"<br>2. Immediately click initial "B"<br>3. Immediately click initial "C" | Table reflects the last-clicked initial ("C") only; no stale intermediate filter result is permanently shown | Medium |
| MS-PART-012 | Row checkbox selection persists after navigating to participant profile and pressing Back | Participants page is visible; at least two participant rows exist | 1. Check the checkbox for `student1` row<br>2. Click `student1` name to open profile<br>3. Press browser Back | Participants page reloads; the previously checked row checkbox for `student1` is no longer checked (fresh page state) and no JavaScript error appears | Low |
| MS-PART-013 | Student role enrollment management features not visible or interactive | `student1` is on the Participants page | 1. Inspect each participant row for role-edit controls<br>2. Inspect the toolbar for enrollment management buttons | Role-edit icons, "Enrol users" button, and enrollment duration controls are not rendered for any row | High |

---

## 6. Grades

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-GRADE-001 | Student User report displayed | Student opens Grades | 1. Open Grades page | Grade item, calculated weight, grade, range, percentage, feedback, and contribution columns are visible | High |
| MS-GRADE-002 | Expand course group | Grades contain `QA Automation 101` course group with activities | 1. Collapse `QA Automation 101` group<br>2. Expand it again | Child grade items are hidden after collapse and visible again after expand | Medium |
| MS-GRADE-003 | Course total row displayed | Student has grade items | 1. Scroll to total row | AGGREGATION Course total displays cumulative grade | High |
| MS-GRADE-004 | Ungraded item displays placeholder | An activity is not graded | 1. Inspect ungraded row | Grade column shows `-` and no numeric grade is displayed for that item | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-GRADE-005 | Student cannot access full gradebook | Student is logged in | 1. Navigate directly to Grader report/full gradebook URL | Access denied page is shown before grader report rows render; other students' names and grades are not visible | High |
| MS-GRADE-006 | Grades blocked while unauthenticated | User is logged out | 1. Navigate directly to Grades URL | User is redirected to login | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-GRADE-007 | No graded activities yet | Student has no graded activities | 1. Open Grades | User report opens with empty grade placeholders for activity rows and no other students' grades | Low |
| MS-GRADE-008 | Decimal percentage display | Grade item has decimal percentage | 1. Inspect percentage column | Decimal precision is displayed consistently | Low |
| MS-GRADE-009 | Rapid consecutive course-group toggle ends in stable expanded/collapsed state | `student1` is on the Grades page; `QA Automation 101` course group is visible | 1. Click the course-group collapse control three times in rapid succession | Course group ends in the state corresponding to the final click; no intermediate state is locked and no JavaScript error appears | Medium |
| MS-GRADE-010 | Keyboard Space/Enter activates course-group collapse control | `student1` is on the Grades page; `QA Automation 101` course-group row is focused | 1. Tab to the course-group collapse control<br>2. Press Space or Enter | Course group expands or collapses in response to the keypress; the same toggle behavior as a mouse click is produced | Medium |
| MS-GRADE-011 | Long feedback text (200+ chars) truncated in cell; full text accessible on hover | Teacher has entered 200+ character feedback for `Essay Draft` | 1. Open Grades page<br>2. Locate the Feedback cell for `Essay Draft`<br>3. Hover over the cell | Feedback cell displays truncated text within the column width; full feedback text is accessible via tooltip or hover reveal | Low |
| MS-GRADE-012 | Unicode/emoji in Feedback column renders correctly without garbled display | Teacher has entered feedback containing Unicode and emoji for `Essay Draft` | 1. Open Grades page<br>2. Locate the Feedback cell for `Essay Draft` | Feedback cell renders Unicode characters and emoji as intended; no garbled or replacement characters are displayed | Low |
| MS-GRADE-013 | Whitespace-only feedback displays as empty placeholder not as visible whitespace | Teacher has entered whitespace-only feedback for a grade item | 1. Open Grades page<br>2. Inspect the Feedback cell for the whitespace-feedback item | Feedback cell shows the empty-placeholder indicator (dash or blank); no visible whitespace block occupies the cell | Low |

---

## 7. Assignment

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-ASGN-001 | Assignment details displayed | Assignment is available | 1. Open assignment page | Opened date, due date, description, and submission status are visible | High |
| MS-ASGN-002 | Submit online text | `Essay Draft` accepts online text and is open for submissions | 1. Click "Add submission"<br>2. Enter `My essay draft text` in the online text editor<br>3. Click "Save changes"<br>4. Reopen the assignment page | Submission status shows Submitted for grading and `My essay draft text` is visible in the submission preview | High |
| MS-ASGN-003 | Submit file upload | `Essay Draft` accepts file submissions and is open for submissions | 1. Click "Add submission"<br>2. Upload `essay-draft.pdf` within the allowed size/type<br>3. Save/submit the submission<br>4. Reopen the assignment page | Submission status includes `essay-draft.pdf` as a downloadable file link | High |
| MS-ASGN-004 | Edit submission before deadline | Editable submission exists before due date | 1. Click "Edit submission"<br>2. Replace text with `Updated essay draft text`<br>3. Save changes<br>4. Reopen the assignment page | Updated text is shown and the previous text is no longer the active submission content | Medium |
| MS-ASGN-005 | Remove submission when allowed | Removable submission exists before due date | 1. Click "Remove submission"<br>2. Confirm removal<br>3. Reopen the assignment page | Submission file/text is removed and submission status returns to not submitted or draft-empty state | Medium |
| MS-ASGN-006 | View grade and feedback | Teacher has graded submission | 1. Open assignment page | Earned grade and teacher feedback are visible | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-ASGN-007 | Required online text missing | Assignment requires online text | 1. Add submission<br>2. Leave online text empty<br>3. Submit | Submission is blocked with validation feedback | High |
| MS-ASGN-008 | Required file missing | Assignment requires file upload | 1. Add submission<br>2. Do not attach file<br>3. Submit | Submission is blocked with validation feedback | High |
| MS-ASGN-009 | Late submission blocked when closed | Due/cut-off date has passed and late submissions are disabled | 1. Open assignment<br>2. Inspect submission controls<br>3. Navigate directly to the submission edit URL | Add/Edit submission controls are not rendered and direct submission edit URL shows the assignment-closed message before an editor appears | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-ASGN-010 | File at allowed upload limit | Assignment accepts files with 10 MB maximum upload size | 1. Upload `essay-limit-10mb.pdf`<br>2. Click "Save changes"<br>3. Reopen assignment page | `essay-limit-10mb.pdf` appears in the submission file list after reopening the assignment page | Low |
| MS-ASGN-011 | Long online text submission | Assignment accepts online text | 1. Enter boundary text starting `GT-LONG-TEXT-START` and ending `GT-LONG-TEXT-END`<br>2. Click "Save changes"<br>3. Reopen assignment page | Submission preview contains both `GT-LONG-TEXT-START` and `GT-LONG-TEXT-END`, proving the saved text kept its beginning and ending sentinels | Low |
| MS-ASGN-012 | Resubmit after grading not allowed | Assignment is graded and resubmission disabled | 1. Open assignment page | Edit/resubmit controls are absent or disabled | Medium |
| MS-ASGN-013 | Submit when no input areas are enabled still succeeds | `Essay Draft` is configured with no online text and no file submission enabled | 1. Open the assignment page<br>2. Click "Add submission"<br>3. Click "Save changes" without entering any content | Submission status changes to Submitted for grading; no validation error is raised for an empty submission when no input types are enabled | Medium |
| MS-ASGN-014 | Edit submission allowed when due date is exactly today and teacher permits resubmission | `Essay Draft` due date is set to today; teacher has enabled resubmission | 1. Open assignment page<br>2. Click "Edit submission" | Edit submission form opens without a late-submission or access-denied message | Medium |
| MS-ASGN-015 | Edit submission blocked when due date passed by one day even if teacher permits resubmission | `Essay Draft` due date was yesterday; teacher has enabled resubmission but late submissions are disabled | 1. Open assignment page<br>2. Inspect submission controls | Edit/resubmit controls are absent or show an assignment-closed message; submission form does not render | High |
| MS-ASGN-016 | Online text with leading/trailing whitespace is trimmed on save | `Essay Draft` is open for online text submission | 1. Click "Add submission"<br>2. Enter `   Trimmed essay text   ` (with leading and trailing spaces) in the online text editor<br>3. Click "Save changes"<br>4. Reopen the assignment page | Submission preview shows `Trimmed essay text` without the surrounding whitespace | Low |
| MS-ASGN-017 | File with special-character/emoji filename uploads and filename is preserved | `Essay Draft` accepts file submissions | 1. Click "Add submission"<br>2. Upload a file whose name contains special characters and emoji (e.g., `essay_🎓_draft.pdf`)<br>3. Click "Save changes"<br>4. Reopen the assignment page | The file appears in the submission file list with its original filename preserved including the special characters and emoji | Low |
| MS-ASGN-018 | Rapid re-submission via browser Back does not create duplicate submission | `student1` has just saved an `Essay Draft` submission | 1. Immediately after saving, press browser Back<br>2. Resubmit the form if prompted<br>3. Reopen the assignment page | Only one submission record exists for `student1`; no duplicate submission entry or duplicate file appears | Medium |

---

## 8. Activities

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-ACT-001 | Activities overview displayed | Course has activities | 1. Open Activities tab | Activities are grouped by type; Assignments section is expanded by default | High |
| MS-ACT-002 | Assignment activity table | Assignments exist | 1. Inspect Assignments section | Name, due date, and submission status columns are visible | High |
| MS-ACT-003 | Expand collapsed activity type | Forums or Resources section is collapsed | 1. Click section arrow | Section expands and displays activities | Medium |
| MS-ACT-004 | Open activity from overview | Activity row exists | 1. Click activity name | Activity page opens | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-ACT-005 | Activities blocked while unauthenticated | User is logged out | 1. Navigate directly to Activities URL | User is redirected to the login page before activity groups render | High |
| MS-ACT-006 | Hidden activity not exposed | Teacher has hidden `Essay Draft` in `QA Automation 101` | 1. Open Activities page as `student1`<br>2. Search or browse activity groups for `Essay Draft`<br>3. Try the direct `Essay Draft` URL | `Essay Draft` is absent from Activities page and the direct URL shows an access restriction page without rendering assignment content | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-ACT-007 | Course with no activities | Course has no activities | 1. Open Activities tab | Activities page shows an empty-state message and no activity-group table is rendered | Low |
| MS-ACT-008 | Many activity types | Course has Assignments, Forums, Resources, and one additional activity group | 1. Open Activities tab<br>2. Expand Forums<br>3. Expand Resources<br>4. Collapse Forums | Resources remains expanded while Forums collapses, proving activity groups toggle independently | Low |
| MS-ACT-009 | Rapid double-click on assignment name causes only one navigation | Activities tab is open; at least one assignment row is visible | 1. Double-click the assignment name link rapidly | Browser navigates to the assignment page exactly once; no duplicate page-load or error page appears | Medium |
| MS-ACT-010 | Expand collapsed Forums section then immediately click first activity — succeeds | Activities tab is open; Forums section is collapsed | 1. Click the Forums section arrow to expand it<br>2. Immediately click the first forum activity name | Forums section expands and the forum activity page opens successfully; no stale-state error appears | Medium |
| MS-ACT-011 | Activity name with 200+ chars and special characters is displayed and clickable | An activity with a 200+ character name containing special characters exists in `QA Automation 101` | 1. Open Activities tab<br>2. Locate the long-name activity row<br>3. Click the activity name | Activity name is displayed (possibly truncated) without overflow breaking the table layout; clicking the name opens the activity page | Low |
| MS-ACT-012 | Rapidly toggling multiple collapsible sections each ends in its final state | Activities tab shows Assignments, Forums, and Resources sections | 1. Rapidly click the toggle for Assignments, then Forums, then Resources in quick succession | Each section ends in the state corresponding to its own last click; no section is permanently stuck in a transitional state | Medium |
| MS-ACT-013 | Cannot click activity name in collapsed additional activity type section | Activities tab is open; at least one additional activity type section is collapsed | 1. Locate a collapsed activity section<br>2. Attempt to click an activity name inside that collapsed section | Activity names inside the collapsed section are not visible or not clickable; no navigation occurs until the section is expanded | Medium |

---

## 9. Profile

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-PROFILE-001 | Student profile details displayed | Student is logged in | 1. Open Profile | Initials icon, full name, message button, and optional description are visible | High |
| MS-PROFILE-002 | Profile information cards displayed | Profile page is open | 1. Inspect information cards | User details, privacy/policies, course details, miscellaneous, reports, and login activity are visible | High |
| MS-PROFILE-003 | Edit profile form opens | Profile page is open | 1. Click "Edit profile" | Edit profile form opens | High |
| MS-PROFILE-004 | Update own profile | Edit profile form is open for `student1` | 1. Edit City/town to `Dhaka QA` and Description to `Student profile update check`<br>2. Click "Update profile"<br>3. Reopen Profile | City/town and description updates are visible on `student1` profile | High |
| MS-PROFILE-005 | Upload own profile picture | Edit profile form is open | 1. Upload `student-avatar.png` under 10 MB<br>2. Click "Update profile"<br>3. Reopen Profile | Student profile picture changes from initials to the uploaded image preview | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-PROFILE-006 | Profile blocked while unauthenticated | User is logged out | 1. Navigate directly to profile URL | User is redirected to login | High |
| MS-PROFILE-007 | Student cannot edit another user's profile | Student opens another user's profile | 1. Inspect profile controls<br>2. Navigate directly to that user's edit-profile URL | Edit controls are not rendered and direct edit URL shows access denied before the edit form renders | High |
| MS-PROFILE-008 | Required profile field empty | Edit profile form is open | 1. Clear First name, Last name, or Email<br>2. Save | Required-field validation blocks save | High |
| MS-PROFILE-009 | Invalid profile email | Edit profile form is open | 1. Enter invalid email<br>2. Save | Email validation blocks save | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-PROFILE-010 | Cancel edit profile | Edit profile form has unsaved changes | 1. Click "Cancel" | Unsaved changes are discarded | Medium |
| MS-PROFILE-011 | Missing optional description | Student profile has no description | 1. Open Profile | Profile page renders initials, full name, and information cards; description area is empty and no placeholder error is shown | Low |
| MS-PROFILE-012 | Very long Description field (200+ chars) accepted or blocked with visible feedback | Edit profile form is open for `student1` | 1. Enter a 200+ character string in the Description field<br>2. Click "Update profile" | Either the description is saved and visible on the profile page, or a clear validation message explains the length limit; no silent data loss or crash occurs | Low |
| MS-PROFILE-013 | Non-Latin Unicode and emoji in First/Last name fields accepted or blocked with visible feedback | Edit profile form is open for `student1` | 1. Enter `জন 🎓` in the First name field and `ডো 🎓` in the Last name field<br>2. Click "Update profile" | Either the names are saved and rendered correctly on the profile page, or a clear validation message explains the character restriction; no garbled text or silent failure occurs | Low |
| MS-PROFILE-014 | Rapid re-submit of Update profile does not create duplicate profile records | Edit profile form is open for `student1` with a change ready | 1. Click "Update profile" rapidly twice | Profile is saved once; no duplicate profile record is created and no duplicate success/error message is stacked | Medium |

---

## 10. Logout

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-LOGOUT-001 | Logout from user menu | Student is logged in | 1. Open user menu<br>2. Click "Log out" | Session ends and login page is displayed | High |
| MS-LOGOUT-002 | Protected page requires re-authentication after logout | Student has logged out | 1. Navigate directly to Dashboard, course, or assignment URL | User is redirected to login | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-LOGOUT-003 | Browser back after logout | Student logged out from protected page | 1. Press browser Back | Login page remains active or protected page immediately redirects to login; dashboard/course content is not rendered from browser cache | High |
| MS-LOGOUT-004 | Logout option unavailable while logged out | User is on login page | 1. Inspect user menu area | Authenticated user menu and logout option are absent | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MS-LOGOUT-005 | Double-click logout | Student is logged in | 1. Double-click "Log out" | Logout completes once without visible error | Low |
| MS-LOGOUT-006 | Session timeout behaves like logout | Student session has expired | 1. Open protected page | User is required to authenticate again | High |
| MS-LOGOUT-007 | Logout in Tab A blocks protected page reload in Tab B — redirect to login | `student1` is logged in on two browser tabs showing a protected page | 1. In Tab A, log out via the user menu<br>2. Switch to Tab B<br>3. Reload the protected page in Tab B | Tab B redirects to the login page; no authenticated content from the previous session is rendered | High |
| MS-LOGOUT-008 | Navigate directly to protected URL after logout redirects to login page | `student1` has just logged out | 1. Type the Dashboard URL directly into the address bar and press Enter | Browser is redirected to the login page; Dashboard content is not rendered | High |

---

## Test Summary

| Area | Count |
|------|-------|
| Modules covered | 10 |
| Ground-truth test cases | 136 |
| Primary role | Student |
| Source functional description | dataset/raw_specifications/Moodle/MoodleStudent.md |
