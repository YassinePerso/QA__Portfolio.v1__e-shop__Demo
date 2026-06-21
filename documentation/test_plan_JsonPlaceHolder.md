# Test Plan --> JSONPlaceholder API

## 1. Objective & Scope
<!-- What do we test ? What do we no test ? -->
-> IN SCOPE:
        → GET requests (users, posts)
        → POST requests (create new post)
        → PUT requests (update existing post)
        → DELETE requests (delete post)
        → Negative scenarios (non-existent resources)
        → Response status codes, response time, response body structure
        → Collection variable chaining (user_id, post_id)

-> OUT OF SCOPE:
        → Authentication / authorization (JSONPlaceholder is a public fake API, no auth required)
        → PATCH requests
        → Load testing / performance testing
        → Security testing (the API is a public mock, not a production system)
        → Data persistence validation (JSONPlaceholder does not actually persist changes server-side)


## 2. Application Under Test
<!-- URL, type of app, context -->
→ **Name:** JSONPlaceholder
→ **URL:** https://jsonplaceholder.typicode.com/
→ **Type:** Public REST API (fake online mock server)
→ **Description:** JSONPlaceholder is a free public API used for testing and prototyping. It simulates a typical REST resource (`/users`, `/posts`) and returns realistic but non-persistent responses. It is used here as a complementary target to demonstrate API testing skills.


## 3. Test Environment
<!-- OS, browser, versions Python/Selenium/etc. -->
→ OS: Linux/Ubuntu
→ Postman (Desktop App)
→ Newman (CLI runner, version: 6.x)
→ newman-reporter-html
→ Node.js (version: 24)


## 4. Test Types
<!-- List the types of tests you are going to execute -->
→ Functional API tests 
→ Negative tests 
→ Smoke tests

> All requests executed against the live public JSONPlaceholder API.


## 5. Strategy & Approach
<!-- In which order? manual testing first or automated testing first? Why? -->
-> Requests designed and validated manually in Postman first
-> Collection variables used to chain dynamic data between requests (e.g. created post_id reused in PUT/DELETE)
-> Full collection automated and executed with Newman
-> Integrated in CI/CD via GitHub Actions (independent from the UI test suite)


## 6. Entry & Exit Criteria
<!-- When do we start? When do we stop? -->
-> ENTRY CRITERIA:
        - The Postman collection and environment files are created and validated
        - Collection variables are correctly configured for request chaining
        - Newman and the HTML reporter are installed in the test environment

-> EXIT CRITERIA:
        - All planned endpoints (GET, POST, PUT, DELETE) are covered
        - All assertions pass (status code, response body, response time)
        - Newman HTML report is generated and reviewed
        - No blocking issues remain on the collection


## 7. Risks & Dependencies
<!-- What could block your tests ? -->
| Risk | Impact | Mitigation |
|------|--------|------------|
| Public API unavailable or rate-limited | Tests cannot be executed, pipeline fails | Add a fallback/retry step before failing the job |
| Non-existent resource ID used in request | Test fails due to data setup error, not application defect | Verify ID ranges available on JSONPlaceholder (e.g. posts only go up to ID 100) before hardcoding values |
| API does not persist data (mock server) | False expectation of stateful behavior between requests | Document this clearly in test design — assertions target response structure, not real persistence |
| Newman HTML reporter not installed on CI runner | Report generation fails even if tests pass | Explicitly install `newman-reporter-html` as a separate CI step |