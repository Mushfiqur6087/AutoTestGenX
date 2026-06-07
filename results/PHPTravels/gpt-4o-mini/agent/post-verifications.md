# Post-Verification Specifications

### [TC-001] User successfully logs out
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Logout_Button

**Original Expected Result:** terminates the current session and clears sensitive session data; user is redirected to the home page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard`
- **Observe**:
  - user's profile information
  - list of bookings
  - wallet/credits balance

**Post-Check**
- **Navigate To**: `User Dashboard`
- **Observe**:
  - user's profile information
  - list of bookings
  - wallet/credits balance

**Expected Change**: User's profile information is updated with the new registration details, and the account is created successfully.

---

### [TC-001] User successfully logs out
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Logout_Button

**Original Expected Result:** terminates the current session and clears sensitive session data; user is redirected to the home page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Forgot Password page`
- **Observe**:
  - Email field
  - Reset Password button

**Post-Check**
- **Navigate To**: `Email inbox`
- **Observe**:
  - reset password link email

**Expected Change**: A reset password link email is received at the specified email address.

---

### [TC-002] Attempt to access a protected page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button

**Original Expected Result:** User is redirected to the login page when attempting to access a protected page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Login page`
- **Observe**:
  - Login button
  - Forgot Password? link

**Post-Check**
- **Navigate To**: `Login page`
- **Observe**:
  - Login button
  - Forgot Password? link

**Expected Change**: User can now log in with the new password.

---

### [TC-002] Attempt to access a protected page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button

**Original Expected Result:** User is redirected to the login page when attempting to access a protected page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - list of bookings
  - booking reference
  - service type
  - travel dates
  - status

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - list of bookings
  - booking reference
  - service type
  - travel dates
  - status

**Expected Change**: A new booking entry appears in the My Bookings section with the correct service type, travel dates, and status 'Confirmed'.

---

### [TC-001] User successfully logs out
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Logout_Button

**Original Expected Result:** terminates the current session and clears sensitive session data; user is redirected to the home page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - list of bookings
  - booking reference
  - service type
  - travel dates
  - status

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - list of bookings
  - booking reference
  - service type
  - travel dates
  - status

**Expected Change**: A new booking entry appears in the My Bookings section with the correct details and status 'Pending'.

---

### [TC-001] User successfully logs out
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Logout_Button

**Original Expected Result:** terminates the current session and clears sensitive session data; user is redirected to the home page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Flight Booking Summary`
- **Observe**:
  - passenger count
  - cabin class
  - fare breakdown

**Post-Check**
- **Navigate To**: `Payment Page`
- **Observe**:
  - booking summary
  - total price
  - payment options

**Expected Change**: User is redirected to the payment page with a complete booking summary and total price displayed.

---

### [TC-001] User successfully logs out
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Logout_Button

**Original Expected Result:** terminates the current session and clears sensitive session data; user is redirected to the home page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - list of bookings
  - booking reference
  - tour details

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - list of bookings
  - new booking reference
  - tour details

**Expected Change**: A new booking entry appears in the My Bookings section with the correct tour details and booking reference.

---

### [TC-002] Attempt to access a protected page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button

**Original Expected Result:** User is redirected to the login page when attempting to access a protected page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - list of bookings
  - booking reference
  - service type
  - status

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - list of bookings
  - booking reference
  - service type
  - status

**Expected Change**: A new booking entry appears in the My Bookings section with the status 'Confirmed'.

---

### [TC-001] User successfully logs out
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Logout_Button

**Original Expected Result:** terminates the current session and clears sensitive session data; user is redirected to the home page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Car Booking page`
- **Observe**:
  - Driver Full Name field
  - Age field
  - License Number field
  - Email field
  - Phone Number field

**Post-Check**
- **Navigate To**: `Payment page`
- **Observe**:
  - Booking summary
  - Total cost
  - Payment options

**Expected Change**: User is redirected to the payment page where they can see the booking summary and proceed with payment.

---

### [TC-001] User successfully logs out
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Logout_Button

**Original Expected Result:** terminates the current session and clears sensitive session data; user is redirected to the home page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - application status
  - visa application details

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - application status
  - visa application details

**Expected Change**: A new visa application entry appears in the My Bookings section with the status indicating it is under review or submitted.

---

### [TC-002] Attempt to access a protected page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button

**Original Expected Result:** User is redirected to the login page when attempting to access a protected page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking reference
  - status of the booking

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking reference
  - status of the booking

**Expected Change**: Booking status changed to 'Cancelled'.

---

### [TC-003] Attempt to click Logout button when already logged out
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button

**Original Expected Result:** No action occurs; user remains on the current page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking reference
  - service type
  - status

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking reference
  - service type
  - status

**Expected Change**: Booking status remains the same, but the booking modification form is opened for editing.

---

### [TC-001] User successfully logs out
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Logout_Button

**Original Expected Result:** terminates the current session and clears sensitive session data; user is redirected to the home page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking reference
  - travel dates
  - traveler information

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking reference
  - updated travel dates
  - updated traveler information

**Expected Change**: Travel dates and traveler information have been updated as per the modification.

---

### [TC-001] User successfully logs out
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Logout_Button

**Original Expected Result:** terminates the current session and clears sensitive session data; user is redirected to the home page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Payment Summary`
- **Observe**:
  - total amount due
  - payment method selected

**Post-Check**
- **Navigate To**: `Booking Confirmation`
- **Observe**:
  - booking reference number
  - total amount charged
  - payment method

**Expected Change**: User is redirected to the booking confirmation page displaying a booking reference number and the total amount charged matches the amount due on the payment summary.

---

### [TC-002] Attempt to access a protected page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button

**Original Expected Result:** User is redirected to the login page when attempting to access a protected page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Payment Summary Page`
- **Observe**:
  - total amount due
  - selected payment method

**Post-Check**
- **Navigate To**: `Booking Confirmation Page`
- **Observe**:
  - booking reference number
  - total amount charged

**Expected Change**: User is redirected to the booking confirmation page displaying a booking reference number and the total amount charged matches the amount displayed on the payment summary page.

---

### [TC-003] Attempt to click Logout button when already logged out
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button

**Original Expected Result:** No action occurs; user remains on the current page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - list of bookings
  - booking reference number
  - booking status

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - list of bookings
  - new booking reference number
  - booking status as 'Confirmed'

**Expected Change**: A new booking appears in the list with a unique reference number and status updated to 'Confirmed'.

---

### [TC-004] Rapid logout attempts
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button
2. 2. Immediately click the Logout button again

**Original Expected Result:** Second logout attempt is blocked; user remains on the home page without session termination

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - booking reference
  - booking status

**Post-Check**
- **Navigate To**: `User Dashboard -> My Bookings`
- **Observe**:
  - new booking reference
  - booking status

**Expected Change**: A new booking appears in the My Bookings section with a status of 'Confirmed'.

---

### [TC-001] User successfully logs out
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Logout_Button

**Original Expected Result:** terminates the current session and clears sensitive session data; user is redirected to the home page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `My Bookings -> Reviews`
- **Observe**:
  - list of submitted reviews
  - review count

**Post-Check**
- **Navigate To**: `My Bookings -> Reviews`
- **Observe**:
  - list of submitted reviews
  - review count

**Expected Change**: A new review appears in the list of submitted reviews, and the review count increases by one.

---

### [TC-002] Attempt to access a protected page after logout
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button

**Original Expected Result:** User is redirected to the login page when attempting to access a protected page

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `User Dashboard`
- **Observe**:
  - newsletter subscription status
  - email address in subscription list

**Post-Check**
- **Navigate To**: `User Dashboard`
- **Observe**:
  - newsletter subscription status
  - email address in subscription list

**Expected Change**: Email address is now listed as subscribed for future exclusive deals.

---
