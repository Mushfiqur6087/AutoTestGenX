You are a software tester. You will be given a functional description of a Moodle (student role) module. Your task is to generate UI test cases for it.

There are three types of test cases:

**Positive test case** — A valid user action that should succeed. The system receives correct input and produces the expected outcome.

**Negative test case** — An invalid or missing input that should cause the system to reject the action and show an error.

**Edge test case** — An unusual but technically valid input that tests the limits of the system (e.g. empty fields, maximum length, boundary values).

Here are examples from the Moodle Student system:

```json
{
  "tc_id": "P-001",
  "category": "positive",
  "test_case": "Submit an assignment using the online text editor",
  "preconditions": ["User logged in as Student", "An assignment with online text submission is open and within the due date"],
  "steps": [
    "1. Navigate to the Assignment page from the Course page",
    "2. Click 'Add submission'",
    "3. Enter <submission text> in the online text editor",
    "4. Click 'Save changes'"
  ],
  "expected_result": "Submission status row updates to 'Submitted for grading'; Last modified timestamp reflects the submission time",
  "priority": "high"
}
```

```json
{
  "tc_id": "N-001",
  "category": "negative",
  "test_case": "Attempt to log in with an incorrect password",
  "preconditions": ["A registered student account exists"],
  "steps": [
    "1. Navigate to the Moodle login page",
    "2. Enter <valid username> in the Username field",
    "3. Enter <wrong password> in the Password field",
    "4. Click 'Log in'"
  ],
  "expected_result": "An inline error message is displayed; the Password field is cleared; the Username field retains the entered value",
  "priority": "high"
}
```

```json
{
  "tc_id": "E-001",
  "category": "edge",
  "test_case": "Filter the Timeline block with a date range that contains no upcoming activities",
  "preconditions": ["User logged in as Student", "No activities are due within the next 7 days"],
  "steps": [
    "1. Navigate to the Dashboard",
    "2. In the Timeline block, select 'Next 7 days' from the time range dropdown"
  ],
  "expected_result": "The Timeline block displays an empty state message indicating no upcoming activities within the selected range",
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
