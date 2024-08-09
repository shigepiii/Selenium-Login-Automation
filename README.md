# web-application-login-automation


# Web Application Login Automation

## Overview

This project demonstrates how to automate the testing of a web application's login functionality using Selenium with Python. The goal is to ensure that the login functionality works correctly and to provide an example of how to use Selenium for browser automation.

## Features

- Automated testing of login functionality
- Verifies login success and failure scenarios
- Supports configuration for different environments

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher
- [Google Chrome](https://www.google.com/chrome/) or [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new/) installed
- WebDriver for your browser (e.g., ChromeDriver or GeckoDriver)

## Installation

1. Clone the repository:

  ```bash
  git clone https://github.com/yourusername/web-application-login-automation.git
  cd web-application-login-automation

2. Create a virtual environment and activate it:

  ```bash
  python -m venv env
  source env/bin/activate  # For Windows: env\Scripts\activate

3. Install the required packages:

  ```bash
  pip install -r requirements.txt

## Usage

1. Open `login_test.py` and update the `URL`, `username`, and `password` variables with your web application’s login details.

2. Run the test script:

  ```bash
  python login_test.py

3. Check the test results in the terminal.


## Example

Here is an example of how the test script works:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configure WebDriver
driver = webdriver.Chrome()  # Or use webdriver.Firefox() for Firefox

# Navigate to the login page
driver.get("https://example.com/login")

# Locate and fill in the login form
username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")
login_button = driver.find_element(By.NAME, "login")

username_input.send_keys("testuser")
password_input.send_keys("password123")
login_button.click()

# Wait for the result
time.sleep(5)

# Check for successful login
if "Welcome" in driver.page_source:
   print("Login successful")
else:
   print("Login failed")

# Close the browser
driver.quit()
