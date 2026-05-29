- [ ] Email must be in valid format (e.g. user@example.com)
- [ ] Password must be at least 6 characters
- [ ] Email must not already be registered
- [ ] After successful registration, user is redirected to home page as a logged-in user
- [ ] If registration fails, a clear error message is displayed

User Story 1: Registration
    AC1:
        → TC-001 : Register with valid email format         → PASS
        → TC-002 : Register with invalid email (no @)       → FAIL
        → TC-003 : Register with invalid email (no domain)  → FAIL

    AC2:
        → TC-004 : Register with 6 characters password      → PASS
        → TC-005 : Register with 5 characters password      → FAIL
        → TC-006 : Register with 7 characters password  → PASS

    AC3:
        → TC-007 : Register with non-registered email      → PASS
        → TC-008 : Register with registered email           → FAIL

    AC4:
        → TC-009 : After registration, verify user is redirected to home page as logged-in user  → PASS

    AC5:  
        → TC-010 : Register with invalid credentials, verify error message is displayed → FAIL


| TC ID | Title | Preconditions | Steps | Expected Result | Status |
|-------|-------|---------------|-------|-----------------|--------|
| TC-001 | Register with valid email format | User is on registration page | 1. Go to registration page 2. Enter valid email 3. Enter valid password 4. Click Register | User is successfully registered | TODO |

| TC-002 | Register with invalid email (no @) | User is on registration page | 1. Go to registration page 2. Enter invalid email (no @) 3. Enter valid password 4. Click Register | An error message is displayed | TODO |

| TC-003 | Register with invalid email (no domain) | User is on registration page | 1. Go to registration page 2. Enter invalid email (no domain) 3. Enter valid password 4. Click Register | An error message is displayed | TODO | 

| TC-004 | Register with 6 characters password | User is on registration page | 1. Go to registration page 2. Enter password with 6 characters 3. Submit password 4. Click Register | User is successfully registered | TODO |

| TC-005 |  |  |  |  |  |

| TC-006 |  |  |  |  |  |

| TC-007 |  |  |  |  |  |

| TC-008 |  |  |  |  |  |

| TC-009 |  |  |  |  |  |

| TC-010 |  |  |  |  |  |
