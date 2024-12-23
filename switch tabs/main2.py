from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
service = Service (executabLe_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)


# Open a website (example: Google)
driver.get('https://www.google.com')

# Close the browser after a few seconds
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.send_keys("Karthick raja S M"+Keys.ENTER)
time.sleep(5)

# secondtab
driver.execute_script("window.open('about:blank', 'secondtab');")
driver.switch_to.window("secondtab")
driver.get('https://karthiweb.vercel.app')
time.sleep(5)


#thirdtab
driver.execute_script("window.open('about:blank',  'thirdtab');")
driver.switch_to.window("thirdtab")
driver.get('https://www.facebook.com/')

time.sleep(5)
driver.quit()

#close() method closes the current window.
#quit() method quits the driver instance, closing every associated window, which is opened.

# Selenium.get()
# This method is used to launch a new browser and will open the given URL in the browser.

# driver.get(url) 