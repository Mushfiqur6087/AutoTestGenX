# Post-Verification Specifications

### [TC-001] Authenticated user clicks Logout and is returned to Home page
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button in the action bar

**Original Expected Result:** terminates current session; clears sensitive session data; redirects to home page; subsequent attempts to access protected pages redirect to login page. The Home page is displayed after logout.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Home page`
- **Observe**:
  - Login/Signup button visible
  - Dashboard header not present
  - No user profile link or account menu visible

**Post-Check**
- **Navigate To**: `Dashboard -> My Profile`
- **Observe**:
  - Dashboard header visible
  - Profile displays First Name and Last Name matching the registration input
  - Profile displays the registered Email address
  - Mobile number displayed if it was provided during registration
  - Logout button visible

**Expected Change**: After registration the user is automatically logged in: the Dashboard is accessible, the My Profile view shows the registered name and email (and mobile if provided), and a Logout option is present indicating an authenticated session.

---

### [TC-002] Logged-out user attempting to open a protected page is redirected to Login page
**Category**: `positive` | **Verification Type**: `other` | **Coverage**: `partial`

**Coverage Note**: *Receipt of the verification email requires access to the recipient's external email inbox (external system) and so cannot be fully verified in-app. Partial verification can be done via login behavior and by checking the user record via admin UI or API to confirm account creation and email_verified status.*

**Original Steps:**
1. 1. Attempt to navigate to <protected page> (enter protected page URL or click link to protected page)

**Original Expected Result:** The Login page is displayed; the Login form is visible, and access to the requested protected page is not granted.

---

#### Verification Plan

---

### [TC-001] Authenticated user clicks Logout and is returned to Home page
**Category**: `positive` | **Verification Type**: `other` | **Coverage**: `partial`

**Coverage Note**: *Fully proving the backend state (email delivery and creation of a reset token) requires access to the recipient's email inbox or server logs/database. If those are not accessible, only the in-app confirmation message can be verified.*

**Original Steps:**
1. 1. Click the Logout button in the action bar

**Original Expected Result:** terminates current session; clears sensitive session data; redirects to home page; subsequent attempts to access protected pages redirect to login page. The Home page is displayed after logout.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Forgot Password page`
- **Observe**:
  - Email input field is present and empty
  - No password reset confirmation message currently visible on the page
  - If inbox is accessible: note timestamp of most recent password-reset-related email for the test address (expect none related to this test)

**Post-Check**
- **Navigate To**: `Forgot Password page (or returned confirmation UI)`
- **Observe**:
  - In-app confirmation message displayed (e.g., 'If this email is registered, a reset link has been sent' or 'Password reset link sent to your email')
  - If inbox is accessible: a new email is received at the registered address within a short time window with a subject referencing password reset
  - If inbox is accessible: the email body contains a reset link (URL) that points to the application and includes a unique token or identifier
  - If inbox/access to server logs is available: a password reset record/token exists in server logs or database associated with the registered email and has an expiry (expected ~24 hours)

**Expected Change**: A password reset record/token is created for the registered email and the system sends a password reset email containing a valid reset link; the UI displays a confirmation message. If the reset link is followed, it opens the password reset page allowing setting a new password; the token is time-limited (expires within ~24 hours).

---

### [TC-002] Logged-out user attempting to open a protected page is redirected to Login page
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to <protected page> (enter protected page URL or click link to protected page)

**Original Expected Result:** The Login page is displayed; the Login form is visible, and access to the requested protected page is not granted.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Password Reset page (opened via valid reset link)`
- **Observe**:
  - presence of New Password field
  - presence of Confirm Password field
  - presence of Change Password button
  - no success/confirmation message displayed yet
  - URL contains a reset token parameter (optional check to confirm link context)

**Post-Check**
- **Navigate To**: `Login page`
- **Observe**:
  - a visible success message indicating password changed successfully
  - Login form with Email and Password fields
  - successful login when authenticating with the new password (user lands on dashboard or previous target page)
  - failed login when attempting with the old password (shows invalid credentials)

**Expected Change**: User is redirected to the Login page with a visible success message; the new password is accepted for authentication (login succeeds) and the old password is no longer valid (login with old password fails).

---

### [TC-001] Authenticated user clicks Logout and is returned to Home page
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button in the action bar

**Original Expected Result:** terminates current session; clears sensitive session data; redirects to home page; subsequent attempts to access protected pages redirect to login page. The Home page is displayed after logout.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Flight Booking page -> Passenger Details / Lead Passenger Contact section`
- **Observe**:
  - Traveler 1: Title field value
  - Traveler 1: First Name field value
  - Traveler 1: Last Name field value
  - Traveler 1: Date of Birth field value
  - Traveler 1: Passport Number field value
  - Traveler 1: Passport Expiry field value
  - Lead Passenger Contact: Email field value
  - Lead Passenger Contact: Phone field value

**Post-Check**
- **Navigate To**: `Payment page -> Booking summary / Itinerary & Passenger details section`
- **Observe**:
  - Booking summary: Traveler 1 Title
  - Booking summary: Traveler 1 First Name
  - Booking summary: Traveler 1 Last Name
  - Booking summary: Traveler 1 Date of Birth
  - Booking summary: Traveler 1 Passport Number
  - Booking summary: Traveler 1 Passport Expiry
  - Booking summary: Lead Passenger Contact Email
  - Booking summary: Lead Passenger Contact Phone

**Expected Change**: After clicking Continue, the Payment page booking summary displays Traveler 1's Title, First Name, Last Name, Date of Birth, Passport Number, Passport Expiry, and the Lead Passenger Contact email and phone, and each of these values exactly matches the values entered on the Flight Booking page.

---

### [TC-003] Attempt to invoke Logout action when user is not authenticated (precondition not met)
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is signed out (no active session)
2. 2. Navigate directly to the Logout URL / click the Logout endpoint link (attempt to trigger Logout while unauthenticated)

**Original Expected Result:** Navigation is blocked: the application redirects to the Login page and displays the login form. The Logout action is not performed (no session termination occurs because there is no active session). No protected content is shown.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Flight Booking page -> Passenger/Traveler list / Itinerary summary (ensure Traveler 1 row is visible)`
- **Observe**:
  - Traveler 1 - Meal preference value/display (e.g., 'Not selected' or current value)
  - Traveler 1 - Seat selection value/display (e.g., 'Not selected' or current value)

**Post-Check**
- **Navigate To**: `Flight Booking page -> Itinerary summary / Passenger/Traveler list (refresh or re-open booking details if necessary)`
- **Observe**:
  - Traveler 1 - Meal preference display
  - Traveler 1 - Seat selection display

**Expected Change**: Traveler 1's row displays the meal preference and seat selection chosen in the test steps (Meal = <Meal_Preference>; Seat = <Seat_Selection>). If values were previously 'Not selected' or different, they now reflect the new selections.

---

### [TC-004] Unauthenticated state shows no action buttons (Logout not visible)
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is signed out (no active session)
2. 2. Open the application UI area that normally contains session actions (header, user menu, or action bar)

**Original Expected Result:** The action bar / user menu does not display a 'Logout' button or any authenticated-only actions. There is no clickable Logout control visible in the Unauthenticated state (no action buttons are present).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Flight Booking page -> Travelers section`
- **Observe**:
  - number of traveler rows
  - list of traveler names (Title, First Name, Last Name) currently displayed
  - passport expiry values shown for each existing traveler (if any)

**Post-Check**
- **Navigate To**: `Flight Booking page -> Travelers section`
- **Observe**:
  - number of traveler rows
  - list of traveler names (Title, First Name, Last Name)
  - passport expiry values shown for each traveler
  - passport number presence or masked indicator for the new traveler row

**Expected Change**: Number of traveler rows increased by 1; a new traveler row is present showing the entered Title, First Name, and Last Name; the Passport Expiry displayed for that new row matches the entered passport expiry; the passport number is recorded (may be shown masked) or a passport field is present for the new traveler.

---

### [TC-003] Attempt to invoke Logout action when user is not authenticated (precondition not met)
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is signed out (no active session)
2. 2. Navigate directly to the Logout URL / click the Logout endpoint link (attempt to trigger Logout while unauthenticated)

**Original Expected Result:** Navigation is blocked: the application redirects to the Login page and displays the login form. The Logout action is not performed (no session termination occurs because there is no active session). No protected content is shown.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard -> My Bookings`
- **Observe**:
  - existing bookings list for the selected Tour (presence or absence of prior bookings)
  - most recent booking entry's booking reference, traveler count, departure date, and total cost (if any)

**Post-Check**
- **Navigate To**: `Dashboard -> My Bookings -> Open most recent booking (booking detail view) for the selected Tour and Departure Date`
- **Observe**:
  - booking reference and creation timestamp
  - departure date shown on booking
  - Travellers list (each traveler row/name) and total number of traveler rows
  - contact details shown on booking (email and phone)
  - Special Requirements text
  - Total cost breakdown including base fares for adults and children, taxes/fees, and grand total
  - booking status (e.g., Confirmed, Pending)

**Expected Change**: A new booking entry is created for the selected Tour and <Departure Date>; the booking detail shows exactly (<Adults> + <Children>) traveler rows (matching the names entered), contact email and phone equal to the submitted values, Special Requirements text matches the submitted value, and the Total cost breakdown equals the calculated total based on <Adults> and <Children> (base fares + taxes/fees) as shown on the Booking Form. A booking reference and a non-empty booking status (Confirmed or Pending) are present.

---

### [TC-005] After Logout, accessing a protected page is blocked and redirects to login
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `partial`

**Coverage Note**: *Clicking 'Book Now' typically opens the in-app Car Booking page with the selected vehicle and details pre-filled. A permanent backend booking record is usually only created after the user confirms booking and completes payment, so verifying a persisted booking record is not possible at this step.*

**Original Steps:**
1. 1. Sign in as <role> to create an authenticated session
2. 2. Click the Logout action to terminate the session
3. 3. After logout completes, navigate to a known protected page URL (direct URL entry or bookmarked link)

**Original Expected Result:** Access is blocked: the application redirects to the Login page and displays the login form. Protected page content is not displayed; the terminated session is not restored by the navigation.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Cars Listing Page (results for the search criteria used in the test)`
- **Observe**:
  - presence of the chosen vehicle listing (make/model or title)
  - visible price per day and estimated total for the selected dates
  - Book Now button for the chosen vehicle
  - displayed pick-up and drop-off locations and dates/times in the listing summary

**Post-Check**
- **Navigate To**: `Car Booking Page for the chosen vehicle (booking form / checkout step opened)`
- **Observe**:
  - booking summary shows the selected vehicle name/make/model
  - rental period and pick-up/drop-off locations/times match the values used on the listing
  - pricing breakdown displayed (daily rate, number of rental days, taxes/fees, insurance options, total)
  - booking form is present with contact fields (First Name, Last Name, Email, Phone) pre-filled for the logged-in user or the lead passenger fields present
  - Confirm Booking (or Continue to Payment) button is present

**Expected Change**: User is navigated from the listing to the Car Booking page and the booking page is pre-populated with the selected vehicle, rental period, locations/times, and pricing; contact fields are pre-filled for the authenticated user. (Note: no final booking record is expected in backend until Confirm Booking and payment complete.)

---

### [TC-001] Authenticated user clicks Logout and is returned to Home page
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button in the action bar

**Original Expected Result:** terminates current session; clears sensitive session data; redirects to home page; subsequent attempts to access protected pages redirect to login page. The Home page is displayed after logout.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings (Bookings list)`
- **Observe**:
  - count of existing car bookings for the selected vehicle and rental period
  - whether any booking exists with driver name <driver full name> for the selected rental dates
  - latest booking reference visible in the list (if any) to allow ordinal comparison

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings (Bookings list)`
- **Observe**:
  - presence of a booking with service type 'Car' that matches the selected vehicle and exact rental period (pick-up and drop-off dates)
  - booking displays driver name: <driver full name>
  - booking contact shows email: <valid email> and/or phone: <phone number>
  - booking status indicates 'Pending', 'Awaiting Payment', or 'Payment Required'
  - booking reference number is shown and there is a visible 'Pay Now' / 'Proceed to Payment' action or link

**Expected Change**: The My Bookings list has one additional booking compared to pre_check for the selected vehicle and rental period; the new booking contains the provided driver name (<driver full name>) and contact (<valid email> / <phone number>), includes a booking reference, and its status is recorded as 'Pending'/'Awaiting Payment' with a visible action to proceed to payment.

---

### [TC-002] Logged-out user attempting to open a protected page is redirected to Login page
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to <protected page> (enter protected page URL or click link to protected page)

**Original Expected Result:** The Login page is displayed; the Login form is visible, and access to the requested protected page is not granted.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings (Bookings table)`
- **Observe**:
  - current count of bookings with service = 'Visa'
  - presence of any booking row where Full Name = <Full_Name>
  - presence of any booking row where Passport Number = <Passport_Number>
  - status column values for any matching rows

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings (Bookings table)`
- **Observe**:
  - booking rows filtered by service = 'Visa' (or all bookings list)
  - Full Name column for new/updated rows
  - Passport Number column for new/updated rows
  - Status badge column for the new row
  - attachments/documents indicator for the new row (shows uploaded Passport Copy and Photographs)
  - total count of bookings with service = 'Visa' after submission

**Expected Change**: The count of Visa bookings increases by 1; a new booking row appears for service 'Visa' with Full Name = <Full_Name> and Passport Number = <Passport_Number>, showing a status badge 'Pending' and document indicators confirming Passport Copy and Photographs were uploaded.

---

### [TC-003] Attempt to invoke Logout action when user is not authenticated (precondition not met)
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is signed out (no active session)
2. 2. Navigate directly to the Logout URL / click the Logout endpoint link (attempt to trigger Logout while unauthenticated)

**Original Expected Result:** Navigation is blocked: the application redirects to the Login page and displays the login form. The Logout action is not performed (no session termination occurs because there is no active session). No protected content is shown.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings -> Visa Applications`
- **Observe**:
  - list of visa application entries showing full name, passport number (or masked), service type, and status
  - whether an entry with Full Name (<Full_Name>) and Passport Number (<Passport_Number>) already exists
  - supporting documents indicator or attachments link/count for any matching entry

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings -> Visa Applications`
- **Observe**:
  - a booking row with the entered Full Name (<Full_Name>)
  - passport number or identifier matching <Passport_Number> shown in the booking row or booking details
  - service type indicating 'Visa' (or equivalent)
  - status badge showing 'Pending' for the new application
  - application's document list/attachments showing both the uploaded passport copy (Passport_Copy) and the uploaded supporting document from the added row

**Expected Change**: A new visa application appears in the Visa Applications list with the entered Full Name (<Full_Name>) and Passport Number (<Passport_Number>), status set to 'Pending'; the application's documents include the uploaded passport copy and the supporting document added via 'Add Row'; the total count of visa applications for the account increases by one.

---

### [TC-002] Logged-out user attempting to open a protected page is redirected to Login page
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to <protected page> (enter protected page URL or click link to protected page)

**Original Expected Result:** The Login page is displayed; the Login form is visible, and access to the requested protected page is not granted.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking row identified by booking reference (use the booking referenced in the core test case)
  - status badge shows 'Pending'
  - Cancel action/button is present and enabled for that row
  - booking details link or View Details action is available

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings (and open the Booking Detail view for the same booking reference)`
- **Observe**:
  - booking row identified by the same booking reference
  - status badge shows 'Cancelled'
  - Cancel action/button is no longer present or is disabled for that row
  - Booking Detail page shows status = 'Cancelled'
  - Booking Detail shows a cancellation timestamp/date and (where applicable) the displayed refund amount or refund status
  - Activity/history or audit log entry for the booking shows an entry for the cancellation (if available in the UI)

**Expected Change**: The booking's status changes from 'Pending' to 'Cancelled' in My Bookings and in the Booking Detail view; the Cancel action is removed or disabled; a cancellation timestamp (and any displayed refund amount/status) is recorded and visible in the booking details or activity log.

---

### [TC-008] Logout in one tab then quickly access protected page in another tab
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. In Tab A, click the Logout button
2. 2. Immediately in Tab B, attempt to navigate to a protected page (click a protected page link or enter its URL)

**Original Expected Result:** Logout in Tab A succeeds: session is terminated and Tab A redirects to the home page. Access attempt in Tab B is blocked: navigation to the protected page redirects to the login page (no protected content is shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking row for the target booking (identify by booking reference or service/date)
  - status badge reads 'Confirmed'
  - presence of 'Cancel' action/button for that row

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking row for the same booking (use same booking reference or service/date)
  - status badge
  - availability of 'Cancel' action/button for that row
  - booking details view (open the booking) shows status and cancellation metadata (cancellation timestamp or note)

**Expected Change**: The booking's status badge changes from 'Confirmed' to 'Cancelled'; the 'Cancel' action/button is no longer available for that booking; the booking details view indicates the booking is cancelled and shows cancellation metadata (e.g., cancellation time or note).

---

### [TC-017] Rapid resubmission after redirect: attempt to create duplicate review by using browser Back and Submit again
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the Review Submission Form and fill all required fields (Overall_Rating and any visible category ratings)
2. 2. Click Submit and wait for the success redirect to the item or review confirmation
3. 3. Press the browser Back button to return to the Review Submission Form
4. 4. Immediately click Submit again without modifying fields

**Original Expected Result:** Second submission attempt is blocked; a visible blocking message is shown indicating the review cannot be duplicated and only one review is associated with the booking (is blocked / error shown).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Profile (edit mode)`
- **Observe**:
  - current displayed value(s) of the field(s) to be edited (e.g., First Name, Last Name, Mobile Number, Address)
  - presence of editable input fields for those fields
  - visibility of 'Save' and 'Cancel' buttons indicating edit mode

**Post-Check**
- **Navigate To**: `User Dashboard -> My Profile`
- **Observe**:
  - displayed value(s) of the same field(s) that were edited
  - absence of editable input fields for those fields (i.e., view/read-only display)
  - presence of the 'Edit' button (and absence of 'Save'/'Cancel')
  - top-of-page account display (if present) reflects updated name fields (e.g., First/Last Name) where applicable

**Expected Change**: The profile fields edited during the test now display the new values entered; the My Profile section has exited edit mode (inputs replaced by read-only display and 'Edit' button visible; 'Save' and 'Cancel' no longer shown).

---

### [TC-020] Change Sort_By reorders results
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the Sort By dropdown
2. 2. Select <sort option> from the Sort By dropdown
3. 3. Observe the Results grid ordering and the Sort By control state

**Original Expected Result:** Results grid reorders according to <sort option>; the Sort By control shows <sort option> as the selected option and the visible ordering of result items updates accordingly

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> Reviews (or Booking Details -> Reviews section) with the target booking selected`
- **Observe**:
  - current count of reviews for the target booking
  - texts and ratings of existing reviews for the target booking
  - presence/absence of the exact review text to be submitted

**Post-Check**
- **Navigate To**: `User Dashboard -> Reviews (or Booking Details -> Reviews section) with the target booking selected`
- **Observe**:
  - updated count of reviews for the target booking
  - texts and ratings of reviews for the target booking (most recent first)
  - author name associated with the new review
  - timestamp or relative time label for the new review

**Expected Change**: A new review appears in the Reviews list for the target booking containing the submitted rating and review text; the review count for the booking has increased by 1; the new review is attributed to the logged-in user and shows a recent timestamp (i.e., reflects the submission).

---

### [TC-022] Departure time range end is before start (invalid time-range) is rejected
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Expand 'Flights Filters' in the left sidebar
2. 2. Set Departure_Time_Range start to <start time>
3. 3. Set Departure_Time_Range end to <end time earlier than start>
4. 4. Click outside the control or wait for the widget to apply changes

**Original Expected Result:** Departure_Time_Range field displays an inline validation error on the time-range control indicating end time must be after start time (e.g. 'End time must be after start time'); the Results grid does not update and Result_Count remains unchanged; the invalid time-range is not applied as a filter.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> Settings`
- **Observe**:
  - Default Currency
  - Default Language
  - Notification Preferences (e.g., email, SMS, push toggles)

**Post-Check**
- **Navigate To**: `User Dashboard -> Settings (after clicking 'Save Settings', then navigate away (e.g., Dashboard or Home) and return, or after a full page reload)`
- **Observe**:
  - Visible confirmation message indicating settings were saved (e.g., 'Settings saved', success toast/alert)
  - Default Currency
  - Default Language
  - Notification Preferences (e.g., email, SMS, push toggles)

**Expected Change**: The settings page shows the updated values entered in the test: Default Currency equals <Default_Currency>, Default Language equals <Default_Language>, and Notification Preferences reflect the adjusted options. The success confirmation is visible immediately after save, and the updated preference values persist after navigating away and returning or after a page reload.

---

### [TC-001] Authenticated user clicks Logout and is returned to Home page
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `partial`

**Coverage Note**: *Email notification about the modification is sent externally and cannot be fully verified from the in-app UI. This post-verification confirms in-app indicators (success notification, booking detail updates, modification history, and fee lines). Email delivery should be validated separately via the recipient mailbox or system email logs.*

**Original Steps:**
1. 1. Click the Logout button in the action bar

**Original Expected Result:** terminates current session; clears sensitive session data; redirects to home page; subsequent attempts to access protected pages redirect to login page. The Home page is displayed after logout.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings -> Booking Details page for the existing booking`
- **Observe**:
  - current travel dates shown on the booking detail
  - Special Requests field value (existing special requests)
  - traveler list and details (names, passenger types) and count
  - price breakdown (base rate, existing fees/taxes, total)
  - modification history/log (most recent modification entry and timestamp) or absence of recent modification

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings -> Booking Details page for the same booking (refresh if necessary)`
- **Observe**:
  - updated travel dates reflect the newly submitted <new travel dates>
  - Special Requests field shows the newly entered <special requests>
  - traveler list includes the newly added/updated traveler row with the provided <traveler update details> (name/details visible and count updated accordingly)
  - price breakdown includes a visible fee line item for modification or applicable charges and shows updated total amount
  - modification history/log contains a new entry for this modification with timestamp and summary
  - presence of an on-screen success notification/toast with text indicating the modification succeeded (e.g., contains 'applies requested modifications, charges applicable fees as needed, updates booking')

**Expected Change**: Booking detail now displays the new travel dates; the Special Requests field contains the submitted text; the traveler list includes the newly added/updated traveler row; the price breakdown shows a new fee line item for modification and an updated total reflecting that fee; the booking's modification history/log contains a new entry for this change; an in-app success notification confirming the successful modification is displayed. (Note: actual email notification delivery is external and not verifiable here.)

---

### [TC-002] Logged-out user attempting to open a protected page is redirected to Login page
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `partial`

**Coverage Note**: *Full verification of refund disbursement to the original external payment method and delivery of the outbound cancellation email cannot be performed inside the app. This check verifies in-app state changes (status, displayed refund amount, and any in-app refund/activity records).*

**Original Steps:**
1. 1. Attempt to navigate to <protected page> (enter protected page URL or click link to protected page)

**Original Expected Result:** The Login page is displayed; the Login form is visible, and access to the requested protected page is not granted.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard -> My Bookings -> Booking Details for the target booking (use the same booking reference used in the test)`
- **Observe**:
  - booking status badge (expected 'Default' or 'Confirmed' prior to cancellation)
  - presence and enabled state of 'Cancel' action/button in the action bar
  - absence of a Refund_Amount field or any 'Refund' entry in booking details or booking activity log
  - Wallet/Credits -> Transaction History does not contain a refund entry for this booking reference (if applicable)

**Post-Check**
- **Navigate To**: `Dashboard -> My Bookings -> Booking Details for the same booking reference`
- **Observe**:
  - booking status badge
  - Refund_Amount display in booking details or in the cancellation confirmation/activity log
  - state of 'Cancel' action/button (expected removed or disabled)
  - Wallet/Credits -> Transaction History contains a refund transaction referencing this booking (if refunds are recorded to Wallet/Credits)
  - in-app booking activity/log entry indicating 'Cancellation processed' or 'Refund initiated' (if available)

**Expected Change**: Booking status changes to 'Cancelled'; the booking detail shows a Refund_Amount with the calculated refund; the Cancel action is no longer available or is disabled; and, if the system records refunds in-app, a refund transaction or 'Refund Initiated' activity entry appears in Wallet/Credits or the booking activity log. (Actual refund to the original external payment method and outbound cancellation email delivery are external and not verifiable from the app.)

---

### [TC-001] Authenticated user clicks Logout and is returned to Home page
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button in the action bar

**Original Expected Result:** terminates current session; clears sensitive session data; redirects to home page; subsequent attempts to access protected pages redirect to login page. The Home page is displayed after logout.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Payment Page (booking summary) and Profile -> Saved Cards`
- **Observe**:
  - booking status on Payment Page (e.g., 'Pending Payment' or 'Awaiting Payment')
  - presence or absence of a booking reference on the Payment Page
  - Saved Cards list in Profile (note any existing saved card last 4 digits)

**Post-Check**
- **Navigate To**: `Dashboard -> My Bookings -> Booking Details; Profile -> Saved Cards; Dashboard -> Transactions/Wallet`
- **Observe**:
  - booking reference shown on Booking Confirmation page and listed in My Bookings
  - booking status in My Bookings (expected 'Confirmed' or equivalent successful status)
  - payment method displayed on the booking (e.g., 'Credit/Debit Card ••••1234')
  - Saved Cards list contains a card entry with last 4 digits matching the entered card
  - transaction record in Transactions/Wallet showing the booking amount with status 'Completed' or 'Paid'

**Expected Change**: The booking transitions from 'Pending Payment' to a confirmed/paid state and appears in My Bookings with a booking reference that matches the confirmation page; the booking shows the payment method as the masked card (last 4 digits matching the entered card); the card is added to the user's Saved Cards list; and a completed payment transaction for the booking amount is recorded in Transactions/Wallet.

---

### [TC-002] Logged-out user attempting to open a protected page is redirected to Login page
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to <protected page> (enter protected page URL or click link to protected page)

**Original Expected Result:** The Login page is displayed; the Login form is visible, and access to the requested protected page is not granted.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard -> My Bookings -> Open the specific Booking Details for the booking ready for payment`
- **Observe**:
  - booking status (e.g., 'Pending Payment' or 'Awaiting Payment')
  - booking reference (should be empty or marked as provisional if present)
  - payment method (if listed) or 'Not Paid'
  - total amount / price breakdown shown
  - presence/absence of invoice/voucher download link
  - payment transaction id (if any) in the booking details or Transactions/Wallet

**Post-Check**
- **Navigate To**: `Dashboard -> My Bookings -> Open the same Booking Details (and optionally view Wallet/Transactions)`
- **Observe**:
  - booking status
  - booking reference number
  - payment method listed on the booking (payment record)
  - payment transaction id and timestamp
  - invoice/voucher download link or Download Confirmation/Invoice button
  - Wallet/Transactions shows a debit of the booking amount with method 'PayPal' (if Wallet/Transactions is used)

**Expected Change**: Booking status changes from 'Pending Payment' (or equivalent) to 'Confirmed'; a booking reference number is generated and displayed in Booking Details and the My Bookings list; the payment method is recorded as 'PayPal' with a payment transaction id and timestamp; an invoice/voucher download becomes available; the transaction appears in Wallet/Transactions as a debit for the booking amount noting PayPal as the method.

---

### [TC-003] Attempt to invoke Logout action when user is not authenticated (precondition not met)
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is signed out (no active session)
2. 2. Navigate directly to the Logout URL / click the Logout endpoint link (attempt to trigger Logout while unauthenticated)

**Original Expected Result:** Navigation is blocked: the application redirects to the Login page and displays the login form. The Logout action is not performed (no session termination occurs because there is no active session). No protected content is shown.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Payment Page for the booking (before submitting payment)`
- **Observe**:
  - booking status (e.g., 'Pending Payment' or 'Ready for Payment')
  - price breakdown (room/flight/tour/car base price, taxes, fees, total)
  - absence of an invoice download link on the page
  - no payment transaction ID or payment method recorded in the booking summary

**Post-Check**
- **Navigate To**: `Booking Confirmation page and Dashboard -> My Bookings -> Booking Details (confirmed booking)`
- **Observe**:
  - booking status displays 'Confirmed' (or equivalent confirmed state)
  - payment method shows Credit/Debit Card with masked card number (last 4 digits) or cardholder name
  - payment transaction ID or payment reference is present in the booking details
  - Download Invoice button/link is present
  - clicking Download Invoice downloads a PDF file
  - downloaded invoice PDF contains the booking reference/confirmation number and total amount matching the confirmation page

**Expected Change**: Booking status changes from 'Pending Payment' to 'Confirmed'; a payment record is created showing Credit/Debit Card (masked number) and a transaction ID; an invoice PDF becomes available via a Download Invoice link and the downloaded PDF contains the booking reference and total amount that match the Booking Confirmation page.

---

### [TC-004] Unauthenticated state shows no action buttons (Logout not visible)
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is signed out (no active session)
2. 2. Open the application UI area that normally contains session actions (header, user menu, or action bar)

**Original Expected Result:** The action bar / user menu does not display a 'Logout' button or any authenticated-only actions. There is no clickable Logout control visible in the Unauthenticated state (no action buttons are present).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard -> My Bookings -> Open the booking that is ready for payment`
- **Observe**:
  - booking reference number
  - booking status (expecting 'Pending Payment' or 'Awaiting Payment')
  - payment status/details (expecting 'Payment Required' or similar)
  - voucher download button/link (should NOT be present or should be disabled)

**Post-Check**
- **Navigate To**: `Dashboard -> My Bookings -> Open the booking just paid -> Booking Details / Confirmation page`
- **Observe**:
  - booking reference number (same as pre-check)
  - booking status (expecting 'Confirmed')
  - payment status (expecting 'Paid' or 'Payment Confirmed')
  - voucher download button/link (should be present and enabled)
  - clicking the Download Voucher button initiates a download or opens a file with MIME type 'application/pdf' containing the booking reference

**Expected Change**: Booking status changes from 'Pending Payment' to 'Confirmed'; payment status becomes 'Paid'; a voucher download link/button appears and, when activated, returns a valid PDF voucher referencing the booking.

---

### [TC-005] After Logout, accessing a protected page is blocked and redirects to login
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Sign in as <role> to create an authenticated session
2. 2. Click the Logout action to terminate the session
3. 3. After logout completes, navigate to a known protected page URL (direct URL entry or bookmarked link)

**Original Expected Result:** Access is blocked: the application redirects to the Login page and displays the login form. Protected page content is not displayed; the terminated session is not restored by the navigation.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard -> My Bookings -> Booking Details for the relevant booking (before payment)`
- **Observe**:
  - booking status (expected: Pending Payment or Awaiting Payment)
  - payment method (expected: not yet recorded or shows selected method as PayPal but not completed)
  - Invoices/Documents section or Download Invoice button (expected: not present or disabled)
  - booking reference/confirmation number (may be absent or provisional)

**Post-Check**
- **Navigate To**: `Booking Confirmation page (immediately after payment) and Dashboard -> My Bookings -> Booking Details (refresh if necessary)`
- **Observe**:
  - booking status
  - booking reference/confirmation number
  - payment method recorded for the booking
  - Invoices/Documents section or Download Invoice button/link present and enabled
  - browser downloads list shows a downloaded PDF file (or prompt to save) after clicking Download Invoice
  - downloaded invoice filename (should include booking reference or invoice number)

**Expected Change**: Booking status changes from 'Pending Payment' to 'Confirmed' and a booking reference/confirmation number is present; payment method is recorded as 'PayPal'; an invoice is created and made available in the Booking Details/Invoices section with a working Download Invoice action that triggers a PDF download whose filename includes the booking reference and whose contents reflect the booking reference and total amount.

---

### [TC-006] Double-click Logout rapidly (duplicate click race)
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. From the authenticated session, click the Logout button
2. 2. Immediately (within milliseconds) click the Logout button again

**Original Expected Result:** First click succeeds: session termination runs, user is redirected to the home page. Second click is ignored (no duplicate logout or error shown). Subsequent navigation attempts to protected pages are blocked and redirect to the login page.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Payment Page for the booking (where price breakdown is visible)`
- **Observe**:
  - price breakdown (base fare, taxes, fees, total) displayed
  - payment methods list present (PayPal available)
  - booking status shown as 'Pending Payment' or 'Awaiting Payment'
  - no Voucher download link/button present on this page

**Post-Check**
- **Navigate To**: `Booking Confirmation page, then Dashboard -> My Bookings -> Booking Details for the same booking`
- **Observe**:
  - booking status changed to 'Confirmed' (or equivalent success state)
  - Download Voucher button or voucher download link is present on the Booking Confirmation and Booking Details pages
  - initiating the Download Voucher action returns an HTTP response indicating a PDF (e.g., Content-Type: application/pdf) and a file download is initiated

**Expected Change**: After completing PayPal payment and arriving at the Booking Confirmation, the booking status changes from 'Pending Payment' to 'Confirmed' and a Download Voucher button/link appears; activating the download returns a PDF voucher (download initiates and response content-type is application/pdf).

---

### [TC-002] Logged-out user attempting to open a protected page is redirected to Login page
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Attempt to navigate to <protected page> (enter protected page URL or click link to protected page)

**Original Expected Result:** The Login page is displayed; the Login form is visible, and access to the requested protected page is not granted.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Any page with the top navigation (e.g., Home page) that shows the Currency dropdown in the header`
- **Observe**:
  - currently selected currency in the Currency dropdown
  - a visible sample price on the page (note its currency symbol/unit) 

**Post-Check**
- **Navigate To**: `Reload the same page (or navigate away and back). Then open Dashboard -> My Profile -> Preferences (if available) to confirm saved preference`
- **Observe**:
  - selected currency in the Currency dropdown after reload
  - the same sample price on the page (verify its currency symbol/unit reflects the selected currency)
  - profile currency preference in My Profile / Preferences (if the profile stores currency)

**Expected Change**: After selecting <currency> and reloading, the Currency dropdown still displays <currency>; visible prices on the page show the currency symbol/unit for <currency>; for authenticated users the profile Preferences (if present) reflect <currency> as the saved currency preference.

---

### [TC-006] Double-click Logout rapidly (duplicate click race)
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. From the authenticated session, click the Logout button
2. 2. Immediately (within milliseconds) click the Logout button again

**Original Expected Result:** First click succeeds: session termination runs, user is redirected to the home page. Second click is ignored (no duplicate logout or error shown). Subsequent navigation attempts to protected pages are blocked and redirect to the login page.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Dashboard (authenticated session) or any protected page`
- **Observe**:
  - language dropdown current selection (confirm it's not Arabic)
  - a visible UI label/text (e.g., top navigation label) to record current language rendering

**Post-Check**
- **Navigate To**: `Reload the current page; then navigate to Dashboard -> My Profile (Settings)`
- **Observe**:
  - language dropdown current selection
  - top navigation and several UI labels to confirm interface language
  - My Profile / Settings -> preferred language field

**Expected Change**: After selecting <language> and reloading, the language dropdown displays <language>; top navigation and UI labels are rendered in <language>; My Profile / Settings shows preferred language set to <language>.

---

### [TC-011] Travel_Dates Start set one day after End should be blocked
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Offers_Filters form to open filter controls
2. 2. In Travel_Dates, set Start = <date B>
3. 3. In Travel_Dates, set End = <date A> where <date B> is exactly one day after <date A>
4. 4. Click Apply Filters

**Original Expected Result:** Travel_Dates field displays an inline error indicating the start date is after the end date and Apply Filters is blocked (error shown); Promotions_List is not changed

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Any authenticated page with the top navigation (e.g., Dashboard) containing the Language dropdown`
- **Observe**:
  - current value of the Language dropdown (record existing language)
  - a couple of key UI labels to establish language context (e.g., 'Home', 'My Bookings', 'Account')
  - My Profile -> language preference field (if present) to record the stored preference

**Post-Check**
- **Navigate To**: `1) Reload the current page; 2) Navigate to another authenticated area such as Dashboard or My Profile`
- **Observe**:
  - value of the Language dropdown (should show 'Arabic' or the Arabic label)
  - site UI labels/navigation are displayed in Arabic (e.g., 'Home', 'My Bookings', 'Account' rendered in Arabic)
  - My Profile -> language preference field equals Arabic

**Expected Change**: After selecting Arabic and reloading, the Language dropdown displays Arabic and the site's UI labels render in Arabic; the user's profile language preference is updated to Arabic, demonstrating that the selection persisted in the backend and across pages.

---

### [TC-003] Attempt to invoke Logout action when user is not authenticated (precondition not met)
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is signed out (no active session)
2. 2. Navigate directly to the Logout URL / click the Logout endpoint link (attempt to trigger Logout while unauthenticated)

**Original Expected Result:** Navigation is blocked: the application redirects to the Login page and displays the login form. The Logout action is not performed (no session termination occurs because there is no active session). No protected content is shown.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Item Detail page -> Reviews section`
- **Observe**:
  - total review count
  - most recent review: overall rating
  - most recent review: Cleanliness rating (if present)
  - most recent review: Service rating (if present)
  - most recent review: Location rating (if present)
  - most recent review: written feedback text
  - presence/absence of photo thumbnails on most recent review
  - verify there is no existing review that matches the to-be-submitted combination of ratings + text + photo (record absence)

**Post-Check**
- **Navigate To**: `Item Detail page -> Reviews section`
- **Observe**:
  - total review count
  - most recent review: overall rating
  - most recent review: Cleanliness rating
  - most recent review: Service rating
  - most recent review: Location rating
  - most recent review: written feedback text
  - most recent review: photo thumbnails
  - review association with the item (item name or identifier shown)
  - review attribution (display name matches submitting user or shows configured anonymity)

**Expected Change**: Total review count increased by 1 and a new review appears as the most recent entry that displays the submitted Overall rating and the category-specific ratings (Cleanliness, Service, Location), contains the entered written feedback text, shows the uploaded photo thumbnails, and is associated with and attributed to the item/submitting user.

---

### [TC-004] Unauthenticated state shows no action buttons (Logout not visible)
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is signed out (no active session)
2. 2. Open the application UI area that normally contains session actions (header, user menu, or action bar)

**Original Expected Result:** The action bar / user menu does not display a 'Logout' button or any authenticated-only actions. There is no clickable Logout control visible in the Unauthenticated state (no action buttons are present).

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Item Detail page -> Reviews section (or Dashboard -> My Reviews if item review appears there)`
- **Observe**:
  - current count of reviews for the item (e.g., "X reviews")
  - presence of any review authored by the current user (identify by user name/email or recent timestamp)
  - for the most recent review entry: overall rating value, written feedback text, photo thumbnails (if any)
  - for existing review entries: presence or absence of category-specific rating fields/labels (e.g., Cleanliness, Service, Location)

**Post-Check**
- **Navigate To**: `Item Detail page -> Reviews section (refresh the page or navigate away and back to ensure backend state is loaded)`
- **Observe**:
  - updated count of reviews for the item
  - presence of a new review authored by the current user (matching the submission timestamp)
  - the new review entry's overall rating value matches the submitted Overall Rating
  - the new review entry's written feedback matches the submitted text
  - the new review entry displays any uploaded photo thumbnails
  - the new review entry does NOT display any category-specific rating fields/labels

**Expected Change**: The reviews count for the item has increased by 1 and a new review authored by the current user appears; the new review displays the submitted Overall Rating, the submitted written feedback, and any uploaded photos, and does not show any category-specific rating fields (since applicable categories are absent).

---

### [TC-003] Attempt to invoke Logout action when user is not authenticated (precondition not met)
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Ensure the user is signed out (no active session)
2. 2. Navigate directly to the Logout URL / click the Logout endpoint link (attempt to trigger Logout while unauthenticated)

**Original Expected Result:** Navigation is blocked: the application redirects to the Login page and displays the login form. The Logout action is not performed (no session termination occurs because there is no active session). No protected content is shown.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> Settings -> Notification Preferences`
- **Observe**:
  - newsletter subscription status (e.g., 'Subscribed' or 'Unsubscribed')
  - email address on file / email used for newsletter

**Post-Check**
- **Navigate To**: `Offers page (Newsletter subscription section) and User Dashboard -> Settings -> Notification Preferences`
- **Observe**:
  - confirmation notification on Offers page with text 'subscribed to newsletter'
  - newsletter subscription status in Notification Preferences is 'Subscribed' for the user's email

**Expected Change**: A confirmation notification 'subscribed to newsletter' is displayed on the Offers page immediately after subscribing, and the user's Notification Preferences now show the newsletter subscription status as 'Subscribed' for the email used.

---

### [TC-001] Authenticated user clicks Logout and is returned to Home page
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button in the action bar

**Original Expected Result:** terminates current session; clears sensitive session data; redirects to home page; subsequent attempts to access protected pages redirect to login page. The Home page is displayed after logout.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard (e.g., My Bookings / Account Dashboard)`
- **Observe**:
  - user avatar or account name displayed in the top navigation
  - Logout button present in action bar/account menu
  - Dashboard content visible (e.g., list of bookings, booking reference numbers, profile link)

**Post-Check**
- **Navigate To**: `Home Page (then attempt to access a protected page: Dashboard / My Bookings)`
- **Observe**:
  - Home page main content visible (search widget, public navigation items like Hotels/Flights/Cars)
  - Login/Signup button visible in top navigation
  - user avatar or account name NOT present in top navigation; Logout button NOT present
  - When navigating to Dashboard / My Bookings: browser is redirected to Login page (login form visible with Email and Password fields and Login button) OR a login prompt is shown
  - Attempting to load a protected URL does not display booking details or user-specific data

**Expected Change**: The user's authenticated session is terminated: the top navigation no longer shows user-specific UI (avatar/account name) or Logout; the Home page is displayed after logout; direct navigation to protected pages (Dashboard/My Bookings) results in a redirect to the Login page and protected content is no longer accessible.

---
