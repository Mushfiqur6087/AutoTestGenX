# Moodle Teacher Test Cases

**Website URL:** http://localhost:8080
**Test Suite Version:** 2.1 (Moodle gold oracle)
**Role Scope:** Teacher/instructor workflows only

---

## Table of Contents
1. [Login](#1-login)
2. [Dashboard](#2-dashboard)
3. [Dashboard Edit Mode](#3-dashboard-edit-mode)
4. [My Courses](#4-my-courses)
5. [Course Page](#5-course-page)
6. [Course Edit Mode and Activity Chooser](#6-course-edit-mode-and-activity-chooser)
7. [Assignment Creation](#7-assignment-creation)
8. [Course Settings](#8-course-settings)
9. [Participants Management](#9-participants-management)
10. [Assignment Teacher View](#10-assignment-teacher-view)
11. [Assignment Submissions](#11-assignment-submissions)
12. [Gradebook Grader Report](#12-gradebook-grader-report)
13. [Profile](#13-profile)
14. [Profile Edit](#14-profile-edit)
15. [Logout](#15-logout)

---

## Test Credentials

| Field | Value |
|-------|-------|
| Teacher account | `teacher1`, seeded teacher enrolled in the test course |
| Student account | `student1`, seeded student enrolled in the same test course |
| Test course | `QA Automation 101`, editable by `teacher1` |
| Reference assignment | `Essay Draft`, online text and file submission enabled |
| Reference block | `Latest announcements`, available in Add a block |
| Boundary grade range | 0 to 100 points for `Essay Draft` |
| Boundary upload limit | 10 MB maximum upload size for assignment/profile upload checks |
| Boundary files | `essay-draft.pdf` under 1 MB, `essay-limit-10mb.pdf` exactly at limit, `oversize-11mb.pdf` over limit |

## Moodle Gold Oracle Contract

| Rule | Requirement |
|------|-------------|
| Source anchoring | Every module below maps to `dataset/raw_specifications/Moodle/MoodleTeacher.md`; inferred Moodle behavior is allowed only when the expected result names observable UI evidence. |
| Atomicity | Each test case should verify one user-facing workflow or permission boundary. Compound setup is allowed only when the assertion remains single-purpose. |
| Observable result | Expected results must name visible UI state, persisted data, redirect, access denial, validation feedback, or absence of privileged controls. |
| Deterministic oracle | Avoid generic success words, conditional applicability, ambiguous alternatives, and implementation-variable outcomes. A reviewer should be able to mark pass/fail without guessing. |
| Fixture stability | Use seeded teacher, student, course, assignment, file, grade, and block fixtures rather than unspecified users or courses. |
| Persistence check | Creation, update, grading, and layout tests should verify state after save and refresh when practical. |
| Role boundary | Teacher-only controls should be checked against a student account where the permission is important. |
| Data cleanup | Tests that mutate data must restore the named fixture or create disposable records with the `Ground Truth` suffix for cleanup. |

## Quality and Traceability Rules

| Rule | Requirement |
|------|-------------|
| `MT-NAV` | Shared navigation, user menu, breadcrumbs, course tabs, Course Index, notifications, and messaging. |
| `MT-LOGIN` | Authentication form, guest entry, cookies notice, and login validation. |
| `MT-DASH` | Teacher Dashboard timeline, calendar, filtering, and empty states. |
| `MT-DEDIT` | Teacher dashboard edit mode, block addition/configuration, reset, and read-only state outside edit mode. |
| `MT-COURSES` | My Courses filtering, searching, sorting, layout, starring, and hidden-course behavior. |
| `MT-COURSE` | Course page content, tabs, section collapse, Course Index navigation, and restricted activity visibility. |
| `MT-CEDIT` | Course authoring controls, Activity Chooser, section/activity editing, and student visibility boundaries. |
| `MT-ACREATE` | Assignment creation form, required fields, availability, submission/feedback settings, grading, and upload constraints. |
| `MT-CSET` | Course Settings required fields, visibility, dates, format, completion, groups, tags, and validation. |
| `MT-PART` | Participants filters, enrollment dialog, row actions, bulk selection, and unauthorized access protection. |
| `MT-ATVIEW` | Teacher assignment page metadata, grading summary, Grade entry, tabs, and zero-submission state. |
| `MT-ASUB` | Assignment submissions table, filters, row grading, quick grading, files, invalid grades, and late submissions. |
| `MT-GRADE` | Grader report, report switching, user search/filter, grade editing, and student access denial. |
| `MT-PROFILE` | Teacher profile display, information cards, course profile links, edit entry, and private-field restrictions. |
| `MT-PEDIT` | Teacher profile edit form, required fields, picture upload, optional metadata, and cancel behavior. |
| `MT-LOGOUT` | Logout, protected-route reauthentication, browser-back protection, and timeout behavior. |

---

## 1. Login

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-LOGIN-001 | Valid teacher login | `teacher1` account exists and is active | 1. Navigate to the Moodle login page<br>2. Enter `teacher1` username<br>3. Enter the teacher password<br>4. Click "Log in" | Teacher is redirected to Dashboard and the user menu shows the teacher initials/name | High |
| MT-LOGIN-002 | Guest access from login page | Guest access is enabled | 1. Open login page<br>2. Click "Access as a guest" | Guest browsing opens without authenticating as teacher | Medium |
| MT-LOGIN-003 | Cookie notice opens | Login page is visible | 1. Click "Cookies notice" | Cookie usage information is displayed without clearing login fields | Low |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-LOGIN-004 | Invalid teacher credentials | Login page is visible | 1. Enter `teacher1` username<br>2. Enter `WrongPass#2026`<br>3. Click "Log in" | Login error is shown, password is cleared, username remains populated, and Dashboard is not opened | High |
| MT-LOGIN-005 | Empty username | Login page is visible | 1. Leave Username empty<br>2. Enter the teacher password<br>3. Click "Log in" | Login is rejected, username field is identified as missing, and no authenticated page is opened | High |
| MT-LOGIN-006 | Empty password | Login page is visible | 1. Enter `teacher1` username<br>2. Leave Password empty<br>3. Click "Log in" | Login is rejected, password field is identified as missing, and no authenticated page is opened | High |
| MT-LOGIN-007 | Disabled lost-password link | Lost-password feature is disabled | 1. Click "Lost password?" | Recovery flow does not open and user remains on the login page | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-LOGIN-008 | Failed login retains username | Login page is visible | 1. Enter invalid username and password<br>2. Submit login | Username remains populated and password is cleared | Medium |
| MT-LOGIN-009 | Rapid double login click | Login page is visible | 1. Enter invalid credentials<br>2. Double-click "Log in" | One login error message is visible, password is cleared once, username remains populated, and the form controls remain enabled | Medium |
| MT-LOGIN-010 | Both fields empty shows simultaneous validation | Login page is visible | 1. Leave Username and Password both empty<br>2. Click "Log in" | Both username and password fields are flagged with validation errors simultaneously; no authenticated page opens | High |
| MT-LOGIN-011 | Username with leading/trailing whitespace retained after failed login | Login page is visible | 1. Enter `  teacher1  ` (with spaces) as the username<br>2. Enter `WrongPass#2026`<br>3. Click "Log in" | Login is rejected with error; username field retains the entered string including the surrounding whitespace | Low |
| MT-LOGIN-012 | Very long username rejected without crash | Login page is visible | 1. Enter a 200+ character username and an invalid password<br>2. Click "Log in" | Login error is shown, the long username remains populated without breaking the page layout, and password is cleared | Low |

---

## 2. Dashboard

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-DASH-001 | Personalized dashboard greeting | Teacher is logged in | 1. Open Dashboard | Greeting for the logged-in teacher is displayed | High |
| MT-DASH-002 | Timeline block displays teaching actions | `Essay Draft` has a due date within the selected timeline range | 1. Log in as `teacher1`<br>2. Open Dashboard<br>3. Inspect Timeline block | Timeline lists `Essay Draft` with its course name and due date; no unrelated course item appears when the course filter is active | High |
| MT-DASH-003 | Timeline filtering and search | Timeline contains `Essay Draft` and at least one non-matching activity | 1. Select a range containing `Essay Draft`<br>2. Sort by date<br>3. Search for `Essay` | Timeline shows `Essay Draft`, hides non-matching activities, and preserves the selected range/sort controls | High |
| MT-DASH-004 | Calendar block navigation | Calendar block is visible and has at least one event for `QA Automation 101` | 1. Select `QA Automation 101` in the course filter<br>2. Record the month heading<br>3. Click previous month<br>4. Click next month | Month heading changes on navigation, returns to the original month after the second click, and only selected-course events are shown | High |
| MT-DASH-005 | Calendar links open destination pages | Calendar block is visible | 1. Click "Full calendar"<br>2. Return<br>3. Click "Import or export calendars" | Full calendar and calendar data management pages open | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-DASH-006 | Dashboard blocked while unauthenticated | User is logged out | 1. Navigate directly to Dashboard URL | User is redirected to login and dashboard blocks are not exposed | High |
| MT-DASH-007 | Timeline search with no matches | Teacher is logged in | 1. Search for `zz-no-teaching-item` in the Timeline block | Timeline shows the no-results state, keeps the search term in the field, and leaves range/sort controls enabled | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-DASH-008 | Calendar year boundary | Calendar displays January | 1. Click previous-month arrow | Calendar shows December of the previous year | Medium |
| MT-DASH-009 | Very long timeline search | Timeline block is visible | 1. Enter a 200+ character search term ending in `Essay` | Search field retains the full entered term, Timeline displays the no-results state, and the Calendar block remains visible beside it | Low |
| MT-DASH-010 | Timeline empty state when selected range has zero activities | `teacher1` is on Dashboard; a date range with no activities is known | 1. Select the date range that contains no scheduled activities | Timeline block displays its empty-state message and no activity rows are rendered | Low |
| MT-DASH-011 | Timeline search with special characters and emoji accepted | `teacher1` is on Dashboard | 1. Type `@@##🎓` into the Timeline search field | Search field accepts the input without error; timeline shows empty-results state or matching items; no crash or validation dialog appears | Low |
| MT-DASH-012 | Navigate calendar to previous month removes current-date highlight | Calendar block is visible and shows the current month | 1. Click the previous-month arrow on the Calendar block | Calendar advances to the previous month; the current-date highlight is absent on the previous month view | Low |
| MT-DASH-013 | Rapid toggle of Timeline sort by date/courses | Timeline block is visible | 1. Toggle sorting rapidly between Sort by dates and Sort by courses | Timeline block ends in the sorting state corresponding to the final click; no intermediate or broken state is locked | Medium |

---

## 3. Dashboard Edit Mode

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-DEDIT-001 | Enable dashboard edit mode | Teacher is on Dashboard | 1. Toggle Edit mode on | Reset button, Add a block button, block move icons, and block menus are visible | High |
| MT-DEDIT-002 | Add a dashboard block | Edit mode is on and `Latest announcements` block is not already present | 1. Click "+ Add a block"<br>2. Select `Latest announcements` | `Latest announcements` block appears on the teacher Dashboard and remains visible after page refresh | High |
| MT-DEDIT-003 | Configure a dashboard block | Edit mode is on and `Latest announcements` block is visible | 1. Open the block menu<br>2. Select configure<br>3. Change a non-destructive block setting<br>4. Save and refresh Dashboard | Updated block configuration is preserved for `teacher1` and does not change the student's dashboard | Medium |
| MT-DEDIT-004 | Reset dashboard to default | Edit mode is on and layout was customized | 1. Click "Reset page to default" | Dashboard returns to default block arrangement | High |
| MT-DEDIT-010 | Move a block via drag and drop | Edit mode is on and Dashboard contains at least two blocks | 1. Click and hold the Move icon for a block<br>2. Drag the block to a new position in the layout<br>3. Release to drop the block | The block is moved to the new position and the layout persists for the teacher | High |
| MT-DEDIT-011 | Move a block via the block options menu | Edit mode is on and Dashboard contains at least two blocks | 1. Open the block menu for a block<br>2. Select the Move action | The block is moved to the selected position and the layout persists for the teacher | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-DEDIT-005 | Add block unavailable outside edit mode | Edit mode is off | 1. Inspect dashboard controls | "+ Add a block" is not rendered and no add-block URL is exposed from the Dashboard controls | High |
| MT-DEDIT-006 | Block menu unavailable outside edit mode | Edit mode is off | 1. Inspect existing dashboard blocks | Configure, move, and delete options are not rendered on dashboard blocks | High |
| MT-DEDIT-007 | Cancel add-block flow | Add-block page is open | 1. Click "Cancel" | No block is added and teacher returns to Dashboard | Medium |
| MT-DEDIT-012 | Add block blocked when block type is not selected | Edit mode is on and Add a block page is open | 1. Leave the Block Type dropdown empty<br>2. Click to submit or add | Submission is blocked by required-field validation and no block is added | High |
| MT-DEDIT-013 | Move handle is hidden when edit mode is off | Edit mode is off and Dashboard contains blocks | 1. Inspect existing blocks on the Dashboard | Move handles (drag icons) are absent and blocks cannot be dragged | High |
| MT-DEDIT-014 | Reset dashboard button hidden when edit mode is off | Edit mode is off | 1. Inspect Dashboard controls | "Reset page to default" button is absent | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-DEDIT-008 | Rapid edit-mode toggle | Dashboard is visible | 1. Toggle Edit mode on and off several times quickly | Final UI state matches the final toggle state | Medium |
| MT-DEDIT-009 | Delete all optional blocks | Edit mode is on and blocks exist | 1. Delete available optional blocks<br>2. Reload Dashboard | Layout persists without duplicate or ghost blocks | Medium |
| MT-DEDIT-015 | Toggle edit mode off closes Add block page | Add a block page is open in Edit mode | 1. Click the Edit mode toggle to turn it off | Add a block page closes, teacher is returned to the standard Dashboard, and no block is added | Medium |
| MT-DEDIT-016 | Reset to default immediately after adding a block | Edit mode is on and layout was customized | 1. Add a new block<br>2. Immediately click "Reset page to default" | Dashboard reverts to the default block arrangement and the newly added block is removed if it was not part of the default layout | Medium |
| MT-DEDIT-017 | Rapid Add block double-click | Edit mode is on | 1. Click "+ Add a block" rapidly twice | Add a block page opens only once; no duplicate modal or error state occurs | Low |

---

## 4. My Courses

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-COURSES-001 | Course cards displayed | Teacher is enrolled in courses | 1. Open My Courses | Course cards show image, course name, and category | High |
| MT-COURSES-002 | Filter, search, sort, and layout controls | `teacher1` has access to `QA Automation 101` and at least one other course | 1. Select All status filter<br>2. Search for `QA Automation`<br>3. Sort by course name<br>4. Switch to list layout | Only matching courses remain visible, order follows the sort selection, and list layout persists after refresh | High |
| MT-COURSES-003 | Open course from course card | At least one course is visible | 1. Click a course name | Teacher opens the course main page | High |
| MT-COURSES-004 | Star course from course card | `QA Automation 101` course card menu is visible | 1. Open card menu<br>2. Click "Star this course"<br>3. Refresh My Courses | `QA Automation 101` appears in the Starred filter and teacher enrollment remains unchanged | Medium |
| MT-COURSES-009 | Remove course from view without unenrolling | `QA Automation 101` course card menu is visible | 1. Open card menu<br>2. Click "Remove from view"<br>3. Select Hidden filter<br>4. Open the hidden course card | `QA Automation 101` appears under Hidden, opens successfully, and `teacher1` remains enrolled as teacher | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-COURSES-005 | My Courses blocked while unauthenticated | User is logged out | 1. Navigate directly to My Courses URL | User is redirected to login | High |
| MT-COURSES-006 | Search with no matching course | Teacher is logged in | 1. Search for a non-existent course | Empty/no-results state is shown | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-COURSES-007 | Hidden-course filter | `QA Automation 101` was removed from view | 1. Select Hidden filter<br>2. Search for `QA Automation` | `QA Automation 101` is listed in Hidden with its course name and category; non-hidden courses are absent from the filtered list | Medium |
| MT-COURSES-008 | Special-character search | Courses page is visible | 1. Search with `@@@` | No matching course cards are displayed, no validation error appears, and the search field remains editable | Low |
| MT-COURSES-010 | Very long search query (200+ chars) accepted without error | My Courses is visible | 1. Enter a 200+ character string into the course search field<br>2. Submit the search | Search field accepts and retains the long string; no error dialog appears; a matching or empty-results list is displayed | Low |
| MT-COURSES-011 | Search with leading and trailing whitespace is trimmed | My Courses is visible and `QA Automation 101` exists | 1. Search for `   QA Automation   ` (with spaces) | Course `QA Automation 101` is displayed successfully; whitespace is ignored for the search match | Low |

---

## 5. Course Page

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-COURSE-001 | Teacher course tabs displayed | `teacher1` is enrolled as teacher in `QA Automation 101` | 1. Open the `QA Automation 101` course page | Course, Settings, Participants, Grades, Activities, and Competencies tabs are visible; Settings is visible for the teacher | High |
| MT-COURSE-002 | Sections and activities displayed | Course contains sections | 1. Inspect course content | Sections, activity icons, and activity/resource names are visible | High |
| MT-COURSE-003 | Collapse all sections | Sections are expanded | 1. Click "Collapse all" | All visible sections collapse | Medium |
| MT-COURSE-004 | Course index navigation | Course index is visible | 1. Click a section or activity in Course Index | Page navigates to the selected content | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-COURSE-005 | Course page blocked while unauthenticated | User is logged out | 1. Navigate directly to the `QA Automation 101` course URL | User is redirected to the Moodle login page before course content is rendered | High |
| MT-COURSE-006 | Open hidden activity as teacher and student | `Essay Draft` is hidden from students in `QA Automation 101` | 1. Open the course as `teacher1` and inspect `Essay Draft`<br>2. Open the same activity URL as `student1` | `teacher1` sees `Essay Draft` with a hidden/restricted indicator; `student1` sees an access restriction page and no assignment submission form | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-COURSE-007 | Hide Course Index sidebar | Course Index is open | 1. Click Course Index close button | Sidebar is hidden, course heading remains visible, and the tab bar remains clickable | Low |
| MT-COURSE-008 | Rapid section toggles | Section `Week 1` is visible | 1. Expand/collapse `Week 1` three times | `Week 1` ends in the final clicked state and each activity row appears once | Medium |
| MT-COURSE-009 | Rapid double-click on activity link causes single navigation | Course page is visible and an activity link is present | 1. Double-click the activity name rapidly | Browser navigates to the activity page exactly once; no duplicate page-load or error page appears | Medium |

---

## 6. Course Edit Mode and Activity Chooser

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-CEDIT-001 | Enable course edit mode | Teacher is on course page | 1. Toggle edit mode on | Section, activity, bulk action, and add controls become visible | High |
| MT-CEDIT-002 | Rename a course section inline | Edit mode is on and section `Week 1` exists | 1. Click the section inline edit icon<br>2. Rename `Week 1` to `Week 1 - Orientation`<br>3. Save and refresh course page | The renamed section title persists after refresh and the old title is no longer shown | High |
| MT-CEDIT-003 | Hide an activity from students | Edit mode is on and `Essay Draft` is visible | 1. Open the `Essay Draft` activity menu<br>2. Select Hide<br>3. Open the course as `student1` | `Essay Draft` is hidden from the student view while remaining visible to `teacher1` with a hidden indicator | High |
| MT-CEDIT-004 | Bulk hide selected activities | Edit mode is on and at least two visible activities exist | 1. Select `Essay Draft` and one other activity<br>2. Use the bulk action toolbar to hide selected activities<br>3. Refresh course page | Only the selected activities are hidden; unselected activities remain visible | Medium |
| MT-CEDIT-005 | Open Activity Chooser | Edit mode is on | 1. Click "+ Add an activity or resource" | Activity Chooser modal opens with categories, search, and activity/resource tiles | High |
| MT-CEDIT-006 | Select Assignment from Activity Chooser | Activity Chooser is open | 1. Select Assignment<br>2. Click "Add" | Assignment creation form opens | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-CEDIT-007 | Edit controls hidden when edit mode is off | Teacher is on course page with edit mode off | 1. Inspect sections and activities | Authoring controls are hidden | High |
| MT-CEDIT-008 | Add action with no tile selected | Activity Chooser is open | 1. Click Add without selecting an activity/resource | No activity is created and user is prompted to select an item | Medium |
| MT-CEDIT-009 | Delete action requires confirmation | Edit mode is on | 1. Delete a section or activity<br>2. Cancel confirmation | Item remains unchanged | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-CEDIT-010 | Activity chooser search no results | Activity Chooser is open | 1. Search for non-existent activity type | Empty/no-results state is displayed | Low |
| MT-CEDIT-011 | Nested subsection creation | Edit mode is on in section `Week 1` | 1. Click "+ Add a subsection"<br>2. Name it `Ground Truth Subsection`<br>3. Save and refresh course page | `Ground Truth Subsection` appears nested under `Week 1` after refresh and can be removed during cleanup | Medium |
| MT-CEDIT-012 | Rename section inline with empty text | Edit mode is on | 1. Click inline edit for a section<br>2. Clear the text and press Enter | Section name reverts to its previous value or displays a required-field error; no unnamed section is created | High |
| MT-CEDIT-013 | Rename section inline with very long text | Edit mode is on | 1. Click inline edit for a section<br>2. Enter a 200+ character string and press Enter | Long text is saved and visible, wrapping correctly without breaking the page layout | Low |
| MT-CEDIT-014 | Drag and drop an activity to reorder | Edit mode is on and course has activities | 1. Click and hold the move handle for an activity<br>2. Drag it to a new position<br>3. Release | Activity appears in the new position and layout persists | High |
| MT-CEDIT-015 | Drag and drop a section to reorder | Edit mode is on and course has multiple sections | 1. Click and hold the move handle for a section<br>2. Drag it above another section<br>3. Release | Section appears in the new position with its contents intact and layout persists | High |
| MT-CEDIT-016 | Rapid consecutive clicks on hide/show activity toggle | Edit mode is on and an activity is visible | 1. Open activity action menu<br>2. Rapidly toggle Hide/Show multiple times | Activity ends in the visibility state corresponding to the final toggle action; no intermediate locked state | Medium |
| MT-CEDIT-017 | Duplicate an activity | Edit mode is on and `Essay Draft` exists | 1. Open action menu for `Essay Draft`<br>2. Select Duplicate | A copy of the activity appears with "copy" in the title; original activity remains unchanged | High |
| MT-CEDIT-018 | Delete section containing activities warns of cascading delete | Edit mode is on and section contains activities | 1. Open action menu for the section<br>2. Select Delete | A confirmation dialog explicitly warns that deleting the section will also delete its contained activities | High |
| MT-CEDIT-019 | Rapid double-click on Add activity button | Edit mode is on | 1. Rapidly double-click "+ Add an activity or resource" | Activity Chooser modal opens exactly once | Low |
| MT-CEDIT-020 | Activity chooser search with special characters | Activity Chooser is open | 1. Search for `@@##🎓` | Search field accepts input without error and displays the no-results state | Low |
| MT-CEDIT-021 | Bulk action bar clears selection when closed | Edit mode is on and bulk action bar is visible | 1. Select multiple activities<br>2. Click the 'X' to close the bulk action bar | Bulk action bar closes and all activity checkboxes are deselected | Medium |
| MT-CEDIT-022 | Edit settings action opens activity form | Edit mode is on and an activity exists | 1. Open action menu for the activity<br>2. Select Edit settings | Activity configuration form opens successfully | High |

---

## 7. Assignment Creation

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-ACREATE-001 | Create assignment and return to course | Teacher opens assignment creation form from `QA Automation 101` | 1. Enter assignment name `Essay Draft - Ground Truth`<br>2. Enter a short description<br>3. Enable online text and file submissions<br>4. Click "Save and return to course" | Assignment is created, course page opens, and `Essay Draft - Ground Truth` appears in the selected section after refresh | High |
| MT-ACREATE-002 | Create assignment and display it | Teacher opens assignment creation form from `QA Automation 101` | 1. Enter assignment name `Essay Draft Display Check`<br>2. Configure required fields<br>3. Click "Save and display" | Assignment page opens with the new assignment name, description, due date/status panel, and teacher tabs | High |
| MT-ACREATE-003 | Configure availability dates | Assignment form is open | 1. Enable submission/due/cut-off date controls<br>2. Set dates and times | Date settings are saved and visible after save | Medium |
| MT-ACREATE-004 | Configure submission and feedback types | Assignment form is open | 1. Enable online text and file submissions<br>2. Configure feedback comments/files/offline worksheet | Selected submission and feedback settings are saved | High |
| MT-ACREATE-005 | Configure grade and completion settings | Assignment form is open | 1. Set grade type to Point<br>2. Set maximum points to `100`<br>3. Enable activity completion tracking<br>4. Add tag `ground-truth`<br>5. Save and reopen settings | Grade type, maximum points, completion tracking, and `ground-truth` tag are persisted in the assignment settings | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-ACREATE-006 | Assignment name empty | Assignment form is open | 1. Leave Assignment name empty<br>2. Click save | Inline required-field validation is shown and assignment is not created | High |
| MT-ACREATE-007 | Oversized additional file | Assignment form is open | 1. Upload `oversize-11mb.pdf` to Additional files | Upload is blocked, file-size validation is displayed, and `oversize-11mb.pdf` is not listed in Additional files | Medium |
| MT-ACREATE-008 | Invalid accepted file type | File submissions are enabled | 1. Enter `not-an-extension` in accepted file types<br>2. Save | Save is blocked, the accepted file types field is marked invalid, and no assignment is created from the invalid configuration | Medium |
| MT-ACREATE-009 | Cancel discards assignment creation | Assignment form has unsaved changes | 1. Click "Cancel" | No assignment is created and teacher returns to previous page | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-ACREATE-010 | Disabled availability dates are not enforced | Assignment form is open | 1. Disable Allow submissions from, Due date, and Cut-off date toggles<br>2. Save and display assignment | Assignment page shows no enforced open, due, or cut-off date for the new assignment | Low |
| MT-ACREATE-011 | Maximum number of uploaded files | File submissions are enabled | 1. Select the highest value displayed in "Maximum number of uploaded files"<br>2. Save and reopen assignment settings | The same maximum-file count label remains selected after reopening settings | Low |
| MT-ACREATE-012 | Due date earlier than Allow submissions from date | Assignment form is open | 1. Set Due date to a time earlier than Allow submissions from date<br>2. Save | Save is blocked with an inline date-validation error | High |
| MT-ACREATE-013 | Cut-off date earlier than Due date | Assignment form is open | 1. Set Cut-off date to a time earlier than Due date<br>2. Save | Save is blocked with an inline date-validation error | High |
| MT-ACREATE-014 | Negative maximum points blocked | Assignment form is open with Point grading | 1. Set Maximum points to `-10`<br>2. Save | Save is blocked and a validation error requires points to be greater than 0 | High |
| MT-ACREATE-015 | Very long assignment description | Assignment form is open | 1. Enter a 10,000+ character description<br>2. Save and display | Assignment saves successfully and the full description is displayed on the assignment page | Low |
| MT-ACREATE-016 | Rapid double-click on Save and return to course | Assignment form is open and filled | 1. Rapidly double-click "Save and return to course" | Assignment is created exactly once and no duplicate entries appear on the course page | Medium |
| MT-ACREATE-017 | Disable all submission types | Assignment form is open | 1. Uncheck both Online text and File submissions<br>2. Save | Save is blocked with validation indicating at least one submission type must be enabled | High |
| MT-ACREATE-018 | Additional file with emoji filename | Assignment form is open | 1. Upload a file named `assignment_🎓_reqs.pdf`<br>2. Save and display | File uploads successfully and the emoji filename is preserved on the assignment page | Low |
| MT-ACREATE-019 | Maximum points boundary value | Assignment form is open with Point grading | 1. Set Maximum points to the highest allowed system value (e.g., 1000000)<br>2. Save and reopen settings | High point value is saved and displayed without causing a system overflow error | Low |

---

## 8. Course Settings

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-CSET-001 | Save required course settings | Teacher opens Course Settings | 1. Change full name to `QA Automation 101 - Ground Truth`<br>2. Keep short name and category populated<br>3. Click "Save and display" | Course page opens with heading `QA Automation 101 - Ground Truth`; the original course name is restored during cleanup | High |
| MT-CSET-002 | Configure visibility and date fields | Course Settings is open | 1. Set Course visibility to Hide<br>2. Enable start/end date fields<br>3. Set start before end<br>4. Save and reopen settings | Visibility is Hide and the saved start/end date values are still populated after reopening settings | Medium |
| MT-CSET-003 | Configure course summary and image | Course Settings is open | 1. Set summary to `Ground truth course summary`<br>2. Upload `course-banner-ground-truth.png`<br>3. Save and reopen settings | Summary text and uploaded image filename are visible after reopening Course Settings | Medium |
| MT-CSET-004 | Configure format, completion, groups, and tags | Course Settings is open | 1. Set format to Topics format<br>2. Enable completion tracking<br>3. Set group mode to Separate groups<br>4. Add tag `ground-truth`<br>5. Save and reopen settings | Topics format, completion tracking, Separate groups, and tag `ground-truth` remain selected after reopening settings | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-CSET-005 | Course full name empty | Course Settings is open | 1. Clear Course full name<br>2. Save | Required-field validation blocks save | High |
| MT-CSET-006 | Course short name empty | Course Settings is open | 1. Clear Course short name<br>2. Save | Required-field validation blocks save | High |
| MT-CSET-007 | Course category empty | Course Settings is open | 1. Remove or leave category empty<br>2. Save | Required-field validation blocks save | High |
| MT-CSET-008 | Cancel leaves settings unchanged | Course Settings has unsaved edits | 1. Click "Cancel" | Unsaved changes are discarded | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-CSET-009 | End date earlier than start date | Course Settings is open | 1. Enable end date<br>2. Set end date before course start date<br>3. Save | Save is blocked with a date-range validation message and the previous course dates remain unchanged | Medium |
| MT-CSET-010 | Maximum upload size option | Course Settings is open | 1. Select `10 MB` in Maximum upload size<br>2. Save and reopen settings | Maximum upload size remains `10 MB` after reopening Course Settings | Low |
| MT-CSET-011 | Course end date exactly equals start date | Course Settings is open | 1. Enable end date<br>2. Set end date to the exact same day/time as start date<br>3. Save and display | Form saves successfully and the course dates are updated | Medium |
| MT-CSET-012 | Course end date one day before start date | Course Settings is open | 1. Enable end date<br>2. Set end date to exactly one day before start date<br>3. Save | Save is blocked by date-range validation and settings are not updated | Medium |
| MT-CSET-013 | Very long Course Full Name (200+ chars) | Course Settings is open | 1. Enter a 200+ character string in Course full name<br>2. Save | Name is saved and visible, possibly truncated at system limit, but does not crash the page | Low |
| MT-CSET-014 | Special characters and emoji in Course Short Name | Course Settings is open | 1. Enter a short name containing emoji and special characters<br>2. Save and reopen settings | Form saves successfully and the exact emoji/characters are preserved | Low |
| MT-CSET-015 | Leading/trailing whitespace in Course Short Name trimmed | Course Settings is open | 1. Enter a short name with leading and trailing spaces<br>2. Save and reopen settings | Whitespace is automatically trimmed from the saved short name | Low |
| MT-CSET-016 | Non-numeric value in Appearance News Items | Course Settings is open | 1. Expand Appearance section<br>2. Enter a non-numeric string in "Number of announcements"<br>3. Save | Save is blocked by numeric validation on the field | Medium |
| MT-CSET-017 | Rapid re-submission via browser Back | Course Settings is open | 1. Save settings successfully<br>2. Press browser Back to return to form<br>3. Click save again | Second save succeeds without creating duplicate courses or configurations | Medium |
| MT-CSET-018 | Dropdown visibility toggle state preservation | Course Settings is open | 1. Set Group mode to Separate groups<br>2. Select a Grouping<br>3. Change Group mode to No groups (Grouping field hides)<br>4. Change Group mode back to Separate groups | The previously selected Grouping value is restored when the field becomes visible again | Low |

---

## 9. Participants Management

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-PART-001 | Participants management controls displayed | Teacher opens Participants page | 1. Open Participants tab | Scope dropdown, Enrol users button, filters, alphabetical filters, table, row menus, and bulk dropdown are visible | High |
| MT-PART-002 | Filter participants by student name | Participants include `student1` | 1. Add a First name filter for the seeded student<br>2. Apply filters | Participants table shows `student1` and hides unrelated participant rows | High |
| MT-PART-003 | Alphabetical filtering | Participants exist | 1. Select First name or Last name initial | Participants table filters by selected initial | Medium |
| MT-PART-004 | Enrol user dialog | A non-enrolled fixture user exists | 1. Click "Enrol users"<br>2. Search for the fixture user<br>3. Select Student role and enrollment duration<br>4. Confirm<br>5. Search the participants table for that user | User appears in the participants table with Student role and active enrollment status | High |
| MT-PART-005 | Row action menu targets selected participant | Participants table includes `student1` | 1. Open the row action menu for `student1`<br>2. Select view profile | `student1` profile opens and the page does not navigate to any other participant profile | Medium |
| MT-PART-012 | Bulk action requires explicit checked rows | Participants table includes `student1` and another user | 1. Check only `student1`<br>2. Open "With selected users..." dropdown | Bulk action context is limited to the checked row; unchecked participant rows remain unselected | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-PART-006 | Participants blocked while unauthenticated | User is logged out | 1. Navigate directly to Participants URL | User is redirected to the login page before the participants table is rendered | High |
| MT-PART-007 | Enrol dialog with no selected user | Enrol users dialog is open | 1. Leave user search empty<br>2. Confirm | Enrollment is blocked with validation feedback | High |
| MT-PART-008 | Filter with no matches | Participants page is visible | 1. Apply filter that matches no users | Empty/no-results state is displayed | Medium |
| MT-PART-009 | Clear filters resets conditions | Filters are active | 1. Click "Clear filters" | Filters are removed and full list returns | Medium |
| MT-PART-013 | Confirm enrollment with no user selected | Enrol users dialog is open | 1. Leave User search blank<br>2. Select `Student` role<br>3. Click "Enrol users" | Save is blocked by a required-field validation error on the user search field | High |
| MT-PART-014 | Confirm enrollment with no role selected | Enrol users dialog is open | 1. Select a valid user<br>2. Leave Role dropdown blank<br>3. Click "Enrol users" | Save is blocked by a required-field validation error on the role field | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-PART-010 | Multiple filter conditions | Participants include `student1` and `teacher1` | 1. Add a Role filter for Student<br>2. Add a name filter for `student1`<br>3. Apply filters | Table shows `student1`; `teacher1` and non-matching users are absent from the filtered table | Medium |
| MT-PART-011 | Bulk action with no users selected | Participants page is visible | 1. Leave all checkboxes empty<br>2. Open "With selected users..." dropdown | Bulk action cannot be submitted and the participants table remains unchanged | Medium |
| MT-PART-015 | Confirm enrollment then immediately navigate back | Enrol users dialog is open | 1. Complete enrollment<br>2. Click browser Back | Duplicate enrollment is blocked; no duplicate row appears in the participants table | Medium |
| MT-PART-016 | User search with very long string and emoji | Enrol users dialog is open | 1. Search for a 200+ character string containing emoji<br>2. Submit | Dialog does not crash; UI displays "No results" safely without layout breaking | Low |
| MT-PART-017 | Alphabet filter with no matching participants | Participants list is visible | 1. Select First name `Z`<br>2. Assume no users start with `Z` | Table updates to display the empty state "Nothing to display" without error | Low |

---

## 10. Assignment Teacher View

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-ATVIEW-001 | Assignment metadata visible | Teacher opens assignment | 1. Open an assignment page | Opened date, due date, description, and attached files are visible | High |
| MT-ATVIEW-002 | Grading summary visible | Assignment has enrolled participants | 1. Open assignment page | Number of participants, submissions, needs grading, visibility, and time remaining are displayed | High |
| MT-ATVIEW-003 | Grade button opens grading interface | Assignment has submissions or enrolled students | 1. Click "Grade" | Individual grading interface opens | High |
| MT-ATVIEW-004 | Assignment tabs navigate | Assignment page is open | 1. Click Assignment, Settings, Submissions, Advanced grading, and More tabs | Each selected tab becomes active and displays its matching heading or form before the next tab is clicked | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-ATVIEW-005 | Assignment blocked while unauthenticated | User is logged out | 1. Navigate directly to assignment URL | User is redirected to the login page before assignment metadata or grading controls render | High |
| MT-ATVIEW-006 | Grade unavailable without permission | User lacks grading permission | 1. Open assignment page<br>2. Navigate directly to the grading URL | Grade button is not rendered and the direct grading URL displays access denied before the grading form renders | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-ATVIEW-007 | Assignment with zero submissions | Assignment exists with no submissions | 1. Open assignment page | Grading summary shows Number of submissions `0` and Needs grading `0`; Grade button and assignment tab bar remain visible | Medium |
| MT-ATVIEW-008 | Expired due date | Assignment due date has passed | 1. Open assignment page | Time remaining clearly indicates overdue/closed state | Low |
| MT-ATVIEW-009 | Rapid multiple clicks on Grade button | Assignment view is visible | 1. Rapidly double-click "Grade" | Grading interface modal opens exactly once; no duplicate modal or background load issues occur | Medium |
| MT-ATVIEW-010 | Very long assignment description does not break layout | Assignment view is visible | 1. View an assignment with a 10,000+ character description | Description renders fully and the grading summary table below it remains accessible and correctly aligned | Low |

---

## 11. Assignment Submissions

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-ASUB-001 | Submission table displayed | Assignment has enrolled students | 1. Open Submissions tab | Student identity, status, grading status, date, online text, files, comments, feedback, and final grade columns are visible | High |
| MT-ASUB-002 | Search and filter submissions | Submissions tab includes `student1` | 1. Search for `student1`<br>2. Filter by submission status Submitted for grading | Table shows `student1` submitted row and hides rows that do not match the selected status | High |
| MT-ASUB-003 | Open row grading workflow | Submission row exists | 1. Open row action menu<br>2. Select grade action | Grading workflow opens for selected student | High |
| MT-ASUB-004 | Enable quick grading | Quick grading is available and `student1` has a submission | 1. Enable quick grading<br>2. Enter grade `85` and feedback `Meets rubric` for `student1`<br>3. Save changes<br>4. Refresh Submissions tab | Grade `85` and feedback `Meets rubric` persist for `student1` | High |
| MT-ASUB-005 | Download submitted file | `student1` submitted `essay-draft.pdf` | 1. Click `essay-draft.pdf` in the File submission column | Browser receives the `essay-draft.pdf` file response and no access-denied page is shown | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-ASUB-006 | Submissions blocked while unauthenticated | User is logged out | 1. Navigate directly to submissions URL | User is redirected to the login page before the submissions table renders | High |
| MT-ASUB-007 | Invalid quick grade | Quick grading is enabled | 1. Enter grade `101` for `student1`<br>2. Save | Save is blocked, `101` is marked invalid, and the previous grade value for `student1` remains unchanged after refresh | High |
| MT-ASUB-008 | Search no matching student | Submissions tab is open | 1. Search for non-existent student | Empty/no-results state is displayed | Medium |
| MT-ASUB-011 | Attempt inline Final Grade edit when Quick Grading disabled | Assignment Submissions table is visible and Quick grading is off | 1. Click a student's Final Grade cell | Cell remains read-only; no inline input field appears | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-ASUB-009 | Maximum valid grade | Quick grading is enabled | 1. Enter grade `100` for `student1`<br>2. Save and refresh Submissions tab | Grade `100` remains visible for `student1` after refresh | Medium |
| MT-ASUB-010 | Late submission row | Assignment has late submission | 1. Open Submissions tab | Late timing/status is shown accurately | Medium |
| MT-ASUB-012 | Rapidly toggle Quick Grading on and off | Assignment Submissions table is visible | 1. Rapidly toggle Quick grading multiple times | Table stabilizes in the state matching the final toggle action; no duplicate inline inputs appear | Medium |
| MT-ASUB-013 | Rapid double-click "Grade" in action menu | Assignment Submissions table is visible | 1. Open action menu for a student<br>2. Rapidly double-click "Grade" | Grading interface opens exactly once without triggering multiple browser navigation requests | Medium |
| MT-ASUB-014 | Student Name search with leading and trailing whitespace is trimmed | Assignment Submissions table is visible | 1. Search for `   student1   ` | Table filters to show `student1`; surrounding whitespace is safely ignored | Low |
| MT-ASUB-015 | Student profile link is navigable from submissions | Assignment Submissions table is visible | 1. Click the student's name in a submission row | Browser navigates directly to the student's Moodle profile | Medium |

---

## 12. Gradebook Grader Report

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-GRADE-001 | Grader report table displayed | Teacher opens Grades tab | 1. Open Grader report | Activity columns, student rows, grade cells, and average row are visible | High |
| MT-GRADE-002 | Switch report type | Report selector is visible | 1. Change report type to User report or Overview report | Selected report opens | Medium |
| MT-GRADE-003 | Search/filter gradebook users | Gradebook includes `student1` | 1. Search for `student1` in gradebook user search/filter controls | Grade table shows `student1` row and hides non-matching student rows | High |
| MT-GRADE-004 | Edit individual grade cell | Edit mode is enabled and `student1` has a grade item | 1. Open `student1` grade cell for `Essay Draft`<br>2. Enter `90`<br>3. Save changes<br>4. Reload Grader report | `student1` shows grade `90` for `Essay Draft`; the course total row refreshes and does not show a stale previous total | High |
| MT-GRADE-005 | Edit activity grade settings | Column action menu is visible | 1. Open activity column menu<br>2. Select grade settings action | Grade settings page/dialog opens | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-GRADE-006 | Gradebook blocked while unauthenticated | User is logged out | 1. Navigate directly to gradebook URL | User is redirected to the login page before grader report rows or grade cells render | High |
| MT-GRADE-007 | Out-of-range grade blocked | Edit mode is enabled | 1. Enter grade `101` for `student1` on `Essay Draft`<br>2. Save | Invalid value is flagged, save is blocked, and the previous `Essay Draft` grade remains unchanged after reload | High |
| MT-GRADE-008 | Student cannot access grader report | Student account exists | 1. Log in as student<br>2. Navigate to Grader report URL | Full grader report is not accessible | High |
| MT-GRADE-011 | Edit a Grade cell when Edit Mode is disabled | Grader report is visible and Edit mode is off | 1. Click a student's grade cell | Cell remains read-only; no inline input field or save controls appear | High |
| MT-GRADE-012 | Enter non-numeric value into Grade cell | Grader report is visible and Edit mode is on | 1. Enter `A+` in a grade cell<br>2. Click Save changes | Save is blocked by numeric validation error on the modified cell | High |
| MT-GRADE-014 | Grade one unit above activity maximum | Grader report is visible and Edit mode is on | 1. Enter `101` in a grade cell where max is `100`<br>2. Click Save changes | Save is blocked by maximum value validation error on the modified cell | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-GRADE-009 | Minimum valid grade | Edit mode is enabled | 1. Enter grade `0` for `student1` on `Essay Draft`<br>2. Save and reload Grader report | Grade `0` remains visible for `student1` on `Essay Draft` after reload | Medium |
| MT-GRADE-010 | Decimal grade precision | Grade item is configured for one decimal place | 1. Enter grade `89.5`<br>2. Save and reload Grader report | Grade displays as `89.5` and is not rounded to a whole number | Low |
| MT-GRADE-013 | Grade exactly equals activity maximum | Grader report is visible and Edit mode is on | 1. Enter `100` in a grade cell where max is `100`<br>2. Click Save changes | Grade saves successfully without out-of-bounds error | Medium |
| MT-GRADE-015 | Grade exactly equals activity minimum | Grader report is visible and Edit mode is on | 1. Enter `0` in a grade cell where min is `0`<br>2. Click Save changes | Grade saves successfully without out-of-bounds error | Medium |
| MT-GRADE-016 | Very long comment in grade cell | Grader report is visible and Edit mode is on | 1. Enter a 200+ character comment for a grade<br>2. Click Save changes | Comment is saved successfully and is accessible without breaking the grader report grid | Low |

---

## 13. Profile

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-PROFILE-001 | Teacher profile details displayed | Teacher is logged in | 1. Open Profile | Initials icon, full name, message button, and profile description area are visible | High |
| MT-PROFILE-002 | User details and privacy cards displayed | Profile page is open | 1. Inspect information cards | User details, privacy/policies, course details, miscellaneous, reports, and login activity cards are visible | High |
| MT-PROFILE-003 | Course details links open course profiles | Teacher profile lists `QA Automation 101` under Course details | 1. Click the `QA Automation 101` course profile link | Course profile view for `teacher1` in `QA Automation 101` opens and keeps teacher identity visible | Medium |
| MT-PROFILE-004 | Edit profile link opens form | Profile page is open | 1. Click "Edit profile" | Edit profile form opens | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-PROFILE-005 | Profile blocked while unauthenticated | User is logged out | 1. Navigate directly to profile URL | User is redirected to the login page before profile cards render | High |
| MT-PROFILE-006 | Other-user private details restricted | `teacher1` opens another user's profile | 1. Inspect email visibility, login activity, and private details cards | Fields outside `teacher1` permission are not rendered; public name and allowed course details remain visible | Medium |
| MT-PROFILE-009 | View non-existent user profile | Teacher is logged in | 1. Manually edit profile URL to use an invalid user ID (e.g., `?id=99999`) | System displays a standard user-not-found error page | High |
| MT-PROFILE-010 | Student viewing teacher profile | `student1` is logged in | 1. Navigate to `teacher1` profile | Private activity reports and sensitive data cards are hidden from the student | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-PROFILE-007 | Missing optional description | Teacher profile has no description | 1. Open Profile | Profile page renders initials, full name, and information cards; description area is empty and no placeholder error is shown | Low |
| MT-PROFILE-008 | Long display name | Teacher profile full name is 80+ characters | 1. Open Profile | Full name wraps within the profile header, and the message button remains visible below or beside the name | Low |
| MT-PROFILE-011 | Very long profile description | Teacher profile has a 10,000+ character description | 1. Open Profile | Description renders safely without breaking layout | Low |
| MT-PROFILE-012 | Emoji in display name | Teacher profile name contains emoji | 1. Open Profile | Emoji render correctly in the profile header | Low |
| MT-PROFILE-013 | Profile picture loading failure | Custom profile picture URL is unreachable | 1. Open Profile | Profile falls back gracefully to displaying the teacher's initials | Low |
| MT-PROFILE-014 | Enrolled in numerous courses | Teacher is enrolled in 50+ courses | 1. Open Profile | Course details card displays courses in a scrollable list or paginates cleanly | Low |

---

## 14. Profile Edit

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-PEDIT-001 | Update required profile fields | Teacher opens Edit profile | 1. Set City/town to `Dhaka QA Teacher`<br>2. Set Description to `Teacher profile update check`<br>3. Click "Update profile"<br>4. Reopen Profile | Profile page shows `Dhaka QA Teacher` and `Teacher profile update check` for `teacher1`; original values are restored during cleanup | High |
| MT-PEDIT-002 | Upload profile picture | Edit profile form is open | 1. Upload `teacher-avatar.png` under 10 MB<br>2. Save and reopen Profile | Teacher profile picture changes from initials to the uploaded image preview | Medium |
| MT-PEDIT-003 | Edit additional names and interests | Edit profile form is open | 1. Enter alternative name `GT Teacher Alias`<br>2. Add interest tag `ground-truth`<br>3. Save and reopen Edit profile | `GT Teacher Alias` and `ground-truth` remain populated in their respective fields | Medium |
| MT-PEDIT-004 | Expand all profile panels | Edit profile form is open | 1. Click "Expand all" | All collapsible sections expand | Low |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-PEDIT-005 | First name empty | Edit profile form is open | 1. Clear First name<br>2. Save | Required-field validation blocks save | High |
| MT-PEDIT-006 | Last name empty | Edit profile form is open | 1. Clear Last name<br>2. Save | Required-field validation blocks save | High |
| MT-PEDIT-007 | Invalid email address | Edit profile form is open | 1. Enter invalid email<br>2. Save | Email validation blocks save | High |
| MT-PEDIT-008 | Oversized profile picture | Edit profile form is open | 1. Upload `oversize-11mb.pdf` in the profile picture upload control | Upload is rejected with file-type or file-size validation feedback and no new profile picture is saved | Medium |
| MT-PEDIT-011 | Submit with all required fields cleared | Edit profile form is open | 1. Clear First name, Last name, and Email<br>2. Click "Update profile" | Multiple validation errors appear simultaneously and form is not submitted | High |
| MT-PEDIT-012 | Missing email domain | Edit profile form is open | 1. Enter `teacher1@`<br>2. Save | Email validation explicitly rejects the missing domain | High |
| MT-PEDIT-013 | File size exactly one byte over limit | Edit profile form is open | 1. Upload an image one byte over the site maximum<br>2. Save | Upload is explicitly rejected for exceeding the max upload size | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-PEDIT-009 | Cancel profile edit | Edit profile form has unsaved changes | 1. Click "Cancel" | Unsaved changes are discarded | Medium |
| MT-PEDIT-010 | Maximum valid picture size | Edit profile form is open | 1. Upload `teacher-avatar-10mb.png` at the configured image upload limit<br>2. Save and reopen Profile | Uploaded image displays as the teacher profile picture after reload | Low |
| MT-PEDIT-014 | Description with 10,000+ characters | Edit profile form is open | 1. Enter 10,000+ chars into description<br>2. Save | Profile saves successfully and text is visible | Low |
| MT-PEDIT-015 | Emoji and non-Latin Unicode in First Name | Edit profile form is open | 1. Enter emoji into First name<br>2. Save | Profile saves and emoji are preserved | Low |
| MT-PEDIT-016 | Leading and trailing whitespace trimmed | Edit profile form is open | 1. Enter `   teacher   ` as First name<br>2. Save | Whitespace is automatically trimmed upon save | Low |
| MT-PEDIT-017 | Rapid double-click on Update profile | Edit profile form is open | 1. Rapidly double-click "Update profile" | Form submits exactly once without duplicate requests | Medium |
| MT-PEDIT-018 | Add and immediately remove repeating group item | Edit profile form is open | 1. Add an Additional name item<br>2. Immediately remove it<br>3. Save | Save succeeds without leaving ghost entries for the additional name | Medium |

---

## 15. Logout

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-LOGOUT-001 | Logout from user menu | Teacher is logged in | 1. Open user menu<br>2. Click "Log out" | Session ends and login page is displayed | High |
| MT-LOGOUT-002 | Protected page requires re-authentication after logout | Teacher has logged out | 1. Navigate directly to Dashboard or course URL | User is redirected to login | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-LOGOUT-003 | Browser back after logout | Teacher logged out from protected page | 1. Press browser Back | Login page remains active or protected page immediately redirects to login; dashboard/course content is not rendered from browser cache | High |
| MT-LOGOUT-004 | Logout action unavailable while logged out | User is on login page | 1. Inspect user menu area | Authenticated user menu and logout option are not visible | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| MT-LOGOUT-005 | Double-click logout | Teacher is logged in | 1. Double-click "Log out" | Logout completes once without error or duplicate redirect loops | Low |
| MT-LOGOUT-006 | Session timeout behaves like logout | Teacher session has expired | 1. Open protected page | User is required to authenticate again | High |
| MT-LOGOUT-007 | Concurrent sessions log out | Teacher has two browser tabs open | 1. Log out in tab 1<br>2. Attempt action in tab 2 | Tab 2 redirects to login upon interaction | High |
| MT-LOGOUT-008 | Logout URL CSRF protection | User is logged in | 1. Manually navigate to `logout.php` without token | Action is blocked and requires confirmation to prevent CSRF logout | Medium |
| MT-LOGOUT-009 | Rapid navigation during logout | Teacher clicks logout | 1. Click "Log out"<br>2. Rapidly click a navigation link before redirect | Logout proceeds and user ends up unauthenticated on the destination or login page | Low |

---

## Test Summary

| Area | Count |
|------|-------|
| Modules covered | 15 |
| Ground-truth test cases | 220 |
| Primary role | Teacher |
| Source functional description | dataset/raw_specifications/Moodle/MoodleTeacher.md |
