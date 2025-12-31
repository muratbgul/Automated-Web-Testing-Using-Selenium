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

# Add item to cart
add_button = wait.until(
    EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
)
add_button.click()

# Remove item from cart
remove_button = wait.until(
    EC.element_to_be_clickable((By.ID, "remove-sauce-labs-backpack"))
)
remove_button.click()

# Check that cart badge is gone
cart_badges = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")

assert len(cart_badges) == 0

print("✅ Remove from cart test passed")

driver.quit()
