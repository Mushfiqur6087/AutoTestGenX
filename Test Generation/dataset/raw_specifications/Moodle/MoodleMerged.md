# Moodle Merged Functional Description

---

## Navigation

**Student View:**
The top navigation bar appears on every page and contains the site name "MoodleTest" on the left, which links to the home page, followed by links for Home, Dashboard, and My Courses. On the right side, a notifications bell icon shows alerts when clicked, a messaging icon opens the messaging drawer, and the user's initials in a circular icon opens the user menu dropdown. The user menu contains links for Profile, Grades, Calendar, Private Files, Reports, and Preferences, followed by a Log out option that ends the session and returns to the login page. When viewing a course, a horizontal tab bar appears below the course title with tabs for Course, Participants, Grades, Activities, and Competencies. Students do not see the Settings tab. When viewing an activity, breadcrumbs at the top show the full navigation path from the course, with each segment as a clickable link. The Course Index sidebar on the left side of course pages provides a hierarchical tree of all sections and activities, with expand/collapse arrows per section and a close button (X) to hide the sidebar. The currently active item is highlighted.

**Teacher View:**
The top navigation bar appears on every page and contains the site name "MoodleTest" on the left, which links to the home page, followed by links for Home, Dashboard, and My Courses. On the right side, a notifications bell icon shows alerts when clicked, a messaging icon opens the messaging drawer, and the user's initials in a circular icon opens the user menu dropdown. The user menu contains links for Profile, Grades, Calendar, Private Files, Reports, and Preferences, followed by a Log out option that ends the session and returns to the login page. When viewing a course, a horizontal tab bar appears below the course title with tabs for Course, Participants, Grades, Activities, and Competencies. Teachers also see a Settings tab that is not visible to students. When viewing an activity, breadcrumbs at the top show the full navigation path from the course, with each segment as a clickable link. The Course Index sidebar on the left side of course pages provides a hierarchical tree of all sections and activities, with expand/collapse arrows per section and a close button (X) to hide the sidebar. The currently active item is highlighted.

---

## Login

**Student View:**
The login page displays a form with two required fields — Username and Password — followed by a "Log in" button. A "Lost password?" link is available (currently disabled on this test site). A separate section offers an "Access as a guest" button for unauthenticated browsing, and a "Cookies notice" button provides cookie usage information. On submission, valid credentials redirect the student to the Dashboard. Invalid or empty credentials show an inline error message, clear the password field, and retain the username for correction.

**Teacher View:**
The login page displays a form with two required fields — Username and Password — followed by a "Log in" button. A "Lost password?" link is available (currently disabled on this test site). A separate section offers an "Access as a guest" button for unauthenticated browsing, and a "Cookies notice" button provides cookie usage information. On submission, valid credentials redirect the teacher to the Dashboard. Invalid or empty credentials show an inline error message, clear the password field, and retain the username for correction.

---

## Dashboard

**Student View:**
The Dashboard displays a personalized greeting at the top. The main content area contains two blocks side by side: the Timeline block and the Calendar block. The Timeline block shows upcoming activities and deadlines across all enrolled courses. It includes a time range dropdown (e.g., "Next 7 days"), a sort order dropdown, and a search field to find activities by name or type. When no items exist within the selected range, an empty state is shown. The Calendar block shows a monthly view with the current month and year as a heading. It includes an "All courses" dropdown to filter events by course, a "New event" button to create personal calendar entries, and left/right arrows to navigate between months. The current date is highlighted, and dates with events display their names inline. Two links at the bottom — "Full calendar" and "Import or export calendars" — open the dedicated calendar view and calendar data management respectively. When Edit mode is toggled on, a "Reset page to default" button appears at the top right and a "+ Add a block" button appears below the Dashboard heading, opening a page listing all available block types. In Edit mode, each existing block shows a move icon and a three-dot menu for configure, move, and delete actions.

**Teacher View:**
The Dashboard displays a personalized greeting at the top. The main content area contains two blocks side by side: the Timeline block and the Calendar block. The Timeline block aggregates upcoming teaching actions across all enrolled courses. It includes a time range dropdown (e.g., "Next 7 days"), a sort order dropdown, and a search field to find activities by name or type. When no items exist within the selected range, an empty state is shown. The Calendar block shows a monthly view with the current month and year as a heading. It includes an "All courses" dropdown to filter events by course, a "New event" button to create calendar entries, and left/right arrows to navigate between months. The current date is highlighted, and dates with events display their names inline. Two links at the bottom — "Full calendar" and "Import or export calendars" — open the dedicated calendar view and calendar data management respectively.

---

## Dashboard — Edit Mode

**Teacher View:**
When Edit mode is toggled on, a "Reset page to default" button appears at the top right and a "+ Add a block" button appears below the Dashboard heading. Clicking it opens an Add a block page listing all available block types: Comments, Course overview, Latest announcements, Latest badges, Learning plans, Logged in user, Mentees, Online users, Private files, Random glossary entry, Recently accessed courses, Starred courses, Tags, Text, and Upcoming events. A "Cancel" link at the bottom returns to the Dashboard without adding a block. In Edit mode, each existing block shows a move icon and a three-dot options menu for configure, move, and delete actions. Layout changes are persisted per user and can be fully reverted with "Reset page to default."

---

## My Courses

**Student View:**
The My Courses page displays all courses in which the student is enrolled as visual cards. Each card shows the course banner image, course name as a clickable link, and the category name. Four controls appear above the grid: a status dropdown (All, In progress, Future, Past, Starred, Hidden), a search field, a sort dropdown, and a layout dropdown (Card, List, Summary). Each course card has a three-dot menu with two options: "Star this course" (pins the course to the top) and "Remove from view" (hides the course without unenrolling). Clicking the course name navigates to that course's main page.

**Teacher View:**
The My Courses page displays all courses the teacher has access to as visual cards. Each card shows the course banner image, course name as a clickable link, and the category name. Four controls appear above the grid: a status dropdown (All, In progress, Future, Past, Starred, Hidden), a search field, a sort dropdown, and a layout dropdown (Card, List, Summary). Each course card has a three-dot menu with two options: "Star this course" (pins the course to the top) and "Remove from view" (hides the course without affecting enrollment). Clicking the course name navigates to that course's main page.

---

## Course Page

**Student View:**
The Course page displays the full course content organized into collapsible sections. The course name appears as the page heading, followed by the navigation tab bar. The main content area lists sections, each with a collapsible chevron and section name. A "Collapse all" link at the top right collapses all sections at once. Within each section, activities and resources are listed with a type icon and a clickable name. Students cannot enable Edit mode on course pages.

**Teacher View:**
The Course page displays the full course content organized into collapsible sections. The course name appears as the page heading, followed by the navigation tab bar. The main content area lists sections, each with a collapsible chevron and section name. A "Collapse all" link at the top right collapses all sections at once. Within each section, activities and resources are listed with a type icon and a clickable name.

---

## Course Edit Mode and Activity Chooser

**Teacher View:**
Enabling Edit mode turns the Course page into an authoring interface. Each section and activity row gains inline controls: an edit icon for quick renaming, a section-level three-dot menu (edit, duplicate, hide, delete, move), an activity-level three-dot menu (edit settings, move, duplicate, hide, set access restrictions, delete), and a bulk actions toolbar for batch operations on multiple selected activities. An "+ Add an activity or resource" button appears at the bottom of each section, and an "+ Add a subsection" control allows nesting content hierarchically. Clicking "+ Add an activity or resource" opens the Activity Chooser modal, which contains a category filter bar (All, Activities, Resources, Recommended), a search field, and a grid of activity/resource tiles including Assignment, Forum, Quiz, File, Page, Lesson, SCORM, URL, and Workshop. Each tile has a star/favorite toggle for quick access. Selecting a tile and clicking "Add" opens that activity's creation form.

---

## Course Settings

**Teacher View:**
The Course Settings form is organized into collapsible panels with the following fields: Course full name (required), Course short name (required), Course category (required dropdown), Course visibility (Show/Hide dropdown), Course start date, Course end date (with Enable toggle), Course ID number, Course summary (rich text editor), Course image upload, Course format (Topics format, Weekly format, etc.), layout controls dependent on the selected format, appearance settings (language, news items, activity dates, completion conditions display), Maximum upload size, Completion tracking toggle, Groups (group mode and grouping dropdowns), and Tags. "Save and display" persists the configuration and returns to the course page; "Cancel" leaves existing settings unchanged. Required fields and format validations are enforced inline.

---

## Participants

**Student View:**
The Participants page lists all users enrolled in the course. A filter system at the top allows building conditions using an "Any" toggle, a Select attribute dropdown, and an "+ Add condition" link, with "Clear filters" and "Apply filters" buttons. Alphabetical filter buttons for First name and Last name (All and A–Z) allow quick initial-based filtering. The participants table contains columns for checkbox, First/Last name (sortable, links to profile), Roles, Groups, and Last access to course. Students can click any participant name to view their profile but cannot enrol or unenrol users, edit roles, or access enrollment management features.

**Teacher View (Participants Management):**
The Participants page lists all users enrolled in the course. An enrolled-users scope dropdown at the top filters the list by enrollment context, and an "Enrol users" button opens the enrollment dialog. A filter system below allows building conditions using an "Any" toggle, a Select attribute dropdown, and an "+ Add condition" link, with "Clear filters" and "Apply filters" buttons. Alphabetical filter buttons for First name and Last name (All and A–Z) allow quick initial-based filtering. The participants table contains columns for checkbox (bulk selection), First/Last name (sortable, links to profile), Email address, Roles, Groups, Last access to course, and Status. Each row has a three-dot action menu with options to view profile, edit role, and send a message. At the bottom, a "With selected users…" dropdown applies bulk actions to checked participants. The Enrol users dialog contains a user search field, a Role dropdown, and an optional Enrollment duration control. Confirming enrollment adds the user to the course at the specified role.

---

## Grades / Gradebook

**Student View (Grades):**
The Grades page displays the student's own grades for the course via a User report. The grade table columns are: Grade item (course name as a collapsible header with graded activities indented beneath), Calculated weight, Grade (earned value or "–" if not yet graded), Range, Percentage, Feedback, and Contribution to course total. An "AGGREGATION Course total" row at the bottom displays the cumulative grade across all weighted items. Students can only view their own grades and cannot access the full gradebook or other students' grades.

**Teacher View (Gradebook — Grader Report):**
The Gradebook Grader report provides a spreadsheet-style view of grades. A report-type selector dropdown at the top left allows switching between Grader report, User report, and Overview report. User search and filter controls above the table allow narrowing rows by student name or group. The grade table displays activities as columns and enrolled students as rows. A per-column action menu on each column header provides options to edit that activity's grade settings. A per-cell three-dot menu allows editing individual grade entries. An overall average row at the bottom shows the class average per activity. When Edit mode is enabled, grade cells become editable inline and a "Save changes" action applies edits. Values outside the configured grade range are flagged inline and block saving.

---

## Assignment

**Student View (Assignment Submission):**
The Assignment page displays the assignment's Opened date, Due date, and full Description. A "Add submission" button opens the submission form, which may include an online text editor, a file upload area, or both, depending on the assignment's configuration. The Submission status section shows a summary table with rows for Submission status (e.g., No submissions have been made yet, Submitted for grading), Grading status (e.g., Not graded, Graded), Time remaining, Last modified, and Submission comments. After submitting, the student may view or edit their submission if the due date has not passed and the teacher permits resubmission. Once graded, the earned grade and written feedback appear on this page.

**Teacher View (Assignment Creation):**
The assignment creation form opens after selecting Assignment from the Activity Chooser. Assignment name is a required text field at the top. The form is organized into collapsible panels. General contains the required Assignment name field, a Description rich text editor, and an optional Additional files upload area. Availability contains Allow submissions from, Due date, and Cut-off date, each with a date/time picker and an Enable toggle; disabled toggles exclude that date from enforcement. Submission types contains checkboxes for Online text and File submissions; enabling File submissions reveals additional controls for maximum number of uploaded files, maximum submission size, and accepted file types. Feedback types contains options for feedback comments, feedback files, and offline grading worksheet. Submission settings contains options for requiring a submit button click, requiring submission statements, attempts reopened settings, and maximum attempts. Group submission settings contains controls for group submissions, requiring all group members to submit, and grouping selection. Notifications contains toggles for notifying graders of new and late submissions. Grade contains the grade type and maximum points, grading method selector, and grade category and grade to pass fields. Access restrictions contains an "+ Add restriction" button that opens a restriction-type picker. Activity completion contains completion tracking options and required conditions. Tags contains a tag entry field, and Competencies contains course competency linking controls. At the bottom, "Save and return to course" creates the assignment and redirects to the course page, "Save and display" creates it and opens the new assignment's page, and "Cancel" discards all changes. Required fields and constraints are validated inline before saving.

**Teacher View (Assignment — Teacher View):**
The Assignment page (teacher view) displays the assignment's metadata including Opened date, Due date, and full Description with any attached files. A "Grade" button opens the grading interface for individual students. The Grading summary panel shows the following read-only metrics: Number of participants, Number of submissions, Needs grading, Visibility, and Time remaining. A tab bar below the summary provides navigation to Assignment, Settings, Submissions, Advanced grading, and More.

**Teacher View (Assignment Submissions):**
The Submissions view presents a table of all student submission records. Search and filter controls above the table allow narrowing by student name, submission status, and grading status. The table columns are: Student identity (name and initials icon, links to profile), Submission status (e.g., Submitted for grading, No submission, Draft — not submitted), Grading status (e.g., Graded, Not graded), Submission date/time, Time since submission, Online text preview, File submission links, Submission comments, Feedback comments, Feedback files, and Final grade. Each row has an action menu to open the grading workflow for that student. A "Quick grading" mode can be enabled to allow inline grade entry directly in the table.

---

## Activities

**Student View:**
The Activities page provides a consolidated overview of every activity in the course, grouped by type. The Assignments section is expanded by default and displays a table with columns for Name (clickable link with parent section shown below), Due date, and Submission status. The Forums section and Resources section are collapsed by default and expandable via an arrow. Additional activity types appear as their own collapsible sections. Clicking any activity name navigates directly to that activity's page.

---

## Profile

**Student View:**
The Profile page displays the student's circular initials icon, full name, a "Message" button, and an optional profile description. The page is organized into information cards: User details (email address, visibility note, timezone, and an "Edit profile" link), Privacy and policies (Data retention summary link), Course details (links to all enrolled course profiles), Miscellaneous (links to Blog entries, Forum posts, Forum discussions, and Learning plans), Reports (Browser sessions and Grades overview links), and Login activity (First and Last access to site with exact dates and relative time indicators). Clicking "Edit profile" opens the profile form, which contains collapsible panels for General (First name, Last name, Email address, Email visibility dropdown, MoodleNet profile ID, City/town, Country dropdown, Timezone dropdown, and Description), User picture (current picture, new picture upload, and picture description), Additional names, Interests, and Optional fields. "Update profile" validates all required fields before saving; "Cancel" exits without changes. Students can only modify their own profile.

**Teacher View:**
The Profile page displays the teacher's circular initials icon, full name, a "Message" button, and an optional profile description. The page is organized into information cards: User details (email address, visibility note, timezone, and an "Edit profile" link), Privacy and policies (Data retention summary link), Course details (links to all associated course profiles), Miscellaneous (links to Blog entries, Forum posts, Forum discussions, and Learning plans), Reports (Browser sessions and Grades overview links), and Login activity (First and Last access to site with exact dates and relative time indicators).

---

## Profile Edit

**Teacher View:**
The Edit profile form contains collapsible sections with an "Expand all" link at the top right. General contains First name (required), Last name (required), Email address (required), Email visibility dropdown, MoodleNet profile ID, City/town, Country dropdown, Timezone dropdown, and Description (rich text editor). User picture shows the current picture, a new picture upload area with drag-and-drop support, and a Picture description field. Additional names contains optional fields for alternative name formats. Interests contains a tag-based field. Optional fields contains any site-defined custom fields. "Update profile" validates all required fields and upload constraints before saving and refreshes the profile page on success. "Cancel" exits without making changes.

---

## Logout

**Student View:**
Selecting Log out terminates the current authenticated session and redirects to the login page. Access to all protected pages requires re-authentication after logout.

**Teacher View:**
Selecting Log out terminates the current authenticated session and redirects to the login page. Access to all protected pages requires re-authentication after logout.
