# Post-Verification Specifications

### [TC-003] After logging out, accessing a protected page is blocked (post-logout access requires re-authentication)
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Log in as <role>
2. 2. Click the 'Log out' button
3. 3. Observe that the application redirects to the Login page (post-logout)
4. 4. From the browser address bar, navigate to a protected page at <protected page URL>

**Original Expected Result:** Navigation to <protected page URL> is blocked and the user is redirected to the Login page; protected page content is not displayed and re-authentication is required (session remains terminated).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard`
- **Observe**:
  - Edit mode is enabled (Edit mode toggle on; '+ Add a block' button visible)
  - Current layout of dashboard blocks listed in visual order (e.g., left column: <block names and positions>, right column: <block names and positions>)
  - Any user-added or relocated blocks are present and identifiable by name/position (record names and positions for comparison)

**Post-Check**
- **Navigate To**: `Dashboard`
- **Observe**:
  - Edit mode state (toggle) and availability of '+ Add a block' button
  - Visible dashboard blocks and their visual order (left-to-right / top-to-bottom)
  - Absence of previously recorded user-added blocks (they should no longer appear)

**Expected Change**: The dashboard layout is restored to the per-user default: only the default blocks are present in the default order/positions (e.g., Timeline block and Calendar block side-by-side in their default columns); any user-added blocks or user-moved blocks recorded in the pre_check are removed or returned to their default positions.

---

### [TC-005] Rapid double-click the Log out button
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Log out' button once
2. 2. Immediately click the 'Log out' button a second time (within 1 second of the first click)

**Original Expected Result:** Only a single logout action succeeds: the user is redirected to the login page and the UI shows the login page. The second click is ignored (no duplicate navigation or duplicate login page stacks are visible).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (Edit Mode enabled)`
- **Observe**:
  - Dashboard shows existing blocks in the main blocks area (titles of visible blocks)
  - No block titled 'Comments' is present in the blocks list or page
  - '+ Add a block' button is visible
  - 'Reset page to default' button is visible (indicating Edit Mode)

**Post-Check**
- **Navigate To**: `Dashboard (reload page and toggle Edit Mode off then on; or navigate away and return)`
- **Observe**:
  - Add Block page is closed
  - A block titled 'Comments' appears in the Dashboard blocks area
  - In Edit Mode the 'Comments' block shows a move icon and a three-dot options menu (configure/move/delete)
  - In normal (non-Edit) view the 'Comments' block title or its content is visible on the Dashboard
  - After a full page reload or navigating away and returning, the 'Comments' block remains present

**Expected Change**: The 'Comments' block has been added to and persisted in the user's Dashboard layout: the Add Block page is closed, the 'Comments' block is visible in Edit Mode with move/options controls and is also visible in normal view, and the block remains present after a page reload or navigating away and back.

---

### [TC-006] Log out in one tab, then refresh a protected page in another tab
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Tab A, click the 'Log out' button
2. 2. In Tab B, click the browser refresh button (reload the protected page)

**Original Expected Result:** The logout in Tab A succeeds and redirects Tab A to the login page. In Tab B, the refresh is blocked from showing protected content: Tab B is redirected to the login page (access to protected page is blocked).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (Edit mode enabled)`
- **Observe**:
  - list of blocks currently on the Dashboard (by name)
  - absence or presence of 'Course overview' block (expected: absent before adding)

**Post-Check**
- **Navigate To**: `Dashboard (verify immediately after Add Block, after refreshing page, and after logout/login)`
- **Observe**:
  - list of blocks currently on the Dashboard (by name)
  - presence of 'Course overview' block
  - block rendering (block title and expected controls when Edit mode is on/off)
  - persistence of block after page refresh
  - persistence of block after logging out and logging back in as the same user

**Expected Change**: The 'Course overview' block appears in the Dashboard's block list immediately after adding; it renders with its title and expected controls; it remains present after refreshing the page and after logging out and back in (indicating the layout change was persisted for the user).

---

### [TC-007] Click Log out while the browser is offline
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. With network offline, click the 'Log out' button

**Original Expected Result:** The client-side logout flow succeeds: the app clears the local authenticated state and displays the login page (user is shown the login page). Subsequent navigation to a protected page remains blocked (the login page is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard`
- **Observe**:
  - list of blocks currently present on the Dashboard (e.g., 'Timeline', 'Calendar')
  - absence of a 'Latest announcements' block in the Dashboard blocks area
  - Edit Mode is enabled and '+ Add a block' control is visible

**Post-Check**
- **Navigate To**: `Dashboard (after the Add Block flow completes; then reload the page or navigate away and return to verify persistence)`
- **Observe**:
  - presence of a 'Latest announcements' block in the Dashboard blocks area
  - the new block displays Edit Mode controls (move icon and three-dot menu with configure/move/delete options)
  - Add Block page/modal is closed

**Expected Change**: A 'Latest announcements' block is added to the user's Dashboard layout and is visible with Edit Mode controls; the Add Block page is closed; the block remains present after reloading the Dashboard or navigating away and returning, demonstrating the layout change was persisted.

---

### [TC-008] Use browser Back after successful logout
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Log out' button
2. 2. After being redirected to the login page, press the browser Back button once

**Original Expected Result:** Returning via the browser Back button does not restore access to the previously viewed protected page: the user remains on or is redirected back to the login page and access to protected content is blocked.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (Edit mode enabled)`
- **Observe**:
  - Edit mode toggle state = On
  - '+ Add a block' button visible
  - existing blocks list (e.g., Timeline block, Calendar block)
  - absence of 'Latest badges' block

**Post-Check**
- **Navigate To**: `Dashboard`
- **Observe**:
  - presence of 'Latest badges' block in the Dashboard blocks area with title 'Latest badges'
  - 'Latest badges' block shows Edit-mode controls (move icon and three-dot options menu) while Edit mode is enabled
  - Add Block page/modal is closed (no Add Block UI visible)

**Expected Change**: The Dashboard now contains the 'Latest badges' block in the blocks area (it was absent before); the Add Block page is closed; while Edit mode is enabled the new block shows move and options controls; the block persists in the user's layout after a full page refresh and after toggling Edit mode off and back on.

---

### [TC-009] Enter an invalid email format and attempt to save
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <invalid email format> into the Email_Address field
2. 2. Enter <valid first name> into the First_Name field
3. 3. Enter <valid last name> into the Last_Name field
4. 4. Click the 'Update profile' button

**Original Expected Result:** Inline validation error appears on the Email_Address field indicating the value is not a valid email address; the form does not submit; profile is not updated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (Edit mode enabled)`
- **Observe**:
  - list of block titles currently present on the Dashboard
  - confirmation that 'Learning plans' block is NOT present

**Post-Check**
- **Navigate To**: `Dashboard (exit Edit mode; navigate to another page such as Home; then return to Dashboard)`
- **Observe**:
  - list of block titles currently present on the Dashboard
  - confirmation that 'Learning plans' block IS present

**Expected Change**: A 'Learning plans' block appears in the Dashboard block list after adding it in Edit mode and remains present after exiting Edit mode, navigating away, and returning to the Dashboard, demonstrating the block was persisted in the user's layout.

---

### [TC-010] Upload a file that violates site upload constraints and submit
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attach <file violating site upload constraints> to the Picture_Upload control (via drag-and-drop or file picker)
2. 2. Enter <valid first name> into the First_Name field
3. 3. Enter <valid last name> into the Last_Name field
4. 4. Enter <valid email address> into the Email_Address field
5. 5. Click the 'Update profile' button

**Original Expected Result:** Upload control displays an error indicating the file violates site upload constraints (e.g. file type or size invalid); the form does not submit; profile is not updated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (before adding block)`
- **Observe**:
  - list of blocks currently present on the Dashboard (e.g., 'Timeline', 'Calendar', etc.)
  - presence of 'Logged in user' block (expect: absent)

**Post-Check**
- **Navigate To**: `Dashboard (reload the page or return to Dashboard after the Add a block flow to confirm persistence)`
- **Observe**:
  - list of blocks currently present on the Dashboard (names and positions)
  - presence of 'Logged in user' block
  - when in Edit mode, the 'Logged in user' block shows move icon and three-dot options menu (configure, move, delete)

**Expected Change**: The 'Logged in user' block is added to the Dashboard block list and is visible after the Add a block flow completes; the block remains present after a page reload or returning to the Dashboard (layout change persisted).

---

### [TC-011] Unauthenticated user attempts to access Edit profile page
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to the Edit profile page URL while signed out

**Original Expected Result:** User is redirected to the login page (Edit profile page is not accessible); no profile edit controls are shown to the unauthenticated user

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (Edit mode enabled, before adding block)`
- **Observe**:
  - 'Mentees' block is not present in the dashboard blocks list
  - record number of dashboard blocks (N)
  - Add a block modal/page is not open

**Post-Check**
- **Navigate To**: `Dashboard (after adding block; verify after closing Add Block page, optionally toggle Edit mode off/on or navigate away and return)`
- **Observe**:
  - 'Mentees' block is present in the dashboard blocks list with title 'Mentees'
  - number of dashboard blocks is N+1 compared to pre-check
  - Add a block modal/page is closed

**Expected Change**: The 'Mentees' block has been added to the user's Dashboard layout (visible with title 'Mentees') and the total block count increased by one; the Add Block page/modal is closed; the block remains present after navigating away from the Dashboard and returning, demonstrating the layout change was persisted.

---

### [TC-012] Upload file exactly at the site's maximum allowed upload size and save
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Expand the 'User picture' collapsible section
2. 2. Drag-and-drop the file that is exactly the site's maximum allowed upload size onto the Picture_Upload area
3. 3. Click the 'Update profile' button

**Original Expected Result:** Upload and save succeeds; clicking 'Update profile' submits successfully, the profile page refreshes, and the new picture is visible on the profile page (picture replaced by the uploaded file).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard`
- **Observe**:
  - Presence of 'Online users' block in Dashboard blocks area (should be absent before adding)
  - State of Edit Mode toggle (should be enabled per preconditions)

**Post-Check**
- **Navigate To**: `Dashboard (refresh page and/or navigate away and return; also toggle Edit Mode off then on)`
- **Observe**:
  - 'Online users' block present in the Dashboard blocks area
  - New block shows standard block controls (move icon and three-dot options menu) when Edit Mode is enabled
  - Add a block modal/page is closed

**Expected Change**: The 'Online users' block is present in the Dashboard where it was previously absent; the Add Block page is closed; the block remains present after a page refresh, after navigating away and returning to the Dashboard, and after toggling Edit Mode off and back on, demonstrating the layout change was persisted.

---

### [TC-013] Upload file one unit over the site's maximum allowed upload size and attempt to save
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Expand the 'User picture' collapsible section
2. 2. Drag-and-drop the file that is one unit over the site's maximum allowed upload size onto the Picture_Upload area
3. 3. Click the 'Update profile' button

**Original Expected Result:** Upload is blocked / error shown; submission is blocked and an inline error is shown near the Picture_Upload field indicating the file exceeds the site's maximum allowed upload size, and the profile page does not refresh.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (Edit mode enabled)`
- **Observe**:
  - Edit mode is enabled (Reset page to default and '+ Add a block' visible)
  - Default blocks present: Timeline block, Calendar block
  - No 'Private files' block is present in the current block layout

**Post-Check**
- **Navigate To**: `Dashboard (remain in Edit mode to confirm immediate effect; then reload page and/or navigate away and back to Dashboard to confirm persistence)`
- **Observe**:
  - 'Private files' block is present in the Dashboard blocks list/layout
  - 'Private files' block displays Edit-mode controls (move icon and three-dot menu with configure/move/delete actions)
  - Add a block page/modal is closed and not visible after selection
  - After page reload or returning to Dashboard, 'Private files' block remains present

**Expected Change**: The 'Private files' block is added to the user's Dashboard layout and is visible in the blocks list; it shows Edit-mode controls. The block remains present after reloading the Dashboard and after toggling Edit mode off and on, demonstrating the layout change was persisted.

---

### [TC-014] Enter a very long string (200+ characters) into the Description rich text editor and save
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Expand the 'General' collapsible section
2. 2. Place the cursor in the Description rich text editor
3. 3. Paste a continuous text block of 200+ characters into the Description editor
4. 4. Click the 'Update profile' button

**Original Expected Result:** Form submission proceeds; after clicking 'Update profile' the profile page refreshes. The saved Description either (a) displays the full long text on the profile detail page (accepted), or (b) displays a visibly truncated Description with an explicit truncation indicator/ellipsis or inline message indicating the Description was trimmed. Either outcome must be visible on the refreshed profile page.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (with Edit mode enabled)`
- **Observe**:
  - List of blocks present on the Dashboard (e.g., Timeline, Calendar)
  - Absence of a block titled 'Random glossary entry' in the blocks area

**Post-Check**
- **Navigate To**: `Dashboard (reload page or navigate away and return)`
- **Observe**:
  - Block titled 'Random glossary entry' is present in the Dashboard blocks area
  - When Edit mode is enabled, the 'Random glossary entry' block shows Edit-mode controls (move icon and three-dot options menu)
  - Add Block page is closed and not visible

**Expected Change**: The Dashboard now includes a 'Random glossary entry' block where it was previously absent; the Add Block page is closed; the added block is persisted across a page reload or navigating away and returning (i.e., layout change is saved).

---

### [TC-015] Enter emoji and non-Latin Unicode characters into Description and First Name fields and save
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Expand the 'General' collapsible section
2. 2. Enter emoji and non-Latin Unicode characters into the First_Name field
3. 3. Enter emoji and non-Latin Unicode characters into the Description rich text editor
4. 4. Click the 'Update profile' button

**Original Expected Result:** Unicode input handling visible; after clicking 'Update profile' the profile page refreshes. The saved values either appear exactly as entered (emoji and Unicode characters visible) or an inline validation error is shown indicating unsupported characters. The visible outcome must clearly show whether the characters were saved or rejected.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (Edit Mode enabled)`
- **Observe**:
  - Edit Mode indicator is ON
  - '+ Add a block' button is visible below the Dashboard heading
  - Current blocks listed on the page (e.g., Timeline block, Calendar block)
  - No block titled 'Recently accessed courses' is present in the Dashboard blocks area

**Post-Check**
- **Navigate To**: `Dashboard (complete steps, perform full page reload and re-open Edit Mode)`
- **Observe**:
  - Add a block page/modal is closed
  - 'Recently accessed courses' block is present in the Dashboard blocks area (visible as a block tile with that title)
  - Edit Mode controls (move icon, three-dot menu) are present on the new block
  - Block persists after full page reload
  - Block remains present after toggling Edit Mode off and then on again

**Expected Change**: A 'Recently accessed courses' block is added to the Dashboard blocks area; the Add a block page/modal closes; the new block shows Edit Mode controls and remains present after a full page reload and after toggling Edit Mode off and back on (layout persisted).

---

### [TC-016] Enter leading and trailing whitespace in required First Name and Last Name and save
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Expand the 'General' collapsible section
2. 2. Enter a value with leading and trailing spaces into the First_Name field
3. 3. Enter a value with leading and trailing spaces into the Last_Name field
4. 4. Click the 'Update profile' button

**Original Expected Result:** Whitespace trimming behavior visible; submission succeeds. On the refreshed profile page, the First and Last name values are shown without leading or trailing spaces (whitespace trimmed). If the system treats whitespace-only as empty, submission is blocked and an inline required-field error is shown for the affected field(s).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (Edit mode enabled)`
- **Observe**:
  - No 'Starred courses' block is present in the Dashboard blocks list
  - Current number and order of dashboard blocks (record for comparison)
  - Edit mode indicator is visible

**Post-Check**
- **Navigate To**: `Dashboard (after Add a block dialog closes) — verify both while still in Edit mode and again after exiting Edit mode and reloading the Dashboard`
- **Observe**:
  - 'Starred courses' block is present in the Dashboard blocks list with the title 'Starred courses'
  - 'Starred courses' block displays its expected content area (e.g., list of starred courses or empty-state message)
  - The Add a block page/dialog is closed
  - 'Starred courses' block remains present after exiting Edit mode and after a full page reload

**Expected Change**: A new 'Starred courses' block has been added to the user's Dashboard layout (where none existed in pre-check); the Add a block dialog is closed; the block persists in the layout after exiting Edit mode and after reloading the Dashboard.

---

### [TC-017] Add an Additional Name, remove it, then save (repeating group add-then-remove all)
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Expand the 'Additional names' collapsible section
2. 2. Click to add a new item in Additional_Names_List
3. 3. Enter a value into the Alternative_Name field for the new item
4. 4. Remove the Additional_Names_List item just added
5. 5. Click the 'Update profile' button

**Original Expected Result:** Submission succeeds; because Additional_Names_List has min=0, the form submits successfully and the refreshed profile page shows no additional names entries (no residual empty/ghost entries).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (Edit mode enabled)`
- **Observe**:
  - List of blocks currently on the Dashboard (block names visible)
  - Absence or presence of 'Tags' block (record that 'Tags' block is not present before adding)
  - Edit mode UI indicators (e.g., 'Reset page to default' button, '+ Add a block' button)

**Post-Check**
- **Navigate To**: `Dashboard -> Exit Edit mode -> Navigate to Home -> Navigate back to Dashboard (or reload Dashboard in a new session view)`
- **Observe**:
  - List of blocks currently on the Dashboard (block names visible)
  - Presence of 'Tags' block in the Dashboard block list (visible in the same location as added)
  - Dashboard layout unchanged after navigation/reload (no revert to previous layout)

**Expected Change**: The 'Tags' block appears in the Dashboard blocks list after being added and remains present after exiting Edit mode, navigating away and returning (or reloading), demonstrating the new block was persisted to the user's layout.

---

### [TC-018] Immediately press browser Back after successful Update profile to check for duplicate or stale edit form behavior
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Update profile' button to save changes
2. 2. Wait for the profile page to refresh (successful save)
3. 3. Immediately press the browser Back button

**Original Expected Result:** No duplicate or unintended state; after pressing Back the browser either (a) shows the refreshed profile page (not the edit form), or (b) shows the edit form but with fields blank or reflecting the saved values (not causing a second save). No additional profile entities are created and only the single intended save exists.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard`
- **Observe**:
  - Edit Mode is enabled (Edit controls visible, e.g., 'Reset page to default' and move icons)
  - Presence of a 'Text' block on the Dashboard (should be absent before adding)

**Post-Check**
- **Navigate To**: `Dashboard (then reload the page or navigate to Home and return to Dashboard to confirm persistence)`
- **Observe**:
  - A 'Text' block is present in the Dashboard blocks area
  - The Add a block page/modal is closed
  - Edit Mode remains enabled and block shows move/options controls (three-dot menu) for the new 'Text' block
  - The 'Text' block remains present and in the same location after a full page reload or after navigating away and back

**Expected Change**: A new 'Text' block has been added to the user's Dashboard layout, the Add Block page/modal is closed, and the block persists (remains present in the same location) after navigation or page reload.

---

### [TC-019] Make multiple edits then click Cancel to ensure no changes are saved
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Expand the 'General' collapsible section
2. 2. Change the First_Name field
3. 3. Change the Description rich text editor
4. 4. Click the 'Cancel' button

**Original Expected Result:** Cancel exits without saving; the profile page is shown (or user is navigated away) and the previously saved profile values remain unchanged (the changes made in the edit form are not persisted).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (Edit Mode enabled)`
- **Observe**:
  - presence of 'Upcoming events' block
  - list of visible dashboard blocks (names and positions)
  - Edit Mode toggle state = enabled

**Post-Check**
- **Navigate To**: `Dashboard (after closing Add Block page) -> then reload page and navigate away to Home and back to Dashboard`
- **Observe**:
  - presence of 'Upcoming events' block in the dashboard blocks area (both Edit Mode and normal view)
  - position of 'Upcoming events' block in the blocks list
  - list of visible dashboard blocks (names and positions) after reload and after navigation away/return

**Expected Change**: The 'Upcoming events' block is present in the Dashboard blocks area immediately after adding, is visible in both Edit Mode and normal view, and remains present in the same (or expected) position after a full page reload and after navigating away and returning to the Dashboard, demonstrating the block was added and the layout change persisted.

---

### [TC-021] Confirm enrollment then immediately navigate back to attempt resubmission (avoid duplicate enrollment)
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Enrol users button
2. 2. In User_Search, locate and select an existing user from the dialog results
3. 3. Open the Role dropdown
4. 4. Select a Role for the selected user
5. 5. Click Confirm enrollment
6. 6. After enrollment completes and the participants list updates, use the browser back button (navigate back to the previous page/state)
7. 7. If the enrolment dialog or form appears again, attempt to click Confirm enrollment a second time

**Original Expected Result:** Any attempt to create a duplicate enrollment is blocked; only one enrollment record for the selected user exists in the participants list. The second Confirm enrollment action is either disabled or results in a visible message preventing duplicate creation (no duplicate row appears in the participants table).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (Edit Mode enabled)`
- **Observe**:
  - ordered list of blocks in the Blocks Layout (capture the sequence top-to-bottom / left-to-right)
  - position index of <target block> within the Blocks Layout (e.g., position 1, 2, 3...)
  - visual presence of Move icon on each block

**Post-Check**
- **Navigate To**: `Dashboard -> reload page, then toggle Edit Mode off and back on`
- **Observe**:
  - ordered list of blocks in the Blocks Layout (top-to-bottom / left-to-right)
  - position index of <target block> within the Blocks Layout (e.g., position 1, 2, 3...)
  - visual presence of Move icon on each block

**Expected Change**: The <target block> appears at the new position in the Blocks Layout (its position index equals the position it was dropped into). The overall ordering of blocks reflects the drag-and-drop move. This ordering persists after a page reload and after toggling Edit Mode off and on, demonstrating the layout change is persisted per user.

---

### [TC-023] Open bottom 'With selected users…' bulk actions dropdown with no users selected
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Scroll to the bottom bulk actions area
2. 2. Click the With selected users… dropdown

**Original Expected Result:** Bulk actions menu opens; available bulk action options are visible but actions that operate on selected participants are disabled until at least one participant is checked. The UI shows that no bulk action can be performed without selection (attempting to trigger a bulk action without selection is blocked or results in an inline prompt to select users).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (Edit mode enabled)`
- **Observe**:
  - ordered list of block names/ids as displayed on the Dashboard (record order top-to-bottom, left-to-right)
  - current position/index of '<target block>' within that ordered list
  - Edit mode indicator is visible

**Post-Check**
- **Navigate To**: `Dashboard after page reload and after navigating away and returning (Edit mode enabled)`
- **Observe**:
  - ordered list of block names/ids as displayed on the Dashboard (record order top-to-bottom, left-to-right)
  - current position/index of '<target block>' within that ordered list
  - Edit mode indicator is visible

**Expected Change**: The '<target block>' appears at the new position/index chosen via the Options → Move action; the overall ordering of blocks reflects the move and remains the same after a full page reload and after navigating away from and back to the Dashboard, demonstrating the layout persisted for this user.

---

### [TC-024] Course End Date one day before Course Start Date (enabled) — save blocked with inline error
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <valid Course Full Name> in the Course_Full_Name field
2. 2. Enter <valid Course Short Name> in the Course_Short_Name field
3. 3. Select <valid option> in the Course_Category dropdown
4. 4. Enter <date B> in the Course_Start_Date field
5. 5. Check the Enable_Course_End_Date checkbox
6. 6. Enter <date B minus 1 day> in the Course_End_Date field
7. 7. Click the Save and display button

**Original Expected Result:** Course_End_Date field displays an inline validation error indicating the end date must be on or after the Course_Start_Date and the save action is blocked (error shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (Edit mode enabled)`
- **Observe**:
  - Edit mode is enabled (Edit controls visible)
  - list of visible blocks on the Dashboard (e.g., Timeline block, Calendar block, <target block>)
  - presence of the <target block> in the blocks list / its options menu is available

**Post-Check**
- **Navigate To**: `Navigate away (e.g., Home) then return to Dashboard; reload the Dashboard page; toggle Edit mode off and on`
- **Observe**:
  - list of visible blocks on the Dashboard
  - absence or presence of the <target block>
  - Edit mode controls still function

**Expected Change**: The <target block> is no longer present in the Dashboard blocks list; the total number of blocks on the Dashboard is reduced by one compared to pre_check; the deletion persists after navigating away and returning, after a full page reload, and after toggling Edit mode off and on.

---

### [TC-006] Log out in one tab, then refresh a protected page in another tab
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Tab A, click the 'Log out' button
2. 2. In Tab B, click the browser refresh button (reload the protected page)

**Original Expected Result:** The logout in Tab A succeeds and redirects Tab A to the login page. In Tab B, the refresh is blocked from showing protected content: Tab B is redirected to the login page (access to protected page is blocked).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `My Courses page`
- **Observe**:
  - position/index of the target course card within the list/grid (e.g., 1-based index)
  - starred state of the target course card (star indicator present or absent)
  - top 5 course cards order (identify course names shown in top positions)

**Post-Check**
- **Navigate To**: `My Courses page`
- **Observe**:
  - position/index of the target course card within the list/grid (e.g., 1-based index)
  - starred state of the target course card (star indicator present or absent)
  - top 5 course cards order (identify course names shown in top positions)
  - card menu option for the target course (e.g., 'Unstar this course' should be present)

**Expected Change**: The target course card is pinned to the top (position 1) and shows a Starred indicator; it was not starred and not at position 1 in the pre-check. Other courses previously above it have moved down accordingly. The card menu for the course now presents the opposite action (e.g., 'Unstar this course').

---

### [TC-007] Click Log out while the browser is offline
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. With network offline, click the 'Log out' button

**Original Expected Result:** The client-side logout flow succeeds: the app clears the local authenticated state and displays the login page (user is shown the login page). Subsequent navigation to a protected page remains blocked (the login page is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `My Courses (Teacher view) - default status filter (All)`
- **Observe**:
  - presence of the target course card in the grid (identify by course name used in the test)
  - target course card is visible (not hidden) in the current list
  - target course card shows a three-dot card menu containing 'Remove from view'

**Post-Check**
- **Navigate To**: `My Courses (Teacher view)`
- **Observe**:
  - absence of the target course card from the default course grid
  - status filter control available above the grid
  - after setting status filter to 'Hidden', the target course card appears in the filtered list

**Expected Change**: The target course card is no longer visible in the My Courses default view and is present when filtering by status 'Hidden', indicating the course has been marked Hidden for this teacher (removed from view).

---

### [TC-002] Attempt to use Log out control while not authenticated (precondition violation) - button visibility
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application's main page while not authenticated
2. 2. Inspect the page header and navigation area for a 'Log out' button
3. 3. If a 'Log out' button is present, attempt to click it

**Original Expected Result:** The 'Log out' button is not visible/available to the anonymous user (control is not present or is disabled); clicking it is not possible. The application does not send a logout request and the user remains unauthenticated (no session was terminated).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course page (ensure Edit mode is ON)`
- **Observe**:
  - Edit mode toggle is ON
  - inline edit icon present for the target section
  - current section header name is '<Old section name>' (visible in the section header)
  - section appears with the same name in the Course Index sidebar

**Post-Check**
- **Navigate To**: `Course page (perform a full page reload or navigate away then return to the course)`
- **Observe**:
  - section header name displays '<New section name>' inline on the course page
  - Course Index sidebar lists the section with name '<New section name>'
  - the inline edit icon is still present for that section (confirming Edit mode persisted)
  - the renamed section remains '<New section name>' after reload/navigation

**Expected Change**: The section header name has been changed from '<Old section name>' to '<New section name>' and this new name is reflected both inline on the Course page and in the Course Index sidebar; the change persists after a page reload or navigating away and back.

---

### [TC-004] Direct access to the Logout endpoint while unauthenticated is blocked/redirects to login
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open a browser while not authenticated
2. 2. Enter the application's Logout endpoint URL (<logout endpoint URL>) in the address bar and navigate there

**Original Expected Result:** The application redirects the anonymous user to the Login page instead of performing a logout; no session termination occurs and no protected content is exposed.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course page (Edit mode)`
- **Observe**:
  - list of section titles in the course content area (capture the exact title of the section to be duplicated)
  - total number of sections visible in the course

**Post-Check**
- **Navigate To**: `Course page (Edit mode)`
- **Observe**:
  - list of section titles in the course content area
  - total number of sections visible in the course

**Expected Change**: A new section row exists with the same title text as the original section that was duplicated; the total number of sections has increased by one; the original section remains unchanged and the duplicate appears adjacent to the original (typically immediately after it).

---

### [TC-005] Rapid double-click the Log out button
**Category**: `edge` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Log out' button once
2. 2. Immediately click the 'Log out' button a second time (within 1 second of the first click)

**Original Expected Result:** Only a single logout action succeeds: the user is redirected to the login page and the UI shows the login page. The second click is ignored (no duplicate navigation or duplicate login page stacks are visible).

---

#### Verification Plan

**Actor A (Role: `teacher`)**
- **Action**: Execute the steps from the core test case: while logged in as the teacher with Edit mode ON on the target course page, open the target section's three-dot menu and select 'Hide'. Confirm the teacher UI shows the section marked as Hidden (e.g., 'Hidden' indicator or dimmed styling).

**Actor B (Role: `student`)**
- **Session**: `new_session`
- **Navigate To**: `Course page for the same course -> Course content (sections list)`
- **Action**: 
- **Observe**:
  - presence or absence of the target section's title in the course sections list
  - visibility indicator for the section (e.g., 'Hidden from students' label, dimmed/strikethrough styling)
  - access to activities/resources within that section (activity links should be inaccessible or not shown)

**Expected Change**: The section is hidden from students: the section and its activities are either not visible in the student's course content list or are displayed with a clear 'Hidden' indicator and their links are not accessible.

---

### [TC-006] Log out in one tab, then refresh a protected page in another tab
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Tab A, click the 'Log out' button
2. 2. In Tab B, click the browser refresh button (reload the protected page)

**Original Expected Result:** The logout in Tab A succeeds and redirects Tab A to the login page. In Tab B, the refresh is blocked from showing protected content: Tab B is redirected to the login page (access to protected page is blocked).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Page (ensure Edit mode is ON) -> Sections list`
- **Observe**:
  - full list of section rows with their index/position and titles
  - total number of sections
  - verify and note the exact title (or index) of the section intended for deletion

**Post-Check**
- **Navigate To**: `Refresh Course Page (remain in Edit mode) -> Sections list`
- **Observe**:
  - full list of section rows with their index/position and titles
  - total number of sections

**Expected Change**: The section that was targeted for deletion (as recorded in pre_check by title or index) is no longer present in the sections list; the total number of sections has decreased by one; remaining sections have updated indices/positions as appropriate (i.e., subsequent sections have shifted up to fill the gap).

---

### [TC-009] Enter an invalid email format and attempt to save
**Category**: `negative` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Enter <invalid email format> into the Email_Address field
2. 2. Enter <valid first name> into the First_Name field
3. 3. Enter <valid last name> into the Last_Name field
4. 4. Click the 'Update profile' button

**Original Expected Result:** Inline validation error appears on the Email_Address field indicating the value is not a valid email address; the form does not submit; profile is not updated

---

#### Verification Plan

**Actor A (Role: `teacher`)**
- **Action**: Execute the steps from the core test case (enable Edit mode, perform inline rename of the target activity to <New activity name>, press Enter to save).

**Actor B (Role: `student`)**
- **Session**: `new_session`
- **Navigate To**: `Course page (open the same course where the activity was renamed)`
- **Action**: 
- **Observe**:
  - activity name as listed in the course section content (the activity row label)
  - activity link label used to navigate to the activity
  - Course Index sidebar item for the activity
  - activity page header/title after clicking the activity link

**Expected Change**: The activity previously showing its old title now displays '<New activity name>' in the course section list and in the Course Index sidebar; clicking the activity navigates to the activity page whose header/title also shows '<New activity name>'.

---

### [TC-012] Upload file exactly at the site's maximum allowed upload size and save
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Expand the 'User picture' collapsible section
2. 2. Drag-and-drop the file that is exactly the site's maximum allowed upload size onto the Picture_Upload area
3. 3. Click the 'Update profile' button

**Original Expected Result:** Upload and save succeeds; clicking 'Update profile' submits successfully, the profile page refreshes, and the new picture is visible on the profile page (picture replaced by the uploaded file).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course page (specific course where duplication will occur) with Edit mode ON`
- **Observe**:
  - location of the original activity (section and position)
  - original activity title
  - count of activities in that section

**Post-Check**
- **Navigate To**: `Course page (same course) — first with Edit mode ON, then with Edit mode OFF (student view)`
- **Observe**:
  - presence of an additional activity row in the same section
  - activity titles in that section (original title should appear twice)
  - count of activities in that section (should be previous count + 1)
  - that the duplicated row has its own three-dot menu / action controls
  - open the duplicated activity's settings or view page and confirm it loads a distinct URL/module id and shows the same title

**Expected Change**: A new activity row with the exact same title as the original appears in the same section; the section's activity count has increased by one; the duplicate is a distinct activity instance (has its own action menu and settings/view page with a different URL/module id).

---

### [TC-013] Upload file one unit over the site's maximum allowed upload size and attempt to save
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Expand the 'User picture' collapsible section
2. 2. Drag-and-drop the file that is one unit over the site's maximum allowed upload size onto the Picture_Upload area
3. 3. Click the 'Update profile' button

**Original Expected Result:** Upload is blocked / error shown; submission is blocked and an inline error is shown near the Picture_Upload field indicating the file exceeds the site's maximum allowed upload size, and the profile page does not refresh.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course page (Edit mode ON) -> section containing the target activity`
- **Observe**:
  - the target activity listed in its section (identify by activity name)
  - activity visibility indicator shows it is Visible (no 'Hidden' label or dimmed styling)
  - activity three-dot menu contains the 'Hide' action

**Post-Check**
- **Navigate To**: `Course page (Edit mode ON) -> same section containing the target activity`
- **Observe**:
  - the target activity is still listed in the section (identify by activity name)
  - a 'Hidden' indicator is present OR the activity is visually marked as hidden (e.g., dimmed, greyed-out, or annotated as Hidden)
  - the activity three-dot menu now contains the 'Show' action instead of 'Hide'

**Expected Change**: The targeted activity's visibility changed from Visible to Hidden: the activity now displays a 'Hidden' indicator or hidden visual styling, and the activity menu offers 'Show' (reveal) instead of 'Hide'.

---

### [TC-015] Enter emoji and non-Latin Unicode characters into Description and First Name fields and save
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Expand the 'General' collapsible section
2. 2. Enter emoji and non-Latin Unicode characters into the First_Name field
3. 3. Enter emoji and non-Latin Unicode characters into the Description rich text editor
4. 4. Click the 'Update profile' button

**Original Expected Result:** Unicode input handling visible; after clicking 'Update profile' the profile page refreshes. The saved values either appear exactly as entered (emoji and Unicode characters visible) or an inline validation error is shown indicating unsupported characters. The visible outcome must clearly show whether the characters were saved or rejected.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course page -> the section containing the target activity (ensure Edit mode is ON)`
- **Observe**:
  - activity name (the specific activity targeted for deletion)
  - count of activities listed in that section

**Post-Check**
- **Navigate To**: `Course page -> the same section containing the target activity (refresh the page or toggle Edit mode OFF then ON to ensure backend state is loaded)`
- **Observe**:
  - activity name (the specific activity targeted for deletion)
  - count of activities listed in that section

**Expected Change**: The targeted activity name is no longer present in the section's activity list and the section's activity count has decreased by one compared to the pre-check.

---

### [TC-017] Add an Additional Name, remove it, then save (repeating group add-then-remove all)
**Category**: `edge` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Expand the 'Additional names' collapsible section
2. 2. Click to add a new item in Additional_Names_List
3. 3. Enter a value into the Alternative_Name field for the new item
4. 4. Remove the Additional_Names_List item just added
5. 5. Click the 'Update profile' button

**Original Expected Result:** Submission succeeds; because Additional_Names_List has min=0, the form submits successfully and the refreshed profile page shows no additional names entries (no residual empty/ghost entries).

---

#### Verification Plan

**Actor A (Role: `teacher`)**
- **Action**: Execute the steps from the core test case to add a subsection under a chosen parent section with the title '<Subsection_Title>'.

**Actor B (Role: `student`)**
- **Session**: `new_session`
- **Navigate To**: `Course page -> locate the parent section where the subsection was added`
- **Action**: 
- **Observe**:
  - a subsection row with the title '<Subsection_Title>' is present
  - the subsection is displayed nested/indented under the specified parent section (shows hierarchy or nested indicator)
  - the parent's subsection count (or list) has increased by one relative to the prior state

**Expected Change**: A new subsection appears in the course content nested under the parent section with the entered title '<Subsection_Title>'; it is shown as a child row (indented or with a nested indicator) immediately under the parent section and the parent's subsection count increases by one.

---

### [TC-018] Immediately press browser Back after successful Update profile to check for duplicate or stale edit form behavior
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Update profile' button to save changes
2. 2. Wait for the profile page to refresh (successful save)
3. 3. Immediately press the browser Back button

**Original Expected Result:** No duplicate or unintended state; after pressing Back the browser either (a) shows the refreshed profile page (not the edit form), or (b) shows the edit form but with fields blank or reflecting the saved values (not causing a second save). No additional profile entities are created and only the single intended save exists.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course page (Edit mode ON)`
- **Observe**:
  - ordered list of section titles (record full sequence)
  - index/position of the specific section to be moved (record numeric position and section title/ID)
  - visual indicator that Edit mode is ON (e.g., Edit mode toggle/state)

**Post-Check**
- **Navigate To**: `Course page (after performing the drag-and-drop), then refresh page and toggle Edit mode OFF and revisit the course page`
- **Observe**:
  - ordered list of section titles (record full sequence after move)
  - index/position of the moved section (record numeric position and section title/ID)
  - positions of other sections relative to pre_check (verify they shifted as expected)
  - Edit mode indicator (confirm state when checked with Edit mode OFF and after page reload)

**Expected Change**: The moved section appears at the new position in the sections list (its recorded index changes from the pre_check value to the new index). Other sections' positions update accordingly. The new ordering persists after a full page refresh and when Edit mode is turned OFF and the course page is revisited, demonstrating the backend state was updated.

---

### [TC-019] Make multiple edits then click Cancel to ensure no changes are saved
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Expand the 'General' collapsible section
2. 2. Change the First_Name field
3. 3. Change the Description rich text editor
4. 4. Click the 'Cancel' button

**Original Expected Result:** Cancel exits without saving; the profile page is shown (or user is navigated away) and the previously saved profile values remain unchanged (the changes made in the edit form are not persisted).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course page (ensure Edit mode is ON) -> Relevant section containing the activities`
- **Observe**:
  - names/identifiers of the activities that are selected for the bulk action
  - current visibility/status badges or icons for each selected activity (e.g., Visible, Hidden)
  - current section location or position index for each selected activity
  - total activity count in the source section

**Post-Check**
- **Navigate To**: `Course page (refresh the page and remain in Edit mode) -> Same section(s) as pre-check and any target section(s) if applicable`
- **Observe**:
  - names/identifiers of the previously selected activities
  - visibility/status badges or icons for those activities
  - section location or position index for those activities
  - activity count in the source section and in the target section (if move/duplicate was applied)

**Expected Change**: The previously selected activities persistently reflect the chosen bulk operation: for example, if 'Hide' was applied their visibility badge changes from Visible to Hidden; if 'Show' was applied the badge changes to Visible; if 'Move to section X' the activities no longer appear in the original section and appear under section X at the expected position; if 'Duplicate' additional copies appear (n+number_of_duplicates) with identifiable names/markers; if 'Delete' the activities are no longer present; for status/configuration operations the corresponding indicator or setting for each affected activity is updated. These changes remain visible after a page refresh.

---

### [TC-022] First name alphabetical filter when no participants match the chosen initial
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the First name alphabet filter control
2. 2. Select the alphabet letter <chosen initial>

**Original Expected Result:** Filter selection succeeds; the participants table updates to show zero rows (an empty state is visible) indicating no participants match the selected initial. The UI reflects the active filter (the chosen letter is highlighted).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course page (with Edit mode ON) -> click '+ Add an activity or resource' to open the Activity Chooser modal`
- **Observe**:
  - identify the target activity tile by label and type (e.g., 'Assignment')
  - target tile star/favorite icon state (record as 'favorited' if filled/active, or 'not favorited' if outline/inactive)

**Post-Check**
- **Navigate To**: `From the course page, close the Activity Chooser, navigate elsewhere on the course page (e.g., a different section) then click '+ Add an activity or resource' again to re-open the Activity Chooser modal`
- **Observe**:
  - the same target activity tile by label and type (must match pre_check identification)
  - target tile star/favorite icon state (filled/active vs outline/inactive)
  - any change in tile placement or visual highlighting associated with favorited tiles (if applicable)

**Expected Change**: The target tile's star/favorite icon state is the opposite of what was recorded in pre_check (if pre_check recorded 'not favorited', post_check shows 'favorited', and vice versa). The toggled favorite state persists when the Activity Chooser is closed and reopened in the same user session.

---

### [TC-001] Click 'Log out' button terminates session and redirects to Login page
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Log out' button

**Original Expected Result:** terminates the current authenticated session and redirects to the login page; the Login page is displayed and the login form prompting for credentials is visible

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course page -> Activities / Assignments section (Course main page)`
- **Observe**:
  - No assignment with name <assignment name> exists in the Assignments list

**Post-Check**
- **Navigate To**: `Course page -> Assignments list; open the newly created <assignment name> to view its settings`
- **Observe**:
  - Assignment appears in the Assignments list with name <assignment name>
  - Assignment settings / Submission types shows 'File submissions' enabled
  - Max number of uploaded files equals <integer>
  - Maximum submission size equals <number> MB
  - Accepted file types displays <accepted file types>
  - Group submission settings shows 'Group submissions' enabled
  - Require all group members to submit is checked
  - Grouping selection shows <grouping> selected
  - Access restrictions list contains the configured <restriction type>
  - Linked competencies includes <competency type>
  - Browser was redirected to the course page after clicking 'Save and return to course'

**Expected Change**: A new assignment named <assignment name> exists in the course. Its submission type is configured to allow File submissions with max files = <integer>, maximum submission size = <number> MB, and accepted file types = <accepted file types>. Group submissions are enabled with 'Require all group members to submit' checked and grouping = <grouping>. The specified access restriction (<restriction type>) is present and the selected competency (<competency type>) is linked. The teacher was returned to the course page after saving.

---

### [TC-002] Attempt to use Log out control while not authenticated (precondition violation) - button visibility
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application's main page while not authenticated
2. 2. Inspect the page header and navigation area for a 'Log out' button
3. 3. If a 'Log out' button is present, attempt to click it

**Original Expected Result:** The 'Log out' button is not visible/available to the anonymous user (control is not present or is disabled); clicking it is not possible. The application does not send a logout request and the user remains unauthenticated (no session was terminated).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course page -> Activities tab -> Assignments section`
- **Observe**:
  - no activity with name '<assignment name>' present in the Assignments list

**Post-Check**
- **Navigate To**: `New assignment page (opened after 'Save and display') and Course page -> Activities tab -> Assignments section`
- **Observe**:
  - assignment name '<assignment name>' displayed as the page heading and present in the course Assignments list
  - Submission types shows 'File submissions' enabled
  - Max number of uploaded files equals '<integer>'
  - Maximum submission size equals '<number>' MB
  - Accepted file types equals '<accepted file types>'
  - Group submission settings shows 'Group submissions' enabled
  - Selected grouping equals '<grouping>'

**Expected Change**: A new assignment named '<assignment name>' has been created and is visible; File submissions are enabled with the configured max files, maximum submission size (MB), and accepted file types; Group submissions are enabled and the specified grouping is assigned.

---

### [TC-004] Direct access to the Logout endpoint while unauthenticated is blocked/redirects to login
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open a browser while not authenticated
2. 2. Enter the application's Logout endpoint URL (<logout endpoint URL>) in the address bar and navigate there

**Original Expected Result:** The application redirects the anonymous user to the Login page instead of performing a logout; no session termination occurs and no protected content is exposed.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course page -> target section where the assignment will be added`
- **Observe**:
  - No activity or resource with name '<assignment name>' is listed in the section activity list

**Post-Check**
- **Navigate To**: `Course page -> target section where the assignment was added; then click the '<assignment name>' link to open the Assignment page and open the Settings tab`
- **Observe**:
  - Assignment name displayed as '<assignment name>' in the section activity list
  - Assignment page opens for '<assignment name>'
  - Settings tab shows Submission types: 'File submissions' is enabled/checked
  - Settings tab shows 'Max number of uploaded files' = <integer>
  - Settings tab shows 'Maximum submission size' = <number> MB
  - Settings tab shows 'Accepted file types' contains '<accepted file types>'
  - Settings tab shows Group submission settings: Group submissions is unchecked/disabled

**Expected Change**: The newly created assignment '<assignment name>' appears in the course section list and its saved configuration reflects File submissions enabled with Max number of uploaded files = <integer>, Maximum submission size = <number> MB, Accepted file types = '<accepted file types>', and Group submissions disabled.

---

### [TC-005] Rapid double-click the Log out button
**Category**: `edge` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Log out' button once
2. 2. Immediately click the 'Log out' button a second time (within 1 second of the first click)

**Original Expected Result:** Only a single logout action succeeds: the user is redirected to the login page and the UI shows the login page. The second click is ignored (no duplicate navigation or duplicate login page stacks are visible).

---

#### Verification Plan

**Actor A (Role: `teacher`)**
- **Action**: Execute the steps from the core test case to create the assignment (Save and display) with File submissions enabled and Group submissions disabled.

**Actor B (Role: `student`)**
- **Session**: `new_session`
- **Navigate To**: `Course X -> Activities tab -> Assignments section (or Course page where the assignment was added)`
- **Action**: 
- **Observe**:
  - assignment name present in the Assignments list
  - clicking the assignment name opens the assignment page
  - on the assignment page: 'Add submission' button is visible
  - submission form contains a file upload area / file picker (drag-and-drop or choose files)
  - submission UI indicates or enforces the configured maximum number of uploaded files and maximum file size and accepts configured file types
  - no requirement or prompt forcing a group submission (individual submission is possible)

**Expected Change**: The assignment created by the teacher appears in the course's Assignments list and, when opened by the student, the submission interface provides a file upload area that reflects the configured file-submission constraints (max files, max size, accepted types) and allows individual (non-group) submission.

---

### [TC-007] Click Log out while the browser is offline
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. With network offline, click the 'Log out' button

**Original Expected Result:** The client-side logout flow succeeds: the app clears the local authenticated state and displays the login page (user is shown the login page). Subsequent navigation to a protected page remains blocked (the login page is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course page -> Activities tab -> Assignments section`
- **Observe**:
  - List of assignment names in the Assignments section (confirm <assignment name> is NOT present prior to creation)

**Post-Check**
- **Navigate To**: `Course page -> Activities tab -> Assignments section -> Click <assignment name> -> Settings tab`
- **Observe**:
  - Assignment name: <assignment name> is present in the Assignments section
  - Assignment Settings panel is visible
  - Submission types panel: 'File submissions' checkbox is unchecked/disabled
  - Group submission settings panel: 'Group submissions' checkbox is checked/enabled
  - Group submission settings panel: selected grouping == <grouping>

**Expected Change**: A new assignment named <assignment name> appears in the course. Its persisted settings show File submissions disabled (unchecked) and Group submissions enabled with the grouping set to <grouping>.

---

### [TC-008] Use browser Back after successful logout
**Category**: `edge` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Log out' button
2. 2. After being redirected to the login page, press the browser Back button once

**Original Expected Result:** Returning via the browser Back button does not restore access to the previously viewed protected page: the user remains on or is redirected back to the login page and access to protected content is blocked.

---

#### Verification Plan

**Actor A (Role: `teacher`)**
- **Action**: Execute the steps from the core test case to create the assignment with File submissions OFF and Group submissions ON.

**Actor B (Role: `student`)**
- **Session**: `new_session`
- **Navigate To**: `Course -> Activities tab -> Assignments section, then open the assignment named <assignment name>`
- **Action**: 
- **Observe**:
  - Assignment appears in the Assignments list with the name <assignment name>
  - On the assignment page: metadata (Opened date, Due date, Description) is visible
  - Submission area does NOT show any file upload controls or 'File submissions' links/fields
  - Submission area shows a group-submission indicator (e.g., 'Group submission: Yes', 'Submit in groups', or displays group name/ <grouping>)
  - If the submission form permits submitting, the available submission types do not include file uploads (e.g., only online text editor is present if enabled)
  - Submission status table or summary indicates submissions are by group or references the student's group membership

**Expected Change**: The new assignment <assignment name> appears in the course Assignments list and on its assignment page; group submissions are enabled (students see a clear group-submission indicator or group name) and file-upload submission controls are absent from the submission area.

---

### [TC-010] Upload a file that violates site upload constraints and submit
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attach <file violating site upload constraints> to the Picture_Upload control (via drag-and-drop or file picker)
2. 2. Enter <valid first name> into the First_Name field
3. 3. Enter <valid last name> into the Last_Name field
4. 4. Enter <valid email address> into the Email_Address field
5. 5. Click the 'Update profile' button

**Original Expected Result:** Upload control displays an error indicating the file violates site upload constraints (e.g. file type or size invalid); the form does not submit; profile is not updated

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course page (target course) -> Activities / Section listing`
- **Observe**:
  - list of activity/resource names in the target section
  - absence of an activity with name '<assignment name>'

**Post-Check**
- **Navigate To**: `Course page (target course) -> Activities / Section listing; then click the activity link '<assignment name>' to open its Assignment page`
- **Observe**:
  - '<assignment name>' is present in the section activity list as an Assignment activity (clickable link)
  - Assignment page shows Submission types or settings indicating File submissions are disabled
  - Assignment page shows Group submission settings indicating Group submissions are disabled

**Expected Change**: An Assignment named '<assignment name>' exists on the course page where none existed before; opening the assignment confirms File submissions are disabled and Group submissions are disabled.

---

### [TC-011] Unauthenticated user attempts to access Edit profile page
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Navigate to the Edit profile page URL while signed out

**Original Expected Result:** User is redirected to the login page (Edit profile page is not accessible); no profile edit controls are shown to the unauthenticated user

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course page (Course X) -> Activities list / Course content`
- **Observe**:
  - No activity with the title '<assignment name>' is present in the course content
  - No existing assignment entry with title '<assignment name>' in Activities/Assignments list

**Post-Check**
- **Navigate To**: `New assignment page (click the assignment link titled '<assignment name>' in course content) or Course page -> Activities list -> open the assignment`
- **Observe**:
  - Assignment title equals '<assignment name>'
  - Submission types section shows File submissions unchecked/absent and Online text (if present) as the enabled submission type
  - Group submission settings show 'Group submissions' = Off / 'No' (no group submission enabled)
  - Page displays assignment metadata (Opened date / Due date / Description) confirming persisted record

**Expected Change**: An assignment titled '<assignment name>' has been created and persisted in the course. Its settings show File submissions disabled and Group submissions disabled, and the assignment page is accessible (Save and display persisted and navigable).

---

### [TC-001] Click 'Log out' button terminates session and redirects to Login page
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Log out' button

**Original Expected Result:** terminates the current authenticated session and redirects to the login page; the Login page is displayed and the login form prompting for credentials is visible

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Settings page (teacher view) — form is open`
- **Observe**:
  - Course full name field (current value)
  - Course short name field (current value)
  - Course category dropdown (current selection)
  - Course end date Enable toggle (checked/unchecked)
  - Course format dropdown (current selection)
  - Layout controls region (visibility for selected format)
  - Groups -> Group mode setting (current selection)
  - Save and display button is present

**Post-Check**
- **Navigate To**: `Course page -> Click 'Settings' tab -> Open 'Course settings' (teacher view)`
- **Observe**:
  - Course page heading shows the saved Course full name
  - Course full name field value
  - Course short name field value
  - Course category dropdown selection
  - Course end date Enable toggle state
  - Course format dropdown selection
  - Layout controls region visibility for Topics format
  - Groups -> Group mode selection

**Expected Change**: After saving, the app returned to the course page and the Course Settings persist the entered values: Course full name and short name match the submitted values; Course category is the selected category; Course End Date remains disabled (Enable unchecked); Course format is set to 'Topics format' and the Topics-specific layout controls are visible; Groups group mode is set to 'No groups'.

---

### [TC-002] Attempt to use Log out control while not authenticated (precondition violation) - button visibility
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application's main page while not authenticated
2. 2. Inspect the page header and navigation area for a 'Log out' button
3. 3. If a 'Log out' button is present, attempt to click it

**Original Expected Result:** The 'Log out' button is not visible/available to the anonymous user (control is not present or is disabled); clicking it is not possible. The application does not send a logout request and the user remains unauthenticated (no session was terminated).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Settings page (edit form)`
- **Observe**:
  - Course full name (current value)
  - Course short name (current value)
  - Course category (current selection)
  - Course end date Enable toggle state
  - Course format (current selection)
  - Presence of layout controls for the selected format
  - Groups -> Group mode (current selection)
  - Groups -> Grouping (current selection or 'None')

**Post-Check**
- **Navigate To**: `Course page, then reopen Course Settings page (edit form)`
- **Observe**:
  - Course full name (saved value)
  - Course short name (saved value)
  - Course category (saved selection)
  - Course end date Enable toggle state
  - Course format (saved selection)
  - Presence of layout controls for Topics format
  - Groups -> Group mode (saved selection)
  - Groups -> Grouping (saved selection)

**Expected Change**: After clicking 'Save and display' the user is returned to the course page and the persisted Course Settings reflect the inputs: Course full name and short name match the entered values; Course category matches the selected category; the Course End Date Enable toggle is unchecked (End Date disabled); Course Format is set to 'Topics format' and Topics-specific layout controls are visible; Groups Group Mode is set to the selected non-'No groups' value; Groups Grouping is set to the selected grouping.

---

### [TC-003] After logging out, accessing a protected page is blocked (post-logout access requires re-authentication)
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Log in as <role>
2. 2. Click the 'Log out' button
3. 3. Observe that the application redirects to the Login page (post-logout)
4. 4. From the browser address bar, navigate to a protected page at <protected page URL>

**Original Expected Result:** Navigation to <protected page URL> is blocked and the user is redirected to the Login page; protected page content is not displayed and re-authentication is required (session remains terminated).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Settings (Edit course settings form for the target course)`
- **Observe**:
  - Course full name (current value)
  - Course short name (current value)
  - Course category (current selection)
  - Course end date enabled toggle (checked/unchecked)
  - Course format (current selection)
  - Layout controls visibility for Weekly format (visible/hidden)
  - Groups group mode (current selection)

**Post-Check**
- **Navigate To**: `Course Settings (re-open Edit course settings form for the same course after saving)`
- **Observe**:
  - Course full name
  - Course short name
  - Course category
  - Course end date enabled toggle
  - Course format
  - Layout controls visibility for Weekly format
  - Groups group mode

**Expected Change**: Course full name matches the entered value; Course short name matches the entered value; Course category matches the selected category; Course end date enabled toggle remains unchecked (End Date disabled); Course format is set to 'Weekly format' and the weekly layout controls are visible; Groups group mode is set to 'No groups'.

---

### [TC-004] Direct access to the Logout endpoint while unauthenticated is blocked/redirects to login
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open a browser while not authenticated
2. 2. Enter the application's Logout endpoint URL (<logout endpoint URL>) in the address bar and navigate there

**Original Expected Result:** The application redirects the anonymous user to the Login page instead of performing a logout; no session termination occurs and no protected content is exposed.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Settings page (for the course) - current state before making changes`
- **Observe**:
  - Course full name
  - Course short name
  - Course category
  - Course end date enabled state (checked/unchecked)
  - Course format
  - Visibility of layout controls for current format
  - Groups Group mode
  - Groups Grouping selection

**Post-Check**
- **Navigate To**: `Course Settings page (for the course) - after clicking 'Save and display' and returning to Course Settings to confirm persistence`
- **Observe**:
  - Course full name
  - Course short name
  - Course category
  - Course end date enabled state (checked/unchecked)
  - Course format
  - Visibility of layout controls for Weekly format
  - Groups Group mode
  - Groups Grouping selection

**Expected Change**: Course settings persist the saved values: Course full name and Course short name match the entered values; Course category matches the selected category; Course End Date remains disabled (unchecked) so no end date is configured; Course Format is set to 'Weekly' and Weekly-specific layout controls are visible; Groups Group mode is set to the selected non-'No groups' option and the Groups Grouping dropdown shows the chosen grouping. Additionally, the 'Save and display' action returned the user to the course page before re-opening Course Settings to verify persistence.

---

### [TC-005] Rapid double-click the Log out button
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Log out' button once
2. 2. Immediately click the 'Log out' button a second time (within 1 second of the first click)

**Original Expected Result:** Only a single logout action succeeds: the user is redirected to the login page and the UI shows the login page. The second click is ignored (no duplicate navigation or duplicate login page stacks are visible).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Settings page (current state before changes)`
- **Observe**:
  - Course full name
  - Course short name
  - Course category
  - Course start date
  - Course end date enabled (true/false)
  - Course end date value (if enabled)
  - Course format
  - Layout controls visibility for Topics format
  - Groups -> Group mode

**Post-Check**
- **Navigate To**: `Course Settings page (open after Save and display)`
- **Observe**:
  - Course full name
  - Course short name
  - Course category
  - Course start date
  - Course end date enabled (true/false)
  - Course end date value (if enabled)
  - Course format
  - Layout controls visibility for Topics format
  - Groups -> Group mode

**Expected Change**: All Course Settings reflect the values entered in the test steps: Course full name and Course short name match the entered values; Course category matches the selected category; Course start date matches the entered start date; Course End Date toggle is enabled and the end date equals the entered end date (which is >= start date); Course format is set to 'Topics format' and the Topics-specific layout controls are visible; Group mode is set to 'No groups'. Additionally, the action redirected to the course main page after saving (Save and display).

---

### [TC-006] Log out in one tab, then refresh a protected page in another tab
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Tab A, click the 'Log out' button
2. 2. In Tab B, click the browser refresh button (reload the protected page)

**Original Expected Result:** The logout in Tab A succeeds and redirects Tab A to the login page. In Tab B, the refresh is blocked from showing protected content: Tab B is redirected to the login page (access to protected page is blocked).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course page -> Settings -> Edit course settings (Course Settings form)`
- **Observe**:
  - Course full name
  - Course short name
  - Course category
  - Course start date
  - Course end date enabled toggle state and Course end date value
  - Course format
  - Visibility of Topics layout controls
  - Groups Group mode
  - Groups Grouping

**Post-Check**
- **Navigate To**: `Course page -> Settings -> Edit course settings (Course Settings form)`
- **Observe**:
  - Course full name
  - Course short name
  - Course category
  - Course start date
  - Course end date enabled toggle state and Course end date value
  - Course format
  - Visibility of Topics layout controls
  - Groups Group mode
  - Groups Grouping

**Expected Change**: The Course Settings persist the entered values: Course Full Name and Course Short Name match the inputs; Course Category matches selection; Course Start Date equals the entered start date; Course End Date toggle is enabled and the Course End Date equals the entered end date; Course Format is set to 'Topics' and Topics-specific layout controls are visible; Groups Group mode is set to the selected non-'No groups' option and Groups Grouping equals the chosen grouping. The application has returned to the course page after saving.

---

### [TC-007] Click Log out while the browser is offline
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. With network offline, click the 'Log out' button

**Original Expected Result:** The client-side logout flow succeeds: the app clears the local authenticated state and displays the login page (user is shown the login page). Subsequent navigation to a protected page remains blocked (the login page is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course Settings page (Edit course settings) for the target course`
- **Observe**:
  - Course full name (current value)
  - Course short name (current value)
  - Course category (current selection)
  - Course start date (current value)
  - Course end date toggle state (enabled/disabled) and end date value if enabled
  - Course format selection (current value)
  - Presence/visibility of Weekly-format specific layout controls
  - Groups -> Group mode selection (current value)

**Post-Check**
- **Navigate To**: `Course page -> open Course Settings page (Edit course settings) for the same course`
- **Observe**:
  - Course full name equals the entered Course Full Name
  - Course short name equals the entered Course Short Name
  - Course category equals the selected Course Category
  - Course start date equals the entered Course Start Date
  - Course end date toggle is enabled
  - Course end date equals the entered Course End Date
  - Course format is set to 'Weekly format'
  - Weekly-format layout controls are visible
  - Groups -> Group mode is set to 'No groups'
  - Course page heading (after Save and display) matches the entered Course Full Name

**Expected Change**: Course settings were persisted: the Course full name and short name reflect the entered values; Course category and start date match the selections; Course End Date toggle is enabled and the End Date equals the entered date; Course format is set to 'Weekly format' and weekly-specific layout controls are visible; Group mode is set to 'No groups'. The user is returned to the course page whose heading matches the saved Course full name.

---

### [TC-008] Use browser Back after successful logout
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Log out' button
2. 2. After being redirected to the login page, press the browser Back button once

**Original Expected Result:** Returning via the browser Back button does not restore access to the previously viewed protected page: the user remains on or is redirected back to the login page and access to protected content is blocked.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Course settings (Edit course settings)`
- **Observe**:
  - Course full name field (current value)
  - Course short name field (current value)
  - Course category dropdown (selected value)
  - Course start date field (current value)
  - Course end date Enable toggle state
  - Course end date field value (if enabled)
  - Course format selector (current selection)
  - Weekly-format specific layout controls visibility
  - Groups -> Group mode selector (current selection)
  - Groups -> Grouping dropdown (selected value)

**Post-Check**
- **Navigate To**: `Course page (verify heading) -> Course settings (Edit course settings)`
- **Observe**:
  - Course page heading (course full name)
  - Course full name field (value after save)
  - Course short name field (value after save)
  - Course category dropdown (selected value after save)
  - Course start date field (value after save)
  - Course end date Enable toggle state after save
  - Course end date field value after save (if enabled)
  - Course format selector (value after save)
  - Weekly-format specific layout controls visibility after save
  - Groups -> Group mode selector (value after save)
  - Groups -> Grouping dropdown (selected value after save)

**Expected Change**: After saving and returning to the course then reopening Edit course settings, all entered values persist: the Course full name and short name equal the entered values and the course page heading shows the full name; Course category equals the selected category; Start date equals the entered start date; the Course End Date toggle remains enabled and the End Date matches the entered date; Course Format is set to 'Weekly format' and the weekly-specific layout controls are visible; Groups Group mode is set to the chosen non-'No groups' option and the Groups Grouping dropdown shows the selected grouping.

---

### [TC-005] Rapid double-click the Log out button
**Category**: `edge` | **Verification Type**: `cross_actor` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Log out' button once
2. 2. Immediately click the 'Log out' button a second time (within 1 second of the first click)

**Original Expected Result:** Only a single logout action succeeds: the user is redirected to the login page and the UI shows the login page. The second click is ignored (no duplicate navigation or duplicate login page stacks are visible).

---

#### Verification Plan

**Actor A (Role: `teacher`)**
- **Action**: Execute the steps from the core test case.

**Actor B (Role: `student`)**
- **Session**: `new_session`
- **Navigate To**: `My Courses page; then open the enrolled Course -> Participants page`
- **Action**: 
- **Observe**:
  - course card for <course> present on My Courses
  - participants list contains a row for <matching result>
  - role column for <matching result>'s row shows <role>

**Expected Change**: The user <matching result> now appears in My Courses as a card for <course>, and on the Course's Participants page their entry exists with the role set to <role>.

---

### [TC-003] After logging out, accessing a protected page is blocked (post-logout access requires re-authentication)
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Log in as <role>
2. 2. Click the 'Log out' button
3. 3. Observe that the application redirects to the Login page (post-logout)
4. 4. From the browser address bar, navigate to a protected page at <protected page URL>

**Original Expected Result:** Navigation to <protected page URL> is blocked and the user is redirected to the Login page; protected page content is not displayed and re-authentication is required (session remains terminated).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Assignment Submissions page (the assignment used in the test)`
- **Observe**:
  - Quick Grading checkbox is checked/enabled
  - At least one submission row contains an inline grade input field (editable input) in the grade column
  - Quick Grading 'Save changes' control or related quick-grading UI is visible

**Post-Check**
- **Navigate To**: `Assignment Submissions page (refresh the page or navigate away and back to ensure persisted state)`
- **Observe**:
  - Quick Grading checkbox is unchecked/disabled
  - No inline grade input fields exist in the submissions table; grade cells render as static, non-editable text
  - Clicking a grade cell does not open an inline editor or input field
  - Quick Grading 'Save changes' control is hidden or disabled

**Expected Change**: Quick Grading is turned off (checkbox unchecked) and inline grade entry inputs are removed from the submissions table; grades are displayed as non-editable static text and clicking grade cells does not open an inline editor.

---

### [TC-001] Click 'Log out' button terminates session and redirects to Login page
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Log out' button

**Original Expected Result:** terminates the current authenticated session and redirects to the login page; the Login page is displayed and the login form prompting for credentials is visible

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Gradebook -> Grader report`
- **Observe**:
  - Locate the target activity's column header in the grades table (the same activity being edited in the test)
  - Note the displayed grade range or max-points indicator in the column header (e.g., '/ 100' or scale name)
  - Open the column header action menu and open 'Edit activity grade settings' to view the current maximum grade / grade scale value in the dialog (record the value)

**Post-Check**
- **Navigate To**: `Gradebook -> Grader report (refresh the page or reopen the report after saving)`
- **Observe**:
  - Target activity's column header displays the updated grade range or updated max-points indicator consistent with the saved settings
  - Open the column header action menu and open 'Edit activity grade settings' — the dialog shows the updated maximum grade / grade scale and other changed settings
  - Any transient confirmation message has disappeared but the updated values persist in the UI (header and settings dialog)

**Expected Change**: After saving, the activity's grade settings persist: the column header now shows the updated grade range/max-points or grading scale, and reopening 'Edit activity grade settings' displays the new maximum grade and settings entered in the test.

---

### [TC-002] Attempt to use Log out control while not authenticated (precondition violation) - button visibility
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application's main page while not authenticated
2. 2. Inspect the page header and navigation area for a 'Log out' button
3. 3. If a 'Log out' button is present, attempt to click it

**Original Expected Result:** The 'Log out' button is not visible/available to the anonymous user (control is not present or is disabled); clicking it is not possible. The application does not send a logout request and the user remains unauthenticated (no session was terminated).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Gradebook -> Grader report`
- **Observe**:
  - Target student's grade cell for the selected activity (identify by student name/row and activity column) — record current value as prior_grade
  - No recent transient confirmation message about grade updates visible

**Post-Check**
- **Navigate To**: `Gradebook -> Grader report (refresh the page or navigate away and return to ensure persistence)`
- **Observe**:
  - Target student's grade cell for the selected activity (value should match the grade entered in the Edit Grade Entry dialog)
  - Optional transient confirmation message indicating the grade was updated (e.g., 'updates single grade entry') may appear once

**Expected Change**: The target student's grade cell value is updated from the prior value to the newly entered grade (<entered grade>) and remains updated after a page refresh or after navigating away and back to the Grader report; an optional transient confirmation message may be shown once.

---

### [TC-003] After logging out, accessing a protected page is blocked (post-logout access requires re-authentication)
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Log in as <role>
2. 2. Click the 'Log out' button
3. 3. Observe that the application redirects to the Login page (post-logout)
4. 4. From the browser address bar, navigate to a protected page at <protected page URL>

**Original Expected Result:** Navigation to <protected page URL> is blocked and the user is redirected to the Login page; protected page content is not displayed and re-authentication is required (session remains terminated).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Gradebook — Grader report page (Course -> Grades -> Grader report)`
- **Observe**:
  - current value(s) of the grade cell(s) for the student row(s) that will be edited in the selected activity column(s)
  - class average value shown in the Overall average row for the affected activity column(s)

**Post-Check**
- **Navigate To**: `Gradebook — Grader report page (refresh the page or navigate away and back to ensure server-side persistence)`
- **Observe**:
  - edited value(s) of the grade cell(s) for the same student row(s) in the affected activity column(s)
  - class average value shown in the Overall average row for the affected activity column(s)

**Expected Change**: The edited grade cell(s) display the new entered value(s); the class average in the Overall average row for each affected activity column reflects the recalculated average based on the new grade values (displayed value should match the recalculated average within the site's rounding/display rules).

---

### [TC-002] Attempt to use Log out control while not authenticated (precondition violation) - button visibility
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application's main page while not authenticated
2. 2. Inspect the page header and navigation area for a 'Log out' button
3. 3. If a 'Log out' button is present, attempt to click it

**Original Expected Result:** The 'Log out' button is not visible/available to the anonymous user (control is not present or is disabled); clicking it is not possible. The application does not send a logout request and the user remains unauthenticated (no session was terminated).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Edit profile page (Profile -> Edit profile)`
- **Observe**:
  - First name field value
  - Last name field value
  - Email address field value

**Post-Check**
- **Navigate To**: `Profile page (view mode)`
- **Observe**:
  - Profile full name (displayed on page header)
  - Email address in User details card
  - Optional: Open Edit profile to confirm persisted field values

**Expected Change**: The Profile page shows the updated first name and last name combined as the full name and the updated email address in the User details card; opening Edit profile should show the same values in the First name, Last name, and Email address fields, confirming the changes were persisted.

---

### [TC-003] After logging out, accessing a protected page is blocked (post-logout access requires re-authentication)
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Log in as <role>
2. 2. Click the 'Log out' button
3. 3. Observe that the application redirects to the Login page (post-logout)
4. 4. From the browser address bar, navigate to a protected page at <protected page URL>

**Original Expected Result:** Navigation to <protected page URL> is blocked and the user is redirected to the Login page; protected page content is not displayed and re-authentication is required (session remains terminated).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Profile page (view mode)`
- **Observe**:
  - user picture thumbnail (current avatar image or filename/alt text)
  - picture description field value (if shown on profile)
  - list of interests/tags shown on profile
  - profile description card content (rich text)

**Post-Check**
- **Navigate To**: `Profile page (view mode) after saving Edit profile`
- **Observe**:
  - user picture thumbnail (should reflect newly uploaded image or filename/alt text)
  - picture description shown on profile
  - list of interests/tags shown on profile
  - profile description card content (rich text)

**Expected Change**: The profile page refreshes and shows the newly uploaded image as the user picture thumbnail (different from the pre-check image and matching the uploaded file), the picture description updated to the entered <picture description>, the interests list contains the newly added <interest tag>, and the profile Description displays the entered <description content>.

---

### [TC-004] Direct access to the Logout endpoint while unauthenticated is blocked/redirects to login
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open a browser while not authenticated
2. 2. Enter the application's Logout endpoint URL (<logout endpoint URL>) in the address bar and navigate there

**Original Expected Result:** The application redirects the anonymous user to the Login page instead of performing a logout; no session termination occurs and no protected content is exposed.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Profile -> Edit profile -> Additional names section`
- **Observe**:
  - number of Additional names rows (could be 0)
  - existing Alternative Name values listed in Additional names rows

**Post-Check**
- **Navigate To**: `Profile page (view) and Edit profile -> Additional names section`
- **Observe**:
  - presence of an Additional names row with Alternative Name = <alternative name>
  - number of Additional names rows increased by 1 compared to pre-check

**Expected Change**: A new Additional names row appears with Alternative Name exactly equal to <alternative name>, and the total count of Additional names rows has increased by one from the pre-check value.

---

### [TC-001] Click 'Log out' button terminates session and redirects to Login page
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the 'Log out' button

**Original Expected Result:** terminates the current authenticated session and redirects to the login page; the Login page is displayed and the login form prompting for credentials is visible

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (or any authenticated protected page)`
- **Observe**:
  - personalized greeting at top of Dashboard
  - user initials icon / user menu visible
  - Dashboard main content (Timeline and Calendar blocks) accessible

**Post-Check**
- **Navigate To**: `Attempt to open Dashboard (or refresh / navigate to any previously accessible protected URL)`
- **Observe**:
  - Login page displayed
  - Login form fields: Username and Password
  - Log in button visible
  - Authenticated-only UI elements absent (no personalized greeting, no Dashboard blocks, no user menu)

**Expected Change**: After clicking 'Log out', access to authenticated pages is denied: the user is redirected to the Login page and the login form is shown; previously visible authenticated-only UI (personalized greeting, user menu, Dashboard content) is no longer accessible.

---
