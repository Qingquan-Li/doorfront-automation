"""
Demo code from:
- https://chromedriver.chromium.org/getting-started
- https://www.selenium.dev/documentation/webdriver/getting_started/
"""

# import time

# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome('/Users/quan/code/doorfront-automation/chromedriver')  # Optional argument, if not specified will search path.

# driver.get('http://www.google.com/')

# time.sleep(1) # Let the user actually see something!

# # search_box = driver.find_element_by_name('q')

# # search_box.send_keys('ChromeDriver')

# # search_box.submit()
# driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()

# time.sleep(5) # Let the user actually see something!

# driver.quit()

##################################################

# import time

# from selenium import webdriver

# from selenium.webdriver.chrome.service import Service

# service = Service('./chromedriver')

# service.start()

# driver = webdriver.Remote(service.service_url)

# driver.get('http://www.google.com/')

# time.sleep(5) # Let the user actually see something!

# driver.quit()


##################################################

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# service = Service('./chromedriver')
# https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/#1-driver-management-software
# Use install() to get the location used by the manager
# and pass it into service class
service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

time.sleep(5)
driver.quit()
