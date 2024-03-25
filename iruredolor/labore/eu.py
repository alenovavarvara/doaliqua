from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Go to the login page
driver.get("https://www.example.com Find the username and password fields
username_field = driver.find_element_by_id("username")
password_field = driver.find_element_by_id("password")

# Enter the username and password
username_field.send_keys("username")
password_field.send_keys("password")

# Click the login button
login_button = driver.find_element_by_id("login-button")
login_button.click()

# Wait for the page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "main-content")))

# Get the account information from the page
account = {
    'username': username_field.get_attribute("value"),
    'password': password_field.get_attribute("value")
}

# Close the browser
driver.close()
