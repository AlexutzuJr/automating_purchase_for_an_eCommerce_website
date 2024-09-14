# Project Overview

This project automates the process of purchasing a product from an eCommerce website using Python's Selenium WebDriver. The script simulates a real user navigating through the website, adding a product to the cart, and completing the purchase as a guest user. Key functionalities include interacting with the calendar, filling out billing details, and confirming the purchase.

**Project Steps**
* Setup WebDriver
* Navigate to the website
* Image gallery navigation
* Set Shipping date
* Quantity adjustment
* Checkout process
* Billing details
* Order confirmation
* Order verification

# Local Setup

## Installation

To run this project, the following tools and dependencies are required:

* Run the following command to install Selenium and other necessary libraries: pip install selenium webdriver-manager
* webdriver-manager will automatically manage the versioning of ChromeDriver during runtime.
* Ensure that Google Chrome is installed on your machine as the script uses it for browser automation.

# Usage
Run the Python script:

* Execute the automate.py script to run the automation.
* The script will open a browser, navigate through the website, perform the purchase steps, and print the final order details and success message.
  
Capture screenshot:

* The script will capture and save a screenshot of the product gallery during the purchase process.

Verify output:
* Upon successful execution, the script will print the final price and order confirmation message.
