"""
This program demonstrates the mouse pointer movement trail
controlled by selenium.
"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class MoveMouse:
    def __init__(self):
        """ Initialize """
        service = Service('./chromedriver')
        self.driver = webdriver.Chrome(service=service)

        self.MOUSE_TRAIL_URL = 'https://codepen.io/falldowngoboone/pen/PwzPYv'

    def open_website(self):
        print('Opening the website...')
        try:
            self.driver.get(self.DOORFRONT_LOCAL_URL)
            time.sleep(3)
        except TimeoutException:
            print('Time Out!')

    def move(self):
        """ Test on MOUSE_TRAIL_URL """
        iframe = self.driver.find_element(By.XPATH, '//*[@id="result"]')
        self.driver.switch_to.frame(iframe)
        target = self.driver.find_element(By.XPATH, '/html')
        # print(iframe.rect)  # {'height': 519, 'width': 1200, 'x': 0, 'y': 433}
        print(target.rect)  # {'height': 8, 'width': 1200, 'x': 0, 'y': 0}

        action = webdriver.ActionChains(self.driver)
        action.move_to_element(target)  # have to add this line, to move the mouse
        action.click_and_hold()
        action.move_by_offset(400, 100)
        action.perform()


if __name__ == "__main__":
    try:
        move_mouse = MoveMouse()
        move_mouse.open_website()
        move_mouse.move()
    except Exception as e:
        print(e)
    finally:
        time.sleep(5)
        move_mouse.driver.quit()
        print('############ End ############')
