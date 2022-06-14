"""
This script demonstrates how to drag the map (Google Street View)
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
        # Most machines automatically update the browser, but the driver does not.
        # Use "webdriver-manager" to make sure you get the correct driver for your browser.
        # service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)

        self.DOORFRONT_LOCAL_URL = 'http://localhost:3000/'
        # for testing:
        self.MOUSE_TRAIL_URL = 'https://codepen.io/falldowngoboone/pen/PwzPYv'

    def open_website(self):
        print('Opening the website...')
        try:
            self.driver.get(self.DOORFRONT_LOCAL_URL)
            time.sleep(3)  # TODO wait for loading all elements
        except TimeoutException:
            print('Time Out!')

    # def drag(self):
    #     """ https://rangeslider.js.org/ """
    #     draggable = self.driver.find_element(By.XPATH, '//*[@id="js-rangeslider-0"]/div[2]')
    #     bar = self.driver.find_element(By.ID, 'js-rangeslider-0')
    #     webdriver.ActionChains(self.driver)\
    #         .click_and_hold(draggable)\
    #         .move_to_element_with_offset(draggable, 300, 0)\
    #         .perform()

    #         # .drag_and_drop_by_offset(draggable, -100, 0).perform()

    #         # .move_to_element_with_offset(bar, 200, 0)\
    #         # .click(draggable)\
    #         # .perform()

    # def drag(self):
    #     """ MOUSE_TRAIL_URL """
    #     iframe = self.driver.find_element(By.XPATH, '//*[@id="result"]')
    #     self.driver.switch_to.frame(iframe)
    #     target = self.driver.find_element(By.XPATH, '/html')
    #     # print(iframe.rect)  # {'height': 519, 'width': 1200, 'x': 0, 'y': 433}
    #     print(target.rect)  # {'height': 8, 'width': 1200, 'x': 0, 'y': 0}

    #     action = webdriver.ActionChains(self.driver)
    #     action.move_to_element(target)  # have to add this line, to move the mouse
    #     action.click_and_hold()
    #     action.move_by_offset(400, 100)
    #     action.perform()

    def drag(self):
        """ LOCAL_URL """
        # target = self.driver.find_element(By.XPATH, '//*[@id="StreetView"]/div/div[1]/div/div[10]/div/canvas')
        # print(target.rect)  # 

        # action = webdriver.ActionChains(self.driver)
        # action.move_to_element(target)  # have to add this line, to move the mouse
        # action.click_and_hold()
        # action.move_by_offset(100, 100)
        # action.perform()
        
        target = self.driver.find_element(By.XPATH, '//*[@id="StreetView"]/div/div[1]/div/div[10]/div/canvas')
        print(target.rect)  # {'height': 640, 'width': 640, 'x': 24, 'y': 153.59375}
        # webdriver.ActionChains(self.driver)\
        #     .click_and_hold(draggable)\
        #     .move_by_offset(200, 100)\
        #     .perform()
        
        action = webdriver.ActionChains(self.driver)

        action.click_and_hold(target)
        action.move_by_offset(400, 0)
        action.release(target)
        action.perform()
        time.sleep(1)

        action.click_and_hold(target)
        action.move_by_offset(400, 0)
        action.release(target)
        action.perform()
        time.sleep(1)



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
