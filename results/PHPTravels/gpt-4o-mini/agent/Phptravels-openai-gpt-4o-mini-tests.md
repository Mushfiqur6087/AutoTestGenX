# Test Cases — Phptravels

Generated: 2026-06-04T14:29:26.990411Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 21 | 318 | 61 | 143 | 114 | 157 | 104 | 41 |

## Home Page & Search

Total: **26** (positive: 4, negative: 16, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Search for Hotels with valid inputs | User logged in as <Role> | 1. Click on the 'Hotels' tab<br>2. Enter <valid destination> in the Destination field<br>3. Enter <valid check-in date> in the Check-In Date field<br>4. Enter <valid check-out date> in the Check-Out Date field<br>5. Enter <valid number of rooms> in the Number of Rooms field<br>6. Enter <valid number of adults> in the Adults field<br>7. Click the Search button | User is redirected to the hotel results listing page | high |
| TC-002 | WF-002 | Search for Flights with valid inputs | User logged in as <Role> | 1. Click on the 'Flights' tab<br>2. Select 'One-way' from the Trip Type dropdown<br>3. Enter <valid departure city> in the Departure City field<br>4. Enter <valid arrival city> in the Arrival City field<br>5. Enter <valid departure date> in the Departure Date field<br>6. Enter <valid number of adults> in the Adults field<br>7. Select 'Economy' from the Cabin Class dropdown<br>8. Click the Search button | User is redirected to the flight results listing page | high |
| TC-003 | WF-003 | Search for Tours with valid inputs | User logged in as <Role> | 1. Click on the 'Tours' tab<br>2. Enter <valid destination> in the Destination field<br>3. Enter <valid start date> in the Start Date field<br>4. Enter <valid end date> in the End Date field<br>5. Click the Search button | User is redirected to the tour results listing page | high |
| TC-004 | WF-004 | Search for Cars with valid inputs | User logged in as <Role> | 1. Click on the 'Cars' tab<br>2. Enter <valid pick-up location> in the Pick-Up Location field<br>3. Enter <valid drop-off location> in the Drop-Off Location field<br>4. Enter <valid pick-up date and time> in the Pick-Up Date Time field<br>5. Enter <valid drop-off date and time> in the Drop-Off Date Time field<br>6. Click the Search button | User is redirected to the car results listing page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Leave the Destination field blank and submit |  | 1. Click on the Hotels tab<br>2. Leave the Destination field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Destination field indicating it is required | high |
| TC-006 | WF-001 | Leave the Check_In_Date field blank and submit |  | 1. Click on the Hotels tab<br>2. Leave the Check_In_Date field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Check_In_Date field indicating it is required | high |
| TC-007 | WF-001 | Leave the Check_Out_Date field blank and submit |  | 1. Click on the Hotels tab<br>2. Leave the Check_Out_Date field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Check_Out_Date field indicating it is required | high |
| TC-008 | WF-001 | Leave the Number_of_Rooms field blank and submit |  | 1. Click on the Hotels tab<br>2. Leave the Number_of_Rooms field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Number_of_Rooms field indicating it is required | high |
| TC-009 | WF-001 | Leave the Adults field blank and submit |  | 1. Click on the Hotels tab<br>2. Leave the Adults field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Adults field indicating it is required | high |
| TC-010 | WF-002 | Leave the Trip_Type field unselected and submit |  | 1. Click on the Flights tab<br>2. Leave the Trip_Type field unselected<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Trip_Type field indicating it must be selected | high |
| TC-011 | WF-002 | Leave the Departure_City field blank and submit |  | 1. Click on the Flights tab<br>2. Leave the Departure_City field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Departure_City field indicating it is required | high |
| TC-012 | WF-002 | Leave the Arrival_City field blank and submit |  | 1. Click on the Flights tab<br>2. Leave the Arrival_City field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Arrival_City field indicating it is required | high |
| TC-013 | WF-002 | Leave the Departure_Date field blank and submit |  | 1. Click on the Flights tab<br>2. Leave the Departure_Date field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Departure_Date field indicating it is required | high |
| TC-014 | WF-003 | Leave the Destination field blank and submit |  | 1. Click on the Tours tab<br>2. Leave the Destination field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Destination field indicating it is required | high |
| TC-015 | WF-003 | Leave the Start_Date field blank and submit |  | 1. Click on the Tours tab<br>2. Leave the Start_Date field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Start_Date field indicating it is required | high |
| TC-016 | WF-003 | Leave the End_Date field blank and submit |  | 1. Click on the Tours tab<br>2. Leave the End_Date field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the End_Date field indicating it is required | high |
| TC-017 | WF-004 | Leave the Pick_Up_Location field blank and submit |  | 1. Click on the Cars tab<br>2. Leave the Pick_Up_Location field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Pick_Up_Location field indicating it is required | high |
| TC-018 | WF-004 | Leave the Drop_Off_Location field blank and submit |  | 1. Click on the Cars tab<br>2. Leave the Drop_Off_Location field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Drop_Off_Location field indicating it is required | high |
| TC-019 | WF-004 | Leave the Pick_Up_Date_Time field blank and submit |  | 1. Click on the Cars tab<br>2. Leave the Pick_Up_Date_Time field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Pick_Up_Date_Time field indicating it is required | high |
| TC-020 | WF-004 | Leave the Drop_Off_Date_Time field blank and submit |  | 1. Click on the Cars tab<br>2. Leave the Drop_Off_Date_Time field blank<br>3. Fill all other required fields<br>4. Click Search | Inline validation error appears on the Drop_Off_Date_Time field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-021 (boundary) | WF-001 | Check-In Date equals Check-Out Date | User is on the Hotels tab | 1. Enter a valid destination in the Destination field<br>2. Enter today's date in the Check_In_Date field<br>3. Enter today's date in the Check_Out_Date field<br>4. Enter a valid number in the Number_of_Rooms field<br>5. Enter a valid number in the Adults field | Search button is enabled; form submits successfully and user is redirected to the hotel results listing page | medium |
| TC-022 (boundary) | WF-001 | Check-Out Date is one day before Check-In Date | User is on the Hotels tab | 1. Enter a valid destination in the Destination field<br>2. Enter today's date in the Check_In_Date field<br>3. Enter yesterday's date in the Check_Out_Date field<br>4. Enter a valid number in the Number_of_Rooms field<br>5. Enter a valid number in the Adults field | Search button is blocked; inline error shown for Check-Out Date indicating it must be after Check-In Date | medium |
| TC-023 (boundary) | WF-002 | Departure Date equals Return Date | User is on the Flights tab | 1. Select 'Round-trip' in the Trip_Type dropdown<br>2. Enter a valid departure city in the Departure_City field<br>3. Enter a valid arrival city in the Arrival_City field<br>4. Enter today's date in the Departure_Date field<br>5. Enter today's date in the Return_Date field<br>6. Enter a valid number in the Adults field | Search button is enabled; form submits successfully and user is redirected to the flight results listing page | medium |
| TC-024 (boundary) | WF-002 | Return Date is one day before Departure Date | User is on the Flights tab | 1. Select 'Round-trip' in the Trip_Type dropdown<br>2. Enter a valid departure city in the Departure_City field<br>3. Enter a valid arrival city in the Arrival_City field<br>4. Enter today's date in the Departure_Date field<br>5. Enter yesterday's date in the Return_Date field<br>6. Enter a valid number in the Adults field | Search button is blocked; inline error shown for Return Date indicating it must be after Departure Date | medium |
| TC-025 (input_edge) |  | Enter long text in the Destination field | User is on the Hotels tab | 1. Enter a string longer than 200 characters in the Destination field | Inline error shown indicating the input exceeds the maximum length allowed | low |
| TC-026 (input_edge) |  | Enter special characters in the Departure City field | User is on the Flights tab | 1. Enter special characters in the Departure_City field | Inline error shown indicating invalid characters in the field | low |

---

## User Registration

Total: **17** (positive: 1, negative: 10, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful registration with valid details | User logged in as <New User> | 1. Enter <First Name> in the First Name field<br>2. Enter <Last Name> in the Last Name field<br>3. Enter <valid email> in the Email field<br>4. Enter <Password> in the Password field<br>5. Enter <Password> in the Confirm Password field<br>6. Enter <valid mobile number> in the Mobile Number field<br>7. Select <valid country code> from the Country Code dropdown<br>8. Check the Terms and Conditions checkbox<br>9. Click Submit | Account is created and user is redirected to the dashboard | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Leave First Name blank and submit |  | 1. Leave the First Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the First Name field indicating it is required | high |
| TC-003 | WF-001 | Leave Last Name blank and submit |  | 1. Leave the Last Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Last Name field indicating it is required | high |
| TC-004 | WF-001 | Leave Email blank and submit |  | 1. Leave the Email field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Email field indicating it is required | high |
| TC-005 | WF-001 | Leave Password blank and submit |  | 1. Leave the Password field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Password field indicating it is required | high |
| TC-006 | WF-001 | Leave Confirm Password blank and submit |  | 1. Leave the Confirm Password field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Confirm Password field indicating it is required | high |
| TC-007 | WF-001 | Leave Mobile Number blank and submit |  | 1. Leave the Mobile Number field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Mobile Number field indicating it is required | high |
| TC-008 | WF-001 | Leave Terms and Conditions unchecked and submit |  | 1. Leave the Terms and Conditions checkbox unchecked<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Terms and Conditions field indicating it is required | high |
| TC-009 | WF-001 | Enter invalid email format and submit |  | 1. Enter <invalid email format> in the Email field<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Email field indicating 'Must be a valid email format' | medium |
| TC-010 | WF-001 | Enter non-matching passwords and submit |  | 1. Enter <valid password> in the Password field<br>2. Enter <different password> in the Confirm Password field<br>3. Fill all other required fields<br>4. Click Submit | Inline validation error appears on the Confirm Password field indicating 'must match Password' | medium |
| TC-011 | WF-001 | Enter invalid mobile number and submit |  | 1. Enter <invalid mobile number> in the Mobile Number field<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Mobile Number field indicating 'must be a valid mobile number' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (boundary) | WF-001 | Test valid email format at boundary | User is on the registration form | 1. Enter 'user@example.com' in the Email field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form submits successfully; account is created and user is redirected to dashboard | medium |
| TC-013 (boundary) | WF-001 | Test invalid email format just below boundary | User is on the registration form | 1. Enter 'user@example' in the Email field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Email field displays an error indicating 'must be a valid email format' | medium |
| TC-014 (boundary) | WF-001 | Test password confirmation matches exactly | User is on the registration form | 1. Enter 'Password123!' in the Password field<br>2. Enter 'Password123!' in the Confirm Password field<br>3. Fill all other required fields with valid data<br>4. Click Submit | Form submits successfully; account is created and user is redirected to dashboard | medium |
| TC-015 (boundary) | WF-001 | Test password confirmation does not match | User is on the registration form | 1. Enter 'Password123!' in the Password field<br>2. Enter 'Password123' in the Confirm Password field<br>3. Fill all other required fields with valid data<br>4. Click Submit | Confirm Password field displays an error indicating 'must match Password' | medium |
| TC-016 (input_edge) | WF-001 | Test long first name input | User is on the registration form | 1. Enter a very long string (over 200 characters) in the First Name field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Form submission is blocked; First Name field displays an error indicating maximum length exceeded | low |
| TC-017 (input_edge) | WF-001 | Test special characters in last name | User is on the registration form | 1. Enter '@#$%^&*()' in the Last Name field<br>2. Fill all other required fields with valid data<br>3. Click Submit | Last Name field displays an error indicating invalid characters | low |

---

## User Login

Total: **12** (positive: 2, negative: 5, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | User logs in with valid credentials | User logged in as <User>, User is on the Login page | 1. Enter <valid email> in the Email field<br>2. Enter <valid password> in the Password field<br>3. Click Login | User is redirected to dashboard or previous page | high |
| TC-002 | WF-002 | User attempts to log in with invalid credentials | User logged in as <User>, User is on the Login page | 1. Enter <invalid email> in the Email field<br>2. Enter <invalid password> in the Password field<br>3. Click Login | An error message is shown and the password field is cleared | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Email field blank and submit |  | 1. Leave the Email field blank<br>2. Fill the Password field with <valid password><br>3. Click Login | Inline validation error appears on the Email field indicating it is required | high |
| TC-004 |  | Leave the Password field blank and submit |  | 1. Fill the Email field with <valid email><br>2. Leave the Password field blank<br>3. Click Login | Inline validation error appears on the Password field indicating it is required; password field is cleared | high |
| TC-005 |  | Submit with invalid email format |  | 1. Enter <invalid email format> in the Email field<br>2. Fill the Password field with <valid password><br>3. Click Login | Error message shown indicating invalid email format; password field is cleared | medium |
| TC-006 |  | Submit with invalid password format |  | 1. Fill the Email field with <valid email><br>2. Enter <invalid password format> in the Password field<br>3. Click Login | Error message shown indicating invalid password format; password field is cleared | medium |
| TC-007 | WF-002 | Submit with incorrect credentials |  | 1. Fill the Email field with <invalid email><br>2. Fill the Password field with <invalid password><br>3. Click Login | Error message shown indicating invalid credentials; password field is cleared | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) | WF-002 | Attempt login with an empty Email field |  | 1. Leave the Email field empty<br>2. Enter a valid Password<br>3. Click Login | Error message is shown indicating that the Email field is required | medium |
| TC-009 (boundary) | WF-002 | Attempt login with an empty Password field |  | 1. Enter a valid Email<br>2. Leave the Password field empty<br>3. Click Login | Error message is shown indicating that the Password field is required | medium |
| TC-010 (input_edge) |  | Enter a very long string in the Email field |  | 1. Enter a string longer than 254 characters in the Email field<br>2. Enter a valid Password<br>3. Click Login | Error message is shown indicating that the Email format is invalid or field is too long | low |
| TC-011 (input_edge) |  | Enter special characters in the Email field |  | 1. Enter special characters (e.g., '@#$%^&*') in the Email field<br>2. Enter a valid Password<br>3. Click Login | Error message is shown indicating that the Email format is invalid | low |
| TC-012 (interaction_edge) |  | Rapid consecutive login attempts with invalid credentials |  | 1. Enter an invalid Email and Password<br>2. Click Login<br>3. Repeat step 1 and 2 quickly multiple times | After multiple failed attempts, CAPTCHA verification is displayed | medium |

---

## Forgot Password

Total: **16** (positive: 2, negative: 8, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Send reset link for existing email | User logged in as <User>, Email <valid email> exists in the system | 1. Enter <valid email> in the Email field<br>2. Click Reset Password | A confirmation message is shown: 'sends reset link to email' | high |
| TC-002 | WF-002 | Change password with valid reset link | User navigates to the password reset page via a valid reset link | 1. Enter <new password> in the New Password field<br>2. Enter <new password> in the Confirm Password field<br>3. Click Change Password | User is redirected to the login page with a success message | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Email field blank and submit |  | 1. Leave the Email field blank<br>2. Click Reset Password | Inline validation error appears on the Email field indicating it is required | high |
| TC-004 |  | Submit with an invalid email format |  | 1. Enter <invalid email format> in the Email field<br>2. Click Reset Password | Inline validation error appears on the Email field indicating it must be a valid email address | medium |
| TC-005 |  | Submit with a non-existent email |  | 1. Enter <non-existent email> in the Email field<br>2. Click Reset Password | Form does not submit; error shown: 'email not found in the system'; Email field remains editable | high |
| TC-006 |  | Leave New Password field blank on Password Reset Page |  | 1. Leave the New Password field blank<br>2. Enter <valid password> in the Confirm Password field<br>3. Click Change Password | Inline validation error appears on the New Password field indicating it is required | high |
| TC-007 |  | Leave Confirm Password field blank on Password Reset Page |  | 1. Enter <valid password> in the New Password field<br>2. Leave the Confirm Password field blank<br>3. Click Change Password | Inline validation error appears on the Confirm Password field indicating it is required | high |
| TC-008 |  | Submit with New Password and Confirm Password not matching |  | 1. Enter <valid password> in the New Password field<br>2. Enter <different password> in the Confirm Password field<br>3. Click Change Password | Inline validation error appears on the Confirm Password field indicating it must match New Password | medium |
| TC-009 | WF-002 | Attempt to change password with an invalid reset link |  | 1. Enter <valid password> in the New Password field<br>2. Enter <valid password> in the Confirm Password field<br>3. Click Change Password | Form does not submit; error shown indicating the reset link must be valid; user remains on the Password Reset Page | high |
| TC-010 | WF-002 | Attempt to change password with an expired reset link |  | 1. Enter <valid password> in the New Password field<br>2. Enter <valid password> in the Confirm Password field<br>3. Click Change Password | Form does not submit; error shown indicating the link expires after 24 hours; user remains on the Password Reset Page | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) | WF-001 | Submit with valid email format |  | 1. Enter a valid email address in the Email field<br>2. Click Reset Password | Reset link is sent to the email; confirmation message is shown. | medium |
| TC-012 (boundary) | WF-001 | Submit with non-existent email |  | 1. Enter an email address that does not exist in the system<br>2. Click Reset Password | Error message 'email not found in the system' is shown; form remains editable. | medium |
| TC-013 (boundary) | WF-002 | Confirm password matches new password | reset link must be valid | 1. Enter a valid new password in the New Password field<br>2. Enter the same password in the Confirm Password field<br>3. Click Change Password | Redirects to login page with success message. | medium |
| TC-014 (boundary) | WF-002 | Confirm password does not match new password | reset link must be valid | 1. Enter a valid new password in the New Password field<br>2. Enter a different password in the Confirm Password field<br>3. Click Change Password | Error message indicating passwords do not match is shown; form remains editable. | medium |
| TC-015 (input_edge) |  | Submit email with leading and trailing whitespace |  | 1. Enter '   user@example.com   ' in the Email field<br>2. Click Reset Password | Leading and trailing whitespace is trimmed; reset link is sent if email exists. | low |
| TC-016 (input_edge) |  | Submit email with special characters |  | 1. Enter 'user!#$%&'*+/=?^_`{|}~@example.com' in the Email field<br>2. Click Reset Password | Reset link is sent if email exists; otherwise, error message is shown. | low |

---

## Hotels Search & Listing

Total: **14** (positive: 2, negative: 6, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Search for hotels with valid inputs | User logged in as <Role> | 1. Enter <valid destination> in the Destination field<br>2. Enter <valid check-in date> in the Check In Date field<br>3. Enter <valid check-out date> in the Check Out Date field<br>4. Enter <valid number of rooms> in the Number of Rooms field<br>5. Click 'Add Row' in the Guest Count section<br>6. Enter <valid number of adults> in the Adults field<br>7. Click 'Add Row' again in the Guest Count section<br>8. Enter <valid number of children> in the Children field<br>9. Click Search | User is redirected to the listing page | high |
| TC-002 | WF-002 | Book a hotel from the listing page | User logged in as <Role>, User is on the listing page | 1. Click Book Now on the first hotel card | Booking confirmed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave the Destination field blank and submit |  | 1. Leave the Destination field blank<br>2. Fill Check_In_Date, Check_Out_Date, Number_of_Rooms, and Guest_Count fields with valid data<br>3. Click Search | Inline validation error appears on the Destination field indicating it is required | high |
| TC-004 |  | Leave the Check_In_Date field blank and submit |  | 1. Leave the Check_In_Date field blank<br>2. Fill Destination, Check_Out_Date, Number_of_Rooms, and Guest_Count fields with valid data<br>3. Click Search | Inline validation error appears on the Check_In_Date field indicating it is required | high |
| TC-005 |  | Leave the Check_Out_Date field blank and submit |  | 1. Leave the Check_Out_Date field blank<br>2. Fill Destination, Check_In_Date, Number_of_Rooms, and Guest_Count fields with valid data<br>3. Click Search | Inline validation error appears on the Check_Out_Date field indicating it is required | high |
| TC-006 |  | Leave the Number_of_Rooms field blank and submit |  | 1. Leave the Number_of_Rooms field blank<br>2. Fill Destination, Check_In_Date, Check_Out_Date, and Guest_Count fields with valid data<br>3. Click Search | Inline validation error appears on the Number_of_Rooms field indicating it is required | high |
| TC-007 |  | Leave the Adults field blank in Guest_Count and submit |  | 1. Leave the Adults field blank in Guest_Count<br>2. Fill Destination, Check_In_Date, Check_Out_Date, and Number_of_Rooms fields with valid data<br>3. Click Search | Inline validation error appears on the Adults field indicating it is required | high |
| TC-008 |  | Submit with all required fields empty |  | 1. Leave all required fields (Destination, Check_In_Date, Check_Out_Date, Number_of_Rooms, Adults) blank<br>2. Click Search | Inline validation errors appear on the Destination, Check_In_Date, Check_Out_Date, Number_of_Rooms, and Adults fields indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-001 | Check-In Date is the same as Check-Out Date | User is on the Hotels Search Form | 1. Enter a destination in the Destination field<br>2. Enter today's date in the Check_In_Date field<br>3. Enter today's date in the Check_Out_Date field<br>4. Enter a valid number in the Number_of_Rooms field<br>5. Add at least one adult in the Guest_Count repeating group<br>6. Click Search | Search succeeds; user is redirected to the listing page | medium |
| TC-010 (boundary) | WF-001 | Check-Out Date is one day before Check-In Date | User is on the Hotels Search Form | 1. Enter a destination in the Destination field<br>2. Enter tomorrow's date in the Check_In_Date field<br>3. Enter today's date in the Check_Out_Date field<br>4. Enter a valid number in the Number_of_Rooms field<br>5. Add at least one adult in the Guest_Count repeating group<br>6. Click Search | Search is blocked; error shown indicating Check-Out Date must be after Check-In Date | medium |
| TC-011 (boundary) | WF-001 | Number of Rooms is exactly 1 | User is on the Hotels Search Form | 1. Enter a destination in the Destination field<br>2. Enter a valid Check_In_Date<br>3. Enter a valid Check_Out_Date<br>4. Enter 1 in the Number_of_Rooms field<br>5. Add at least one adult in the Guest_Count repeating group<br>6. Click Search | Search succeeds; user is redirected to the listing page | medium |
| TC-012 (boundary) | WF-001 | Number of Rooms is 0 | User is on the Hotels Search Form | 1. Enter a destination in the Destination field<br>2. Enter a valid Check_In_Date<br>3. Enter a valid Check_Out_Date<br>4. Enter 0 in the Number_of_Rooms field<br>5. Add at least one adult in the Guest_Count repeating group<br>6. Click Search | Search is blocked; error shown indicating Number of Rooms must be at least 1 | medium |
| TC-013 (input_edge) |  | Enter a long destination string | User is on the Hotels Search Form | 1. Enter a string longer than 200 characters in the Destination field | Input is either truncated or an error is shown indicating the maximum length | low |
| TC-014 (input_edge) |  | Enter special characters in the Destination field | User is on the Hotels Search Form | 1. Enter special characters (e.g., @#$%^&*) in the Destination field | Input is accepted or an error is shown indicating invalid characters | low |

---

## Hotel Details & Booking

Total: **15** (positive: 1, negative: 7, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful booking after filling out the form | User logged in as <Role> | 1. Enter <valid stay dates> in the Stay Dates field<br>2. Enter <valid guest count> in the Guest Count field<br>3. Enter <valid first name> in the First Name field<br>4. Enter <valid last name> in the Last Name field<br>5. Enter <valid email> in the Email field<br>6. Enter <valid phone number> in the Phone Number field<br>7. Click Book Now | User is redirected to the payment page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to book without being logged in | user is not logged in | 1. Fill in all required fields in the booking form<br>2. Click Book Now | User is redirected to the login page; booking does not proceed | high |
| TC-003 |  | Leave the Stay Dates field blank |  | 1. Leave the Stay Dates field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Stay Dates field indicating it is required | high |
| TC-004 |  | Leave the Guest Count field blank |  | 1. Leave the Guest Count field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Guest Count field indicating it is required | high |
| TC-005 |  | Leave the First Name field blank |  | 1. Leave the First Name field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the First Name field indicating it is required | high |
| TC-006 |  | Leave the Last Name field blank |  | 1. Leave the Last Name field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Last Name field indicating it is required | high |
| TC-007 |  | Leave the Email field blank |  | 1. Leave the Email field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Email field indicating it is required | high |
| TC-008 |  | Leave the Phone Number field blank |  | 1. Leave the Phone Number field blank<br>2. Fill all other required fields<br>3. Click Book Now | Inline validation error appears on the Phone Number field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-001 | Enter today's date in the Stay Dates field | User is logged in | 1. Select a room type<br>2. Enter today's date in the Stay Dates field<br>3. Enter 1 in the Guest Count field<br>4. Fill in First Name, Last Name, Email, and Phone Number<br>5. Click Book Now | Proceeds to payment page | medium |
| TC-010 (boundary) | WF-001 | Enter a date one day before today in the Stay Dates field | User is logged in | 1. Select a room type<br>2. Enter a date one day before today in the Stay Dates field<br>3. Enter 1 in the Guest Count field<br>4. Fill in First Name, Last Name, Email, and Phone Number<br>5. Click Book Now | Booking is blocked; visible error indicating stay dates must be today or later | medium |
| TC-011 (boundary) | WF-001 | Enter a Guest Count of 1 in the Guest Count field | User is logged in | 1. Select a room type<br>2. Enter today's date in the Stay Dates field<br>3. Enter 1 in the Guest Count field<br>4. Fill in First Name, Last Name, Email, and Phone Number<br>5. Click Book Now | Proceeds to payment page | medium |
| TC-012 (boundary) | WF-001 | Enter 0 in the Guest Count field | User is logged in | 1. Select a room type<br>2. Enter today's date in the Stay Dates field<br>3. Enter 0 in the Guest Count field<br>4. Fill in First Name, Last Name, Email, and Phone Number<br>5. Click Book Now | Booking is blocked; visible error indicating guest count must be at least 1 | medium |
| TC-013 (input_edge) |  | Enter a very long string in the First Name field |  | 1. Enter a string of 200+ characters in the First Name field | Input is either accepted or truncated with a visible indicator | low |
| TC-014 (input_edge) |  | Enter special characters in the Last Name field |  | 1. Enter special characters in the Last Name field | Input is accepted or specific error shown | low |
| TC-015 (input_edge) |  | Enter leading/trailing whitespace in the Email field |  | 1. Enter leading and trailing spaces in the Email field<br>2. Fill in other required fields<br>3. Click Book Now | Leading/trailing whitespace is trimmed; saved value shown on the detail page has no extra spaces | low |

---

## Flights Search & Listing

Total: **14** (positive: 2, negative: 7, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Search for flights with valid details | User logged in as <Role> | 1. Select 'Round-trip' from the Trip Type dropdown<br>2. Enter <valid departure city> in the Departure City field<br>3. Enter <valid arrival city> in the Arrival City field<br>4. Select <valid travel date> in the Travel Dates field<br>5. Click 'Add Row' in the Passenger Count section<br>6. Enter <number of adults> in the Adults field<br>7. Enter <number of children> in the Children field<br>8. Enter <number of infants> in the Infants field<br>9. Select 'Economy' from the Cabin Class dropdown<br>10. Click 'Search Flights' | User is redirected to the listing page | high |
| TC-002 | WF-002 | Select a flight from the listing | User logged in as <Role>, User is on the listing page | 1. Click 'Select' on the desired flight | Flight selected for booking | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Leave all required fields blank and submit the search form |  | 1. Leave the Trip Type field blank<br>2. Leave the Departure City field blank<br>3. Leave the Arrival City field blank<br>4. Leave the Travel Dates field blank<br>5. Leave the Passenger Count fields (Adults, Children, Infants) blank<br>6. Leave the Cabin Class field blank<br>7. Click on Search Flights | Form does not submit; error shown on all required fields indicating they are required | high |
| TC-004 | WF-001 | Leave the Departure City field blank and submit the search form |  | 1. Select a Trip Type<br>2. Leave the Departure City field blank<br>3. Enter a valid Arrival City<br>4. Enter valid Travel Dates<br>5. Enter valid Passenger Count<br>6. Select a Cabin Class<br>7. Click on Search Flights | Form does not submit; error shown on Departure City field indicating it is required | high |
| TC-005 | WF-001 | Leave the Arrival City field blank and submit the search form |  | 1. Select a Trip Type<br>2. Enter a valid Departure City<br>3. Leave the Arrival City field blank<br>4. Enter valid Travel Dates<br>5. Enter valid Passenger Count<br>6. Select a Cabin Class<br>7. Click on Search Flights | Form does not submit; error shown on Arrival City field indicating it is required | high |
| TC-006 | WF-001 | Enter an invalid date in the Travel Dates field and submit the search form |  | 1. Select a Trip Type<br>2. Enter a valid Departure City<br>3. Enter a valid Arrival City<br>4. Enter an invalid date in the Travel Dates field<br>5. Enter valid Passenger Count<br>6. Select a Cabin Class<br>7. Click on Search Flights | Form does not submit; error shown on Travel Dates field indicating it must be a valid date | medium |
| TC-007 | WF-001 | Enter a negative number in the Adults field and submit the search form |  | 1. Select a Trip Type<br>2. Enter a valid Departure City<br>3. Enter a valid Arrival City<br>4. Enter valid Travel Dates<br>5. Enter a negative number in the Adults field<br>6. Enter valid numbers in the Children and Infants fields<br>7. Select a Cabin Class<br>8. Click on Search Flights | Form does not submit; error shown on Adults field indicating it must be a non-negative number | medium |
| TC-008 | WF-001 | Attempt to search flights without selecting a Trip Type |  | 1. Leave the Trip Type field blank<br>2. Enter a valid Departure City<br>3. Enter a valid Arrival City<br>4. Enter valid Travel Dates<br>5. Enter valid Passenger Count<br>6. Select a Cabin Class<br>7. Click on Search Flights | Form does not submit; error shown on Trip Type field indicating it is required | high |
| TC-009 | WF-002 | Attempt to select a flight without any flights listed |  | 1. Navigate to the Flights Listing page with no flights available<br>2. Click on Select for any flight | No action occurs; no flight is selected, and an appropriate message is displayed indicating no flights are available | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) | WF-001 | Test maximum passenger count | User is on the Flights Search Form | 1. Select 'Round-trip' in the Trip Type dropdown<br>2. Enter 'New York' in the Departure City field<br>3. Enter 'Los Angeles' in the Arrival City field<br>4. Enter today's date in the Travel Dates field<br>5. Add exactly 10 Adults in the Passenger Count<br>6. Select 'Economy' in the Cabin Class dropdown<br>7. Click 'Search Flights' | Redirects to listing page with available flights | medium |
| TC-011 (boundary) | WF-001 | Test exceeding maximum passenger count | User is on the Flights Search Form | 1. Select 'Round-trip' in the Trip Type dropdown<br>2. Enter 'New York' in the Departure City field<br>3. Enter 'Los Angeles' in the Arrival City field<br>4. Enter today's date in the Travel Dates field<br>5. Add 11 Adults in the Passenger Count<br>6. Select 'Economy' in the Cabin Class dropdown<br>7. Click 'Search Flights' | Form submission is blocked; error shown indicating maximum passenger count exceeded | medium |
| TC-012 (data_edge) | WF-001 | Test today's date for travel dates | User is on the Flights Search Form | 1. Select 'One-way' in the Trip Type dropdown<br>2. Enter 'New York' in the Departure City field<br>3. Enter 'Los Angeles' in the Arrival City field<br>4. Enter today's date in the Travel Dates field<br>5. Select 'Economy' in the Cabin Class dropdown<br>6. Click 'Search Flights' | Redirects to listing page with available flights | medium |
| TC-013 (data_edge) | WF-001 | Test yesterday's date for travel dates | User is on the Flights Search Form | 1. Select 'One-way' in the Trip Type dropdown<br>2. Enter 'New York' in the Departure City field<br>3. Enter 'Los Angeles' in the Arrival City field<br>4. Enter yesterday's date in the Travel Dates field<br>5. Select 'Economy' in the Cabin Class dropdown<br>6. Click 'Search Flights' | Form submission is blocked; error shown indicating travel date cannot be in the past | medium |
| TC-014 (input_edge) | WF-001 | Test long text in Departure City | User is on the Flights Search Form | 1. Select 'One-way' in the Trip Type dropdown<br>2. Enter a very long string (200+ characters) in the Departure City field<br>3. Enter 'Los Angeles' in the Arrival City field<br>4. Enter today's date in the Travel Dates field<br>5. Select 'Economy' in the Cabin Class dropdown<br>6. Click 'Search Flights' | Form submission is blocked; error shown indicating input exceeds maximum length | low |

---

## Flight Booking

Total: **14** (positive: 1, negative: 8, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit booking form with all required fields completed | User logged in as <Role> | 1. Click 'Add Row' to add a traveler<br>2. Select 'Mr' from the Title dropdown<br>3. Enter <valid first name> in the First Name field<br>4. Enter <valid last name> in the Last Name field<br>5. Enter <valid date of birth> in the Date of Birth field<br>6. Enter <valid passport number> in the Passport Number field<br>7. Enter <valid passport expiry date> in the Passport Expiry field<br>8. Enter <valid email> in the Lead Passenger Email field<br>9. Enter <valid phone number> in the Lead Passenger Phone field<br>10. Click Continue | User is redirected to the payment page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the First Name field blank and submit |  | 1. Leave the First_Name field blank<br>2. Fill all other required fields<br>3. Click Continue | Inline validation error appears on the First_Name field indicating it is required | high |
| TC-003 |  | Leave the Last Name field blank and submit |  | 1. Leave the Last_Name field blank<br>2. Fill all other required fields<br>3. Click Continue | Inline validation error appears on the Last_Name field indicating it is required | high |
| TC-004 |  | Leave the Date of Birth field blank and submit |  | 1. Leave the Date_of_Birth field blank<br>2. Fill all other required fields<br>3. Click Continue | Inline validation error appears on the Date_of_Birth field indicating it is required | high |
| TC-005 |  | Leave the Passport Number field blank and submit |  | 1. Leave the Passport_Number field blank<br>2. Fill all other required fields<br>3. Click Continue | Inline validation error appears on the Passport_Number field indicating it is required | high |
| TC-006 |  | Leave the Passport Expiry field blank and submit |  | 1. Leave the Passport_Expiry field blank<br>2. Fill all other required fields<br>3. Click Continue | Inline validation error appears on the Passport_Expiry field indicating it is required | high |
| TC-007 |  | Leave the Lead Passenger Email field blank and submit |  | 1. Leave the Lead_Passenger_Email field blank<br>2. Fill all other required fields<br>3. Click Continue | Inline validation error appears on the Lead_Passenger_Email field indicating it is required | high |
| TC-008 |  | Leave the Lead Passenger Phone field blank and submit |  | 1. Leave the Lead_Passenger_Phone field blank<br>2. Fill all other required fields<br>3. Click Continue | Inline validation error appears on the Lead_Passenger_Phone field indicating it is required | high |
| TC-009 |  | Submit the form with all required fields empty |  | 1. Leave all required fields blank<br>2. Click Continue | Inline validation errors appear on the First_Name, Last_Name, Date_of_Birth, Passport_Number, Passport_Expiry, Lead_Passenger_Email, and Lead_Passenger_Phone fields indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 (boundary) | WF-001 | Add maximum allowed entries to the Travelers group | User is on the flight booking page | 1. Add exactly 5 entries to the Travelers repeating group | Form submits successfully; all 5 travelers are displayed in the summary | medium |
| TC-011 (boundary) | WF-001 | Attempt to add one more traveler beyond the maximum allowed | User has added 5 travelers to the group | 1. Attempt to add one more entry to the Travelers repeating group | Adding another traveler is blocked; inline error displayed indicating the maximum limit has been reached | medium |
| TC-012 (input_edge) |  | Enter a very long first name | User is filling out the booking form | 1. Enter a string of 200+ characters in the First_Name field | Form displays an error indicating the name is too long or truncates the input with a visible indicator | low |
| TC-013 (input_edge) |  | Enter special characters in the Last_Name field | User is filling out the booking form | 1. Enter special characters (e.g., !@#$%^&*) in the Last_Name field | Form displays an inline error indicating invalid characters are not allowed | low |
| TC-014 (state_edge) |  | Rapidly click the Continue button after filling the form | User has filled out all required fields correctly | 1. Click the Continue button<br>2. Immediately click the Continue button again | Form proceeds to payment page only once; no duplicate submissions occur | medium |

---

## Tours Search & Listing

Total: **14** (positive: 2, negative: 5, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Search for Tours with valid inputs | User logged in as <Role> | 1. Enter <valid destination> in the Destination field<br>2. Enter <valid travel dates> in the Travel Dates field<br>3. Select <Tour_Type> from the Tour Type dropdown<br>4. Enter <valid duration> in the Duration field<br>5. Enter <valid budget range> in the Budget Range field<br>6. Click Search | User is redirected to the listing page | high |
| TC-002 | WF-002 | View Tour Details from the listing page | User logged in as <Role>, User is on the listing page | 1. Click View Details on a tour card | Tour details displayed | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Leave the Destination field blank and submit |  | 1. Leave the Destination field blank<br>2. Fill all other required fields<br>3. Click Search | Inline validation error appears on the Destination field indicating it is required | high |
| TC-004 | WF-001 | Leave the Travel Dates field blank and submit |  | 1. Leave the Travel Dates field blank<br>2. Fill all other required fields<br>3. Click Search | Inline validation error appears on the Travel Dates field indicating it is required | high |
| TC-005 | WF-001 | Leave the Duration field blank and submit |  | 1. Leave the Duration field blank<br>2. Fill all other required fields<br>3. Click Search | Inline validation error appears on the Duration field indicating it is required | high |
| TC-006 | WF-001 | Leave the Budget Range field blank and submit |  | 1. Leave the Budget Range field blank<br>2. Fill all other required fields<br>3. Click Search | Inline validation error appears on the Budget Range field indicating it is required | high |
| TC-007 | WF-001 | Submit with all required fields empty |  | 1. Leave the Destination field blank<br>2. Leave the Travel Dates field blank<br>3. Leave the Duration field blank<br>4. Leave the Budget Range field blank<br>5. Click Search | Inline validation error appears on the Destination field indicating it is required; Inline validation error appears on the Travel Dates field indicating it is required; Inline validation error appears on the Duration field indicating it is required; Inline validation error appears on the Budget Range field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (boundary) | WF-001 | Test minimum required input for Destination field |  | 1. Enter a valid destination in the Destination field | Form submits successfully; user is redirected to the listing page | medium |
| TC-009 (boundary) | WF-001 | Test minimum required input for Travel Dates field |  | 1. Enter valid travel dates in the Travel Dates field | Form submits successfully; user is redirected to the listing page | medium |
| TC-010 (boundary) | WF-001 | Test minimum required input for Duration field |  | 1. Enter a valid duration in the Duration field | Form submits successfully; user is redirected to the listing page | medium |
| TC-011 (boundary) | WF-001 | Test minimum required input for Budget Range field |  | 1. Enter a valid budget range in the Budget Range field | Form submits successfully; user is redirected to the listing page | medium |
| TC-012 (input_edge) | WF-001 | Enter a very long string in the Destination field |  | 1. Enter a string longer than 200 characters in the Destination field | Form submission is blocked; error message indicates input exceeds maximum length | low |
| TC-013 (input_edge) | WF-001 | Enter special characters in the Duration field |  | 1. Enter special characters in the Duration field | Form submission is blocked; error message indicates invalid input | low |
| TC-014 (interaction_edge) | WF-001 | Rapid re-submission after redirect | User has successfully submitted the search form | 1. Click the Search button<br>2. After redirect, press the browser back button | User is redirected to the listing page without a second entity being created | low |

---

## Tour Details & Booking

Total: **14** (positive: 1, negative: 7, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | User books a tour successfully | User logged in as <authenticated user>, User is on the Tour Details page | 1. Select a valid <departure date> from the Departure Date field<br>2. Enter <number of adults> in the Adults field<br>3. Enter <number of children> in the Children field<br>4. Click Book Now | redirects to booking form | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to book without authentication |  | 1. Leave the user unauthenticated<br>2. Select a departure date<br>3. Specify the number of travelers<br>4. Click Book Now | User is redirected to the login page | high |
| TC-003 |  | Leave Departure Date blank and submit |  | 1. Leave the Departure_Date field blank<br>2. Specify the number of travelers<br>3. Click Book Now | Inline validation error appears on the Departure_Date field indicating it must be a valid date | high |
| TC-004 |  | Enter an invalid date in Departure Date field |  | 1. Enter <invalid date format> in the Departure_Date field<br>2. Specify the number of travelers<br>3. Click Book Now | Inline validation error appears on the Departure_Date field indicating it must be a valid date | high |
| TC-005 |  | Enter negative number for Children |  | 1. Enter <negative number> in the Children field<br>2. Specify the number of adults<br>3. Click Book Now | Inline validation error appears on the Children field indicating it must be at least 0 | high |
| TC-006 |  | Leave Name field blank in Booking Form |  | 1. Click Book Now after filling previous fields<br>2. Leave the Name field in the Traveler_Names group blank<br>3. Click Submit | Inline validation error appears on the Name field indicating it is required | high |
| TC-007 |  | Leave Email field blank in Booking Form |  | 1. Click Book Now after filling previous fields<br>2. Leave the Email field blank<br>3. Click Submit | Inline validation error appears on the Email field indicating it is required | high |
| TC-008 |  | Enter invalid email format in Email field |  | 1. Click Book Now after filling previous fields<br>2. Enter <invalid email format> in the Email field<br>3. Click Submit | Inline validation error appears on the Email field indicating it must be a valid email address | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-001 | Enter a valid departure date as today | User is authenticated | 1. Select today's date in the Departure_Date field<br>2. Fill in the number of travelers with 1 adult and 0 children<br>3. Click Book Now | Redirects to booking form with today's date accepted | medium |
| TC-010 (boundary) | WF-001 | Enter a departure date as yesterday | User is authenticated | 1. Select yesterday's date in the Departure_Date field<br>2. Fill in the number of travelers with 1 adult and 0 children<br>3. Click Book Now | Displays an error indicating the date must be today or later | medium |
| TC-011 (boundary) |  | Enter a negative number of children | User is authenticated | 1. Select today's date in the Departure_Date field<br>2. Fill in the number of travelers with 1 adult and -1 children<br>3. Click Book Now | Displays an error indicating the number of children must be at least 0 | medium |
| TC-012 (input_edge) |  | Enter a very long name in the Traveler Names field | User is authenticated | 1. Select today's date in the Departure_Date field<br>2. Fill in the number of travelers with 1 adult and 0 children<br>3. Add a traveler with a name longer than 200 characters<br>4. Click Book Now | Displays an error indicating the name exceeds the maximum length | low |
| TC-013 (input_edge) |  | Enter special characters in the Traveler Names field | User is authenticated | 1. Select today's date in the Departure_Date field<br>2. Fill in the number of travelers with 1 adult and 0 children<br>3. Add a traveler with a name containing special characters<br>4. Click Book Now | Traveler name is accepted and displayed correctly in the booking form | low |
| TC-014 (input_edge) |  | Enter leading/trailing whitespace in the Traveler Names field | User is authenticated | 1. Select today's date in the Departure_Date field<br>2. Fill in the number of travelers with 1 adult and 0 children<br>3. Add a traveler with a name that has leading and trailing spaces<br>4. Click Book Now | Leading/trailing whitespace is trimmed; saved value shown in the booking form has no extra spaces | low |

---

## Cars Search & Listing

Total: **12** (positive: 2, negative: 6, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Search for available cars | User logged in as <Role> | 1. Enter <Pick Up Location> in the Pick Up Location field<br>2. Enter <Drop Off Location> in the Drop Off Location field<br>3. Enter <Pick Up Date and Time> in the Pick Up Date Time field<br>4. Enter <Drop Off Date and Time> in the Drop Off Date Time field<br>5. Enter <Driver Age> in the Driver Age field<br>6. Click Search | User is redirected to the listing page | high |
| TC-002 | WF-002 | Book a vehicle from the listing | User logged in as <Role>, User has searched for cars and is on the listing page | 1. Click Book Now on a vehicle listing | Booking confirmed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Leave the Pick Up Location blank and submit |  | 1. Leave the Pick Up Location blank<br>2. Fill all other required fields with valid data<br>3. Click Search | Inline validation error appears on the Pick Up Location field indicating it is required | high |
| TC-004 | WF-001 | Leave the Drop Off Location blank and submit |  | 1. Leave the Drop Off Location blank<br>2. Fill all other required fields with valid data<br>3. Click Search | Inline validation error appears on the Drop Off Location field indicating it is required | high |
| TC-005 | WF-001 | Leave the Pick Up Date Time blank and submit |  | 1. Leave the Pick Up Date Time blank<br>2. Fill all other required fields with valid data<br>3. Click Search | Inline validation error appears on the Pick Up Date Time field indicating it is required | high |
| TC-006 | WF-001 | Leave the Drop Off Date Time blank and submit |  | 1. Leave the Drop Off Date Time blank<br>2. Fill all other required fields with valid data<br>3. Click Search | Inline validation error appears on the Drop Off Date Time field indicating it is required | high |
| TC-007 | WF-001 | Leave the Driver Age blank and submit |  | 1. Leave the Driver Age blank<br>2. Fill all other required fields with valid data<br>3. Click Search | Inline validation error appears on the Driver Age field indicating it is required | high |
| TC-008 | WF-001 | Submit with all required fields empty |  | 1. Leave all required fields blank<br>2. Click Search | Inline validation error appears on the Pick Up Location, Drop Off Location, Pick Up Date Time, Drop Off Date Time, and Driver Age fields indicating they are required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-001 | Test pick-up date equal to drop-off date |  | 1. Enter a valid pick-up location in the Pick_Up_Location field<br>2. Enter a valid drop-off location in the Drop_Off_Location field<br>3. Enter today's date in the Pick_Up_Date_Time field<br>4. Enter today's date in the Drop_Off_Date_Time field<br>5. Enter a valid driver age in the Driver_Age field<br>6. Click Search | Redirects to listing page with search results | medium |
| TC-010 (boundary) | WF-001 | Test drop-off date one day before pick-up date |  | 1. Enter a valid pick-up location in the Pick_Up_Location field<br>2. Enter a valid drop-off location in the Drop_Off_Location field<br>3. Enter tomorrow's date in the Pick_Up_Date_Time field<br>4. Enter today's date in the Drop_Off_Date_Time field<br>5. Enter a valid driver age in the Driver_Age field<br>6. Click Search | Form is blocked; error shown indicating drop-off date must be after pick-up date | medium |
| TC-011 (boundary) | WF-001 | Test driver age at minimum legal age |  | 1. Enter a valid pick-up location in the Pick_Up_Location field<br>2. Enter a valid drop-off location in the Drop_Off_Location field<br>3. Enter the minimum legal age in the Driver_Age field<br>4. Enter valid dates in the Pick_Up_Date_Time and Drop_Off_Date_Time fields<br>5. Click Search | Redirects to listing page with search results | medium |
| TC-012 (boundary) | WF-001 | Test driver age below minimum legal age |  | 1. Enter a valid pick-up location in the Pick_Up_Location field<br>2. Enter a valid drop-off location in the Drop_Off_Location field<br>3. Enter a driver age below the minimum legal age in the Driver_Age field<br>4. Enter valid dates in the Pick_Up_Date_Time and Drop_Off_Date_Time fields<br>5. Click Search | Form is blocked; error shown indicating driver must be of legal age | medium |

---

## Car Booking

Total: **14** (positive: 1, negative: 7, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Confirm Booking with valid inputs | User logged in as <Role> | 1. Enter <valid full name> in the Driver Full Name field<br>2. Enter <valid age> in the Age field<br>3. Enter <valid license number> in the License Number field<br>4. Select <valid country> from the License Issue Country dropdown<br>5. Enter <valid email> in the Email field<br>6. Enter <valid phone number> in the Phone Number field<br>7. Click 'Add Row' to add an add-on<br>8. Check the GPS checkbox<br>9. Select 'Damage Liability' from the Insurance Plan dropdown<br>10. Click Confirm Booking Button | User is redirected to the payment page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the Driver Full Name field blank and submit |  | 1. Leave the Driver Full Name field blank<br>2. Fill all other required fields with valid data<br>3. Click Confirm Booking | Inline validation error appears on the Driver Full Name field indicating it is required | high |
| TC-003 |  | Leave the Age field blank and submit |  | 1. Leave the Age field blank<br>2. Fill all other required fields with valid data<br>3. Click Confirm Booking | Inline validation error appears on the Age field indicating it is required | high |
| TC-004 |  | Leave the License Number field blank and submit |  | 1. Leave the License Number field blank<br>2. Fill all other required fields with valid data<br>3. Click Confirm Booking | Inline validation error appears on the License Number field indicating it is required | high |
| TC-005 |  | Leave the License Issue Country field blank and submit |  | 1. Leave the License Issue Country field blank<br>2. Fill all other required fields with valid data<br>3. Click Confirm Booking | Inline validation error appears on the License Issue Country field indicating it is required | high |
| TC-006 |  | Leave the Email field blank and submit |  | 1. Leave the Email field blank<br>2. Fill all other required fields with valid data<br>3. Click Confirm Booking | Inline validation error appears on the Email field indicating it is required | high |
| TC-007 |  | Leave the Phone Number field blank and submit |  | 1. Leave the Phone Number field blank<br>2. Fill all other required fields with valid data<br>3. Click Confirm Booking | Inline validation error appears on the Phone Number field indicating it is required | high |
| TC-008 |  | Select an invalid option for Insurance Plan and submit |  | 1. Select an invalid option for Insurance Plan<br>2. Fill all other required fields with valid data<br>3. Click Confirm Booking | Inline validation error appears on the Insurance Plan field indicating a valid selection is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 (boundary) | WF-001 | Enter minimum age for booking | User is on the car booking page | 1. Enter exactly 18 in the Age field<br>2. Fill all other required fields with valid data<br>3. Click Confirm Booking | Form submits successfully; user is directed to payment page | medium |
| TC-010 (boundary) | WF-001 | Enter one unit below minimum age for booking | User is on the car booking page | 1. Enter 17 in the Age field<br>2. Fill all other required fields with valid data<br>3. Click Confirm Booking | Age field displays an error indicating the value is below the minimum allowed | medium |
| TC-011 (input_edge) |  | Enter a long name in the Driver Full Name field | User is on the car booking page | 1. Enter a string of 200+ characters in the Driver Full Name field<br>2. Fill all other required fields with valid data<br>3. Click Confirm Booking | Form submits successfully or displays an error indicating the name is too long | low |
| TC-012 (input_edge) |  | Enter special characters in the License Number field | User is on the car booking page | 1. Enter special characters in the License Number field<br>2. Fill all other required fields with valid data<br>3. Click Confirm Booking | License Number field displays an error indicating invalid characters | low |
| TC-013 (input_edge) |  | Enter a phone number with leading/trailing whitespace | User is on the car booking page | 1. Enter ' 1234567890 ' in the Phone Number field<br>2. Fill all other required fields with valid data<br>3. Click Confirm Booking | Leading/trailing whitespace is trimmed; saved value shown in detail page has no extra spaces | low |
| TC-014 (interaction_edge) |  | Rapid re-submission after redirect | User has successfully submitted the booking form | 1. Click Confirm Booking<br>2. Press the browser back button | User is redirected to the booking form which is shown blank (not pre-filled) | low |

---

## Visa Services

Total: **20** (positive: 2, negative: 11, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit Visa Application Form with valid data | User logged in as <Applicant> | 1. Select <valid nationality> from the Nationality dropdown<br>2. Select <valid destination country> from the Destination Country dropdown<br>3. Enter <full name> in the Full Name field<br>4. Enter <passport number> in the Passport Number field<br>5. Enter <valid expiry date> in the Passport Expiry Date field<br>6. Enter <valid date of birth> in the Date of Birth field<br>7. Select <valid nationality> from the Nationality dropdown<br>8. Enter <valid email> in the Email field<br>9. Enter <valid phone number> in the Phone field<br>10. Enter <purpose of visit> in the Purpose of Visit field<br>11. Enter <valid intended travel dates> in the Intended Travel Dates field<br>12. Upload a <valid file type> in the Document Upload section<br>13. Click Submit | Application status can be tracked through the bookings section of the dashboard | high |
| TC-002 | WF-002 | View Visa Requirements for selected nationality and destination country | User logged in as <Applicant> | 1. Select <valid nationality> from the Nationality dropdown<br>2. Select <valid destination country> from the Destination Country dropdown<br>3. Click 'View Requirements' | Visa requirements displayed for selected nationality and destination country | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 |  | Leave Nationality dropdown blank and submit |  | 1. Leave the Nationality dropdown blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Nationality field indicating it is required | high |
| TC-004 |  | Leave Destination Country dropdown blank and submit |  | 1. Leave the Destination Country dropdown blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Destination Country field indicating it is required | high |
| TC-005 |  | Leave Full Name blank and submit |  | 1. Leave the Full Name field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Full Name field indicating it is required | high |
| TC-006 |  | Leave Passport Number blank and submit |  | 1. Leave the Passport Number field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Passport Number field indicating it is required | high |
| TC-007 |  | Leave Passport Expiry Date blank and submit |  | 1. Leave the Passport Expiry Date field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Passport Expiry Date field indicating it is required | high |
| TC-008 |  | Leave Date of Birth blank and submit |  | 1. Leave the Date of Birth field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Date of Birth field indicating it is required | high |
| TC-009 |  | Leave Email blank and submit |  | 1. Leave the Email field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Email field indicating it is required | high |
| TC-010 |  | Leave Phone blank and submit |  | 1. Leave the Phone field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Phone field indicating it is required | high |
| TC-011 |  | Leave Purpose of Visit blank and submit |  | 1. Leave the Purpose of Visit field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Purpose of Visit field indicating it is required | high |
| TC-012 |  | Leave Intended Travel Dates blank and submit |  | 1. Leave the Intended Travel Dates field blank<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Intended Travel Dates field indicating it is required | high |
| TC-013 |  | Leave Document Upload blank and submit |  | 1. Leave the Document Upload section empty<br>2. Fill all other required fields<br>3. Click Submit | Inline validation error appears on the Document Upload field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 (boundary) | WF-001 | Passport expiry date is today | User has filled all required fields in the Visa Application Form | 1. Enter today's date in the Passport Expiry Date field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; application is created with today's expiry date | medium |
| TC-015 (boundary) | WF-001 | Passport expiry date is one day in the past | User has filled all required fields in the Visa Application Form | 1. Enter yesterday's date in the Passport Expiry Date field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is blocked; error shown indicating the passport must be valid | medium |
| TC-016 (boundary) | WF-001 | Intended travel dates are today | User has filled all required fields in the Visa Application Form | 1. Enter today's date in the Intended Travel Dates field<br>2. Fill all other required fields<br>3. Click Submit | Form submits successfully; application is created with today's travel date | medium |
| TC-017 (boundary) | WF-001 | Intended travel dates are in the past | User has filled all required fields in the Visa Application Form | 1. Enter a date in the past in the Intended Travel Dates field<br>2. Fill all other required fields<br>3. Click Submit | Form submission is blocked; error shown indicating travel dates must be in the future | medium |
| TC-018 (input_edge) |  | Enter a very long full name | User is on the Visa Application Form | 1. Enter a string longer than 200 characters in the Full Name field | Form submission is blocked; error shown indicating the name is too long | low |
| TC-019 (input_edge) |  | Enter special characters in the email field | User is on the Visa Application Form | 1. Enter special characters in the Email field | Form submission is blocked; error shown indicating invalid email format | low |
| TC-020 (input_edge) |  | Enter leading/trailing whitespace in the phone field | User is on the Visa Application Form | 1. Enter leading and trailing spaces in the Phone field<br>2. Fill all other required fields<br>3. Click Submit | Leading/trailing whitespace is trimmed; saved value shown on the detail page has no extra spaces | low |

---

## User Dashboard

Total: **22** (positive: 9, negative: 7, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Booking Details | User logged in as <Role>, User has at least one booking | 1. Click View Details on a booking row | Booking details displayed | high |
| TC-002 | WF-002 | Cancel Booking | User logged in as <Role>, User has a booking type and cancellation policy permit | 1. Click Cancel on a booking row<br>2. Confirm cancellation if prompted | Booking cancelled; success message shown | high |
| TC-003 | WF-003 | Modify Booking | User logged in as <Role>, User has a booking type and cancellation policy permit | 1. Click Modify on a booking row | Booking modification form opened | high |
| TC-004 | WF-004 | Download Confirmations | User logged in as <Role>, User has bookings available for confirmation download | 1. Click Download Confirmations | Confirmations downloaded | medium |
| TC-005 | WF-005 | Download Invoices | User logged in as <Role>, User has invoices available for download | 1. Click Download Invoices | Invoices downloaded | medium |
| TC-006 | WF-006 | Download Vouchers | User logged in as <Role>, User has vouchers available for download | 1. Click Download Vouchers | Vouchers downloaded | medium |
| TC-007 | WF-007 | Edit Profile | User logged in as <Role> | 1. Click Edit in My Profile section | opens profile edit form | medium |
| TC-008 | WF-008 | Change Password | User logged in as <Role> | 1. Click Change Password in Settings section | opens change password form | medium |
| TC-009 | WF-009 | Logout | User logged in as <Role> | 1. Click Logout | ends the session | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-010 | WF-002 | Attempt to cancel a booking when the booking type and cancellation policy do not permit | Booking type and cancellation policy do not permit cancellation | 1. Click on the Cancel button for a booking | Cancellation is blocked; error message displayed indicating cancellation is not permitted | high |
| TC-011 | WF-003 | Attempt to modify a booking when the booking type and cancellation policy do not permit | Booking type and cancellation policy do not permit modification | 1. Click on the Modify button for a booking | Modification is blocked; error message displayed indicating modification is not permitted | high |
| TC-012 |  | Attempt to access the dashboard without being logged in | User is not authenticated | 1. Navigate to the User Dashboard | User is redirected to the login page | high |
| TC-013 |  | Attempt to view a booking without a valid booking reference | Booking reference is invalid or does not exist | 1. Enter an invalid booking reference<br>2. Click View Details | Error message displayed indicating the booking reference is not valid | medium |
| TC-014 |  | Attempt to download confirmations when there are no bookings | No bookings available | 1. Click on Download Confirmations | Download is blocked; error message displayed indicating no bookings available for download | medium |
| TC-015 |  | Attempt to download invoices when there are no bookings | No bookings available | 1. Click on Download Invoices | Download is blocked; error message displayed indicating no invoices available for download | medium |
| TC-016 |  | Attempt to download vouchers when there are no bookings | No bookings available | 1. Click on Download Vouchers | Download is blocked; error message displayed indicating no vouchers available for download | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-017 (boundary) | WF-002 | Cancel booking with valid cancellation policy | Booking type and cancellation policy permit | 1. Click on the Cancel button for a booking | Booking cancelled; success message shown | medium |
| TC-018 (boundary) | WF-002 | Attempt to cancel booking with invalid cancellation policy | Booking type and cancellation policy do not permit | 1. Click on the Cancel button for a booking | Cancellation is blocked; appropriate error message is shown | medium |
| TC-019 (boundary) | WF-003 | Modify booking with valid modification policy | Booking type and modification policy permit | 1. Click on the Modify button for a booking | Booking modification form opened | medium |
| TC-020 (boundary) | WF-003 | Attempt to modify booking with invalid modification policy | Booking type and modification policy do not permit | 1. Click on the Modify button for a booking | Modification is blocked; appropriate error message is shown | medium |
| TC-021 (input_edge) |  | Enter long text in Review Text field |  | 1. Navigate to Reviews section<br>2. Enter a very long review text (200+ characters) | Review text is accepted or truncated; visible indicator shown | low |
| TC-022 (input_edge) |  | Enter special characters in Review Text field |  | 1. Navigate to Reviews section<br>2. Enter special characters in the Review Text field | Special characters are accepted or a specific error is shown | low |

---

## Booking Management

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Modify booking details successfully | User logged in as <Role>, booking type and cancellation policy permit modification | 1. Open the booking detail view<br>2. Click Modify | allows changing travel dates, adding special requests, or updating traveler information | high |
| TC-002 | WF-002 | Open cancellation confirmation flow | User logged in as <Role>, user must explicitly confirm cancellation | 1. Open the booking detail view<br>2. Click Cancel | opens cancellation confirmation flow | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Attempt to modify booking without meeting precondition | booking type and cancellation policy do not permit modification | 1. Open the booking detail view<br>2. Click Modify | Modification is blocked; no changes are made to the booking | high |
| TC-004 | WF-002 | Attempt to cancel booking without explicit confirmation | user does not confirm cancellation | 1. Open the booking detail view<br>2. Click Cancel | Cancellation is blocked; no cancellation confirmation flow is opened | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (interaction_edge) | WF-001 | Rapid resubmission after modifying booking details | Booking type and cancellation policy permit modification | 1. Click Modify to change booking details<br>2. After the modification is successful, press the browser back button | The modification form is shown blank and no duplicate modification is submitted | medium |
| TC-006 (interaction_edge) | WF-002 | Rapid resubmission after cancelling booking | User must explicitly confirm cancellation | 1. Click Cancel to initiate cancellation<br>2. Confirm the cancellation<br>3. Press the browser back button after cancellation is confirmed | The cancellation confirmation flow is not pre-filled and shows the initial booking details | medium |

---

## Payment Processing

Total: **19** (positive: 4, negative: 9, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit payment with Credit/Debit Card | User logged in as <Role>, Payment_Method is set to 'Credit/Debit Card' | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Enter <Cardholder Name> in the Cardholder_Name field<br>3. Enter <Card Number> in the Card_Number field<br>4. Enter <Expiration Date> in the Expiration_Date field<br>5. Enter <CVV> in the CVV field<br>6. Click Submit | redirects to booking confirmation page with reference number | high |
| TC-002 | WF-002 | Submit payment with PayPal | User logged in as <Role>, Payment_Method is set to 'PayPal' | 1. Select 'PayPal' from the Payment_Method dropdown<br>2. Click Submit | redirects to booking confirmation page with reference number | high |
| TC-003 | WF-003 | Submit payment with Bank Transfer | User logged in as <Role>, Payment_Method is set to 'Bank Transfer' | 1. Select 'Bank Transfer' from the Payment_Method dropdown<br>2. Click Submit | redirects to booking confirmation page with reference number | high |
| TC-004 | WF-004 | Submit payment with Wallet/Credits | User logged in as <Role>, Payment_Method is set to 'Wallet/Credits' | 1. Select 'Wallet/Credits' from the Payment_Method dropdown<br>2. Click Submit | redirects to booking confirmation page with reference number | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Leave Payment Method blank and submit |  | 1. Leave the Payment_Method dropdown blank<br>2. Fill all other required fields | Inline validation error appears on the Payment_Method field indicating it is required | high |
| TC-006 |  | Leave Cardholder Name blank and submit |  | 1. Select 'Credit/Debit Card' from Payment_Method<br>2. Leave the Cardholder_Name field blank<br>3. Fill all other required fields | Inline validation error appears on the Cardholder_Name field indicating it is required | high |
| TC-007 |  | Leave Card Number blank and submit |  | 1. Select 'Credit/Debit Card' from Payment_Method<br>2. Leave the Card_Number field blank<br>3. Fill all other required fields | Inline validation error appears on the Card_Number field indicating it is required | high |
| TC-008 |  | Leave Expiration Date blank and submit |  | 1. Select 'Credit/Debit Card' from Payment_Method<br>2. Leave the Expiration_Date field blank<br>3. Fill all other required fields | Inline validation error appears on the Expiration_Date field indicating it is required | high |
| TC-009 |  | Leave CVV blank and submit |  | 1. Select 'Credit/Debit Card' from Payment_Method<br>2. Leave the CVV field blank<br>3. Fill all other required fields | Inline validation error appears on the CVV field indicating it is required | high |
| TC-010 |  | Submit with all required fields empty |  | 1. Select 'Credit/Debit Card' from Payment_Method<br>2. Leave all required fields empty | Form does not submit; errors shown on Payment_Method, Cardholder_Name, Card_Number, Expiration_Date, and CVV fields | high |
| TC-011 |  | Submit payment with invalid Card Number format |  | 1. Select 'Credit/Debit Card' from Payment_Method<br>2. Enter <invalid format> in the Card_Number field<br>3. Fill all other required fields | Error message displayed indicating invalid Card Number format | medium |
| TC-012 |  | Submit payment with past Expiration Date |  | 1. Select 'Credit/Debit Card' from Payment_Method<br>2. Enter <past date> in the Expiration_Date field<br>3. Fill all other required fields | Error message displayed indicating the Expiration Date must be in the future | medium |
| TC-013 |  | Attempt to submit payment with unsupported Payment Method |  | 1. Select 'Unsupported Method' from Payment_Method<br>2. Fill all required fields | Error message displayed indicating unsupported Payment Method | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-014 (boundary) | WF-001 | Enter valid card number at the maximum length | Payment_Method is set to 'Credit/Debit Card' | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Enter a valid card number with maximum length in the Card_Number field<br>3. Fill in all other required fields<br>4. Click Submit | Form submits successfully; user is redirected to booking confirmation page with reference number | medium |
| TC-015 (boundary) | WF-001 | Enter card number one digit below the maximum length | Payment_Method is set to 'Credit/Debit Card' | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Enter a valid card number with one digit less than the maximum length in the Card_Number field<br>3. Fill in all other required fields<br>4. Click Submit | Form is blocked; error message displayed indicating card number is invalid | medium |
| TC-016 (data_edge) | WF-001 | Enter today's date in the Expiration_Date field | Payment_Method is set to 'Credit/Debit Card' | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Enter a valid card number in the Card_Number field<br>3. Enter today's date in the Expiration_Date field<br>4. Fill in all other required fields<br>5. Click Submit | Form submits successfully; user is redirected to booking confirmation page with reference number | medium |
| TC-017 (data_edge) | WF-001 | Enter a date in the Expiration_Date field that is one month in the past | Payment_Method is set to 'Credit/Debit Card' | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Enter a valid card number in the Card_Number field<br>3. Enter a date one month in the past in the Expiration_Date field<br>4. Fill in all other required fields<br>5. Click Submit | Form is blocked; error message displayed indicating the expiration date is invalid | medium |
| TC-018 (input_edge) | WF-001 | Enter a very long cardholder name | Payment_Method is set to 'Credit/Debit Card' | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Enter a very long string (200+ characters) in the Cardholder_Name field<br>3. Fill in all other required fields<br>4. Click Submit | Form is blocked; error message displayed indicating the cardholder name is too long | low |
| TC-019 (input_edge) | WF-001 | Enter card number with special characters | Payment_Method is set to 'Credit/Debit Card' | 1. Select 'Credit/Debit Card' from the Payment_Method dropdown<br>2. Enter a card number with special characters in the Card_Number field<br>3. Fill in all other required fields<br>4. Click Submit | Form is blocked; error message displayed indicating the card number is invalid | low |

---

## Currency & Language Selection

Total: **14** (positive: 8, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Select USD as currency | User logged in as <Role> | 1. Select 'USD' from the Currency Selector dropdown | All prices displayed across the site update in real-time | high |
| TC-002 | WF-002 | Select EUR as currency | User logged in as <Role> | 1. Select 'EUR' from the Currency Selector dropdown | All prices displayed across the site update in real-time | high |
| TC-003 | WF-003 | Select GBP as currency | User logged in as <Role> | 1. Select 'GBP' from the Currency Selector dropdown | All prices displayed across the site update in real-time | high |
| TC-004 | WF-004 | Select JPY as currency | User logged in as <Role> | 1. Select 'JPY' from the Currency Selector dropdown | All prices displayed across the site update in real-time | high |
| TC-005 | WF-005 | Select English as language | User logged in as <Role> | 1. Select 'English' from the Language Selector dropdown | The entire site interface switches to English | high |
| TC-006 | WF-006 | Select Arabic as language | User logged in as <Role> | 1. Select 'Arabic' from the Language Selector dropdown | The entire site interface switches to Arabic | high |
| TC-007 | WF-007 | Select Spanish as language | User logged in as <Role> | 1. Select 'Spanish' from the Language Selector dropdown | The entire site interface switches to Spanish | high |
| TC-008 | WF-008 | Select French as language | User logged in as <Role> | 1. Select 'French' from the Language Selector dropdown | The entire site interface switches to French | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-009 |  | Attempt to select a currency when no currency is selected |  | 1. Leave the Currency Selector blank<br>2. Click Select | Form does not submit; Currency Selector is highlighted and displays an error: 'Please select a currency.' | high |
| TC-010 |  | Attempt to select a language when no language is selected |  | 1. Leave the Language Selector blank<br>2. Click Select | Form does not submit; Language Selector is highlighted and displays an error: 'Please select a language.' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (interaction_edge) | WF-001 | Rapid currency selection change | User is on the currency selection page | 1. Select USD from the Currency Selector<br>2. Immediately select EUR from the Currency Selector | All prices update correctly to EUR without delay or error | medium |
| TC-012 (interaction_edge) | WF-005 | Rapid language selection change | User is on the language selection page | 1. Select English from the Language Selector<br>2. Immediately select Arabic from the Language Selector | The entire site interface switches to Arabic without delay or error | medium |
| TC-013 (input_edge) |  | Special characters in language selection | User is on the language selection page | 1. Enter special characters in the Language Selector | The Language Selector does not accept special characters and shows an error | low |
| TC-014 (input_edge) |  | Leading/trailing whitespace in currency selection | User is on the currency selection page | 1. Select ' USD ' from the Currency Selector | Leading/trailing whitespace is trimmed; Currency Selector shows 'USD' | low |

---

## Search & Filters

Total: **24** (positive: 11, negative: 7, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Apply Price Range filter | User logged in as <Role> | 1. Adjust the Price Range slider to select a valid range | Results update dynamically with applied filters | high |
| TC-002 | WF-002 | Apply Star Ratings filter | User logged in as <Role> | 1. Select '4 Stars' from the Star Ratings dropdown | Results update dynamically with applied filters | high |
| TC-003 | WF-003 | Apply Hotels Filters | User logged in as <Role> | 1. Select a valid option from the Facilities/Amenities checkbox<br>2. Select 'Luxury' from the Hotel Type dropdown<br>3. Select 'All Inclusive' from the Board Basis dropdown<br>4. Select 'Downtown' from the Location Area dropdown | Results update dynamically with applied filters | high |
| TC-004 | WF-004 | Apply Flights Filters | User logged in as <Role> | 1. Select 'Airline A' from the Airlines dropdown<br>2. Select 'Non-stop' from the Number of Stops dropdown<br>3. Set the Departure Time Range to a valid range<br>4. Set the Arrival Time Range to a valid range | Results update dynamically with applied filters | high |
| TC-005 | WF-005 | Apply Tours Filters | User logged in as <Role> | 1. Select 'Adventure' from the Tour Type dropdown<br>2. Enter a valid duration in the Duration field<br>3. Set the Departure Dates to a valid range | Results update dynamically with applied filters | high |
| TC-006 | WF-006 | Apply Cars Filters | User logged in as <Role> | 1. Select 'SUV' from the Car Type dropdown<br>2. Select 'Automatic' from the Transmission dropdown<br>3. Select 'Full' from the Fuel Policy dropdown<br>4. Select 'Rental Company A' from the Rental Company dropdown | Results update dynamically with applied filters | high |
| TC-007 | WF-007 | Sort results by Price: Low to High | User logged in as <Role> | 1. Select 'Price: Low to High' from the Sort By dropdown | Results sorted by price from low to high | medium |
| TC-008 | WF-008 | Sort results by Price: High to Low | User logged in as <Role> | 1. Select 'Price: High to Low' from the Sort By dropdown | Results sorted by price from high to low | medium |
| TC-009 | WF-009 | Sort results by Rating: High to Low | User logged in as <Role> | 1. Select 'Rating: High to Low' from the Sort By dropdown | Results sorted by rating from high to low | medium |
| TC-010 | WF-010 | Sort results by Rating: Low to High | User logged in as <Role> | 1. Select 'Rating: Low to High' from the Sort By dropdown | Results sorted by rating from low to high | medium |
| TC-011 | WF-011 | Reset all filters | User logged in as <Role> | 1. Click on the Reset All Filters button | All filters reset; results updated accordingly | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 | WF-001 | Attempt to apply Price Range filter without adjusting the slider |  | 1. Open the filter section for Price Range<br>2. Click on 'Apply Filters' | No filters applied; results remain unchanged |  |
| TC-013 | WF-002 | Attempt to apply Star Ratings filter without selecting a rating |  | 1. Open the filter section for Star Ratings<br>2. Click on 'Apply Filters' | No filters applied; results remain unchanged |  |
| TC-014 | WF-003 | Attempt to apply Hotels Filters without selecting any options |  | 1. Open the Hotels Filters section<br>2. Click on 'Apply Filters' | No filters applied; results remain unchanged |  |
| TC-015 | WF-004 | Attempt to apply Flights Filters without selecting any options |  | 1. Open the Flights Filters section<br>2. Click on 'Apply Filters' | No filters applied; results remain unchanged |  |
| TC-016 | WF-005 | Attempt to apply Tours Filters without selecting any options |  | 1. Open the Tours Filters section<br>2. Click on 'Apply Filters' | No filters applied; results remain unchanged |  |
| TC-017 | WF-006 | Attempt to apply Cars Filters without selecting any options |  | 1. Open the Cars Filters section<br>2. Click on 'Apply Filters' | No filters applied; results remain unchanged |  |
| TC-018 | WF-011 | Attempt to reset filters when no filters are applied |  | 1. Click on 'Reset All Filters' | No filters reset; results remain unchanged |  |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-019 (boundary) | WF-001 | Apply price range filter at minimum value |  | 1. Adjust the Price Range slider to the minimum value<br>2. Click Apply Filters | Results update dynamically with applied filters; minimum price is reflected in results | medium |
| TC-020 (boundary) | WF-001 | Apply price range filter just above minimum value |  | 1. Adjust the Price Range slider to one unit above the minimum value<br>2. Click Apply Filters | Results update dynamically with applied filters; price range includes the new minimum | medium |
| TC-021 (boundary) | WF-002 | Apply star ratings filter at maximum value |  | 1. Select the 5 Stars option from the Star Ratings dropdown<br>2. Click Apply Filters | Results update dynamically with applied filters; only 5-star rated listings are shown | medium |
| TC-022 (boundary) | WF-002 | Apply star ratings filter just below maximum value |  | 1. Select the 4 Stars option from the Star Ratings dropdown<br>2. Click Apply Filters | Results update dynamically with applied filters; only 4-star and 5-star rated listings are shown | medium |
| TC-023 (interaction_edge) | WF-003 | Rapidly apply filters for hotels |  | 1. Select a hotel type from the Hotel_Type dropdown<br>2. Select a board basis from the Board_Basis dropdown<br>3. Click Apply Filters<br>4. Immediately select a different hotel type from the Hotel_Type dropdown<br>5. Click Apply Filters again | Results update dynamically with the latest applied filters; previous filter results are replaced | low |
| TC-024 (interaction_edge) | WF-011 | Reset all filters after applying some |  | 1. Apply filters for hotels<br>2. Click Reset All Filters | All filters reset; results updated accordingly to show all listings | low |

---

## Reviews & Ratings

Total: **16** (positive: 1, negative: 9, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit a review with valid inputs | User logged in as <authenticated user>, User must have completed a booking | 1. Navigate to the Submit Review section<br>2. Enter <Overall Experience Rating> in the Overall Experience Rating field<br>3. Click 'Add Category Rating'<br>4. Enter <Category> in the Category field<br>5. Enter <Rating> in the Rating field<br>6. Click 'Add Category Rating' again<br>7. Enter <Category> in the Category field<br>8. Enter <Rating> in the Rating field<br>9. Enter <Written Feedback> in the Written Feedback field<br>10. Click 'Submit Review' | A success notification is displayed: 'review submitted successfully' | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to submit a review without being authenticated |  | 1. Leave the authentication step<br>2. Navigate to the Submit Review form<br>3. Fill in all required fields with valid data<br>4. Click Submit Review | User is redirected to the login page; review is not submitted |  |
| TC-003 | WF-001 | Attempt to submit a review without having completed a booking | user is authenticated | 1. Navigate to the Submit Review form<br>2. Fill in all required fields with valid data<br>3. Click Submit Review | Error message displayed: 'You must have completed a booking to submit a review'; review is not submitted |  |
| TC-004 |  | Leave Overall Experience Rating blank and submit |  | 1. Navigate to the Submit Review form<br>2. Leave the Overall Experience Rating field blank<br>3. Fill in all other required fields with valid data<br>4. Click Submit Review | Inline validation error appears on the Overall Experience Rating field indicating it is required; review is not submitted |  |
| TC-005 |  | Leave Category Rating Category blank and submit |  | 1. Navigate to the Submit Review form<br>2. Leave the Category field blank in the Category Ratings section<br>3. Fill in the Rating field with a valid number<br>4. Click Submit Review | Inline validation error appears on the Category field indicating it is required; review is not submitted |  |
| TC-006 |  | Leave Category Rating blank and submit |  | 1. Navigate to the Submit Review form<br>2. Fill in the Category field with a valid category<br>3. Leave the Rating field blank in the Category Ratings section<br>4. Click Submit Review | Inline validation error appears on the Rating field indicating it is required; review is not submitted |  |
| TC-007 |  | Leave Reviewer_Name blank and submit |  | 1. Navigate to the Submit Review form<br>2. Leave the Reviewer_Name field blank<br>3. Fill in all other required fields with valid data<br>4. Click Submit Review | Inline validation error appears on the Reviewer_Name field indicating it is required; review is not submitted |  |
| TC-008 |  | Leave Reviewer_Country blank and submit |  | 1. Navigate to the Submit Review form<br>2. Leave the Reviewer_Country field blank<br>3. Fill in all other required fields with valid data<br>4. Click Submit Review | Inline validation error appears on the Reviewer_Country field indicating it is required; review is not submitted |  |
| TC-009 |  | Leave Review_Date blank and submit |  | 1. Navigate to the Submit Review form<br>2. Leave the Review_Date field blank<br>3. Fill in all other required fields with valid data<br>4. Click Submit Review | Inline validation error appears on the Review_Date field indicating it is required; review is not submitted |  |
| TC-010 |  | Leave Stay_Date blank and submit |  | 1. Navigate to the Submit Review form<br>2. Leave the Stay_Date field blank<br>3. Fill in all other required fields with valid data<br>4. Click Submit Review | Inline validation error appears on the Stay_Date field indicating it is required; review is not submitted |  |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) | WF-001 | Submit overall experience rating at minimum value | user must be authenticated, user must have completed a booking | 1. Enter exactly 1 in the Overall_Experience_Rating field<br>2. Fill all required fields in the Category_Ratings repeating group<br>3. Click Submit Review | Review submitted successfully; overall experience rating is recorded as 1 | medium |
| TC-012 (boundary) | WF-001 | Submit overall experience rating above maximum value | user must be authenticated, user must have completed a booking | 1. Enter 6 in the Overall_Experience_Rating field<br>2. Fill all required fields in the Category_Ratings repeating group<br>3. Click Submit Review | Submission is blocked; error shown indicating rating exceeds maximum allowed value | medium |
| TC-013 (boundary) | WF-001 | Add maximum allowed entries to Category Ratings | user must be authenticated, user must have completed a booking | 1. Add exactly N entries to the Category_Ratings repeating group<br>2. Fill all required fields<br>3. Click Submit Review | Review submitted successfully with N category ratings recorded | medium |
| TC-014 (boundary) | WF-001 | Attempt to add one more entry to Category Ratings beyond maximum | user must be authenticated, user must have completed a booking | 1. Add N entries to the Category_Ratings repeating group<br>2. Attempt to add one more entry<br>3. Click Submit Review | Submission is blocked; error shown indicating maximum entries exceeded | medium |
| TC-015 (input_edge) |  | Enter a very long name in the Reviewer_Name field |  | 1. Enter a string longer than 200 characters in the Reviewer_Name field<br>2. Fill all other required fields<br>3. Click Submit Review | Submission is blocked; error shown indicating name exceeds maximum length | low |
| TC-016 (input_edge) |  | Enter special characters in the Written_Feedback field |  | 1. Enter special characters in the Written_Feedback field<br>2. Fill all other required fields<br>3. Click Submit Review | Review submitted successfully; special characters are accepted in feedback | low |

---

## Offers & Deals

Total: **10** (positive: 2, negative: 2, edge: 6)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Book Now for an offer | User logged in as <Role> | 1. Select 'Hotels' from the Service Type Filter<br>2. Enter <valid destination> in the Destination Filter<br>3. Select <valid travel date> in the Travel Dates Filter<br>4. Click 'Book Now' on a promotional offer | User is redirected to a pre-filled search with discounted rates applied | high |
| TC-002 | WF-002 | Newsletter subscription | User logged in as <Role> | 1. Enter <valid email> in the Email field of the newsletter subscription<br>2. Click 'Submit' | Email submitted for future exclusive deals | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-002 | Attempt to subscribe to newsletter without providing an email |  | 1. Leave the Email field blank<br>2. Click Submit | Inline validation error appears on the Email field indicating it is required | high |
| TC-004 |  | Attempt to book an offer without any filters applied |  | 1. Click Book Now for any offer | No promotional code is applied; user remains on the current page | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (boundary) | WF-002 | Email submission with maximum length |  | 1. Enter a valid email address with maximum allowed length in the Email field<br>2. Click Submit | Email submitted for future exclusive deals | medium |
| TC-006 (boundary) | WF-002 | Email submission with one character too long |  | 1. Enter a valid email address with one character over the maximum length in the Email field<br>2. Click Submit | Email submission is blocked; inline error shown indicating the email is too long | medium |
| TC-007 (input_edge) |  | Email submission with special characters |  | 1. Enter an email address containing special characters in the Email field<br>2. Click Submit | Email submission is blocked; inline error shown indicating invalid email format | low |
| TC-008 (input_edge) |  | Email submission with leading/trailing whitespace |  | 1. Enter an email address with leading and trailing spaces in the Email field<br>2. Click Submit | Leading/trailing whitespace is trimmed; email submitted successfully for future exclusive deals | low |
| TC-009 (data_edge) |  | Travel date selection with today's date |  | 1. Select today's date in the Travel Dates Filter<br>2. Click Book Now for any offer | Redirects to pre-filled search with discounted rates applied | medium |
| TC-010 (data_edge) |  | Travel date selection with a far future date |  | 1. Select a date several years in the future in the Travel Dates Filter<br>2. Click Book Now for any offer | Redirects to pre-filled search with discounted rates applied | medium |

---

## Logout

Total: **5** (positive: 1, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | User successfully logs out | User logged in as <Role> | 1. Click Logout_Button | terminates the current session and clears sensitive session data; user is redirected to the home page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to access a protected page after logout | User is logged in | 1. Click the Logout button | User is redirected to the login page when attempting to access a protected page | high |
| TC-003 |  | Attempt to click Logout button when already logged out | User is logged out | 1. Click the Logout button | No action occurs; user remains on the current page | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 (interaction_edge) | WF-001 | Rapid logout attempts | User is logged in and on a protected page | 1. Click the Logout button<br>2. Immediately click the Logout button again | Second logout attempt is blocked; user remains on the home page without session termination | medium |
| TC-005 (interaction_edge) | WF-001 | Access protected page after logout | User is logged in and clicks Logout | 1. Click the Logout button<br>2. Attempt to navigate to a protected page | User is redirected to the login page after attempting to access a protected page | medium |

---
