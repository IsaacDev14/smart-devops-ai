from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Automated Login Test Script using Selenium with WebDriver Manager

print("=== Starting Automated Login Tests ===")

# Initialize Chrome browser automatically
print("Initializing Chrome WebDriver...")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
print("Browser launched successfully.")

# Open demo login page
print("Navigating to demo login page...")
driver.get("https://the-internet.herokuapp.com/login")
time.sleep(2)

# Test 1: Valid credentials
print("\n--- Running Test 1: Valid Credentials ---")
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(2)

if "You logged into a secure area!" in driver.page_source:
    print("✅ Result: Valid Login Test Passed")
else:
    print("❌ Result: Valid Login Test Failed")

# Test 2: Invalid credentials
print("\n--- Running Test 2: Invalid Credentials ---")
driver.get("https://the-internet.herokuapp.com/login")
driver.find_element(By.ID, "username").send_keys("wronguser")
driver.find_element(By.ID, "password").send_keys("wrongpass")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(2)

if "Your username is invalid!" in driver.page_source:
    print("✅ Result: Invalid Login Test Passed")
else:
    print("❌ Result: Invalid Login Test Failed")

# End of test
print("\nClosing browser...")
driver.quit()
print("Browser closed.")
print("=== Automated Tests Completed ===")

# Summary:
# AI-assisted tools like Testim.io extend Selenium by identifying UI changes automatically
# and reducing test maintenance overhead.
