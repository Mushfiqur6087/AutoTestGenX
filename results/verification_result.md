# Coverage Metrics Report

This report aggregates the coverage metrics (`verifiable`, `partial`, `unverifiable`) across all applications and models.

| Application | Model | Verifiable | Partial | Unverifiable | Total |
|-------------|-------|------------|---------|--------------|-------|
| Mifos | gpt-4o-mini | 117 | 0 | 1 | 118 |
| Mifos | gpt-5-mini | 167 | 5 | 0 | 172 |
| MoodleStudent | gpt-4o-mini | 6 | 0 | 0 | 6 |
| MoodleStudent | gpt-5-mini | 17 | 0 | 0 | 17 |
| MoodleTeacher | gpt-4o-mini | 26 | 0 | 0 | 26 |
| MoodleTeacher | gpt-5-mini | 58 | 1 | 0 | 59 |
| PHPTravels | gpt-4o-mini | 18 | 0 | 0 | 18 |
| PHPTravels | gpt-5-mini | 22 | 9 | 0 | 31 |
| Parabank | gpt-4o-mini | 18 | 0 | 0 | 18 |
| Parabank | gpt-5-mini | 29 | 1 | 0 | 30 |
| SwagLab | gpt-4o-mini | 7 | 0 | 0 | 7 |
| SwagLab | gpt-5-mini | 9 | 0 | 0 | 9 |

---

## Coverage Definitions

The post-verification framework categorizes test coverage based on the observable degree of state mutation in the application UI. The goal is to enforce rigorous standards for what constitutes a "successful" test execution.

### 1. Verifiable
The state change caused by the test case can be fully observed and verified within the application UI (either by the same actor navigating to a different page or by a cross-actor interaction). 

> **Case Study: Mifos (Group Creation)**
> - **Verification Setup:** `same_actor_navigation`
> - **Scenario:** A Maker submits a form to create a new Client Group.
> - **Why it is verifiable:** The actor can navigate to the Groups Page post-creation and definitively observe the new group name in the data table with a 'Pending' status. The entire backend state mutation is explicitly and immediately reflected in the UI.

### 2. Partial
The state change is only partially observable in the application UI. The core action has occurred, and secondary effects can be seen, but a critical component of the action (such as an external system dispatch) cannot be verified in-app.

> **Case Study: PHPTravels (User Registration)**
> - **Verification Setup:** `same_actor_navigation`
> - **Scenario:** A user registers a new account, which triggers an email verification workflow.
> - **Why it is partial:** The creation of the account *can* be indirectly verified by attempting to log in (which returns a 'Please verify your email' block instead of 'Account not found'). However, the actual delivery of the verification email to the user's external inbox cannot be verified from within the application, making the total action only partially observable.

### 3. Unverifiable
The core state change caused by the test case cannot be verified at all within the application's UI, often because it occurs entirely in an external system without any in-app confirmation, or because the application lacks the necessary UI to view the result.

> **Case Study: Mifos (Form Submission without Confirmation)**
> - **Verification Setup:** `same_actor_navigation`
> - **Scenario:** Submitting a Recurring Deposit (RD) Account creation form.
> - **Why it is unverifiable:** The core action submits the creation form, but in this specific edge case, the system fails to provide a confirmation screen or a subsequent dashboard view to confirm the entity was actually created. Because there is no immediate UI change or list to check, the state change remains a "black box" operation relative to the immediate UI.
