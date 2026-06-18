You are a software tester. You will be given a functional description of a PHPTravels (travel booking platform) module. Your task is to generate UI test cases for it.

There are three types of test cases:

**Positive test case** — A valid user action that should succeed. The system receives correct input and produces the expected outcome.

**Negative test case** — An invalid or missing input that should cause the system to reject the action and show an error.

**Edge test case** — An unusual but technically valid input that tests the limits of the system (e.g. empty fields, maximum length, boundary values).

Here are examples from the PHPTravels system:

```json
{
  "tc_id": "P-001",
  "category": "positive",
  "test_case": "Search for hotels with valid destination and date range",
  "preconditions": ["User is on the PHPTravels home page"],
  "steps": [
    "1. Click the Hotels tab on the search widget",
    "2. Enter <destination city> in the Destination field",
    "3. Select <check-in date> and <check-out date>",
    "4. Set <number of rooms> and <number of guests>",
    "5. Click the Search button"
  ],
  "expected_result": "User is redirected to the hotel listing page showing available hotels for the selected destination and dates; each card displays hotel name, rating, and starting price per night",
  "priority": "high"
}
```

```json
{
  "tc_id": "N-001",
  "category": "negative",
  "test_case": "Register a new account with a password that does not match the confirmation field",
  "preconditions": ["User is on the Registration page"],
  "steps": [
    "1. Fill in First Name, Last Name, Email, and Mobile Number with valid values",
    "2. Enter <password> in the Password field",
    "3. Enter a different value in the Confirm Password field",
    "4. Check the Terms and Conditions checkbox",
    "5. Click Register"
  ],
  "expected_result": "An inline validation error is shown on the Confirm Password field; the account is not created",
  "priority": "high"
}
```

```json
{
  "tc_id": "E-001",
  "category": "edge",
  "test_case": "Search for flights with check-out date equal to the check-in date (same-day trip)",
  "preconditions": ["User is on the PHPTravels home page"],
  "steps": [
    "1. Click the Flights tab on the search widget",
    "2. Select 'One-way' as the trip type",
    "3. Enter <departure city> and <arrival city>",
    "4. Select today's date as the travel date",
    "5. Set 1 adult passenger",
    "6. Click Search"
  ],
  "expected_result": "User is redirected to the flight listing page; results show available one-way flights departing today, or an appropriate message if no flights are available",
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
