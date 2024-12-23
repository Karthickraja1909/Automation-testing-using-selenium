from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
# https://sites.google.com/chromium.org/driver/ 
service = Service (executabLe_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://google.com")

#load 5 seconds

WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))  # Wait for the search input field to appear on the page.
)

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.send_keys("Karthick raja S M"+Keys.ENTER)


link = driver.find_element(By.PARTIAL_LINK_TEXT,"Karthick Raja S M - Greater Chennai Area")
link.click()

time.sleep(10)
driver.quit()