### US-02 : Account Log-in

#### Acceptance Criteria
- [ ] Email and password must match an existing account in the database
- [ ] After successful login, user is redirected to home page as a logged-in user
- [ ] If log-in fails, a clear error message is displayed

User Story 2: Account Log-in
    AC1:
        → TC-001 : Log-in with credentials of existing account in database  → PASS
        → TC-002 : Log-in with invalid mail  → FAIL
        → TC-003 : Log-in with invalid password  → FAIL

    AC2:
        → TC-004 : Log-in with existing account and verify if user is redirected to home page as a logged-in user  → PASS

    AC3:
        → TC-005 : Log-in with empty fields, verify error message is displayed → FAIL


| TC ID | Title | Preconditions | Steps | Expected Result | Status |
|-------|-------|---------------|-------|-----------------|--------|
| TC-001 | Log-in with credentials of existing account | User has a registered account and is on login page | 1. Go to login page 2. Enter valid email 3. Enter valid password 4. Click Login | User is successfully logged in | TODO |
| TC-002 | Log-in with invalid email | User is on login page | 1. Go to login page 2. Enter invalid email 3. Enter valid password 4. Click Login | An error message is displayed | TODO |
| TC-003 | Log-in with invalid password | User has a registered account and is on login page | 1. Go to login page 2. Enter valid email 3. Enter invalid password 4. Click Login | An error message is displayed | TODO |
| TC-004 | Log-in and verify redirection to home page | User has a registered account and is on login page | 1. Go to login page 2. Enter valid email 3. Enter valid password 4. Click Login | User is redirected to home page as logged-in user | TODO |
| TC-005 | Log-in with empty fields | User is on login page | 1. Go to login page 2. Leave all fields empty 3. Click Login | An error message is displayed | TODO |