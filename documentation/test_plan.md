# Test Plan — Demo Web Shop

## 1. Objective & Scope
<!-- Que teste-t-on ? Que ne teste-t-on PAS ? -->
-> IN SCOPE:
        → Registered customer authentication
        → New account creation
        → Search bar functionality
        → Adding items to the cart
        → Cart checkout and payment

-> OUT OF SCOPE:
        → Wishlist (out of perimeter <-> non-critical)
        → Blog/Forum
        → Product comparison feature
        → Performance testing
        → Load testing
        → Cross-browser compatibility (Firefox, Safari, Edge)
        → Security testing (SQL injection, XSS, etc.)


## 2. Application Under Test
<!-- URL, type d'app, contexte -->
→ **Name:** Demo Web Shop
→ **URL:** https://demowebshop.tricentis.com/
→ **Type:** E-commerce website
→ **Description:** Demo Web Shop is a sample e-commerce platform provided by Tricentis,
simulating the purchase of electronic products. It is used strictly for testing purposes.


## 3. Test Environment
<!-- OS, navigateur, versions Python/Selenium/etc. -->
→ OS: Linux/Ubuntu
→ Navigateur: Google Chrome (version 148.0.7778.166)
→ Python (version: 3.12.3)
→ Selenium (version: 4.44.0)
→ Pytest (version: 9.0.3)


## 4. Test Types
<!-- Liste les types de tests que tu vas exécuter -->
→ End-to-End tests
→ API tests
→ Smoke tests
→ Regression 

> All simulated without real deployment.



## 5. Strategy & Approach
<!-- Dans quel ordre ? Manuel d'abord ou auto ? Pourquoi ? -->
-> Manual testing limited to exploratory testing (to validate happy path) and test case design 
-> All repetitive scenarios are automated with Selenium + Pytest
-> Critical user journeys are covered with BDD/Gherkin
-> API endpoints validated with Postman/Newman
-> Full suite integrated in CI/CD via GitHub Actions


## 6. Entry & Exit Criteria
<!-- Quand commence-t-on ? Quand s'arrête-t-on ? -->
-> ENTRY CRITERIA:
        - The test environment is fully configured and operational
        - User Stories, acceptance criteria and test cases are written and validated
        - Test data is prepared and available 
        - All required access and permissions are granted to the QA team
        - The build to be tested has been successfully deployed to the test environment

-> EXIT CRITERIA:
        - Test coverage is complete
        - All test cases have been executed
        - All blocking bugs have been reported, triaged, and resolved or formally accepted
        - Test execution report has been reviewed and approved
        - No critical or high severity bugs remain open

## 7. Risks & Dependencies
<!-- Qu'est-ce qui pourrait bloquer tes tests ? -->
-> Le site est public et peut être indisponible
-> Les données de test peuvent être modifiées par d'autres utilisateurs
-> Pas d'accès à la base de données pour réinitialiser l'état
-> ChromeDriver doit être compatible avec la version de Chrome installée