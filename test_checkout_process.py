from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

# Add product
add_button = wait.until(
    EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
)
add_button.click()

# Go to cart
cart_icon = wait.until(
    EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
)
cart_icon.click()

# Checkout
checkout_button = wait.until(
    EC.element_to_be_clickable((By.ID, "checkout"))
)
checkout_button.click()

# Fill checkout info
first_name = wait.until(EC.presence_of_element_located((By.ID, "first-name")))
last_name = driver.find_element(By.ID, "last-name")
postal_code = driver.find_element(By.ID, "postal-code")

first_name.send_keys("Test")
last_name.send_keys("User")
postal_code.send_keys("12345")

continue_button = driver.find_element(By.ID, "continue")
continue_button.click()

# Finish order
finish_button = wait.until(
    EC.element_to_be_clickable((By.ID, "finish"))
)
finish_button.click()

# Verify success message
complete_header = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
)

assert "thank you" in complete_header.text.lower()

print("✅ Checkout process test passed")

driver.quit()
