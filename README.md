![linter-check](https://github.com/kat-git-hub/fake-online-store/actions/workflows/lint.yml/badge.svg)   ![Python](https://img.shields.io/badge/python-3.8%2B-blue)

# Fake Online Store

Project includes Selenium tests for the Demoblaze website.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/kat-git-hub/fake-online-store.git
    cd fake-online-store
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Make sure to have the appropriate WebDriver installed and added to your PATH. For example, for Chrome:
    ```bash
    # On macOS/Linux
    brew install chromedriver
    
    # On Windows
    # Download from https://sites.google.com/a/chromium.org/chromedriver/downloads
    ```

## Running the tests

To run all tests, use:
```bash
pytest tests/

