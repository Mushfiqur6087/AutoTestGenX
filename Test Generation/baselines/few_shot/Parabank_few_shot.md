You are a software tester. You will be given a functional description of a Parabank (online banking demo) module. Your task is to generate UI test cases for it.

There are three types of test cases:

**Positive test case** — A valid user action that should succeed. The system receives correct input and produces the expected outcome.

**Negative test case** — An invalid or missing input that should cause the system to reject the action and show an error.

**Edge test case** — An unusual but technically valid input that tests the limits of the system (e.g. empty fields, maximum length, boundary values).

Here are examples from the Parabank system:

```json
{
  "tc_id": "P-001",
  "category": "positive",
  "test_case": "Transfer funds between two internal ParaBank accounts",
  "preconditions": ["User logged in", "At least two Checking or Savings accounts exist with sufficient balance"],
  "steps": [
    "1. Navigate to Transfer Funds from the left-hand menu",
    "2. Select 'My ParaBank Account' as the transfer type",
    "3. Enter <transfer amount> in the Transfer Amount field",
    "4. Select <source account> from the Source Account dropdown",
    "5. Select <destination account> from the destination dropdown",
    "6. Click Transfer"
  ],
  "expected_result": "Page shows 'Transfer completed successfully.' with a transaction ID; navigating to Accounts Overview shows the source account balance decreased and the destination account balance increased by the transfer amount",
  "priority": "high"
}
```

```json
{
  "tc_id": "N-001",
  "category": "negative",
  "test_case": "Attempt a fund transfer with an amount exceeding the source account balance",
  "preconditions": ["User logged in", "A Checking or Savings account exists with a known balance"],
  "steps": [
    "1. Navigate to Transfer Funds",
    "2. Select 'My ParaBank Account' as the transfer type",
    "3. Enter an amount greater than the source account balance",
    "4. Select the source and a destination account",
    "5. Click Transfer"
  ],
  "expected_result": "An error message 'Insufficient funds' is displayed; no transfer is processed",
  "priority": "high"
}
```

```json
{
  "tc_id": "E-001",
  "category": "edge",
  "test_case": "Open a Savings account with the exact minimum deposit amount",
  "preconditions": ["User logged in", "A funding account with at least $100 exists"],
  "steps": [
    "1. Navigate to Open New Account",
    "2. Select the Savings account type card",
    "3. Enter exactly 100 in the Initial Deposit Amount field",
    "4. Select <funding account> from the Funding Source Account dropdown",
    "5. Click Open Account"
  ],
  "expected_result": "Page shows 'Account opened successfully!' and the user is redirected to Accounts Overview where the new Savings account appears",
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
