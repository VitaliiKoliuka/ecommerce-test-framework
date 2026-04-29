# 🧪 E-commerce Test Automation Framework

A scalable test automation framework for API and UI testing, built with **Python, pytest, Playwright, and Requests**.  
This project demonstrates modern QA practices including **Page Object Model, data-driven testing, CI/CD, and Allure reporting**.

---

## 🚀 Features

### ✅ API Testing
- REST API testing using `requests`
- Reusable API client layer
- Schema validation using dataclasses
- Token-based authentication
- Request/response logging with Allure attachments

### ✅ UI Testing
- Playwright-based automation
- Page Object Model (POM)
- Reusable base page
- Screenshot capture on failure
- Validation layer for assertions

### ✅ Test Design
- Data-driven testing (JSON + Faker)
- Pytest markers:
  - `sanity`
  - `smoke`
  - `regression`
- Dependency-based test flows

### ✅ Reporting & Logging
- Allure Reports (logs, screenshots, API details)
- Custom logging system
- Automatic request/response tracking

### ✅ CI/CD
- GitHub Actions pipeline
- Dockerized test execution
- Allure report published via GitHub Pages

---

## 📊 Test Report

👉 [View Allure Report](https://vitaliikoliuka.github.io/ecommerce-test-framework/)

---

## 📁 Project Structure

ecommerce-test-framework/\
│\
├── api/ # API clients, schemas, tests\
├── ui/ # UI pages and tests\
├── utils/ # Helpers, logger, data generator\
├── config/ # Configuration files\
├── data/ # Test data\
├── .github/workflows/ # CI/CD pipeline\
├── Dockerfile\
├── docker-compose.yml\
└── pytest.ini

---

## ⚙️ Installation

```bash
git clone https://github.com/<your-username>/ecommerce-test-framework.git
cd ecommerce-test-framework

pip install -r requirements.txt
playwright install
```

## ▶️ Running Tests
- **Run all tests**\
pytest
- **Run API tests**\
pytest api/tests
- **Run UI tests**\
pytest ui/tests
- **Run by marker**\
pytest -m smoke
pytest -m regression
- **🐳 Run with Docker**\
docker compose up --build

## 📊 Allure Report (Local)
```bash
pytest --alluredir=allure-results
allure serve allure-results
```
## ⚠️ API Limitations
This framework uses https://dummyjson.com as a mock API.
- Some endpoints (e.g., DELETE) do not persist data
- Responses may differ from real production APIs

The framework still uses correct HTTP methods (GET, POST, PUT, DELETE) to reflect real-world API design.

## 🧩 Tech Stack
Python\
pytest\
Playwright\
Requests\
Allure Reporting\
Docker\
GitHub Actions

## 🧠 Design Principles
Page Object Model (POM)\
Separation of concerns\
Reusable API client architecture\
Data-driven testing\
Scalable and maintainable structure

## 👨‍💻 Author
Vitalii Koliuka
GitHub: https://github.com/VitaliiKoliuka
LinkedIn: https://www.linkedin.com/in/vitalii-koliuka-1389a8251

## 🎯 Purpose
This project is part of my QA automation portfolio, demonstrating practical experience with modern testing tools, frameworks, and CI/CD integration.
