# Test Cases — Swaglab

Generated: 2026-06-04T14:06:32.842285Z  
Model: openai/gpt-4o-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 9 | 66 | 19 | 21 | 26 | 27 | 27 | 7 |

## Login

Total: **12** (positive: 1, negative: 4, edge: 7)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Login with valid credentials | User logged in as <User>, User is on the Login page | 1. Enter 'standard_user' in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click the Login button | authenticates and redirects to Product Inventory page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 |  | Leave the Username field blank and submit |  | 1. Leave the Username field blank<br>2. Fill the Password field with <valid password><br>3. Click Login | Inline validation error appears on the Username field indicating it is required | high |
| TC-003 |  | Leave the Password field blank and submit |  | 1. Fill the Username field with <valid username><br>2. Leave the Password field blank<br>3. Click Login | Inline validation error appears on the Password field indicating it is required | high |
| TC-004 |  | Submit with invalid credentials |  | 1. Fill the Username field with <invalid username><br>2. Fill the Password field with <invalid password><br>3. Click Login | Error message displayed: 'Epic sadface: Username and password do not match any user in this service.' | high |
| TC-005 |  | Attempt to login with locked out user |  | 1. Fill the Username field with 'locked_out_user'<br>2. Fill the Password field with 'secret_sauce'<br>3. Click Login | Error message displayed: 'Epic sadface: Sorry, this user has been locked out.' | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (boundary) | WF-002 | Attempt login with empty Username |  | 1. Leave the Username field empty<br>2. Enter a valid password in the Password field<br>3. Click the Login button | Epic sadface: Username is required. | medium |
| TC-007 (boundary) | WF-003 | Attempt login with empty Password |  | 1. Enter a valid username in the Username field<br>2. Leave the Password field empty<br>3. Click the Login button | Epic sadface: Password is required. | medium |
| TC-008 (boundary) | WF-004 | Attempt login with invalid credentials |  | 1. Enter an invalid username in the Username field<br>2. Enter an invalid password in the Password field<br>3. Click the Login button | Epic sadface: Username and password do not match any user in this service. | medium |
| TC-009 (boundary) | WF-005 | Attempt login with locked out user |  | 1. Enter 'locked_out_user' in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click the Login button | Epic sadface: Sorry, this user has been locked out. | medium |
| TC-010 (input_edge) |  | Attempt login with long Username |  | 1. Enter a long string (200+ characters) in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click the Login button | Login attempt is blocked; error message is shown indicating the username is too long. | low |
| TC-011 (input_edge) |  | Attempt login with special characters in Username |  | 1. Enter special characters (e.g., '!@#$%^&*()') in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click the Login button | Login attempt is blocked; error message is shown indicating invalid username. | low |
| TC-012 (input_edge) |  | Attempt login with leading/trailing whitespace in Username |  | 1. Enter '   standard_user   ' in the Username field<br>2. Enter 'secret_sauce' in the Password field<br>3. Click the Login button | Leading/trailing whitespace is trimmed; user is authenticated and redirected to Product Inventory page. | low |

---

## Product Inventory

Total: **11** (positive: 5, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | View Product Details | User logged in as <Role> | 1. Click on the product name or image in the Product List | opens Product Detail page | high |
| TC-002 | WF-002 | Add Product to Cart | User logged in as <Role> | 1. Click 'Add to cart' button for a product | adds item to cart | high |
| TC-003 | WF-003 | Remove Product from Cart | User logged in as <Role>, Item is added to cart | 1. Click 'Remove' button for the product in the cart | removes item from cart | high |
| TC-004 |  | Sort Products by Name A-Z | User logged in as <Role> | 1. Select 'Name (A–Z)' from the Sort Dropdown | Products are sorted in ascending order by name | medium |
| TC-005 |  | Sort Products by Price Low-High | User logged in as <Role> | 1. Select 'Price (low–high)' from the Sort Dropdown | Products are sorted in ascending order by price | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 |  | Attempt to add product to cart without selecting an item |  | 1. Navigate to the Product Inventory page<br>2. Click 'Add to cart' without selecting any product | No product is added to cart; 'Add to cart' button remains unchanged |  |
| TC-007 |  | Attempt to remove product from cart without selecting an item |  | 1. Navigate to the Product Inventory page<br>2. Click 'Remove' without having any product in the cart | No product is removed from cart; 'Remove' button remains unchanged |  |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (interaction_edge) | WF-002 | Rapidly click 'Add to cart' twice | Product is available in the inventory | 1. Click 'Add to cart' for a product<br>2. Immediately click 'Add to cart' again for the same product | Second click is blocked; only one item is added to the cart, and the cart badge count updates accordingly | medium |
| TC-009 (interaction_edge) | WF-003 | Rapidly click 'Remove' twice | Product is in the cart | 1. Click 'Remove' for a product in the cart<br>2. Immediately click 'Remove' again for the same product | Second click is blocked; product remains removed from the cart, and the cart badge count updates accordingly | medium |
| TC-010 (input_edge) |  | Enter a very long product name |  | 1. Enter a string of 200+ characters in the 'Name' field of a new product | Form accepts the long name or shows an error indicating the name is too long | low |
| TC-011 (input_edge) |  | Enter special characters in the product description |  | 1. Enter a string with special characters in the 'Description' field of a new product | Form accepts the special characters or shows a specific error indicating invalid characters | low |

---

## Product Detail

Total: **9** (positive: 3, negative: 3, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Add product to cart | User logged in as <Role> | 1. Click 'Add to cart / Remove' button | The cart state updates to reflect the added product | high |
| TC-002 | WF-002 | Navigate back to products | User logged in as <Role> | 1. Click 'Back to products' button | Navigates to Product Inventory page | high |
| TC-003 | WF-003 | Navigate to shopping cart | User logged in as <Role> | 1. Click on the Cart Icon | Navigates to Shopping Cart | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Attempt to add a product to the cart when the cart is already full | Cart is at maximum capacity | 1. Click 'Add to cart / Remove' button | Action is blocked; cart state remains unchanged; error shown indicating 'Cart is full' | high |
| TC-005 | WF-002 | Attempt to navigate back to products without any products in the cart | No products in the cart | 1. Click 'Back to products' button | Navigates to Product Inventory page; cart state remains unchanged | medium |
| TC-006 | WF-003 | Attempt to navigate to shopping cart without any items added | No items in the cart | 1. Click on the Cart Icon | Navigates to Shopping Cart; message displayed 'Your cart is empty' | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (interaction_edge) | WF-001 | Rapid consecutive Add to cart / Remove actions | Product is available for adding to cart | 1. Click 'Add to cart' button<br>2. Immediately click 'Remove' button | 'Add to cart' action succeeds, followed by 'Remove' action also succeeding; cart state updates accordingly. | medium |
| TC-008 (interaction_edge) | WF-002 | Back to products navigation after adding to cart | Product has been added to cart | 1. Click 'Add to cart' button<br>2. Click 'Back to products' button | Navigates to Product Inventory page without duplicating the product in the cart. | medium |
| TC-009 (interaction_edge) | WF-003 | Navigate to Shopping Cart from Product Detail | Product is in cart | 1. Click on Cart Icon | Navigates to the Shopping Cart page displaying the product added. | medium |

---

## Shopping Cart

Total: **8** (positive: 3, negative: 3, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Continue Shopping from Shopping Cart | User logged in as <Role>, Shopping Cart has items added | 1. Click Continue Shopping | returns to Product Inventory | high |
| TC-002 | WF-002 | Begin Checkout from Shopping Cart | User logged in as <Role>, Shopping Cart has items added | 1. Click Checkout | begins checkout process | high |
| TC-003 | WF-003 | Remove Item from Shopping Cart | User logged in as <Role>, Shopping Cart has items added | 1. Click Remove button for an item | Item removed from cart | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 | WF-001 | Attempt to continue shopping without any items in the cart |  | 1. Ensure the cart is empty<br>2. Click 'Continue Shopping' | User remains on the Shopping Cart page; no items are returned to the Product Inventory |  |
| TC-005 | WF-002 | Attempt to checkout with no items in the cart |  | 1. Ensure the cart is empty<br>2. Click 'Checkout' | User remains on the Shopping Cart page; no checkout process begins |  |
| TC-006 | WF-003 | Attempt to remove an item that is not in the cart |  | 1. Ensure the cart is empty<br>2. Click 'Remove' for a non-existent item | No action occurs; the item is not removed and remains unchanged |  |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (interaction_edge) | WF-001 | Rapid re-submission after redirect from Continue Shopping | User has items in the cart | 1. Click Continue Shopping<br>2. Press the browser back button immediately after redirection | User is redirected to the Product Inventory without the cart being pre-filled with items | medium |
| TC-008 (interaction_edge) | WF-003 | Remove Item from Cart and check cart status | User has items in the cart | 1. Click Remove on an item in the cart<br>2. Check the cart items displayed | The item is removed from the cart; remaining items are displayed correctly | medium |

---

## Checkout - Information

Total: **11** (positive: 2, negative: 4, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Submit valid checkout information | User logged in as <Customer> | 1. Enter <valid first name> in the First Name field<br>2. Enter <valid last name> in the Last Name field<br>3. Enter <valid zip/postal code> in the Zip/Postal Code field<br>4. Click Continue | User proceeds to the overview step | high |
| TC-002 | WF-002 | Cancel checkout information | User logged in as <Customer> | 1. Click Cancel | User returns to the Shopping Cart | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Leave First Name blank and submit |  | 1. Leave the First_Name field blank<br>2. Fill Last_Name with <valid last name><br>3. Fill Zip_Postal_Code with <valid postal code><br>4. Click Continue | Inline validation error appears on the First_Name field indicating it is required | high |
| TC-004 | WF-001 | Leave Last Name blank and submit |  | 1. Fill First_Name with <valid first name><br>2. Leave the Last_Name field blank<br>3. Fill Zip_Postal_Code with <valid postal code><br>4. Click Continue | Inline validation error appears on the Last_Name field indicating it is required | high |
| TC-005 | WF-001 | Leave Zip/Postal Code blank and submit |  | 1. Fill First_Name with <valid first name><br>2. Fill Last_Name with <valid last name><br>3. Leave the Zip_Postal_Code field blank<br>4. Click Continue | Inline validation error appears on the Zip_Postal_Code field indicating it is required | high |
| TC-006 | WF-001 | Leave all required fields empty and submit |  | 1. Leave the First_Name field blank<br>2. Leave the Last_Name field blank<br>3. Leave the Zip_Postal_Code field blank<br>4. Click Continue | Inline validation error appears on the First_Name field indicating it is required; Inline validation error appears on the Last_Name field indicating it is required; Inline validation error appears on the Zip_Postal_Code field indicating it is required | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (boundary) | WF-001 | Submit with First Name filled, Last Name and Zip/Postal Code empty |  | 1. Enter a valid value in the First Name field<br>2. Leave the Last Name field empty<br>3. Leave the Zip/Postal Code field empty<br>4. Click Continue | Error banner displays: 'Error: Last Name is required' | medium |
| TC-008 (boundary) | WF-001 | Submit with Last Name filled, First Name and Zip/Postal Code empty |  | 1. Enter a valid value in the Last Name field<br>2. Leave the First Name field empty<br>3. Leave the Zip/Postal Code field empty<br>4. Click Continue | Error banner displays: 'Error: First Name is required' | medium |
| TC-009 (boundary) | WF-001 | Submit with Zip/Postal Code filled, First Name and Last Name empty |  | 1. Enter a valid value in the Zip/Postal Code field<br>2. Leave the First Name field empty<br>3. Leave the Last Name field empty<br>4. Click Continue | Error banner displays: 'Error: First Name is required' | medium |
| TC-010 (input_edge) | WF-001 | Submit with leading/trailing whitespace in First Name |  | 1. Enter '   John   ' in the First Name field<br>2. Enter a valid value in the Last Name field<br>3. Enter a valid value in the Zip/Postal Code field<br>4. Click Continue | Form submits successfully; saved value for First Name shows 'John' without extra spaces | low |
| TC-011 (input_edge) | WF-001 | Submit with special characters in Last Name |  | 1. Enter a valid value in the First Name field<br>2. Enter '@Doe!' in the Last Name field<br>3. Enter a valid value in the Zip/Postal Code field<br>4. Click Continue | Form submits successfully; saved value for Last Name shows '@Doe!' | low |

---

## Checkout - Overview

Total: **6** (positive: 2, negative: 2, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Complete the order successfully | User logged in as <Role>, Order summary is displayed with items and totals | 1. Click Finish | The order is completed and navigates to the confirmation page | high |
| TC-002 | WF-002 | Cancel the checkout process | User logged in as <Role>, Order summary is displayed with items and totals | 1. Click Cancel | Exits checkout | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Attempt to finish the order without any payment or shipping information |  | 1. Leave the Payment Information section blank<br>2. Leave the Shipping Information section blank<br>3. Click Finish | Form does not submit; order is not completed; error shown indicating that payment and shipping information are required | high |
| TC-004 | WF-002 | Attempt to cancel the checkout |  | 1. Click Cancel | User is exited from checkout; no order is completed | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (interaction_edge) | WF-001 | Rapid re-submission after redirect | Order summary is displayed, Payment and shipping information are filled | 1. Click the Finish button to complete the order<br>2. Immediately press the browser back button | User is redirected to the confirmation page without a second order being created | medium |
| TC-006 (interaction_edge) | WF-002 | Cancel checkout and ensure exit | Order summary is displayed | 1. Click the Cancel button | User exits checkout and is returned to the previous page without any order being processed | medium |

---

## Checkout - Confirmation

Total: **3** (positive: 1, negative: 1, edge: 1)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Return to Product Inventory from Confirmation Page | User logged in as <Role> | 1. Click Back Home button | returns to Product Inventory and clears the cart | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to return to Product Inventory without a valid order |  | 1. Navigate to the Confirmation Page<br>2. Click on the 'Back Home' button | User remains on the Confirmation Page; no cart is cleared; confirmation message is still displayed. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | Rapid re-submission after redirect | User has completed the checkout process and is on the confirmation page. | 1. Click the 'Back Home' button. | User is redirected to the Product Inventory page; the cart is cleared and no duplicate order confirmation appears. | medium |

---

## Logout

Total: **4** (positive: 1, negative: 1, edge: 2)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | User successfully logs out | User logged in as <Role> | 1. Click Logout_Action button | ends the session and redirects to the login page | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to logout while not logged in | user must be logged out | 1. Ensure the user is not logged in<br>2. Click the Logout button | Logout action is not performed; user remains on the current page and is not redirected | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 (interaction_edge) | WF-001 | Attempt to logout when not logged in | User is not logged in | 1. Click the Logout button | Logout action is blocked; user remains on the current page with no session ended. | medium |
| TC-004 (interaction_edge) | WF-001 | Logout after rapid consecutive clicks | User is logged in | 1. Click the Logout button<br>2. Immediately click the Logout button again | First logout action succeeds; user is redirected to the login page, and the second click has no effect. | medium |

---

## Reset App State

Total: **2** (positive: 1, negative: 1, edge: 0)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Reset App State functionality | User logged in as <Role> | 1. Click Reset App State Button | clears the cart and resets in-app state | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-002 | WF-001 | Attempt to reset app state without any preconditions |  | 1. Click the Reset App State button | The app state does not reset; the cart remains unchanged | high |

---
