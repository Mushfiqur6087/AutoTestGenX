# PHPTravels Test Cases

**Website URL:** https://phptravels.com/demo
**Test Suite Version:** 1.0

---

## Table of Contents
1. [Home Page And Search](#1-home-page-and-search)
2. [Registration](#2-registration)
3. [Login](#3-login)
4. [Forgot Password](#4-forgot-password)
5. [Hotels Search And Listing](#5-hotels-search-and-listing)
6. [Hotel Details And Booking](#6-hotel-details-and-booking)
7. [Flights Search And Booking](#7-flights-search-and-booking)
8. [Tours Search And Booking](#8-tours-search-and-booking)
9. [Cars Search And Booking](#9-cars-search-and-booking)
10. [Visa Services](#10-visa-services)
11. [User Dashboard And Booking Management](#11-user-dashboard-and-booking-management)
12. [Payment Processing](#12-payment-processing)
13. [Currency And Language Selection](#13-currency-and-language-selection)
14. [Search And Filters](#14-search-and-filters)
15. [Reviews And Ratings](#15-reviews-and-ratings)
16. [Offers And Deals](#16-offers-and-deals)
17. [Logout](#17-logout)

---

## 1. Home Page And Search

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HOME-001 | Home page navigation elements displayed | None | 1. Navigate to the PHPTravels home page | Top navigation, currency selector, language selector, login/signup links, and search widget are visible | High |
| HOME-002 | Hotel search from home page | None | 1. Select the Hotels tab<br>2. Enter destination<br>3. Select valid check-in and check-out dates<br>4. Set guests and rooms<br>5. Click "Search" | User is redirected to the hotel listing page with matching search criteria summary | High |
| HOME-003 | Flight search from home page | None | 1. Select the Flights tab<br>2. Enter origin and destination<br>3. Select valid dates and class<br>4. Click "Search" | User is redirected to the flight listing page with results matching the search criteria | High |
| HOME-004 | Tour search from home page | None | 1. Select the Tours tab<br>2. Enter destination<br>3. Select travel date<br>4. Click "Search" | User is redirected to the tour listing page with matching results | Medium |
| HOME-005 | Car search from home page | None | 1. Select the Cars tab<br>2. Enter pick-up and drop-off data<br>3. Select valid date and time values<br>4. Click "Search" | User is redirected to the car listing page with matching results | Medium |
| HOME-006 | Featured content sections displayed | None | 1. Scroll through the home page | Featured hotels, popular destinations, and promotional sections are visible | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HOME-007 | Hotel search with required fields missing | None | 1. Select Hotels tab<br>2. Leave destination or required dates empty<br>3. Click "Search" | Validation message is shown and search is not submitted | High |
| HOME-008 | Flight search with required fields missing | None | 1. Select Flights tab<br>2. Leave origin or destination empty<br>3. Click "Search" | Validation message is shown and search is not submitted | High |
| HOME-009 | Invalid hotel date range | None | 1. Select Hotels tab<br>2. Choose check-out before check-in<br>3. Click "Search" | Search is blocked or date validation feedback is displayed | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HOME-010 | One-way flight disables return date | None | 1. Select Flights tab<br>2. Choose "One Way" | Return date field becomes disabled or inactive | Medium |
| HOME-011 | Same-day search values | None | 1. Perform search using the earliest allowed same-day date values | Search handles the earliest valid date boundary consistently | Low |

---

## 2. Registration

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REG-001 | Registration page elements displayed | None | 1. Navigate to the signup page | Required fields, mobile number country code selector, terms checkbox, and "Sign Up" button are visible | High |
| REG-002 | Successful registration | Email address is not already registered | 1. Enter valid required data<br>2. Accept terms and conditions<br>3. Click "Sign Up" | Account is created and success message or post-registration redirect is shown | High |
| REG-003 | Country code selector works | None | 1. Open mobile country code selector<br>2. Select another country code | Selected country code is applied to the mobile number field | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REG-004 | First name empty | None | 1. Leave first name empty<br>2. Fill other required fields<br>3. Submit form | Validation error is displayed for first name | High |
| REG-005 | Invalid email format | None | 1. Enter invalid email format<br>2. Fill other required fields<br>3. Submit form | Validation error indicates email format is invalid | High |
| REG-006 | Password mismatch | None | 1. Enter password<br>2. Enter different confirm password<br>3. Submit form | Validation error indicates passwords do not match | High |
| REG-007 | Duplicate email | Existing user with same email already exists | 1. Enter already-registered email<br>2. Fill other valid data<br>3. Submit form | Registration is blocked and duplicate-email error is displayed | High |
| REG-008 | Terms and conditions unchecked | None | 1. Fill valid registration data<br>2. Leave terms unchecked<br>3. Submit form | Registration is blocked and user is prompted to accept terms | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REG-009 | Minimum password length boundary | None | 1. Enter password at the minimum accepted length<br>2. Fill other valid data<br>3. Submit form | Registration succeeds or validates consistently at the minimum boundary | Low |
| REG-010 | Mobile number with selected country code | None | 1. Select country code<br>2. Enter valid number at expected length boundary | Number is accepted in the expected format | Low |

---

## 3. Login

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGIN-001 | Successful login | Registered user exists | 1. Navigate to login page<br>2. Enter valid email<br>3. Enter valid password<br>4. Click "Login" | User is redirected to the dashboard or prior protected page | High |
| LOGIN-002 | Remember Me login | Registered user exists | 1. Enter valid credentials<br>2. Check "Remember Me"<br>3. Click "Login" | Session remains active according to remember-me behavior | Medium |
| LOGIN-003 | Login page alternate options displayed | None | 1. Navigate to login page | Forgot password link, signup link, and any enabled social login buttons are visible | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGIN-004 | Invalid email or password | None | 1. Enter invalid email or password<br>2. Click "Login" | Error message is displayed and login does not succeed | High |
| LOGIN-005 | Empty email | None | 1. Leave email empty<br>2. Enter password<br>3. Click "Login" | Validation or login error is displayed | High |
| LOGIN-006 | Empty password | None | 1. Enter email<br>2. Leave password empty<br>3. Click "Login" | Validation or login error is displayed | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGIN-007 | Email retained after failed login | None | 1. Enter email<br>2. Enter invalid password<br>3. Click "Login" | Email remains populated while password is cleared | Medium |
| LOGIN-008 | Multiple failed login attempts | None | 1. Submit invalid credentials repeatedly | Site consistently handles repeated failures and may activate additional protection such as CAPTCHA | Low |

---

## 4. Forgot Password

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FP-001 | Request password reset with existing email | Registered user exists | 1. Open Forgot Password page<br>2. Enter registered email<br>3. Click submit | Confirmation message indicates reset email was sent | High |
| FP-002 | Reset password with valid link | Valid reset link is available | 1. Open reset password page from email link<br>2. Enter valid new password<br>3. Confirm password<br>4. Submit | Password is changed and user is returned to login with success feedback | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FP-003 | Unknown email address | None | 1. Enter non-existent email on Forgot Password page<br>2. Submit | Error message indicates no account exists for that email | High |
| FP-004 | Empty email field | None | 1. Leave email field empty<br>2. Submit | Validation error is displayed | High |
| FP-005 | Reset password mismatch | Valid reset link is available | 1. Enter new password<br>2. Enter different confirm password<br>3. Submit | Password reset is blocked and mismatch error is displayed | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FP-006 | Expired reset link | Expired reset link is available | 1. Open expired reset link | Link is rejected and user is prompted to request a new reset email | Medium |

---

## 5. Hotels Search And Listing

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HOTEL-001 | Hotel listing page displays search summary and results count | Valid hotel search has been submitted | 1. View hotel listing page | Search summary, total results count, filters, and sorting controls are visible | High |
| HOTEL-002 | Hotel cards display expected content | Valid hotel search has been submitted | 1. View hotel listing page | Each hotel card shows image, name, location, rating, price, and action button | High |
| HOTEL-003 | Sort hotels by price | Valid hotel search has been submitted | 1. Change sort to "Price: Low to High" or "Price: High to Low" | Hotel results reorder according to selected sort | Medium |
| HOTEL-004 | Filter hotels by star rating or facilities | Valid hotel search has been submitted | 1. Apply star or facility filters | Hotel results update to match selected filters | High |
| HOTEL-005 | Open hotel details from listing | Valid hotel search has been submitted | 1. Click hotel name or "View Details" | Hotel details page opens | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HOTEL-006 | Search with non-matching destination | None | 1. Search for destination with no available properties | Empty-state or no-results feedback is shown | Medium |
| HOTEL-007 | Invalid hotel date range from listing edit | Listing page is open with editable search summary | 1. Set check-out before check-in<br>2. Apply search | Validation prevents invalid search update | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HOTEL-008 | Price range slider minimum and maximum bounds | Hotel listing page is open | 1. Drag slider to minimum and maximum ends | Result set updates correctly at both range extremes | Low |
| HOTEL-009 | Clear all hotel filters | One or more filters are active | 1. Click "Clear All Filters" | Filters reset and full unfiltered listing returns | Medium |

---

## 6. Hotel Details And Booking

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HBOOK-001 | Hotel details page content displayed | Hotel details page is open | 1. Review hotel details page | Gallery, description, map link, amenities, room availability, reviews, and policies are visible | High |
| HBOOK-002 | View room availability and select room | Hotel details page is open and rooms are available | 1. Review room options<br>2. Click "Select" or "Book Now" on an available room | Booking form opens for the chosen room | High |
| HBOOK-003 | Submit valid hotel booking form | Room selection form is open | 1. Enter valid guest information<br>2. Review price breakdown<br>3. Click booking continuation button | User proceeds to payment step | High |
| HBOOK-004 | Reviews section displayed on hotel details page | Hotel details page is open | 1. Scroll to reviews area | Aggregate rating and individual reviews are visible | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HBOOK-005 | Required guest details missing | Hotel booking form is open | 1. Leave required guest fields empty<br>2. Submit booking form | Validation errors are displayed and form is not submitted | High |
| HBOOK-006 | Sold-out room cannot be booked | Hotel details page includes sold-out inventory | 1. Attempt to select a sold-out room | Booking action is blocked and room remains unavailable | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| HBOOK-007 | Special requests text boundary | Hotel booking form is open | 1. Enter special requests at maximum practical length<br>2. Continue booking | Text is accepted or validated consistently at the boundary | Low |

---

## 7. Flights Search And Booking

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FLIGHT-001 | Flight listing displays itinerary cards | Valid flight search has been submitted | 1. View flight listing page | Airline, times, stops, price, and selection controls are displayed for each result | High |
| FLIGHT-002 | Flight filters work | Valid flight search has been submitted | 1. Apply airline, stops, or departure-time filters | Flight results update to match selected filters | High |
| FLIGHT-003 | View flight details from listing | Valid flight search has been submitted | 1. Click "View Details" | Expanded or detailed fare information is displayed | Medium |
| FLIGHT-004 | Proceed to flight booking with valid passenger data | Flight has been selected | 1. Enter valid passenger details<br>2. Accept terms if required<br>3. Continue | User proceeds to payment step | High |
| FLIGHT-005 | Round-trip search shows outbound and return selections | Valid round-trip search has been submitted | 1. Review results | Outbound and return itineraries are displayed | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FLIGHT-006 | Required passenger field missing | Flight booking form is open | 1. Leave a required passenger field empty<br>2. Continue | Validation error is displayed | High |
| FLIGHT-007 | Passport expiry too soon | Flight booking form is open for travel requiring passport | 1. Enter passport expiry less than six months from travel date<br>2. Continue | Validation error indicates passport validity is insufficient | High |
| FLIGHT-008 | Invalid passport number format | Flight booking form is open | 1. Enter invalid passport format<br>2. Continue | Validation error is displayed | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FLIGHT-009 | One-way trip boundary on booking flow | Valid one-way flight search has been submitted | 1. Complete one-way flight selection<br>2. Continue to booking | Booking flow proceeds without requiring return leg data | Low |

---

## 8. Tours Search And Booking

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| TOUR-001 | Tour listing cards displayed | Valid tour search has been submitted | 1. View tours listing page | Tour cards show image, title, destination, duration, price, and rating | High |
| TOUR-002 | Filter tours by destination or type | Valid tour search has been submitted | 1. Apply destination or tour-type filters | Tours list updates to match selected filters | Medium |
| TOUR-003 | Tour details page displays itinerary and inclusions | Tour details page is open | 1. Review tour details page | Itinerary, inclusions, exclusions, departure dates, and pricing are visible | High |
| TOUR-004 | Book tour with valid traveler information | Tour details page is open and departure date is available | 1. Select departure date<br>2. Enter traveler details<br>3. Click "Book Now" | User proceeds to payment step | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| TOUR-005 | Lead traveler details missing | Tour booking form is open | 1. Leave required traveler fields empty<br>2. Submit | Validation errors are displayed | High |
| TOUR-006 | Unavailable departure date selected | Tour has unavailable dates | 1. Attempt to select an unavailable departure date | Booking cannot continue with unavailable departure | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| TOUR-007 | Adult and child count recalculates total | Tour booking form is open | 1. Adjust adult and child counts at minimum or maximum tested values | Total price recalculates consistently | Low |

---

## 9. Cars Search And Booking

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| CAR-001 | Car listing cards displayed | Valid car search has been submitted | 1. View car listing page | Vehicle image, category, features, rental company, and pricing are visible | High |
| CAR-002 | Compare cars | Valid car search has been submitted | 1. Select compare option for multiple cars | Comparison view or comparison data is displayed | Medium |
| CAR-003 | Add insurance and extras to booking | Car booking form is open | 1. Select insurance or extras<br>2. Review total | Total price updates to include selected options | High |
| CAR-004 | Book car with valid driver information | Car booking form is open | 1. Enter valid driver details<br>2. Accept terms<br>3. Continue | User proceeds to payment step | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| CAR-005 | Required driver information missing | Car booking form is open | 1. Leave required driver fields empty<br>2. Continue | Validation errors are displayed | High |
| CAR-006 | Driver below minimum age | Car booking form is open | 1. Enter age below minimum policy threshold<br>2. Continue | Booking is blocked or age surcharge/policy message is shown | High |
| CAR-007 | Terms and conditions unchecked | Car booking form is open | 1. Fill valid data<br>2. Leave terms unchecked<br>3. Continue | Booking does not proceed and terms validation is shown | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| CAR-008 | Same pick-up and drop-off location | Car booking form is open | 1. Set same pick-up and drop-off location<br>2. Continue | Booking flow handles same-location return consistently | Low |

---

## 10. Visa Services

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| VISA-001 | Visa requirements form displayed | None | 1. Open the Visa page | Nationality selector, Destination selector, and requirement lookup action are visible | High |
| VISA-002 | Check visa requirements for selected route | None | 1. Select nationality<br>2. Select destination<br>3. Click "Check Requirements" or equivalent action | Visa requirement details, processing time, validity, required documents, and fees are displayed | High |
| VISA-003 | Submit visa application when application form is available | Visa application form is enabled and user has required documents | 1. Complete visa application fields<br>2. Upload required documents<br>3. Submit application | Visa application is submitted and application status or confirmation is displayed | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| VISA-004 | Nationality not selected | None | 1. Leave nationality empty<br>2. Select destination<br>3. Submit requirement check | Validation message is displayed | High |
| VISA-005 | Destination not selected | None | 1. Select nationality<br>2. Leave destination empty<br>3. Submit requirement check | Validation message is displayed | High |
| VISA-006 | Missing required visa application fields | Visa application form is enabled | 1. Leave one or more required applicant fields empty<br>2. Submit application | Validation errors are displayed and application is not submitted | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| VISA-007 | Document upload at allowed size limit | Visa application form is enabled | 1. Upload a supported document at the maximum allowed size<br>2. Submit application | Document is accepted at the allowed boundary | Low |

---

## 11. User Dashboard And Booking Management

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| UDB-001 | Dashboard sections displayed | Logged in as authenticated user | 1. Open dashboard | My Bookings, My Profile, Wallet, Wishlist, Reviews, and Settings sections are available | High |
| UDB-002 | View booking details | Logged in and at least one booking exists | 1. Open My Bookings<br>2. Click "View Details" | Booking detail page opens with status, traveler data, and pricing breakdown | High |
| UDB-003 | Modify eligible booking | Logged in and modifiable booking exists | 1. Open booking details<br>2. Click "Modify"<br>3. Change eligible details<br>4. Confirm changes | Booking updates successfully and confirmation is shown | High |
| UDB-004 | Cancel eligible booking | Logged in and cancellable booking exists | 1. Open booking details<br>2. Click "Cancel"<br>3. Confirm cancellation | Booking status changes to cancelled and refund details are displayed | High |
| UDB-005 | Remove item from wishlist | Logged in and wishlist is not empty | 1. Open Wishlist<br>2. Click "Remove" on an item | Item is removed from wishlist | Medium |
| UDB-006 | Update profile details | Logged in | 1. Open My Profile<br>2. Update editable fields<br>3. Save | Profile information is updated successfully | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| UDB-007 | Modify non-eligible booking | Logged in and non-modifiable booking exists | 1. Open booking details for restricted booking<br>2. Attempt modification | Modification is blocked and policy feedback is displayed | Medium |
| UDB-008 | Cancel non-eligible booking | Logged in and non-cancellable booking exists | 1. Open booking details for restricted booking<br>2. Attempt cancellation | Cancellation is blocked and applicable policy is displayed | Medium |
| UDB-009 | Invalid profile email update | Logged in | 1. Enter invalid email format in profile<br>2. Save | Validation error is displayed | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| UDB-010 | Cancellation policy threshold boundary | Logged in and booking has a free-cancellation deadline | 1. Attempt cancellation near the policy cut-off time | Refund amount and policy messaging match the applicable boundary rules | Low |

---

## 12. Payment Processing

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| PAY-001 | Payment summary displayed | User is on payment page | 1. Review payment page | Booking summary, price breakdown, payment methods, and terms checkbox are visible | High |
| PAY-002 | Apply valid promo code | Valid promo code exists | 1. Enter valid promo code<br>2. Click "Apply" | Discount is applied and total updates | Medium |
| PAY-003 | Successful card payment | User is on payment page and uses valid card | 1. Select card payment<br>2. Enter valid cardholder, card number, expiry, and CVV<br>3. Accept terms<br>4. Click "Pay Now" | Payment succeeds and booking confirmation page is displayed | High |
| PAY-004 | Successful wallet payment | User has enough wallet balance | 1. Select wallet or credits payment<br>2. Confirm payment | Payment succeeds and booking confirmation page is displayed | Medium |
| PAY-005 | Confirmation page displayed after successful payment | Payment was successful | 1. Review confirmation page | Booking reference and follow-up actions such as invoice or voucher download are visible | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| PAY-006 | Invalid card number | User is on payment page | 1. Enter invalid card number<br>2. Submit payment | Card validation error is displayed | High |
| PAY-007 | Expired card | User is on payment page | 1. Enter past expiry date<br>2. Submit payment | Expiry validation error is displayed | High |
| PAY-008 | Invalid CVV | User is on payment page | 1. Enter invalid CVV length or format<br>2. Submit payment | CVV validation error is displayed | High |
| PAY-009 | Terms unchecked | User is on payment page | 1. Fill valid payment data<br>2. Leave terms unchecked<br>3. Submit payment | Payment does not proceed and terms validation is displayed | High |
| PAY-010 | Payment declined or insufficient funds | User is on payment page | 1. Submit payment with failing payment source | Error message is displayed with retry or alternate-payment options | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| PAY-011 | CVV length boundary by card type | User is on payment page | 1. Enter 3-digit CVV for standard card or 4-digit CVV for AmEx-like card | CVV is accepted only when length matches card type rules | Medium |
| PAY-012 | Promo code expiry boundary | Promo code is near expiration | 1. Apply promo code at validity boundary | Promo code is accepted or rejected consistently based on actual validity window | Low |

---

## 13. Currency And Language Selection

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| PREF-001 | Currency selector updates displayed prices | None | 1. Change currency from the top navigation | Prices across the current page update to the selected currency | High |
| PREF-002 | Language selector updates interface text | None | 1. Change language from the top navigation | Interface text updates to the selected language | High |
| PREF-003 | Arabic or RTL language applies RTL layout | RTL language option is available | 1. Select Arabic or another RTL language | Page layout and text direction switch to RTL where applicable | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| PREF-005 | Unsupported preference value cannot be applied | None | 1. Attempt to select unavailable currency or language option | Invalid selection is not applied | Low |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| PREF-006 | Currency preference persists across page navigation | None | 1. Change currency<br>2. Navigate to another page | Selected currency remains active across navigation | Medium |
| PREF-007 | Authenticated preference persists after relogin | Logged in as user | 1. Change language or currency<br>2. Log out and log back in | Stored preference remains applied if profile persistence is supported | Low |

---

## 14. Search And Filters

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FILTER-001 | Filter sidebar controls displayed on listing pages | User is on a hotels, flights, tours, or cars listing page | 1. Review the listing page sidebar | Filter groups and sort controls are visible | High |
| FILTER-002 | Result count updates after applying filter | User is on a listing page with available filters | 1. Apply one or more filters | Result count updates to reflect the filtered result set | High |
| FILTER-003 | Active filter tag can be removed | One or more filters are active | 1. Remove an active filter tag | Corresponding filter is cleared and results refresh | Medium |
| FILTER-004 | Clear all filters resets listing | One or more filters are active | 1. Click "Clear All Filters" | All active filters are cleared and listing resets to the default state | Medium |
| FILTER-005 | Sorting control reorders results | User is on a listing page | 1. Select a different sort option | Result ordering updates according to the selected sort | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FILTER-006 | Filter combination returns no results | User is on a listing page | 1. Apply a restrictive combination of filters | Empty-state or zero-results feedback is displayed | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FILTER-007 | Price or time range filter at extreme bounds | User is on a listing page with range sliders | 1. Move a range slider to the minimum or maximum boundary | Results update correctly at the selected extreme | Low |

---

## 15. Reviews And Ratings

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REVIEW-001 | Aggregate ratings displayed on listing cards | User is on a hotel, tour, or car listing page | 1. Review listing cards | Rating score, label, and review count are displayed | High |
| REVIEW-002 | Review breakdown displayed on detail page | Hotel, tour, or car detail page is open | 1. Scroll to the reviews section | Aggregate score, category breakdown, and individual reviews are visible | High |
| REVIEW-003 | Submit review for completed booking | Logged in user has an eligible completed booking | 1. Open review submission flow<br>2. Enter valid ratings and comment<br>3. Submit review | Review is submitted successfully or queued for moderation | High |
| REVIEW-004 | Sort reviews | Detail page has multiple reviews | 1. Change review sort option | Review list updates according to selected order | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REVIEW-005 | Review comment below minimum length | Logged in user is on review submission form | 1. Enter comment shorter than the minimum length<br>2. Submit review | Validation error is displayed | Medium |
| REVIEW-006 | Ineligible user attempts to submit review | Logged in user does not have a completed booking for the item | 1. Attempt to access or submit review form | Review submission is blocked | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REVIEW-007 | Maximum allowed photo upload count | Logged in user is on review submission form | 1. Upload the maximum allowed number of photos<br>2. Submit review | Upload is accepted at the allowed boundary | Low |

---

## 16. Offers And Deals

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| OFFER-001 | Offers page content displayed | None | 1. Open Offers page | Hero banner, category filters, destination controls, and offer cards are visible | High |
| OFFER-002 | Filter offers by category | Offers page is open | 1. Select a category tab or filter | Visible offers update to match selected category | Medium |
| OFFER-003 | Offer Book Now action applies deal | Valid offer exists | 1. Click "Book Now" on an offer | Offer is applied and user is redirected to relevant booking or listing flow | High |
| OFFER-004 | Newsletter subscription with valid email | Offers page is open | 1. Enter valid email<br>2. Click "Subscribe" | Subscription confirmation message is displayed | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| OFFER-005 | Newsletter subscription with invalid email | Offers page is open | 1. Enter invalid email<br>2. Click "Subscribe" | Validation error is displayed | Medium |
| OFFER-006 | Expired offer cannot be applied | Expired offer exists | 1. Attempt to use expired offer | Offer is rejected or clearly marked as unavailable | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| OFFER-007 | Offer validity date boundary | Offer expires today or at a known cut-off time | 1. Attempt to use the offer near expiration time | Offer acceptance or rejection matches the documented validity boundary | Low |

---

## 17. Logout

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGOUT-001 | Logout from user dropdown | User is logged in | 1. Open user menu<br>2. Click "Logout" | Session ends and the home page shows Login and Signup links again | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGOUT-002 | Access protected page after logout | User has logged out | 1. Attempt to open dashboard or booking-management URL | User is redirected to login page and cannot access protected content | High |
