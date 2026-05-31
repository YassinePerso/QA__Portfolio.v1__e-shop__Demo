### US-03 : Product Search

#### Acceptance Criteria
- [ ] When a valid product name is entered, matching results are displayed
- [ ] If the product doesn't exist, a "no results" message is displayed
- [ ] Search is case-insensitive



User Story 2: Account Log-in
    AC1:
        → TC-001 : Log-in with credentials of existing account in database  → PASS
        → TC-002 : Log-in with invalid mail  → FAIL
        → TC-003 : Log-in with invalid password  → FAIL

    AC2:
        → TC-004 : Log-in with existing account and verify if user is redirected to home page as a logged-in user  → PASS

    AC3:
        → TC-005 : Log-in with empty fields, verify error message is displayed → FAIL
