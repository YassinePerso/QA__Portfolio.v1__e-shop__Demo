| TC ID | Title | Preconditions | Steps | Expected Result | Status |
|-------|-------|---------------|-------|-----------------|--------|
| TC-01 | Register with valid email format | User is on registration page | 1. Go to registration page 2. Enter valid email 3. Enter valid password 4. Click Register | User is successfully registered | TODO |

| TC-02 | Register with invalid email (no @) | User is on registration page | 1. Go to registration page 2. Enter invalid email (no @) 3. Enter valid password 4. Click Register | An error message is displayed | TODO |

| TC-03 | Register with invalid email (no domain) | User is on registration page | 1. Go to registration page 2. Enter invalid email (no domain) 3. Enter valid password 4. Click Register | An error message is displayed | TODO | 

| TC-04 | Register with 6 characters password | User is on registration page | 1. Go to registration page 2. Enter valid email 3. Enter password with 6 characters 4. Click Register | User is successfully registered | TODO |

| TC-05 | Register with 5 characters password | User is on registration page | 1. Go to registration page 2. Enter valid email 3. Enter password with 5 characters 4. Click Register | An error message is displayed | TODO |

| TC-06 | Register with 7 characters password | User is on registration page | 1. Go to registration page 2. Enter valid email 3. Enter password with 7 characters 4. Click Register | User is successfully registered | TODO |

| TC-07 | Register with registered email | User is on registration page | 1. Go to registration page 2. Enter registered email 3. Enter password 4. Click Register | An error message is displayed | TODO |

| TC-08 | After registration, verify user is redirected to home page as logged-in user | User is on registration page | 1. Go to registration page 2. Enter valid email 3. Enter password 4. Click Register | User is successfully redirected to home page as logged-in user | TODO |

| TC-09 | Register with invalid credentials, verify error message is displayed | User is on registration page | 1. Go to registration page 2. Enter invalid credentials 4. Click Register 5. Verify error message is displayed| An error message is successfully displayed | TODO |
