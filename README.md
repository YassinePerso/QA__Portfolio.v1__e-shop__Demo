# QA Automation Portfolio -> Demo Web Shop && JSon Place Holder

[![Demo Web Shop Automation Pipeline](https://github.com/YassinePerso/QA__Portfolio.v1__e-shop__Demo/actions/workflows/ci.yml/badge.svg)](https://github.com/YassinePerso/QA__Portfolio.v1__e-shop__Demo/actions/workflows/ci.yml)

🇬🇧 **EN**
End-to-end QA automation portfolio built on [Demo Web Shop](https://demowebshop.tricentis.com/), a public e-commerce demo site by Tricentis, and [JSONPlaceholder](https://jsonplaceholder.typicode.com/), a public REST API for testing purposes.
This portfolio covers UI automation with Selenium, BDD testing with pytest-bdd/Gherkin, API testing with Postman/Newman, and a full CI/CD pipeline with GitHub Actions.

🇫🇷 **FR**
Portfolio d'automatisation QA end-to-end construit sur [Demo Web Shop](https://demowebshop.tricentis.com/), un site e-commerce de démonstration public par Tricentis, et [JSONPlaceholder](https://jsonplaceholder.typicode.com/), une API REST publique destinée aux tests.
Ce portfolio couvre l'automatisation UI avec Selenium, les tests BDD avec pytest-bdd/Gherkin, les tests API avec Postman/Newman, et un pipeline CI/CD complet avec GitHub Actions.

---

## Stack

| Category | Tools |
|----------|-------|
| Language | Python 3.12.3 |
| UI Automation | Selenium 4, WebDriver Manager |
| Test Framework | Pytest, pytest-bdd |
| BDD | Gherkin (.feature files) |
| API Testing | Postman, Newman |
| Reporting | pytest-html, Allure Report |
| Data Generation | Faker |
| Lint | flake8, autopep8 |
| CI/CD | GitHub Actions |
| Environment | python-dotenv |
| OS | Linux |

---

## Project Structure

```
QA.Portfolio.v1/
├── .github/
│   └── workflows/
│       └── ci.yml                  # GitHub Actions CI/CD pipeline
├── features/                       # Gherkin .feature files
│   ├── cart.feature
│   ├── checkout.feature
│   ├── login.feature
│   ├── register.feature
│   └── search.feature
├── pages/                          # Page Object Model classes
│   ├── base_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── product_page.py
│   └── register_page.py
├── postman/                        # Postman collection and environment
│   ├── demowebshop_collection.json
│   └── environment.json
├── step_definitions/               # pytest-bdd step definitions
│   ├── cart_steps.py
│   ├── checkout_steps.py
│   ├── login_steps.py
│   ├── register_steps.py
│   └── search_steps.py
├── tests/
│   └── End-to-end/                 # Pytest test suites
│       ├── test_cart.py
│       ├── test_checkout.py
│       ├── test_login.py
│       ├── test_product_search.py
│       └── test_register.py
├── conftest.py                     # Pytest fixtures
├── pytest.ini                      # Pytest configuration
└── requirements.txt                # Python dependencies
```

---

## Installation

### Prerequisites

- Python 3.12.3
- Google Chrome
- Node.js 24 (for Newman)
- Java (for Allure CLI)

### Setup

```bash
# Clone the repository
git clone https://github.com/YassinePerso/QA__Portfolio.v1__e-shop__Demo.git
cd QA__Portfolio.v1__e-shop__Demo

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Install Newman globally
npm install -g newman newman-reporter-html
```

### Environment variables

Create a `.env` file at the root of the project:

```
REGISTERED_EMAIL=your_email@example.com
REGISTERED_PASSWORD=your_password
```

---

## Running the tests

### All End-to-end tests
```bash
pytest tests/End-to-end/ -v
```

### Smoke tests only
```bash
pytest tests/End-to-end/ -v -m smoke
```

### Regression tests only
```bash
pytest tests/End-to-end/ -v -m regression
```

### BDD/Gherkin tests
```bash
pytest step_definitions/ -v
```

### API tests (Newman)
```bash
newman run postman/demowebshop_collection.json -e postman/environment.json --reporters cli,html --reporter-html-export reports/api_report.html
```

### Generate Allure report
```bash
pytest tests/End-to-end/ step_definitions/ -v --alluredir=allure-results
allure generate allure-results --clean -o allure-report
allure open allure-report
```

---

## CI/CD Pipeline

The pipeline runs on every `push` and `pull_request` on `main` and `dev` branches.

| Job | Description | Depends on |
|-----|-------------|------------|
| `lint` | Code quality check with flake8 | — |
| `smoke-tests` | Critical smoke tests | lint |
| `regression-tests` | Full regression suite | smoke-tests |
| `bdd-tests` | BDD/Gherkin scenarios via pytest-bdd | smoke-tests |
| `api-tests` | Postman/Newman API tests | smoke-tests |
| `allure-report` | Consolidated Allure report | regression-tests, bdd-tests, api-tests |

### Known CI limitation

🇬🇧 **EN**
Login, checkout, and existing-email registration tests pass 100% locally but fail systematically in CI. After investigation, the most likely hypothesis is that Demo Web Shop blocks form submissions from GitHub Actions external IPs. This is a possible limitation of the target site, not the test framework. All other tests pass in CI without issue.
This limitation is documented with `continue-on-error: true` on the affected jobs, allowing the pipeline to complete and generate reports regardless.

🇫🇷 **FR**
Les tests de connexion, de paiement et d'inscription avec un e-mail déjà existant passent à 100% en local mais échouent systématiquement en CI. Après investigation, l'hypothèse la plus probable est que Demo Web Shop bloque les soumissions de formulaires provenant des IP externes de GitHub Actions. Il s'agit d'une limitation possible du site cible, et non du framework de test. Tous les autres tests passent en CI sans problème.
Cette limitation est documentée avec `continue-on-error: true` sur les jobs concernés, ce qui permet au pipeline de se terminer et de générer les rapports malgré tout.

---

## Test Results Summary

| Suite | Tests | Status |
|-------|-------|--------|
| End-to-end (local) | 29 | 26 passed, 1 skipped, 2 failed (IP restriction) |
| BDD/Gherkin (local) | 19 | All passed |
| API (Newman) | 21 assertions | All passed |

---

## Key QA Practices

- **Page Object Model (POM)** with inheritance --> all waits via `WebDriverWait` (no time.sleep() -> no flaky test)
- **Data-driven testing** with Faker for dynamic test data generation
- **BDD** with Gherkin Scenario Outline and Boundary Value Analysis (BVA)
- **Headless mode** auto-detected via `CI` environment variable
- **Exploratory testing findings**: 3-character minimum on search bar, out-of-stock products hide the Add-to-Cart button
- **pytest.skip()** used for TC-05 checkout email verification (Gmail API integration deferred)
- **Secrets management** via GitHub Secrets for CI credentials

