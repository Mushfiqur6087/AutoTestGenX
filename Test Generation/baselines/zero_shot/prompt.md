You are a software tester. You will be given a functional description of a web application module. Your task is to generate UI test cases for it.

There are three types of test cases:

**Positive test case** — A valid user action that should succeed. The system receives correct input and produces the expected outcome.

**Negative test case** — An invalid or missing input that should cause the system to reject the action and show an error.

**Edge test case** — An unusual but technically valid input that tests the limits of the system (e.g. empty fields, maximum length, boundary values).

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
