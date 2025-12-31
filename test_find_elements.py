from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")

# Find elements
username_input = driver.find_element(By.ID, "user-name")
password_input = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

print("Username input found:", username_input is not None)
print("Password input found:", password_input is not None)
print("Login button found:", login_button is not None)

driver.quit()
