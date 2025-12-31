from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")

wait = WebDriverWait(driver, 10)

# Locate elements
username = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

# Locked user credentials
username.send_keys("locked_out_user")
password.send_keys("secret_sauce")
login_button.click()

# Wait for error message
error_message = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
)

# Assertion
assert "locked out" in error_message.text.lower()

print("✅ Locked out user test passed")

driver.quit()
