from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import re


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
driver.get("https://www.last.fm/settings/subscription/automatic-edits")

# Get number of automatic edits
num_auto_edits = re.sub("\D", "", driver.find_element(By.CLASS_NAME, 'buffer-standard').text)

# Find the delete button and delete just the first one
delete_button = driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div[5]/div[3]/section/table/tbody/tr[1]/td[6]/form[2]/button")
hover = ActionChains(driver).move_to_element(delete_button)
driver.implicitly_wait(10)
hover.perform()
delete_button.click()


# below driver can't locate the button
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "/html/body/div[11]/div[1]/div/div[2]/ul/li[2]/button").click()

# Close after finishing
driver.close()
