from selenium import webdriver

# Start Chrome browser
driver = webdriver.Chrome()

# Open SauceDemo website
driver.get("https://www.saucedemo.com")

# Print page title
print("Page title:", driver.title)

# Close browser
driver.quit()
