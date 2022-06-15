"""
This program demonstrates how to drag the map (Google Street View)
on the DoorFront website.
"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class GsvAuto:
    """ Run the Google Street View automatically """

    def __init__(self):
        """ Initialize """
        service = Service('./chromedriver')
        self.driver = webdriver.Chrome(service=service)

        # DoorFront code: https://github.com/Qingquan-Li/DoorFront-Automation-Map
        self.DOORFRONT_LOCAL_URL = 'http://localhost:3000/'

    def open_website(self):
        print('Opening the website...')
        try:
            self.driver.get(self.DOORFRONT_LOCAL_URL)
            time.sleep(3)  # TODO use WebDriverWait
        except TimeoutException:
            print('Time Out!')

    def drag(self):
        """ Drag the map, to turn left or right """
        target = self.driver.find_element(By.XPATH, '//*[@id="StreetView"]/div/div[1]/div/div[10]/div/canvas')
        print(target.rect)  # {'height': 640, 'width': 640, 'x': 24, 'y': 153.59375}
        
        action = webdriver.ActionChains(self.driver)

        action.click_and_hold(target)
        action.move_by_offset(300, 0)
        action.release(target)
        action.perform()
        time.sleep(2)

        action.click_and_hold(target)
        action.move_by_offset(300, 0)
        action.release(target)
        action.perform()
        time.sleep(2)

        action.click_and_hold(target)
        action.move_by_offset(300, 0)
        action.release(target)
        action.perform()
        time.sleep(2)

        action.click_and_hold(target)
        action.move_by_offset(300, 0)
        action.release(target)
        action.perform()
        time.sleep(2)


if __name__ == "__main__":
    try:
        gsv_auto = GsvAuto()
        gsv_auto.open_website()
        gsv_auto.drag()
    except Exception as e:
        print(e)
    finally:
        time.sleep(5)
        gsv_auto.driver.quit()
        print('############ End ############')
