# Swag Labs Test Cases

**Website URL:** https://www.saucedemo.com/
**Test Suite Version:** 1.0

---

## Table of Contents
1. [Login](#1-login)
2. [Product Inventory](#2-product-inventory)
3. [Product Detail](#3-product-detail)
4. [Shopping Cart](#4-shopping-cart)
5. [Checkout - Information](#5-checkout---information)
6. [Checkout - Overview](#6-checkout---overview)
7. [Checkout - Confirmation](#7-checkout---confirmation)
8. [Navigation Menu](#8-navigation-menu)
9. [Logout](#9-logout)
10. [Reset App State](#10-reset-app-state)

---

## Test Credentials

| Username | Description |
|----------|-------------|
| standard_user | Standard user for normal testing |
| locked_out_user | User that is locked out |
| problem_user | User with UI/functionality problems |
| performance_glitch_user | User with delayed responses |
| error_user | User that triggers errors |
| visual_user | User with visual glitches |

**Password for all users:** secret_sauce

---

## 1. Login

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-LOGIN-001 | Valid login with standard_user | None | 1. Navigate to login page<br>2. Enter "standard_user" as username<br>3. Enter "secret_sauce" as password<br>4. Click "Login" | User redirected to product inventory page | High |
| SL-LOGIN-002 | Login page elements displayed | None | 1. Navigate to login page | Username field, Password field, Login button, and accepted usernames/password info visible | Medium |
| SL-LOGIN-003 | Login with each valid user type | None | 1. Login with standard_user<br>2. Logout<br>3. Repeat for each user type | All valid users can log in (except locked_out_user) | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-LOGIN-004 | Invalid username | None | 1. Enter invalid username<br>2. Enter valid password<br>3. Click "Login" | Error message: "Epic sadface: Username and password do not match" | High |
| SL-LOGIN-005 | Invalid password | None | 1. Enter valid username<br>2. Enter incorrect password<br>3. Click "Login" | Error message displayed, user remains on login page | High |
| SL-LOGIN-006 | Empty username | None | 1. Leave username empty<br>2. Enter password<br>3. Click "Login" | Error message: "Epic sadface: Username is required" | High |
| SL-LOGIN-007 | Empty password | None | 1. Enter username<br>2. Leave password empty<br>3. Click "Login" | Error message: "Epic sadface: Password is required" | High |
| SL-LOGIN-008 | Both fields empty | None | 1. Leave both fields empty<br>2. Click "Login" | Error message: "Epic sadface: Username is required" | High |
| SL-LOGIN-009 | Locked out user | None | 1. Enter "locked_out_user"<br>2. Enter "secret_sauce"<br>3. Click "Login" | Error message: "Epic sadface: Sorry, this user has been locked out" | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-LOGIN-010 | Username with leading/trailing spaces | None | 1. Enter " standard_user " (with spaces)<br>2. Enter valid password<br>3. Click "Login" | Login fails or spaces trimmed and login succeeds | Medium |
| SL-LOGIN-011 | Case sensitivity | None | 1. Enter "Standard_User" (different case)<br>2. Enter valid password<br>3. Click "Login" | Login fails (username is case-sensitive) | Medium |

### UI/UX Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-LOGIN-012 | Password field masking | None | 1. Enter text in password field | Password characters are masked | High |
| SL-LOGIN-013 | Error message dismissible | SL-LOGIN-004 completed | 1. Click X button on error message | Error message disappears | Medium |
| SL-LOGIN-014 | Tab navigation | None | 1. Use Tab key to navigate | Focus moves: username → password → Login button | Medium |
| SL-LOGIN-015 | Enter key submission | None | 1. Fill credentials<br>2. Press Enter | Form submits | Medium |

---

## 2. Product Inventory

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-INV-001 | Products displayed | User logged in | 1. View inventory page | All products displayed with name, description, price, and "Add to cart" button | High |
| SL-INV-002 | Add product to cart | User logged in | 1. Click "Add to cart" on any product | Button changes to "Remove", cart badge shows "1" | High |
| SL-INV-003 | Add multiple products | User logged in | 1. Add product 1 to cart<br>2. Add product 2 to cart<br>3. Add product 3 to cart | Cart badge shows "3" | High |
| SL-INV-004 | Remove product from cart | Product in cart | 1. Click "Remove" button | Button changes to "Add to cart", cart badge decrements | High |
| SL-INV-005 | Sort A-Z (default) | User logged in | 1. Check default sort order | Products sorted alphabetically A-Z | High |
| SL-INV-006 | Sort Z-A | User logged in | 1. Select "Name (Z to A)" from dropdown | Products sorted alphabetically Z-A | High |
| SL-INV-007 | Sort Price low to high | User logged in | 1. Select "Price (low to high)" | Products sorted by price ascending | High |
| SL-INV-008 | Sort Price high to low | User logged in | 1. Select "Price (high to low)" | Products sorted by price descending | High |
| SL-INV-009 | Navigate to product detail | User logged in | 1. Click on product name or image | Navigates to product detail page | High |
| SL-INV-010 | Cart icon navigation | User logged in | 1. Click cart icon | Navigates to shopping cart page | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-INV-011 | Access inventory without login | Not logged in | 1. Navigate directly to inventory URL | Redirected to login or access denied | High |

### UI/UX Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-INV-012 | Product images displayed | User logged in | 1. View inventory | All products have images | Medium |
| SL-INV-013 | Price formatting | User logged in | 1. View product prices | Prices formatted as $XX.XX | Medium |
| SL-INV-014 | Cart badge visibility | User logged in, cart empty | 1. View cart icon | No badge shown when cart is empty | Medium |
| SL-INV-015 | Cart badge updates real-time | User logged in | 1. Add item<br>2. Observe badge | Badge updates immediately | High |
| SL-INV-016 | Sort dropdown options | User logged in | 1. Click sort dropdown | Shows 4 options: A-Z, Z-A, Price low-high, Price high-low | Medium |
| SL-INV-017 | Hamburger menu visible | User logged in | 1. View top-left corner | Hamburger menu icon visible | Medium |

---

## 3. Product Detail

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-PD-001 | Product details displayed | User logged in | 1. Click on a product | Product name, description, price, and image displayed | High |
| SL-PD-002 | Add to cart from detail page | User logged in, on product detail | 1. Click "Add to cart" | Product added, button changes to "Remove", cart badge updates | High |
| SL-PD-003 | Remove from cart on detail page | Product in cart, on detail page | 1. Click "Remove" | Product removed, button changes to "Add to cart" | High |
| SL-PD-004 | Back to products | On product detail page | 1. Click "Back to products" | Returns to inventory page | High |

### UI/UX Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-PD-005 | Large product image | On product detail | 1. View product image | Larger image than inventory thumbnail | Medium |
| SL-PD-006 | Price matches inventory | On product detail | 1. Compare price with inventory listing | Price is identical | High |
| SL-PD-007 | Cart state preserved | Product added from inventory | 1. Navigate to product detail | "Remove" button shown (not "Add to cart") | High |

---

## 4. Shopping Cart

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CART-001 | View cart with items | Items added to cart | 1. Click cart icon | All added items displayed with name, description, price, quantity | High |
| SL-CART-002 | Remove item from cart | Items in cart | 1. Click "Remove" on an item | Item removed from cart, list updates | High |
| SL-CART-003 | Continue shopping | On cart page | 1. Click "Continue Shopping" | Returns to inventory page | High |
| SL-CART-004 | Proceed to checkout | Items in cart | 1. Click "Checkout" | Navigates to checkout information page | High |
| SL-CART-005 | Cart persists across pages | Items added | 1. Navigate to different pages<br>2. Return to cart | Items still in cart | High |
| SL-CART-006 | Quantity display | Items in cart | 1. View cart | Quantity shown as "1" for each item | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CART-007 | Empty cart | No items added | 1. Navigate to cart | Empty cart state or message displayed | Medium |
| SL-CART-008 | Checkout with empty cart | No items in cart | 1. Navigate to cart<br>2. Try to checkout | Prevented or appropriate error | Medium |

### UI/UX Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CART-009 | Cart item layout | Items in cart | 1. View cart | Each item shows quantity, name, description, price | Medium |
| SL-CART-010 | Remove button for each item | Multiple items in cart | 1. View cart | Each item has its own "Remove" button | Medium |

---

## 5. Checkout - Information

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CHK1-001 | Complete checkout info | Items in cart, on checkout page | 1. Enter First Name<br>2. Enter Last Name<br>3. Enter Postal Code<br>4. Click "Continue" | Navigates to checkout overview | High |
| SL-CHK1-002 | Cancel checkout | On checkout info page | 1. Click "Cancel" | Returns to cart page | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CHK1-003 | First Name empty | On checkout info | 1. Leave First Name empty<br>2. Fill other fields<br>3. Click "Continue" | Error: "Error: First Name is required" | High |
| SL-CHK1-004 | Last Name empty | On checkout info | 1. Leave Last Name empty<br>2. Fill other fields<br>3. Click "Continue" | Error: "Error: Last Name is required" | High |
| SL-CHK1-005 | Postal Code empty | On checkout info | 1. Leave Postal Code empty<br>2. Fill other fields<br>3. Click "Continue" | Error: "Error: Postal Code is required" | High |
| SL-CHK1-006 | All fields empty | On checkout info | 1. Leave all fields empty<br>2. Click "Continue" | Error message for first required field | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CHK1-007 | Single character inputs | On checkout info | 1. Enter single character in each field<br>2. Click "Continue" | Form accepts or rejects appropriately | Low |
| SL-CHK1-008 | Very long inputs | On checkout info | 1. Enter very long strings<br>2. Click "Continue" | System handles gracefully (truncates or accepts) | Low |
| SL-CHK1-009 | Special characters | On checkout info | 1. Enter special characters in fields<br>2. Click "Continue" | System handles appropriately | Low |
| SL-CHK1-010 | Numeric First/Last Name | On checkout info | 1. Enter numbers in name fields<br>2. Click "Continue" | May accept (no strict validation) | Low |

### UI/UX Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CHK1-011 | Form elements displayed | On checkout info | 1. View page | First Name, Last Name, Postal Code fields, Continue and Cancel buttons visible | Medium |
| SL-CHK1-012 | Error message style | Error triggered | 1. Submit with empty field | Error displayed with red styling and X icon | Medium |

---

## 6. Checkout - Overview

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CHK2-001 | Order summary displayed | Completed checkout info | 1. View checkout overview | All cart items listed with prices | High |
| SL-CHK2-002 | Item total correct | Items in cart | 1. View Item total | Sum of all item prices | High |
| SL-CHK2-003 | Tax calculated | On overview page | 1. View Tax amount | Tax calculated (typically 8%) | High |
| SL-CHK2-004 | Total correct | On overview page | 1. View Total | Total = Item Total + Tax | High |
| SL-CHK2-005 | Finish purchase | On overview page | 1. Click "Finish" | Order placed, confirmation page shown | High |
| SL-CHK2-006 | Cancel from overview | On overview page | 1. Click "Cancel" | Returns to inventory page | High |

### UI/UX Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CHK2-007 | Payment info displayed | On overview page | 1. View payment section | Shows "SauceCard #31337" | Medium |
| SL-CHK2-008 | Shipping info displayed | On overview page | 1. View shipping section | Shows shipping method (Free Pony Express) | Medium |
| SL-CHK2-009 | Price breakdown clear | On overview page | 1. View totals section | Item total, Tax, and Total clearly labeled | Medium |

---

## 7. Checkout - Confirmation

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CHK3-001 | Confirmation displayed | Order completed | 1. Complete checkout | "Thank you for your order!" message displayed | High |
| SL-CHK3-002 | Cart cleared | Order completed | 1. View cart after order | Cart is empty, no badge | High |
| SL-CHK3-003 | Back to products | On confirmation page | 1. Click "Back Home" | Returns to inventory page | High |

### UI/UX Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-CHK3-004 | Success image displayed | Order completed | 1. View confirmation page | Pony Express image or checkmark visible | Medium |
| SL-CHK3-005 | Order dispatch message | Order completed | 1. View confirmation page | "Your order has been dispatched" or similar message | Medium |

---

## 8. Navigation Menu

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-NAV-001 | Open hamburger menu | User logged in | 1. Click hamburger icon (☰) | Side menu opens with options | High |
| SL-NAV-002 | All Items navigation | Menu open | 1. Click "All Items" | Navigates to inventory page | High |
| SL-NAV-003 | About navigation | Menu open | 1. Click "About" | Navigates to Sauce Labs website | Medium |
| SL-NAV-004 | Close menu | Menu open | 1. Click X or outside menu | Menu closes | Medium |

### UI/UX Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-NAV-005 | Menu items visible | Menu open | 1. View menu | All Items, About, Logout, Reset App State visible | Medium |
| SL-NAV-006 | Menu animation | Open/close menu | 1. Open and close menu | Smooth slide animation | Low |

---

## 9. Logout

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-LOGOUT-001 | Successful logout | User logged in | 1. Open hamburger menu<br>2. Click "Logout" | User redirected to login page | High |
| SL-LOGOUT-002 | Session cleared | Logged out | 1. Try to access inventory directly | Redirected to login | High |
| SL-LOGOUT-003 | Cart cleared on logout | Items in cart, logged out | 1. Log back in<br>2. Check cart | Cart is empty (session reset) | High |
| SL-LOGOUT-004 | Back button after logout | Logged out | 1. Click browser back button | Cannot access protected pages | High |

---

## 10. Reset App State

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-RESET-001 | Reset clears cart | Items in cart | 1. Open hamburger menu<br>2. Click "Reset App State" | Cart cleared, badge removed | High |
| SL-RESET-002 | Reset button states | Items added (buttons show "Remove") | 1. Click "Reset App State" | All "Remove" buttons revert to "Add to cart" | High |
| SL-RESET-003 | Reset preserves login | User logged in with items | 1. Click "Reset App State" | User remains logged in | Medium |

---

## 11. Browser Behavior & Session Management

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-BROWSER-001 | Refresh preserves cart | Items in cart | 1. Add items to cart<br>2. Refresh the page<br>3. Check cart | Cart items still present | High |
| SL-BROWSER-002 | Refresh preserves sort | Inventory sorted | 1. Sort inventory Z-A<br>2. Refresh page<br>3. Check sort order | Sort order preserved as Z-A | High |
| SL-BROWSER-003 | Direct URL navigation | Logged in | 1. Enter inventory.html directly in URL | Page loads and is accessible | High |
| SL-BROWSER-004 | Direct URL without login | Not logged in | 1. Enter inventory URL directly<br>2. Check redirect | Redirected to login page | High |
| SL-BROWSER-005 | Browser back button | On product detail | 1. View product detail<br>2. Click browser back | Returns to inventory with sort preserved | High |
| SL-BROWSER-006 | Browser forward button | After clicking back | 1. Click browser back<br>2. Click browser forward | Returns to product detail page | Medium |
| SL-BROWSER-007 | Multi-tab cart sync | Cart open in tab 1 | 1. Add item in tab 1<br>2. Switch to tab 2 cart<br>3. Refresh tab 2 | Cart in tab 2 shows new item | Medium |
| SL-BROWSER-008 | Session persistence | Logged in | 1. Close browser completely<br>2. Reopen site | Session state depending on browser settings | Low |
| SL-BROWSER-009 | Incognito session isolation | Normal and incognito windows | 1. Login in normal window<br>2. Open incognito<br>3. Try to access inventory | Incognito requires separate login | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-BROWSER-010 | Access inventory while logged out | Logged out | 1. Navigate to inventory URL<br>2. Check error message | Error: "You can only access '/inventory.html' when logged in" | High |

---

## 12. User Persona Special Behaviors

### Functional Tests - Standard User

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-PERSONA-001 | standard_user normal flow | None | 1. Login as standard_user<br>2. Browse inventory<br>3. Add to cart<br>4. Checkout | All functionality works perfectly, no errors | High |
| SL-PERSONA-002 | standard_user pricing | Logged in as standard_user | 1. View all products | All prices display correctly ($29.99, $9.99, etc.) | High |

### Functional Tests - Locked Out User

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-PERSONA-003 | locked_out_user login denied | None | 1. Enter locked_out_user<br>2. Enter secret_sauce<br>3. Click Login | Error: "Sorry, this user has been locked out" | High |

### Functional Tests - Problem User

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-PERSONA-004 | problem_user missing buttons | None | 1. Login as problem_user<br>2. View inventory | Some products may not have "Add to cart" button | High |
| SL-PERSONA-005 | problem_user missing prices | Logged in as problem_user | 1. View inventory<br>2. Check prices | Some product prices may not display | High |
| SL-PERSONA-006 | problem_user missing images | Logged in as problem_user | 1. View inventory<br>2. Check images | Some product images may not load | Medium |

### Functional Tests - Performance Glitch User

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-PERSONA-007 | performance_glitch_user slow load | None | 1. Login as performance_glitch_user<br>2. Monitor page load time | Inventory page loads 5-10 seconds slower than normal | Medium |
| SL-PERSONA-008 | performance_glitch_user delayed cart | Logged in as performance_glitch_user | 1. Add item to cart<br>2. Observe badge update delay | Cart badge updates with slight delay | Medium |

### Functional Tests - Error User

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-PERSONA-009 | error_user checkout error | Logged in as error_user, items in cart | 1. Proceed to checkout<br>2. Complete info<br>3. Click Finish | Error message like "Payment failed" | High |
| SL-PERSONA-010 | error_user inconsistent state | Logged in as error_user | 1. Try to complete checkout<br>2. Observe order status | Order may be created despite error message | Medium |

### Functional Tests - Visual User

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-PERSONA-011 | visual_user CSS glitches | None | 1. Login as visual_user<br>2. View inventory | Text misaligned, colors incorrect, fonts rendering improperly | Medium |
| SL-PERSONA-012 | visual_user button functionality | Logged in as visual_user | 1. Despite visual glitches<br>2. Try "Add to cart" button | Button still functions despite styling issues | High |

---

## 13. Cart & Inventory State Management

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-STATE-001 | No duplicate items in cart | Standard user, item added | 1. Add item from inventory<br>2. Navigate to product detail<br>3. Try to add same item again | Item not duplicated, quantity remains 1 | High |
| SL-STATE-002 | Add from multiple pages | Standard user | 1. Add item from inventory<br>2. Go to product detail<br>3. Remove from detail<br>4. Add again from inventory | Item is removed and re-added correctly | High |
| SL-STATE-003 | Sorting preserves cart | Standard user with items | 1. Add items to cart<br>2. Sort inventory different ways<br>3. Check cart | Cart contents unchanged by sorting | High |
| SL-STATE-004 | Badge accuracy | Standard user | 1. Add 3 items<br>2. Remove 1 item<br>3. Refresh page | Badge accurately shows number of items | High |
| SL-STATE-005 | Reset clears cart items | Standard user with multiple items | 1. Add 3 items<br>2. Click Reset App State<br>3. Check cart | Cart completely empty | High |
| SL-STATE-006 | Reset reverts buttons | Items in cart (Remove buttons visible) | 1. Click Reset App State<br>2. Go to inventory | All buttons revert to "Add to cart" | High |
| SL-STATE-007 | Cart persistence across pages | Standard user with items | 1. Add to cart<br>2. Navigate to detail page<br>3. Go back to inventory | Cart items still present | High |

---

## 14. Checkout Flow Edge Cases

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-EDGE-001 | Single character name | On checkout info | 1. Enter "A" in First Name<br>2. Enter "B" in Last Name<br>3. Click Continue | Either accepted or rejected with validation message | Medium |
| SL-EDGE-002 | Very long name | On checkout info | 1. Enter 100+ character string<br>2. Click Continue | System truncates or rejects gracefully | Low |
| SL-EDGE-003 | Special characters in name | On checkout info | 1. Enter "John@123" in First Name<br>2. Click Continue | May accept or reject depending on validation | Low |
| SL-EDGE-004 | Non-numeric postal code | On checkout info | 1. Enter "ABC12" in Postal Code<br>2. Click Continue | Error: "Postal Code must contain only numbers" | High |
| SL-EDGE-005 | Minimum length validation | On checkout info | 1. Enter 1 character names<br>2. Click Continue | Minimum 2 characters enforced or accepted | Medium |
| SL-EDGE-006 | Postal code numeric only | On checkout info | 1. Enter "12345"<br>2. Click Continue | Accepted, proceeds to next step | High |

### Error Handling Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-EDGE-007 | Partial form submission | On checkout info | 1. Enter only First Name<br>2. Leave others empty<br>3. Click Continue | Partial submission prevented, errors for missing fields | High |
| SL-EDGE-008 | Multiple duplicate orders | Standard user | 1. Complete checkout<br>2. Quickly click Finish again | Either prevented or handled gracefully, no duplicate | Medium |
| SL-EDGE-009 | Session timeout | On checkout step 2 | 1. Wait for extended period<br>2. Try to complete checkout | Session timeout message or re-authentication | Low |
| SL-EDGE-010 | Browser back during checkout | Checkout info page | 1. Fill checkout form<br>2. Click browser back<br>3. Go forward | State may or may not be preserved | Low |

### Tax Calculation Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| SL-EDGE-011 | Tax calculation (8% applied) | On checkout overview | 1. Add items totaling $100<br>2. Check tax | Tax calculated as $8.00 | High |
| SL-EDGE-012 | Total calculation accuracy | Multiple items in cart | 1. Add various priced items<br>2. View overview | Total = Item total + (Item total × 0.08) | High |
| SL-EDGE-013 | Single item tax | Single $10 item in cart | 1. View checkout overview | Tax = $0.80, Total = $10.80 | High |

---

## End-to-End Test Scenarios

### E2E-001: Complete Purchase Flow
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to https://www.saucedemo.com/ | Login page displayed |
| 2 | Login with standard_user / secret_sauce | Inventory page displayed |
| 3 | Add "Sauce Labs Backpack" to cart | Cart badge shows "1" |
| 4 | Add "Sauce Labs Bike Light" to cart | Cart badge shows "2" |
| 5 | Click cart icon | Cart page with 2 items |
| 6 | Click "Checkout" | Checkout info page |
| 7 | Enter: John, Doe, 12345 | Fields populated |
| 8 | Click "Continue" | Checkout overview page |
| 9 | Verify items and total | Correct items and calculated total |
| 10 | Click "Finish" | Confirmation page, "Thank you" message |
| 11 | Click "Back Home" | Inventory page, empty cart |

### E2E-002: Add and Remove Items Flow
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Login as standard_user | Inventory page |
| 2 | Add 3 different items | Cart badge shows "3" |
| 3 | Navigate to cart | 3 items listed |
| 4 | Remove 1 item | 2 items listed, badge shows "2" |
| 5 | Continue shopping | Inventory page |
| 6 | Remove item from inventory | Button reverts, badge shows "1" |
| 7 | Proceed to checkout | Checkout with 1 item |

### E2E-003: Sort and Filter Products
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Login as standard_user | Inventory page, sorted A-Z |
| 2 | Sort by Price (low to high) | Cheapest item first |
| 3 | Sort by Price (high to low) | Most expensive item first |
| 4 | Sort by Name (Z to A) | Reverse alphabetical |
| 5 | Sort by Name (A to Z) | Default alphabetical order |

---

## Test Summary

| Module | Total Tests | High Priority | Medium Priority | Low Priority |
|--------|-------------|---------------|-----------------|--------------|
| Login | 15 | 9 | 5 | 1 |
| Product Inventory | 17 | 10 | 7 | 0 |
| Product Detail | 7 | 5 | 2 | 0 |
| Shopping Cart | 10 | 6 | 4 | 0 |
| Checkout - Information | 12 | 6 | 2 | 4 |
| Checkout - Overview | 9 | 6 | 3 | 0 |
| Checkout - Confirmation | 5 | 3 | 2 | 0 |
| Navigation Menu | 6 | 2 | 3 | 1 |
| Logout | 4 | 4 | 0 | 0 |
| Reset App State | 3 | 2 | 1 | 0 |
| Browser Behavior & Session | 10 | 6 | 3 | 1 |
| User Persona Special Behaviors | 12 | 6 | 4 | 2 |
| Cart & Inventory State | 7 | 7 | 0 | 0 |
| Checkout Flow Edge Cases | 13 | 6 | 5 | 2 |
| **TOTAL** | **151** | **84** | **42** | **11** |

---

## Special User Testing

| User Type | Purpose | Test Focus |
|-----------|---------|------------|
| locked_out_user | Verify lockout functionality | Login should fail with specific error |
| problem_user | Test application error handling | Images may not load, add to cart may fail |
| performance_glitch_user | Performance testing | Pages load slowly, interactions delayed |
| error_user | Error state testing | Various errors triggered during flow |
| visual_user | Visual regression testing | UI elements may appear incorrectly |
