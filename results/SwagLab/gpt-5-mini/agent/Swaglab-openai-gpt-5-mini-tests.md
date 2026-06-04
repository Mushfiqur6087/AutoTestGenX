# Test Cases — Swaglab

Generated: 2026-06-04T14:12:17.957367Z  
Model: openai/gpt-5-mini  

## Summary

| Modules | Total | Positive | Negative | Edge | High | Medium | Low |
|---------|-------|----------|----------|------|------|--------|-----|
| 9 | 92 | 31 | 25 | 36 | 38 | 44 | 10 |

## Login

Total: **15** (positive: 6, negative: 5, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Successful login with accepted username and correct password | User on the Login page, User not authenticated | 1. Enter standard_user in the Username field<br>2. Enter secret_sauce in the Password field<br>3. Click the Login button | redirects to Product Inventory page | high |
| TC-002 | WF-002 | Locked out user submits credentials and sees locked-out error | User on the Login page, User not authenticated | 1. Enter locked_out_user in the Username field<br>2. Enter secret_sauce in the Password field<br>3. Click the Login button | Epic sadface: Sorry, this user has been locked out. | medium |
| TC-003 | WF-003 | Submit unrecognized username with a password shows credential mismatch error | User on the Login page, User not authenticated | 1. Enter <unrecognized_username> in the Username field<br>2. Enter <incorrect_password> in the Password field<br>3. Click the Login button | Epic sadface: Username and password do not match any user in this service. | medium |
| TC-004 | WF-004 | Submit with missing Username and provided Password shows username required error | User on the Login page, User not authenticated | 1. Enter secret_sauce in the Password field<br>2. Ensure the Username field is empty<br>3. Click the Login button | Epic sadface: Username is required. | medium |
| TC-005 | WF-005 | Submit with provided Username and missing Password shows password required error | User on the Login page, User not authenticated | 1. Enter standard_user in the Username field<br>2. Ensure the Password field is empty<br>3. Click the Login button | Epic sadface: Password is required. | medium |
| TC-006 | WF-006 | Submit with both Username and Password missing shows both required errors | User on the Login page, User not authenticated | 1. Ensure the Username field is empty<br>2. Ensure the Password field is empty<br>3. Click the Login button | Epic sadface: Username is required. Epic sadface: Password is required. | low |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 | WF-004 | Submit with Username blank (required text field) | User is on the Login page, User is not authenticated | 1. Ensure the Username field is empty (clear it if necessary)<br>2. Enter "secret_sauce" in the Password field<br>3. Click the Login button | Username field displays an inline validation error: "Epic sadface: Username is required."; the form does not submit and the user remains on the Login page (no redirect to Product Inventory). | high |
| TC-008 | WF-005 | Submit with Password blank (required password field) | User is on the Login page, User is not authenticated | 1. Enter <valid accepted username> in the Username field<br>2. Ensure the Password field is empty (clear it if necessary)<br>3. Click the Login button | Password field displays an inline validation error: "Epic sadface: Password is required."; the form does not submit and the user remains on the Login page (no redirect to Product Inventory). | high |
| TC-009 | WF-006 | Submit with both Username and Password blank | User is on the Login page, User is not authenticated | 1. Ensure the Username field is empty<br>2. Ensure the Password field is empty<br>3. Click the Login button | Username field displays an inline validation error: "Epic sadface: Username is required." AND Password field displays an inline validation error: "Epic sadface: Password is required."; the form does not submit and the user remains on the Login page (no redirect). | high |
| TC-010 | WF-003 | Submit with invalid credentials (username/password mismatch) | User is on the Login page, User is not authenticated | 1. Enter <unknown accepted username> in the Username field<br>2. Enter <incorrect password> in the Password field<br>3. Click the Login button | An error banner is shown with text: "Epic sadface: Username and password do not match any user in this service."; the form does not submit and the user remains on the Login page (no redirect to Product Inventory). | high |
| TC-011 | WF-002 | Locked out user attempts login | User is on the Login page, User is not authenticated | 1. Enter "locked_out_user" in the Username field<br>2. Enter "secret_sauce" in the Password field<br>3. Click the Login button | An error banner is shown with text: "Epic sadface: Sorry, this user has been locked out."; the form does not submit and the user remains on the Login page (no redirect to Product Inventory). | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-012 (input_edge) | WF-001 | Accepted username with leading and trailing whitespace | Login page is open | 1. Focus the Username field<br>2. Enter accepted username with a single leading space and a single trailing space in the Username field (e.g. leading/trailing whitespace around an accepted username)<br>3. Focus the Password field<br>4. Enter the accepted shared password in the Password field<br>5. Click the Login button | Form submits successfully; authentication succeeds and the user is redirected to the Product Inventory page (redirect succeeds) — visible: Product Inventory page is shown and no error banner is displayed (verifies whitespace is trimmed/ignored). | medium |
| TC-013 (input_edge) | WF-003 | Username case-variation (same characters, different case) with correct password | Login page is open | 1. Focus the Username field<br>2. Enter an accepted username but change letter casing (e.g. change one or more letters to upper/lower case)<br>3. Focus the Password field<br>4. Enter the accepted shared password in the Password field<br>5. Click the Login button | Login is blocked / error shown: the error banner displays "Epic sadface: Username and password do not match any user in this service." (verifies username matching is case-sensitive or that altered-case usernames are treated as invalid). | medium |
| TC-014 (input_edge) | WF-003 | Accepted username with appended emoji / special unicode character | Login page is open | 1. Focus the Username field<br>2. Enter an accepted username with a single appended emoji or other non-ASCII character<br>3. Focus the Password field<br>4. Enter the accepted shared password in the Password field<br>5. Click the Login button | Login is blocked / error shown: the error banner displays "Epic sadface: Username and password do not match any user in this service." (verifies extra characters/emoji break credential matching and are rejected at authentication). | medium |
| TC-015 (interaction_edge) | WF-001 | Rapid double-submit of Login with valid credentials | Login page is open | 1. Focus the Username field<br>2. Enter an accepted username in the Username field<br>3. Focus the Password field<br>4. Enter the accepted shared password in the Password field<br>5. Click the Login button<br>6. Immediately click the Login button again (second click within a short interval) | Form submits successfully on first submit and redirect to Product Inventory page succeeds; second rapid submit does not produce a second navigation or an error banner (Product Inventory page is shown and no duplicate navigation or additional error banner appears). | medium |

---

## Product Inventory

Total: **11** (positive: 4, negative: 3, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Open Product Detail from product name | User logged in as <User>, Product Inventory page is open with multiple products listed | 1. On the Product Inventory page, locate the row for <target product><br>2. Click the <target product>'s Name in the product list | opens Product Detail page | high |
| TC-002 | WF-002 | Add product to cart from product list (NotInCart state) | User logged in as <User>, <target product> is in NotInCart state on the Product Inventory page, Product Inventory page is open | 1. On the Product Inventory page, locate the row for <target product><br>2. Click the 'Add to cart' button in the <target product> row | adds item to cart; button changes to Remove; cart badge count increments | high |
| TC-003 | WF-003 | Remove product from cart from product list (InCart state) | User logged in as <User>, <target product> is in InCart state on the Product Inventory page, Product Inventory page is open | 1. On the Product Inventory page, locate the row for <target product><br>2. Click the 'Remove' button in the <target product> row | removes item from cart; button changes to Add to cart; cart badge count decrements | high |
| TC-004 |  | Sort products by Name (A–Z) using Sort_By dropdown | User logged in as <User>, Product Inventory page is open with multiple products listed | 1. On the Product Inventory page, open the Sort_By dropdown<br>2. Select 'Name (A–Z)' from the Sort_By dropdown | Product table rows are ordered by Name in ascending alphabetical order (A–Z); visible rows appear in alphabetical sequence by Name | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 |  | Unauthenticated user cannot access Product Inventory page | User is not authenticated (no valid session) | 1. Open the Product Inventory page URL in the browser as an unauthenticated user | Navigation is blocked: user is redirected to the Login page and the Product Inventory content is not displayed; Product list rows and sort controls are not visible (no product rows loaded). | high |
| TC-006 | WF-003 | Cannot perform 'Remove' when product is in NotInCart state | User is logged in, There exists <a product currently in state NotInCart> in the Product Inventory | 1. Log in as a valid user<br>2. Navigate to the Product Inventory page<br>3. Locate the row for <a product currently in state NotInCart><br>4. Inspect the available action buttons in that product's row<br>5. Attempt to click a 'Remove' button in that row if present | The 'Remove' action is not available for the product: the product row does not display a 'Remove' button and instead displays 'Add to cart'. If 'Remove' is not present it cannot be clicked; cart badge count remains unchanged; the product remains in NotInCart state (no removal occurs). | high |
| TC-007 | WF-002 | Cannot perform 'Add to cart' when product is already InCart | User is logged in, There exists <a product currently in state InCart> in the Product Inventory | 1. Log in as a valid user<br>2. Navigate to the Product Inventory page<br>3. Locate the row for <a product currently in state InCart><br>4. Inspect the available action buttons in that product's row<br>5. Attempt to click an 'Add to cart' button in that row if present | The 'Add to cart' action is not available for the product: the product row does not display an 'Add to cart' button and instead displays 'Remove'. If 'Add to cart' is not present it cannot be clicked; cart badge count remains unchanged; the product remains in InCart state (no duplicate add occurs). | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-008 (state_edge) | WF-002 | Double-click Add on a NotInCart product | User is logged in, Product P is displayed on the Product Inventory page and is in state NotInCart, Cart badge shows current count <N> | 1. Locate product P in the product list<br>2. Click the 'Add to cart' button for product P<br>3. Immediately click the 'Add to cart' button for product P again (second click before UI updates) | Only the first Add click succeeds; the second click is ignored. The cart badge increments by exactly 1 and displays the new count; the product's button text changes to 'Remove'. No duplicate increment occurs and no error message is shown. | medium |
| TC-009 (state_edge) | WF-003 | Double-click Remove on an InCart product | User is logged in, Product Q is displayed on the Product Inventory page and is in state InCart, Cart badge shows current count ≥ 1 | 1. Locate product Q in the product list<br>2. Click the 'Remove' button for product Q<br>3. Immediately click the 'Remove' button for product Q again (second click before UI updates) | Only the first Remove click succeeds; the second click is ignored. The cart badge decrements by exactly 1 and displays the new count; the product's button text changes to 'Add'. The cart badge does not go below zero and no error message is shown. | medium |
| TC-010 (interaction_edge) |  | Rapidly add multiple distinct products | User is logged in, Products A, B, and C are displayed and are all in state NotInCart, Cart badge shows current count <N> | 1. Click the 'Add to cart' button for product A<br>2. Click the 'Add to cart' button for product B immediately after step 1<br>3. Click the 'Add to cart' button for product C immediately after step 2 | Each Add action succeeds once for each distinct product. The cart badge increments by exactly 3 and displays the new count; each of products A, B, and C shows the button text 'Remove'. No missed or duplicate increments occur and no error messages are shown. | low |
| TC-011 (interaction_edge) | WF-002 | Click Add then immediately open Product Detail | User is logged in, Product R is displayed and is in state NotInCart, Cart badge shows current count <N> | 1. Click the 'Add to cart' button for product R<br>2. Immediately click the product R name (link) to open the Product Detail page before the list UI finishes any visual update | The Add action succeeds exactly once; the cart badge increments by 1 and displays the new count. The Product Detail page opens and shows the product as InCart (detail page button text 'Remove'). Navigation does not cause a duplicate add and no error messages are shown. | low |

---

## Product Detail

Total: **11** (positive: 4, negative: 2, edge: 5)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Add product to cart when product is not in cart | User logged in as <role>, The <product> exists and is in Not In Cart state | 1. Navigate to the Product Detail page for <product><br>2. Click the 'Add to cart' button | The Product Detail page shows the 'Remove' button and the product is visibly labelled 'In Cart' (product state changed on the page). | high |
| TC-002 | WF-002 | Remove product from cart when product is in cart | User logged in as <role>, The <product> exists and is in In Cart state | 1. Navigate to the Product Detail page for <product><br>2. Click the 'Remove' button | The Product Detail page shows the 'Add to cart' button and the product is visibly labelled 'Not In Cart' (product state changed on the page). | high |
| TC-003 | WF-003 | Navigate back to Product Inventory via Back to products link | User logged in as <role>, Product Detail page is open for <product> | 1. Click the 'Back to products' link | The Product Inventory page is displayed. | medium |
| TC-004 | WF-004 | Open Shopping Cart via cart icon from Product Detail | User logged in as <role>, Product Detail page is open for <product> | 1. Click the Cart icon | The Shopping Cart page is displayed. | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 | WF-001 | Attempt to Add to cart when product is already In Cart (Add action unavailable) | Product <product> is already In Cart, Tester is on the Product Detail page for <product> | 1. Open the Product Detail page for <product> whose state is In Cart<br>2. Look for an 'Add to cart' button on the page<br>3. If 'Add to cart' is visible, click the 'Add to cart' button | 'Add to cart' must not be available when the product is In Cart: the 'Add to cart' button is not visible or is disabled; the page shows the 'Remove' action instead. The product remains In Cart and no additional item is added to the cart (action is blocked). | high |
| TC-006 | WF-002 | Attempt to Remove when product is Not In Cart (Remove action unavailable) | Product <product> is Not In Cart, Tester is on the Product Detail page for <product> | 1. Open the Product Detail page for <product> whose state is Not In Cart<br>2. Look for a 'Remove' button on the page<br>3. If 'Remove' is visible, click the 'Remove' button | 'Remove' must not be available when the product is Not In Cart: the 'Remove' button is not visible or is disabled; the page shows the 'Add to cart' action instead. The product remains Not In Cart and no item is removed from the cart (action is blocked). | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 (state_edge) | WF-001 | Rapid double-click 'Add to cart' when Not In Cart | User is signed in (if required) and on the Product Detail page for a product whose current cart state is Not In Cart, Shopping Cart does not contain this product | 1. Verify the page shows the 'Add to cart' button<br>2. Click the 'Add to cart' button<br>3. Immediately click the 'Add to cart' button again (rapid second click) without waiting for navigation or UI refresh<br>4. Navigate to the Shopping Cart | First click succeeds: product is added to cart and Product Detail state changes to In Cart (UI now shows 'Remove'). The immediate second click is blocked / does not add a duplicate: Shopping Cart lists exactly one instance of the product and no duplicate entries are created. The Product Detail page shows 'Remove' and the 'Add to cart' button is not present. | medium |
| TC-008 (state_edge) | WF-002 | Rapid double-click 'Remove' when In Cart | User is on the Product Detail page for a product whose current cart state is In Cart, Shopping Cart contains exactly one instance of this product | 1. Verify the page shows the 'Remove' button<br>2. Click the 'Remove' button<br>3. Immediately click the 'Remove' button again (rapid second click) before UI updates<br>4. Refresh or navigate to the Shopping Cart | First click succeeds: product is removed from the cart and Product Detail state changes to Not In Cart (UI now shows 'Add to cart'). The immediate second click is blocked / has no effect: Shopping Cart lists zero instances of the product (no negative counts or errors), and the Product Detail page shows 'Add to cart' and not 'Remove'. | medium |
| TC-009 (interaction_edge) | WF-001 | Click 'Add to cart' then immediately use Cart icon to open Shopping Cart | User is on the Product Detail page for a product whose current cart state is Not In Cart, Shopping Cart does not contain this product | 1. Verify the page shows the 'Add to cart' button and the Cart icon is visible<br>2. Click the 'Add to cart' button<br>3. Immediately click the Cart icon (before waiting for any detailed UI text change on the Product Detail page)<br>4. Observe the Shopping Cart contents<br>5. Return to the Product Detail page for the same product | Navigation via the Cart icon succeeds: Shopping Cart page opens. The product appears exactly once in the Shopping Cart (no duplicate from rapid navigation). Returning to Product Detail shows the state as In Cart (the page shows 'Remove' and does not show 'Add to cart'). | medium |
| TC-010 (state_edge) | WF-002 | Attempt to activate 'Add to cart' when product is already In Cart (action visibility boundary) | User is on the Product Detail page for a product whose current cart state is In Cart, Shopping Cart contains this product | 1. Verify the page shows the 'Remove' button and that 'Add to cart' is not shown<br>2. Attempt to click any UI area where 'Add to cart' would normally appear (if clickable element is absent, attempt a click at the same screen coordinates)<br>3. Observe any UI changes | Attempt to use 'Add to cart' is blocked: the 'Add to cart' button is not present and no 'add' action occurs. The 'Remove' button remains visible; Shopping Cart still contains exactly one instance of the product (no additional entries). | medium |
| TC-011 (interaction_edge) | WF-003 | Navigate 'Back to products' immediately after clicking 'Add to cart' | User is on the Product Detail page for a product whose current cart state is Not In Cart, Shopping Cart does not contain this product | 1. Verify the page shows the 'Add to cart' button and the 'Back to products' link is visible<br>2. Click the 'Add to cart' button<br>3. Immediately click the 'Back to products' link (before waiting for UI confirmation on Product Detail)<br>4. From Product Inventory, navigate back to the same Product Detail page | Navigation to Product Inventory succeeds. Upon returning to Product Detail, the product's state reflects that it was added: the page shows 'Remove' (In Cart) and does not show 'Add to cart'. Shopping Cart contains exactly one instance of the product. | medium |

---

## Shopping Cart

Total: **8** (positive: 3, negative: 2, edge: 3)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Remove an item from the cart | User logged in as <Shopper>, Shopping Cart page is open with at least one item in the cart | 1. On the Shopping Cart page, locate the row for <target item> in the Shopping Cart table<br>2. Click the Remove button on the <target item> row | The Shopping Cart table no longer displays the removed item's row; the item's row is absent from the list (removes item from cart). | high |
| TC-002 | WF-002 | Continue Shopping navigates to Product Inventory | User logged in as <Shopper>, Shopping Cart page is open | 1. Click the Continue Shopping link in the cart action bar | The Product Inventory page is displayed (navigates to Product Inventory). | medium |
| TC-003 | WF-003 | Begin Checkout from the cart | User logged in as <Shopper>, Shopping Cart page is open with at least one item in the cart | 1. Click the Checkout button in the cart action bar | The Checkout page is displayed and the checkout flow begins (begins checkout). | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-004 |  | Unauthenticated user cannot access Shopping Cart page | User is not authenticated (not logged in) | 1. As an unauthenticated user, navigate to <Shopping Cart page URL> | Access is blocked: the application redirects to the Login page; the Shopping Cart data table and item rows are not displayed; a login form or sign-in prompt is visible, and no cart actions (Remove, Continue Shopping, Checkout) are available. | high |
| TC-005 | WF-003 | Unauthenticated user cannot begin checkout (Checkout button blocked) | User is not authenticated (not logged in) | 1. As an unauthenticated user, navigate to <Shopping Cart page URL><br>2. Click the 'Checkout' button | Checkout is blocked: user is redirected to the Login page and the checkout flow does not begin; Shopping Cart remains visible only after successful login and no items are removed or modified as a result of this action. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (input_edge) |  | Very long product description in cart table (200+ chars) | A product has been added to the cart whose description is a string of 200+ characters | 1. Navigate to the Shopping Cart page<br>2. Locate the cart row for the product with the long description<br>3. Observe the description cell in the Shopping_Cart_Table | The Shopping_Cart_Table displays the product description without breaking the table layout; the description cell shows truncated overflow with a visible ellipsis (succeeds) and the table row height does not cause layout collapse or overlap. | low |
| TC-007 (input_edge) |  | Unicode and emoji characters in product description | A product has been added to the cart whose description contains Unicode characters and emoji | 1. Navigate to the Shopping Cart page<br>2. Locate the cart row for the product with Unicode/emoji in the description<br>3. Observe the description cell in the Shopping_Cart_Table | The Shopping_Cart_Table renders the Unicode characters and emoji as visible glyphs in the description cell (succeeds); no replacement characters or rendering errors are shown and the row remains readable. | low |
| TC-008 (input_edge) |  | Leading/trailing whitespace in product description is trimmed in display | A product has been added to the cart whose description includes leading and trailing whitespace characters | 1. Navigate to the Shopping Cart page<br>2. Locate the cart row for the product with leading/trailing whitespace in the description<br>3. Observe the value shown in the description cell in the Shopping_Cart_Table | The description displayed in the Shopping_Cart_Table is trimmed of leading and trailing whitespace (succeeds); the visible text in the cell contains no leading or trailing spaces and matches the trimmed value. | low |

---

## Checkout - Information

Total: **14** (positive: 6, negative: 4, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Continue with all required fields filled proceeds to overview | User logged in as <role>, Checkout - Information page is open | 1. Enter <valid first name> in the First Name field<br>2. Enter <valid last name> in the Last Name field<br>3. Enter <valid postal code> in the Zip/Postal Code field<br>4. Click Continue | Overview step is displayed | high |
| TC-002 | WF-002 | Continue with multiple required fields missing shows corresponding error banners | User logged in as <role>, Checkout - Information page is open | 1. Enter <valid first name> in the First Name field<br>2. Leave the Last Name field empty<br>3. Leave the Zip/Postal Code field empty<br>4. Click Continue | Error banners are displayed: 'Error: Last Name is required' and 'Error: Postal Code is required' | medium |
| TC-003 | WF-004 | Continue with First Name missing shows First Name required error | User logged in as <role>, Checkout - Information page is open | 1. Leave the First Name field empty<br>2. Enter <valid last name> in the Last Name field<br>3. Enter <valid postal code> in the Zip/Postal Code field<br>4. Click Continue | Error banner is displayed: 'Error: First Name is required' | medium |
| TC-004 | WF-005 | Continue with Last Name missing shows Last Name required error | User logged in as <role>, Checkout - Information page is open | 1. Enter <valid first name> in the First Name field<br>2. Leave the Last Name field empty<br>3. Enter <valid postal code> in the Zip/Postal Code field<br>4. Click Continue | Error banner is displayed: 'Error: Last Name is required' | medium |
| TC-005 | WF-006 | Continue with Zip/Postal Code missing shows Postal Code required error | User logged in as <role>, Checkout - Information page is open | 1. Enter <valid first name> in the First Name field<br>2. Enter <valid last name> in the Last Name field<br>3. Leave the Zip/Postal Code field empty<br>4. Click Continue | Error banner is displayed: 'Error: Postal Code is required' | medium |
| TC-006 | WF-003 | Click Cancel returns user to Shopping Cart | User logged in as <role>, Checkout - Information page is open | 1. Click Cancel | Shopping Cart page is displayed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-007 | WF-004 | Continue with First Name blank (other required fields filled) | User is on the Checkout - Information page | 1. Ensure the First Name field is blank<br>2. Enter <valid last name> in the Last Name field<br>3. Enter <valid postal code> in the Zip/Postal Code field<br>4. Click the Continue button | The form does not proceed to the overview step; a visible error banner is shown stating "Error: First Name is required" and the page remains on Checkout - Information | high |
| TC-008 | WF-005 | Continue with Last Name blank (other required fields filled) | User is on the Checkout - Information page | 1. Enter <valid first name> in the First Name field<br>2. Ensure the Last Name field is blank<br>3. Enter <valid postal code> in the Zip/Postal Code field<br>4. Click the Continue button | The form does not proceed to the overview step; a visible error banner is shown stating "Error: Last Name is required" and the page remains on Checkout - Information | high |
| TC-009 | WF-006 | Continue with Zip/Postal Code blank (other required fields filled) | User is on the Checkout - Information page | 1. Enter <valid first name> in the First Name field<br>2. Enter <valid last name> in the Last Name field<br>3. Ensure the Zip/Postal Code field is blank<br>4. Click the Continue button | The form does not proceed to the overview step; a visible error banner is shown stating "Error: Postal Code is required" and the page remains on Checkout - Information | high |
| TC-010 | WF-002 | Continue with all required fields empty | User is on the Checkout - Information page | 1. Ensure the First Name field is blank<br>2. Ensure the Last Name field is blank<br>3. Ensure the Zip/Postal Code field is blank<br>4. Click the Continue button | The form does not proceed to the overview step; visible error banners are shown stating "Error: First Name is required", "Error: Last Name is required", and "Error: Postal Code is required"; the page remains on Checkout - Information | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-011 (boundary) | WF-004 | Whitespace-only in First_Name is treated as empty (should be blocked) | User is on the Checkout - Information form | 1. Focus First_Name field<br>2. Enter a whitespace-only value into First_Name (only spaces or tabs)<br>3. Focus Last_Name field<br>4. Enter a non-empty value into Last_Name<br>5. Focus Zip_Postal_Code field<br>6. Enter a non-empty value into Zip_Postal_Code<br>7. Click Continue | Submission is blocked; an error banner with the exact text 'Error: First Name is required' is displayed and the user remains on the Checkout - Information form | medium |
| TC-012 (input_edge) | WF-001 | Leading and trailing whitespace in Last_Name is trimmed on save | User is on the Checkout - Information form | 1. Focus First_Name field<br>2. Enter a non-empty value into First_Name<br>3. Focus Last_Name field<br>4. Enter a value with leading and trailing whitespace into Last_Name<br>5. Focus Zip_Postal_Code field<br>6. Enter a non-empty value into Zip_Postal_Code<br>7. Click Continue | Form submits successfully and proceeds to the overview step; the overview page displays the Last Name without leading or trailing whitespace (saved value shown has no extra spaces) | medium |
| TC-013 (input_edge) | WF-001 | Very long text in name fields (200+ chars) — acceptance or visible truncation behavior | User is on the Checkout - Information form | 1. Focus First_Name field<br>2. Enter a very long string (200+ characters) into First_Name<br>3. Focus Last_Name field<br>4. Enter a very long string (200+ characters) into Last_Name<br>5. Focus Zip_Postal_Code field<br>6. Enter a non-empty value into Zip_Postal_Code<br>7. Click Continue | Either: the form submits successfully and the overview displays the full long strings; OR: submission is blocked or the field is visibly truncated and an inline indicator/error is shown. The UI must clearly indicate which behavior occurred (saved/visible value or truncation/error). | medium |
| TC-014 (input_edge) | WF-001 | Special characters and emoji in name and postal fields are preserved | User is on the Checkout - Information form | 1. Focus First_Name field<br>2. Enter special characters and emoji into First_Name<br>3. Focus Last_Name field<br>4. Enter special characters and emoji into Last_Name<br>5. Focus Zip_Postal_Code field<br>6. Enter special characters and emoji into Zip_Postal_Code<br>7. Click Continue | Form submits successfully and proceeds to the overview step; the overview page displays the entered special characters and emoji unchanged (no replacement characters or error banners) | low |

---

## Checkout - Overview

Total: **8** (positive: 2, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Finish checkout navigates to confirmation page | User logged in as <role>, Checkout Overview page is open with <items in cart>, <valid payment method>, and <shipping address> displayed | 1. Review the Order Summary to confirm <items in cart> are listed<br>2. Verify the totals section shows Item total, Tax, and Total<br>3. Verify payment information displays <valid payment method><br>4. Verify shipping information displays <shipping address><br>5. Click the 'Finish' button | completes order and navigates to confirmation page | high |
| TC-002 | WF-002 | Cancel exits checkout from overview | User logged in as <role>, Checkout Overview page is open with <items in cart>, <valid payment method>, and <shipping address> displayed | 1. Optionally review Order Summary, totals, payment and shipping information<br>2. Click the 'Cancel' button | exits checkout | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Unauthenticated user attempts to Finish checkout | User is not authenticated (logged out) | 1. Navigate to the Checkout Overview page URL<br>2. Observe the page content<br>3. Click the 'Finish' button | User is redirected to the Login page (URL shows /login) and the Checkout Overview content is not accessible; the order is not completed and the confirmation page is not shown (no navigation to confirmation). 'Finish' does not complete the order while unauthenticated. | high |
| TC-004 | WF-002 | Unauthenticated user attempts to Cancel checkout | User is not authenticated (logged out) | 1. Navigate to the Checkout Overview page URL<br>2. Observe the page content<br>3. Click the 'Cancel' button | User is redirected to the Login page (URL shows /login) and the Checkout Overview content is not accessible; the checkout is not exited while unauthenticated (no exit/cleanup occurs). 'Cancel' does not perform the exit action for unauthenticated users. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (interaction_edge) | WF-001 | Rapid double-click of Finish should not create duplicate orders | User is signed in (if required) and has items in cart, User has reached the Overview step and order summary, totals, payment and shipping information are visible | 1. Ensure the Overview step is visible<br>2. Click the 'Finish' button<br>3. Immediately click the 'Finish' button again (within one second)<br>4. Observe the UI until navigation to the confirmation page completes | First submission succeeds; the second click is blocked / error shown: the 'Finish' button is disabled after the first click (or a visible 'processing' indicator appears) and no duplicate order is created — only one confirmation page/order is shown | medium |
| TC-006 (interaction_edge) | WF-001 | Browser Back after successful Finish should not allow duplicate order creation | User is signed in (if required) and has items in cart, User reaches the Overview step and clicks Finish to complete the order | 1. Click the 'Finish' button on the Overview step<br>2. Wait until the confirmation page is displayed<br>3. Use the browser Back button once<br>4. If the Overview page is shown, attempt to click 'Finish' again | Initial submission succeeds; any attempt to re-submit after navigating back is blocked / error shown: no second order is created — either the 'Finish' button is disabled, a prevention message is shown, or the UI prevents submission; only one confirmation/order exists and the confirmation page reflects the single order | medium |
| TC-007 (input_edge) |  | Very long shipping address entered prior to Overview is accepted and how it displays in Overview | User has proceeded through the Shipping step to enter shipping details, Shipping address input is available (prior step) and contains no explicit max-length constraint in the Overview module | 1. In the Shipping step address field, enter a very long string (>= 200 characters)<br>2. Save the Shipping step<br>3. Navigate to the Overview step so the order summary displays the saved shipping address<br>4. Click 'Finish' to complete the order | Saving the long shipping address succeeds; on the Overview page the shipping address is displayed without causing UI overflow — the overview either shows the full address or displays a visibly truncated version (e.g., with ellipsis) but the order completes successfully; a single order is created and confirmation is shown | low |
| TC-008 (input_edge) |  | Special characters and emoji in payer/cardholder name shown in Overview | Payment information (cardholder/payer name) is entered in an earlier payment step and displayed on Overview, No explicit character whitelist/blacklist is specified in the Overview module | 1. In the Payment step cardholder name field, enter a string containing special characters and emoji<br>2. Save the Payment step<br>3. Navigate to the Overview step and confirm the payment information is visible<br>4. Click 'Finish' to complete the order | Saving the payment information with special characters/emoji succeeds; the Overview displays the characters as entered (or clearly indicates any sanitized/truncated form); order completion succeeds and confirmation shows the single created order | low |

---

## Checkout - Confirmation

Total: **8** (positive: 2, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 |  | Confirmation page displays the success message | User logged in as <Customer>, Confirmation page is available after completing checkout | 1. Navigate to the Confirmation page<br>2. Observe the page content | The Confirmation page displays the message "Thank you for your order!" | medium |
| TC-002 | WF-001 | Back Home button returns to Product Inventory and results in an empty cart | User logged in as <Customer>, Confirmation page is open after a successful order placement | 1. Click the 'Back Home' button on the Confirmation page<br>2. Wait for navigation to complete and observe the landing page | 'navigates to Product Inventory and clears the cart' — Product Inventory page is displayed and the cart indicator shows no items; the cart contents list is empty | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Unauthenticated user cannot access Confirmation page | User is not authenticated (no valid session) | 1. Navigate directly to the Confirmation page URL | Access is blocked: the Login page is shown instead of the Confirmation page (Confirmation text such as 'Thank you for your order!' is not displayed); user is not able to use the Back Home button; cart contents remain unchanged. | high |
| TC-004 | WF-001 | Back Home button not accessible to a user role without Product Inventory permission | User is authenticated as a role that does NOT have permission to view Product Inventory, User has completed an order and is on the Confirmation page | 1. Open the Confirmation page while logged in as the restricted-role user<br>2. Attempt to locate and click the Back Home button | The Back Home control is not available or is disabled for this user: Back Home button is either not visible or appears disabled; attempting to click does nothing (no navigation occurs); user remains on the Confirmation page; cart state is unchanged. | medium |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (interaction_edge) | WF-001 | Rapid double-click of Back Home button | User has completed checkout and is on the Confirmation page showing the success message | 1. Rapidly click the 'Back Home' button twice in immediate succession | First click succeeds: the app navigates to the Product Inventory page and the cart is cleared (UI shows empty cart). The immediate second click is ignored / blocked: no additional navigation occurs and no duplicate action or error is shown. | medium |
| TC-006 (interaction_edge) | WF-001 | Use browser Back to return to Confirmation then click Back Home again | User has completed checkout and is on the Confirmation page showing the success message | 1. Click the 'Back Home' button<br>2. Verify Product Inventory page is displayed and the cart appears cleared<br>3. Use the browser Back button to return to the Confirmation page<br>4. On the returned-to Confirmation page, click the 'Back Home' button again | First click succeeds: navigates to Product Inventory and clears the cart (cart UI shows empty). After using browser Back, clicking 'Back Home' again succeeds: the app navigates to Product Inventory and cart remains cleared (no items reappear). No duplicate orders or errors are created or shown. | medium |
| TC-007 (interaction_edge) | WF-001 | Refresh (page reload) on Confirmation page then click Back Home | User has completed checkout and is on the Confirmation page showing the success message | 1. Reload/refresh the Confirmation page (browser refresh)<br>2. Verify the confirmation message is still visible (or a cached confirmation page is shown)<br>3. Click the 'Back Home' button | Clicking 'Back Home' after a page refresh succeeds: the app navigates to Product Inventory and the cart is cleared (cart UI shows empty). No error is shown and no duplicate navigation/order occurs. | medium |
| TC-008 (interaction_edge) | WF-001 | Duplicate tab scenario: Back Home in one tab then in duplicated tab | User has completed checkout and is on the Confirmation page showing the success message | 1. Duplicate the browser tab while on the Confirmation page<br>2. In the original tab, click the 'Back Home' button<br>3. Switch to the duplicated tab (which still shows the Confirmation page)<br>4. Click the 'Back Home' button in the duplicated tab | First tab's 'Back Home' click succeeds: navigates to Product Inventory and clears the cart (cart UI shows empty). The duplicated tab's 'Back Home' click also succeeds in navigating to Product Inventory, but the cart remains cleared (no items reappear). No errors are shown and no duplicate orders are created. | medium |

---

## Logout

Total: **9** (positive: 2, negative: 3, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Click Logout redirects user to Login Page | User logged in as <role> | 1. Ensure the page with the Logout button is open<br>2. Click the Logout button | The application redirects to the Login Page and the Login Page is displayed | high |
| TC-002 |  | After logout, accessing a protected page redirects to Login Page | User logged in as <role> | 1. Click the Logout button<br>2. Attempt to open a protected page by navigating to <protected page: inventory | detail | cart | checkout> | Attempting to access the protected page redirects to the Login Page and the Login Page is displayed | high |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Unauthenticated user should not see Logout button | User is not logged in | 1. Open the <Home_Page><br>2. Look for a control labeled 'Logout' on the page | The 'Logout' button is not visible on the <Home_Page>; there is no visible control to trigger logout and the user remains unauthenticated (no logout action can be performed). | high |
| TC-004 | WF-001 | Direct access to logout endpoint when not authenticated is blocked | User is not logged in | 1. In the browser address bar navigate directly to the <Logout_Endpoint> (the URL used to perform Logout) | Navigation to <Logout_Endpoint> does not perform a logout session-change (there is no active session to end) and the browser is redirected to the Login Page; protected content is not displayed and the user remains unauthenticated. | high |
| TC-005 | WF-001 | After logout, protected pages are inaccessible without logging in | User was logged in and has just clicked 'Logout' (session ended and user is on the Login Page) | 1. From the Login Page, navigate to the <inventory> protected page<br>2. Observe the page content or redirection | Navigation to the <inventory> page redirects to the Login Page; the <inventory> protected content is not displayed and the user is required to authenticate before accessing it. | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-006 (interaction_edge) | WF-001 | Rapid double-click Logout | User is logged in, User is on a protected page (e.g., inventory) | 1. Click the Logout button<br>2. Immediately click the Logout button again before the redirect to Login_Page completes | First logout succeeds: user is redirected to Login_Page and session is ended. The second click is ignored and does not produce an error or create an additional session. Protected pages require authentication when attempted after logout. | medium |
| TC-007 (interaction_edge) | WF-001 | Browser Back after logout (cached page vs navigation) | User is logged in, User is on a protected page with visible sensitive content | 1. Click the Logout button<br>2. Wait until the app redirects to the Login_Page<br>3. Use the browser Back button once | Back navigation to the protected page is blocked: Login_Page is shown (or the app immediately redirects to Login_Page) and no protected content is visible. Access to protected pages after logout is blocked / authentication required is shown. | medium |
| TC-008 (state_edge) | WF-001 | Direct navigation / bookmark to protected page after logout | User is logged in, User has a bookmark or known navigation entry for a protected page (inventory, detail, cart, or checkout) | 1. Click the Logout button<br>2. From the browser address bar or a bookmark, navigate directly to a protected page (e.g., inventory) | Navigation to the protected page is blocked: the app shows Login_Page or an authentication-required message and protected content is not displayed. Access is blocked / error shown indicating authentication is required. | medium |
| TC-009 (interaction_edge) | WF-001 | Browser Back then Reload after logout (cached view vs reload) | User is logged in, User is on a protected page (e.g., detail) that may be cached by the browser | 1. Click the Logout button<br>2. Wait until redirected to Login_Page<br>3. Click the browser Back button to display the cached protected page (if shown by the browser)<br>4. While the cached protected page is visible, click the browser Reload button | Cached view (Back) may briefly show content but on Reload access to protected content is blocked: reload triggers authentication and the Login_Page is shown. Protected content is not available after reload; access is blocked / error shown if authentication is required. | medium |

---

## Reset App State

Total: **8** (positive: 2, negative: 2, edge: 4)

### Positive Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-001 | WF-001 | Reset clears a populated cart and resets in-app button states | User logged in as <role>, Cart contains <items>, At least one product is <in-cart> | 1. Open the page containing the Reset App State button<br>2. Click the Reset App State button | clears cart and resets in-app state (updates cart badge and resets add/remove button states); user remains logged in | high |
| TC-002 | WF-001 | Reset when cart is already empty keeps UI cleared and user logged in | User logged in as <role>, Cart is empty, All product tiles are <not in-cart> | 1. Open the page containing the Reset App State button<br>2. Click the Reset App State button | clears cart and resets in-app state (updates cart badge and resets add/remove button states); user remains logged in | medium |

### Negative Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-003 | WF-001 | Unauthenticated user cannot perform Reset App State | User is not authenticated (not logged in) | 1. Open the application page that contains the Reset App State button<br>2. Click the Reset App State button | Action is blocked: the user is redirected to the Login page (or shown an authentication prompt); Reset App State is not performed — the cart contents remain unchanged and the cart badge and add/remove button states remain as before; no 'reset' confirmation is shown | high |
| TC-004 | WF-001 | Expired session/token prevents Reset App State from running | User session has expired / authentication token is invalid | 1. With an expired session, open the application page that contains the Reset App State button<br>2. Click the Reset App State button | Action is blocked: the user is redirected to the Login page or shown a re-authentication prompt; Reset App State is not performed — the cart contents, cart badge and add/remove button states remain unchanged; no in-app reset effects are applied | high |

### Edge & Boundary Tests

| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|--------|-----------|---------------|-------|-----------------|----------|
| TC-005 (state_edge) | WF-001 | Reset when cart contains multiple items and product buttons in 'Remove' state | User is logged in, User is on a page showing product tiles and the cart badge shows one or more items, One or more product tiles display the in-cart state (e.g., 'Remove' or equivalent) | 1. Click the Reset App State button | Action succeeds: the cart is cleared (cart badge count is cleared/hidden), product add/remove buttons on the page have returned to their default 'Add' state, and the user remains logged in (account/avatar remains visible). | medium |
| TC-006 (interaction_edge) | WF-001 | Reset when cart is already empty (idempotence) | User is logged in, User is on a page where the cart is already empty (cart badge absent or zero), Product tiles are in their default 'Add' state | 1. Click the Reset App State button | Action succeeds (idempotent): no error is shown; the cart remains empty (cart badge stays absent/zero), product add/remove buttons remain in the default 'Add' state, and the user remains logged in (account/avatar remains visible). | medium |
| TC-007 (state_edge) | WF-001 | Rapid consecutive clicks on Reset App State (double-click) | User is logged in, User is on a page showing product tiles and the cart badge shows one or more items | 1. Click the Reset App State button<br>2. Immediately click the Reset App State button again (within typical double-click speed) | Action sequence succeeds: a single reset outcome is applied (cart cleared, cart badge cleared/hidden, product buttons reset to default 'Add' state), no error or duplicate adverse effect is shown, and the user remains logged in (account/avatar remains visible). | medium |
| TC-008 (interaction_edge) | WF-001 | Use browser Back after successful Reset to ensure state is not restored | User is logged in, User has a non-empty cart before reset, User is on a page where Reset App State is available | 1. Click the Reset App State button<br>2. After the reset completes, click the browser Back button | Action succeeds and is persistent: the reset remains effective after navigating back (cart stays cleared and cart badge remains cleared/hidden), product add/remove buttons remain in default 'Add' state, and the user remains logged in (account/avatar remains visible). No additional cart items are restored by navigation. | low |

---
