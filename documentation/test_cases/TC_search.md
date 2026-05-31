### US-03 : Product Search

#### Acceptance Criteria
- [ ] When a valid product name is entered, matching results are displayed
- [ ] If the product doesn't exist, a "no results" message is displayed
- [ ] Search is case-insensitive



User Story 3: Product Search
    AC1:
        → TC-001 : Enter valid name product and verify if matching result(s) is/are displayed  → PASS

    AC2:
        → TC-002 : Enter invalid name product and verify "no results" message is displayed → FAIL

    AC3:
        → TC-003 : Enter valid name product with wrong case and verify is macthing result(s) is /are displayed → PASS


| TC ID | Title | Preconditions | Steps | Expected Result | Status |
|-------|-------|---------------|-------|-----------------|--------|
| TC-001 | Enter valid product name and verify matching results are displayed | User is on home page | 1. Go to home page 2. Enter valid product name in search bar 3. Press Enter | Matching results are displayed | TODO |
| TC-002 | Enter invalid product name and verify "no results" message is displayed | User is on home page | 1. Go to home page 2. Enter invalid product name in search bar 3. Press Enter | "No results" message is displayed | TODO |
| TC-003 | Enter valid product name with wrong case and verify matching results are displayed | User is on home page | 1. Go to home page 2. Enter valid product name in wrong case 3. Press Enter | Matching results are displayed | TODO |