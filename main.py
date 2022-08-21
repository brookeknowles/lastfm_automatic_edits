from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# Open the browser to login
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.last.fm/")
driver.find_element(By.CLASS_NAME, "site-auth-control").send_keys(Keys.ENTER)


# Ask for user details and login
username = input("Enter last.fm username or email: ")
password = input("Enter last.fm password: ")

driver.find_element(By.ID, "id_username_or_email").send_keys(username)
driver.find_element(By.ID, "id_password").send_keys(password)
driver.find_element(By.NAME, "submit").send_keys(Keys.ENTER)


# Navigate to automatic edits page
driver.find_element(By.XPATH, "//a[contains(text(),'Settings')]").send_keys(Keys.ENTER)     # element not interactable error (probs need to hover over dropdown)


# Find the delete button and delete just the first one

# Close after finishing
driver.close()
