You are a software tester. You will be given a functional description of a Swag Labs (e-commerce testing demo) module. Your task is to generate UI test cases for it.

There are three types of test cases:

**Positive test case** — A valid user action that should succeed. The system receives correct input and produces the expected outcome.

**Negative test case** — An invalid or missing input that should cause the system to reject the action and show an error.

**Edge test case** — An unusual but technically valid input that tests the limits of the system (e.g. empty fields, maximum length, boundary values).

Here are examples from the Swag Labs system:

```json
{
  "tc_id": "P-001",
  "category": "positive",
  "test_case": "Complete a full checkout with one item in the cart",
  "preconditions": ["User logged in as standard_user", "At least one product has been added to the cart"],
  "steps": [
    "1. Click the shopping cart icon to navigate to the Shopping Cart page",
    "2. Click Checkout",
    "3. Enter <first name>, <last name>, and <zip code> in the Information form",
    "4. Click Continue",
    "5. Review the order summary on the Overview page",
    "6. Click Finish"
  ],
  "expected_result": "Confirmation page displays 'Thank you for your order!'; the cart badge is no longer visible",
  "priority": "high"
}
```

```json
{
  "tc_id": "N-001",
  "category": "negative",
  "test_case": "Attempt to log in with the locked-out user account",
  "preconditions": ["User is on the Swag Labs login page"],
  "steps": [
    "1. Enter 'locked_out_user' in the Username field",
    "2. Enter 'secret_sauce' in the Password field",
    "3. Click Login"
  ],
  "expected_result": "An error banner is displayed with the message 'Epic sadface: Sorry, this user has been locked out.'; the user remains on the login page",
  "priority": "high"
}
```

```json
{
  "tc_id": "E-001",
  "category": "edge",
  "test_case": "Add all available products to the cart and verify the cart badge count",
  "preconditions": ["User logged in as standard_user", "Cart is empty"],
  "steps": [
    "1. On the Product Inventory page, click 'Add to cart' for every product listed",
    "2. Observe the cart badge in the header after each addition"
  ],
  "expected_result": "The cart badge count equals the total number of products available; all 'Add to cart' buttons change to 'Remove'",
  "priority": "medium"
}
```

---

Now read the following functional description and generate test cases for it.

<module_name>{Module name}</module_name>

<description>
{Functional description text}
</description>

Return a JSON object in this exact format. No markdown, no extra text:

{
  "module": "Module Name",
  "category": "all",
  "test_cases": [
    {
      "tc_id": "string",
      "category": "positive | negative | edge",
      "test_case": "short descriptive name",
      "preconditions": ["..."],
      "steps": ["1. ...", "2. ..."],
      "expected_result": "what the tester sees after the last step",
      "priority": "high | medium | low"
    }
  ],
  "summary": {
    "total": 0,
    "high_priority": 0,
    "medium_priority": 0,
    "low_priority": 0
  }
}
