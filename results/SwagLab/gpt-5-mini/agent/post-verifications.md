# Post-Verification Specifications

### [TC-002] Reset when cart is already empty keeps UI cleared and user logged in
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the page containing the Reset App State button
2. 2. Click the Reset App State button

**Original Expected Result:** clears cart and resets in-app state (updates cart badge and resets add/remove button states); user remains logged in

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Product Inventory page`
- **Observe**:
  - the <target product> row shows an 'Add to cart' button (button label = 'Add to cart')
  - cart badge count (e.g., 0 or current integer value) before adding
  - optional: Shopping Cart does NOT contain <target product> (if accessible)

**Post-Check**
- **Navigate To**: `Product Inventory page, then Shopping Cart page`
- **Observe**:
  - the <target product> row button label now shows 'Remove' on the Product Inventory page
  - cart badge count on header (integer) after adding
  - <target product> appears in the Shopping Cart with quantity = 1
  - <target product> name and price in the Shopping Cart match the Product Inventory values

**Expected Change**: Cart badge count increased by 1 compared to pre_check; the <target product> appears in the Shopping Cart with quantity 1 and matching name/price; the Product Inventory row for <target product> shows the button label changed from 'Add to cart' to 'Remove'.

---

### [TC-003] Unauthenticated user cannot perform Reset App State
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the application page that contains the Reset App State button
2. 2. Click the Reset App State button

**Original Expected Result:** Action is blocked: the user is redirected to the Login page (or shown an authentication prompt); Reset App State is not performed — the cart contents remain unchanged and the cart badge and add/remove button states remain as before; no 'reset' confirmation is shown

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Product Inventory page`
- **Observe**:
  - <target product> row button text (expected 'Remove')
  - cart badge count (numeric, includes the item)

**Post-Check**
- **Navigate To**: `Product Inventory page and then Shopping Cart page`
- **Observe**:
  - <target product> row button text (expected 'Add to cart')
  - cart badge count (numeric, decremented by 1 from pre_check)
  - Shopping Cart contents (should NOT include <target product>)

**Expected Change**: The <target product> row button changes from 'Remove' to 'Add to cart'; the cart badge count decreases by 1 compared to pre_check; the <target product> is no longer listed in the Shopping Cart.

---

### [TC-001] Reset clears a populated cart and resets in-app button states
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the page containing the Reset App State button
2. 2. Click the Reset App State button

**Original Expected Result:** clears cart and resets in-app state (updates cart badge and resets add/remove button states); user remains logged in

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Product Detail page for <product>`
- **Observe**:
  - product action button label (expected: 'Add to cart')
  - cart icon badge count
  - Shopping Cart contents do NOT include <product> (or product not listed)

**Post-Check**
- **Navigate To**: `Product Detail page for <product> and Shopping Cart page`
- **Observe**:
  - product action button label (expected: 'Remove')
  - visible 'In Cart' indicator/label for <product> on Product Detail
  - cart icon badge count
  - Shopping Cart contains <product> with quantity 1

**Expected Change**: On the Product Detail page the 'Add to cart' button has changed to 'Remove' and the product shows an 'In Cart' indicator; the cart icon badge count has increased by 1 compared to pre_check; the Shopping Cart page lists the product with quantity 1.

---

### [TC-002] Reset when cart is already empty keeps UI cleared and user logged in
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the page containing the Reset App State button
2. 2. Click the Reset App State button

**Original Expected Result:** clears cart and resets in-app state (updates cart badge and resets add/remove button states); user remains logged in

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Product Detail for <product> (and optionally Shopping Cart)`
- **Observe**:
  - Product Detail shows a 'Remove' button for <product>
  - Shopping Cart (via cart icon) lists <product> with quantity 1
  - Cart badge count reflects the product is in cart (>= 1)

**Post-Check**
- **Navigate To**: `Product Detail for <product> and Shopping Cart (via cart icon)`
- **Observe**:
  - Product Detail shows an 'Add to cart' button for <product>
  - Shopping Cart does NOT list <product>
  - Cart badge count is decreased by 1 (or is 0 if this was the only item)

**Expected Change**: After clicking 'Remove' on the Product Detail page, the Product Detail button changes from 'Remove' to 'Add to cart'; the product is removed from the Shopping Cart list; and the cart badge count decreases accordingly (by one or to zero if it was the only item).

---

### [TC-001] Reset clears a populated cart and resets in-app button states
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the page containing the Reset App State button
2. 2. Click the Reset App State button

**Original Expected Result:** clears cart and resets in-app state (updates cart badge and resets add/remove button states); user remains logged in

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Shopping Cart page`
- **Observe**:
  - row for <target item> exists in the Shopping Cart table
  - shopping cart badge count (record current value)

**Post-Check**
- **Navigate To**: `Shopping Cart page (then optionally Product Inventory or Product Detail for cross-check)`
- **Observe**:
  - row for <target item> is not present in the Shopping Cart table
  - shopping cart badge count (has decreased by 1 compared to pre-check)
  - optional: on Product Inventory or the Product Detail page for <target item>, the item's action button shows 'Add to cart' (indicating it is not in the cart)

**Expected Change**: The Shopping Cart no longer contains the <target item> row and the shopping cart badge count has decreased by one; optionally, the product's action button on Inventory/Product Detail shows 'Add to cart', confirming the item is removed from the cart.

---

### [TC-001] Reset clears a populated cart and resets in-app button states
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the page containing the Reset App State button
2. 2. Click the Reset App State button

**Original Expected Result:** clears cart and resets in-app state (updates cart badge and resets add/remove button states); user remains logged in

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Checkout - Overview`
- **Observe**:
  - order summary lists the items in cart (product names and quantities)
  - totals section shows Item total, Tax, and Total amounts
  - payment information displays the provided valid payment method
  - shipping information displays the provided shipping address

**Post-Check**
- **Navigate To**: `Checkout - Confirmation`
- **Observe**:
  - confirmation success message (e.g., 'Thank you for your order!')
  - 'Back Home' button is present

**Expected Change**: After clicking 'Finish', the app navigates to the Confirmation page showing the success message. When the user clicks 'Back Home' and returns to Product Inventory, the shopping cart badge is 0 and previously ordered items are no longer in the cart (their product buttons display 'Add to cart').

---

### [TC-002] Reset when cart is already empty keeps UI cleared and user logged in
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the page containing the Reset App State button
2. 2. Click the Reset App State button

**Original Expected Result:** clears cart and resets in-app state (updates cart badge and resets add/remove button states); user remains logged in

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Checkout - Confirmation page (order success)`
- **Observe**:
  - confirmation message present (e.g., 'Thank you for your order!')
  - Back Home button is visible
  - cart item-count badge (capture current numeric value shown on header)

**Post-Check**
- **Navigate To**: `Product Inventory page (landing after clicking 'Back Home')`
- **Observe**:
  - Product Inventory page title/list is visible
  - cart item-count badge shows 0 or badge is not displayed
  - Navigate to Shopping Cart page and observe that the cart items list is empty or a 'Your cart is empty' message is shown

**Expected Change**: After clicking 'Back Home' the app navigates to the Product Inventory page and the cart is cleared: the cart item-count badge is 0 (or absent) and the Shopping Cart contains no items, whereas the pre-check captured a non-zero cart count.

---

### [TC-001] Reset clears a populated cart and resets in-app button states
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the page containing the Reset App State button
2. 2. Click the Reset App State button

**Original Expected Result:** clears cart and resets in-app state (updates cart badge and resets add/remove button states); user remains logged in

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Product Inventory -> Open hamburger menu (verify Reset App State option) -> Inspect Shopping Cart`
- **Observe**:
  - presence of 'Reset App State' option in hamburger menu
  - cart badge count (non-zero, matches number of items preconditioned)
  - Shopping Cart contents list contains the expected items
  - on-product button state for at least one previously added product shows 'Remove' (indicating in-cart)

**Post-Check**
- **Navigate To**: `Product Inventory -> Open hamburger menu (click Reset App State) -> Inspect Shopping Cart and relevant product(s)`
- **Observe**:
  - cart badge count
  - Shopping Cart contents list
  - on-product button state for the previously in-cart product(s)
  - access to protected pages (e.g., Product Inventory) to confirm user is still logged in

**Expected Change**: Cart badge count is cleared or shows 0 (no items); Shopping Cart contents list is empty; on-product buttons for previously in-cart products reset to 'Add to cart'; user remains logged in and protected pages remain accessible.

---

### [TC-002] Reset when cart is already empty keeps UI cleared and user logged in
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Open the page containing the Reset App State button
2. 2. Click the Reset App State button

**Original Expected Result:** clears cart and resets in-app state (updates cart badge and resets add/remove button states); user remains logged in

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Product Inventory (then open Shopping Cart)`
- **Observe**:
  - presence of persistent header (hamburger menu, "Swag Labs" title, cart icon)
  - cart badge count (expected 0)
  - product tile button state for multiple products (each shows "Add to cart" / not in-cart)
  - Shopping Cart page contents (shows no items / empty cart message)

**Post-Check**
- **Navigate To**: `Product Inventory (then open Shopping Cart)`
- **Observe**:
  - presence of persistent header (hamburger menu, "Swag Labs" title, cart icon)
  - cart badge count (should be 0)
  - product tile button state for multiple products (each shows "Add to cart" / not in-cart)
  - Shopping Cart page contents (shows no items / empty cart message)

**Expected Change**: No negative change: cart remains empty with cart badge 0; all product tiles remain in the not-in-cart state showing "Add to cart"; Shopping Cart shows no items/empty message; user remains logged in (protected pages such as Inventory and Cart remain accessible and user is not redirected to login).

---
