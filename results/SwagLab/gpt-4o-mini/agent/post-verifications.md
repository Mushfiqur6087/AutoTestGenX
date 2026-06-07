# Post-Verification Specifications

### [TC-002] Attempt to reset app state without any preconditions
**Category**: `negative` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Reset App State button

**Original Expected Result:** The app state does not reset; the cart remains unchanged

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Product Inventory`
- **Observe**:
  - cart badge count

**Post-Check**
- **Navigate To**: `Product Inventory`
- **Observe**:
  - cart badge count

**Expected Change**: Cart badge count increased by one, indicating the product was successfully added to the cart.

---

### [TC-003] Attempt to logout when not logged in
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button

**Original Expected Result:** Logout action is blocked; user remains on the current page with no session ended.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Shopping Cart`
- **Observe**:
  - item description
  - quantity
  - cart badge count

**Post-Check**
- **Navigate To**: `Shopping Cart`
- **Observe**:
  - cart is empty
  - cart badge count is 0

**Expected Change**: The item is removed from the cart, and the cart badge count is updated to reflect zero items.

---

### [TC-001] Reset App State functionality
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Reset App State Button

**Original Expected Result:** clears the cart and resets in-app state

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Shopping Cart`
- **Observe**:
  - cart item count
  - list of items in the cart

**Post-Check**
- **Navigate To**: `Shopping Cart`
- **Observe**:
  - cart item count
  - list of items in the cart

**Expected Change**: Cart item count increased by one and the newly added product appears in the list of items.

---

### [TC-003] Attempt to logout when not logged in
**Category**: `edge` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click the Logout button

**Original Expected Result:** Logout action is blocked; user remains on the current page with no session ended.

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Shopping Cart`
- **Observe**:
  - list of items in the cart
  - item description
  - item quantity

**Post-Check**
- **Navigate To**: `Shopping Cart`
- **Observe**:
  - list of items in the cart

**Expected Change**: The item that was removed is no longer listed in the cart.

---

### [TC-001] Reset App State functionality
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Reset App State Button

**Original Expected Result:** clears the cart and resets in-app state

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Checkout - Information`
- **Observe**:
  - First Name field
  - Last Name field
  - Zip/Postal Code field

**Post-Check**
- **Navigate To**: `Checkout - Overview`
- **Observe**:
  - order summary
  - totals section
  - payment and shipping information

**Expected Change**: User is redirected to the overview step with a summary of the cart items displayed.

---

### [TC-001] Reset App State functionality
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Reset App State Button

**Original Expected Result:** clears the cart and resets in-app state

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Checkout - Overview`
- **Observe**:
  - order summary
  - item total
  - tax
  - total

**Post-Check**
- **Navigate To**: `Checkout - Confirmation`
- **Observe**:
  - success message
  - order details

**Expected Change**: User is navigated to the confirmation page displaying a success message and order details.

---

### [TC-001] Reset App State functionality
**Category**: `positive` | **Verification Type**: `same_actor_navigation` | **Coverage**: `verifiable`

**Original Steps:**
1. 1. Click Reset App State Button

**Original Expected Result:** clears the cart and resets in-app state

---

#### Verification Plan

**Pre-Check**
- **Navigate To**: `Product Inventory`
- **Observe**:
  - cart badge count
  - Add to cart button states

**Post-Check**
- **Navigate To**: `Product Inventory`
- **Observe**:
  - cart badge count
  - Add to cart button states

**Expected Change**: Cart badge count is zero and all Add to cart buttons are in their default state.

---
