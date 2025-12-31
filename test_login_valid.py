from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start browser
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")

wait = WebDriverWait(driver, 10)

# Locate elements
username = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

# Enter credentials
username.send_keys("standard_user")
password.send_keys("secret_sauce")

# Click login
login_button.click()

# Wait until redirected to inventory page
wait.until(EC.url_contains("inventory"))

# Assertion
assert "inventory" in driver.current_url

print("✅ Valid login test passed")

driver.quit()
