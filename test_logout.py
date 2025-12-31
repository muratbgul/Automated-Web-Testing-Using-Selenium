from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")

wait = WebDriverWait(driver, 10)

# Login
username = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username.send_keys("standard_user")
password.send_keys("secret_sauce")
login_button.click()

# Open menu
menu_button = wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
menu_button.click()

# Click logout
logout_button = wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
logout_button.click()

# Verify redirect to login page
wait.until(EC.presence_of_element_located((By.ID, "login-button")))

assert "saucedemo.com" in driver.current_url

print("✅ Logout test passed")

driver.quit()
