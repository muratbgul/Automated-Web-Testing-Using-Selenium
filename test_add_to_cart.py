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

# Add first product to cart
add_to_cart_btn = wait.until(
    EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
)
add_to_cart_btn.click()

# Check cart badge
cart_badge = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
)

assert cart_badge.text == "1"

print("✅ Add to cart test passed")

driver.quit()
