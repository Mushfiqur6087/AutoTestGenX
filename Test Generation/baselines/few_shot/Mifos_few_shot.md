You are a software tester. You will be given a functional description of a Mifos (microfinance banking platform) module. Your task is to generate UI test cases for it.

There are three types of test cases:

**Positive test case** — A valid user action that should succeed. The system receives correct input and produces the expected outcome.

**Negative test case** — An invalid or missing input that should cause the system to reject the action and show an error.

**Edge test case** — An unusual but technically valid input that tests the limits of the system (e.g. empty fields, maximum length, boundary values).

Here are examples from the Mifos system:

```json
{
  "tc_id": "P-001",
  "category": "positive",
  "test_case": "Activate a Pending client with a valid activation date",
  "preconditions": ["User logged in as Admin", "A client exists in Pending status"],
  "steps": [
    "1. Navigate to the Client Detail page of a Pending client",
    "2. Click the Activate button",
    "3. Enter <valid activation date> in the Activation Date field",
    "4. Click Submit"
  ],
  "expected_result": "Client status badge updates to 'Active' (green chip) on the Client Detail page",
  "priority": "high"
}
```

```json
{
  "tc_id": "N-001",
  "category": "negative",
  "test_case": "Attempt to close a client that has active loan accounts",
  "preconditions": ["User logged in as Admin", "An Active client exists with at least one active loan account"],
  "steps": [
    "1. Navigate to the Client Detail page of an Active client with active loans",
    "2. Click the Close button",
    "3. Select <closure reason> from the dropdown",
    "4. Click Submit"
  ],
  "expected_result": "An error message is displayed stating the client cannot be closed with active accounts; the client status remains Active",
  "priority": "high"
}
```

```json
{
  "tc_id": "E-001",
  "category": "edge",
  "test_case": "Submit a loan repayment with the exact outstanding balance amount",
  "preconditions": ["User logged in as Admin", "An Active loan account exists with a known outstanding balance"],
  "steps": [
    "1. Navigate to the Loan Account Detail page",
    "2. Click Make Repayment",
    "3. Enter the exact total outstanding balance as the transaction amount",
    "4. Select <payment type>",
    "5. Click Submit"
  ],
  "expected_result": "Loan status changes to 'Closed (obligations met)' and outstanding balance shows zero",
  "priority": "high"
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
