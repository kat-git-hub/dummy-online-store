# Fake Online Store

## CI/CD and Tests:
   [![Maintainability](https://api.codeclimate.com/v1/badges/22a8864c30d0bedc00a3/maintainability)](https://codeclimate.com/github/kat-git-hub/fake-online-store/maintainability)   [![Test Coverage](https://api.codeclimate.com/v1/badges/22a8864c30d0bedc00a3/test_coverage)](https://codeclimate.com/github/kat-git-hub/fake-online-store/test_coverage)



   ![Python](https://img.shields.io/badge/python-3.8%2B-blue)   ![Selenium Grid Status](https://img.shields.io/badge/Selenium%20Grid-Online-brightgreen)
   ![Docker](https://img.shields.io/badge/Docker-0db7ed?style=plastic&logo=docker&logoColor=white)

## Introduction ✨
This project is a UI test automation suite for the fake online store [Demoblaze.com](https://www.demoblaze.com) using Selenium Grid, Docker and Python. The suite includes tests for navigating categories, selecting products, adding products to the cart, placing orders, and verifying cart contents.

## Overview 📋

The main feature of this project is to set up a Selenium Grid infrastructure using Docker, which includes installing Chromium on Selenium Grid nodes. This setup allows for scalable, distributed, and automated browser testing with Chromium, leveraging Docker's containerization to ensure consistency, easy management, and deployment of the testing environment.

## Test Capabilities ✅

Category Navigation: Automates the process of navigating through different product categories.
Product Selection: Verifies the ability to select various products from the listings.
Add to Cart: Ensures that products can be added to the shopping cart.
Order Placement: Tests the complete checkout process, including form submissions.
Cart Verification: Checks that the cart contents are correctly displayed and updated.

## Technologies Used 🛠️

Selenium Grid: For distributed test execution across multiple machines.
Python: The primary programming language for the test scripts.
Pytest: The testing framework used to write and run the tests.
ChromeDriver: Used for running tests in a headless Chrome browser.
Docker: For containerizing and managing the Selenium Grid and other dependencies.

## Getting Started 🚀

To get started with running the tests locally, ensure you have the necessary dependencies installed and a Selenium Grid or local WebDriver set up.

- Clone the repository:

```
git clone https://github.com/yourusername/fake-online-store.git
cd fake-online-store
```

- Install [Poetry](https://python-poetry.org/docs/#installing-with-pipx) if it is not already installed.

- Install the dependencies:
```
poetry install
```
- Set up ChromeDriver and ensure it is available in your system PATH.

## Running the Tests 🏃‍♂️

To run the tests, use the following command:

```
poetry run pytest tests/
```

## Docker Compose 🐳

To run tests locally using Selenium, you can use the provided `docker-compose.yml` file, which configures a container with `selenium/standalone-chromium`.

Start the container:
```
docker-compose up -d
```


-----------
License 📜

Usage is provided under the [MIT](https://github.com/release-it/release-it/blob/main/LICENSE) License.