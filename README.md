# WordPress Dark Mode Test Suite

## Overview
This project is an automated test suite designed to validate the functionality of the "WP Dark Mode" WordPress plugin using Python, Selenium, and `unittest`. The tests ensure that dark mode is correctly applied in the WordPress Admin Dashboard and the front end after specific configuration changes.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Tests](#running-the-tests)
- [Test Scenarios](#test-scenarios)

## Prerequisites
Ensure that the following prerequisites are met before you begin:

1. **Python:** Version 3.7+ is required.
2. **Web Browser:** Chrome or Firefox.
3. **Web Driver:**
   - Chrome: [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)
   - Firefox: [GeckoDriver](https://github.com/mozilla/geckodriver/releases)
4. **WordPress Site:** A running instance with administrative access.

## Installation
1. **Clone the Repository:**
   - Clone the repository to your local system:
   ```bash
   git clone https://github.com/your-username/wordpress-dark-mode-tests.git
   cd wordpress-dark-mode-tests

Create and activate a virtual environment:
python -m venv venv
# For Windows
venv\Scripts\activate
# For macOS/Linux
source venv/bin/activate

#Install required Python libraries:
pip install -r requirements.txt

        
Open tests/test_suite.py and replace the following placeholders:
your_username, your_password, and https://your-wordpress-site/wp-admin.

Running the Tests

Execute the Test Suite:
With the virtual environment activated, run the test suite using:
python -m unittest main_script.py
Test Scenarios

The following scenarios are validated in the test suite:

    Login to WordPress:
        Tests the login functionality.

    Check Plugin Installation:
        Verifies if the "WP Dark Mode" plugin is installed and active.
        Installs and activates the plugin if not available.

    Configuration Changes:
        Enables admin dashboard dark mode.
        Changes the floating switch style, size, and position.
        Disables keyboard shortcuts for dark mode.
        Enables page transition animations.

    Validate Dark Mode:
        Checks that the dark mode is applied in the Admin Dashboard.
        Confirms that dark mode settings are also applied to the front end.


  
