from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create a new instance of the web driver
driver = webdriver.Chrome()  # Make sure you have the Chrome driver executable in your PATH

# Navigate to the login page
driver.get("https://example.com/login")  # Replace with the actual login page URL

# Find the username and password input fields
username_field = driver.find_element_by_id("username")  # Replace with the actual username field ID
password_field = driver.find_element_by_id("password")  # Replace with the actual password field ID

# Enter the login credentials
username_field.send_keys("your_username")  # Replace with your actual username
password_field.send_keys("your_password")  # Replace with your actual password

# Submit the form
password_field.send_keys(Keys.RETURN)

# Close the browser
driver.quit()
