from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")

wait = WebDriverWait(driver, 10)

# Locate UI elements
username_input = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
password_input = wait.until(EC.visibility_of_element_located((By.ID, "password")))
login_button = wait.until(EC.visibility_of_element_located((By.ID, "login-button")))
logo = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "login_logo")))

# Assertions
assert username_input.is_displayed()
assert password_input.is_displayed()
assert login_button.is_displayed()
assert logo.is_displayed()

print("✅ UI elements validation test passed")

driver.quit()
