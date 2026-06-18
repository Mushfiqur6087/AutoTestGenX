You are a software tester. You will be given a functional description of a Moodle (teacher role) module. Your task is to generate UI test cases for it.

There are three types of test cases:

**Positive test case** — A valid user action that should succeed. The system receives correct input and produces the expected outcome.

**Negative test case** — An invalid or missing input that should cause the system to reject the action and show an error.

**Edge test case** — An unusual but technically valid input that tests the limits of the system (e.g. empty fields, maximum length, boundary values).

Here are examples from the Moodle Teacher system:

```json
{
  "tc_id": "P-001",
  "category": "positive",
  "test_case": "Create an assignment with online text submission enabled and a due date",
  "preconditions": ["User logged in as Teacher", "A course exists and Edit mode is enabled"],
  "steps": [
    "1. Navigate to the Course page",
    "2. Click '+ Add an activity or resource' in the target section",
    "3. Select Assignment from the Activity Chooser and click Add",
    "4. Enter <assignment name> in the Assignment name field",
    "5. Enable the Due date toggle and select <due date>",
    "6. Check the 'Online text' checkbox under Submission types",
    "7. Click 'Save and return to course'"
  ],
  "expected_result": "The assignment appears in the course section with a link; the Grading summary panel shows 0 submissions",
  "priority": "high"
}
```

```json
{
  "tc_id": "N-001",
  "category": "negative",
  "test_case": "Attempt to save an assignment without entering a name",
  "preconditions": ["User logged in as Teacher", "A course exists and Edit mode is enabled"],
  "steps": [
    "1. Navigate to the Course page and click '+ Add an activity or resource'",
    "2. Select Assignment and click Add",
    "3. Leave the Assignment name field empty",
    "4. Click 'Save and return to course'"
  ],
  "expected_result": "An inline validation error highlights the Assignment name field; the form is not submitted and remains open",
  "priority": "high"
}
```

```json
{
  "tc_id": "E-001",
  "category": "edge",
  "test_case": "Set assignment cut-off date to the same date and time as the due date",
  "preconditions": ["User logged in as Teacher", "A course exists and Edit mode is enabled"],
  "steps": [
    "1. Open the Assignment creation form",
    "2. Enter <assignment name>",
    "3. Enable Due date toggle and set it to <specific date and time>",
    "4. Enable Cut-off date toggle and set it to the exact same date and time as the due date",
    "5. Click 'Save and return to course'"
  ],
  "expected_result": "Assignment is saved successfully and appears in the course; both due and cut-off dates are identical in the assignment metadata",
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
