from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Automated Login Test Script using Selenium

# Initialize Chrome browser
driver = webdriver.Chrome()

# Open demo login page
driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()

# Test 1: Valid credentials
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(2)

if "You logged into a secure area!" in driver.page_source:
    print("Valid Login Test Passed")
else:
    print("Valid Login Test Failed")

# Test 2: Invalid credentials
driver.get("https://the-internet.herokuapp.com/login")
driver.find_element(By.ID, "username").send_keys("wronguser")
driver.find_element(By.ID, "password").send_keys("wrongpass")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(2)

if "Your username is invalid!" in driver.page_source:
    print("Invalid Login Test Passed")
else:
    print("Invalid Login Test Failed")

driver.quit()

# Summary:
# AI-based tools like Testim.io and Selenium AI improve testing
# by automatically handling dynamic elements and reducing manual test updates.
