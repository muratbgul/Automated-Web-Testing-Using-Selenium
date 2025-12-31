# Automated Web Testing Using Selenium

## Tested Website
**https://www.saucedemo.com/**

---

## Project Purpose
The purpose of this project is to evaluate the functionality of a demo e-commerce web application using automated UI testing.

The test scenarios were designed to cover the most critical user actions, including authentication, product interaction, and session termination.

A total of six test cases were created to validate both positive and negative user behaviors. These scenarios ensure that the system responds correctly under different conditions and user inputs.

---

## Tools and Technologies

In this project, **Selenium WebDriver** was used to perform automated user interface testing on a web-based application. Selenium is an open-source testing framework that allows interaction with web elements such as buttons, input fields, and links through real browsers.

The tests were implemented using the **Python programming language** due to its simplicity and strong support for test automation.

**Google Chrome** was selected as the target browser, and **ChromeDriver** was used to establish communication between Selenium and the browser.

This setup enables the execution of automated test scenarios that simulate real user behavior, such as logging in, navigating pages, and interacting with web elements.

---

## Test Environment Setup

- Python version: **Python 3.11**
- Automation tool: **Selenium WebDriver**
- Browser: **Google Chrome**
- Driver: **ChromeDriver**

To verify the setup, a simple Selenium script was executed to launch the browser and open the SauceDemo website.  
The successful execution of this script confirmed that the Selenium environment was correctly installed and ready for further test implementation.

---

## Element Identification

Before implementing the test cases, key elements on the login page were identified using Selenium locators.

The following elements were located using their unique **HTML `id` attributes**:
- Username input field  
- Password input field  
- Login button  

This step ensures stable and reliable interaction with web elements during test execution.

---

## Test Scenarios

### 1. Valid Login Test
This test case verifies that a user can successfully log in using valid credentials.

Selenium locates the username and password input fields and enters predefined valid values.  
After clicking the login button, the system redirects the user to the inventory page.

✅ The test passes if the URL contains the keyword **"inventory"**, indicating a successful login.

---

### 2. Invalid Login Test
This test verifies the system behavior when invalid login credentials are provided.

The user enters incorrect username and password values and attempts to log in.  
The expected behavior is the display of an error message indicating authentication failure.

✅ The test is considered successful when the error message is detected correctly.

---

### 3. Locked Out User Test
This test checks the system behavior when a locked user attempts to log in.

The user enters valid credentials that belong to a locked account.  
The expected result is that the login attempt fails and an appropriate error message is displayed.

✅ This test ensures that restricted users cannot access the system.

---

### 4. Logout Test
This test verifies that a logged-in user can successfully log out of the system.

After logging in, the user opens the side menu and clicks the logout button.  
The expected result is that the system redirects the user back to the login page.

---

### 5. Add to Cart Test
This test verifies that a user can successfully add a product to the shopping cart.

After logging in, the user clicks the **"Add to Cart"** button of a product.  
The system should update the cart badge to show the correct number of added items.

---

### 6. Remove from Cart Test
This test ve
