""" This script demonstrates how to use offset of Selenium
https://www.selenium.dev/documentation/webdriver/actions_api/mouse/
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

        self.URL = 'https://rangeslider.js.org'
        self.JQ_URL = 'https://jqueryui.com/droppable/'
        self.CANVAS_NEST_URL = 'https://git.hust.cc/canvas-nest.js/'
        self.GOOGLE_MAPS_URL = 'https://www.google.com/maps'
        # https://github.com/Qingquan-Li/DoorFront-Automation-Map:
        self.LOCAL_URL = 'http://localhost:3000/'

    def open_website(self):
        print('Opening the website...')
        try:
            self.driver.get(self.LOCAL_URL)
            time.sleep(2)  # TODO wait for loading all elements
        except TimeoutException:
            print('Time Out!')

    # def click_to_go_forward(self):
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

    # def click_to_go_forward(self):
    #     """ https://jqueryui.com/draggable/ """
    #     iframe = self.driver.find_element(By.XPATH, '//*[@id="content"]/iframe')
    #     self.driver.switch_to.frame(iframe)
    #     draggable = self.driver.find_element(By.ID, 'draggable')
    #     print(draggable.rect)  # {'height': 118, 'width': 118, 'x': 8, 'y': 18}
    #     webdriver.ActionChains(self.driver)\
    #         .move_to_element_with_offset(draggable, 600, 600)\
    #         .click_and_hold(draggable)\
    #         .move_to_element_with_offset(draggable, 300, 200)\
    #         .perform()
    #     print(draggable.rect)  # {'height': 118, 'width': 118, 'x': 249, 'y': 159}

    # def click_to_go_forward(self):
    #     """ https://www.google.com/maps """
    #     draggable = self.driver.find_element(By.XPATH, '//*[@id="scene"]/div[3]/canvas')
    #     print(draggable.rect)
    #     webdriver.ActionChains(self.driver)\
    #         .move_to_element(draggable)\
    #         .move_to_element_with_offset(draggable, 300, 300)\
    #         .click_and_hold(draggable)\
    #         .move_to_element_with_offset(draggable, 400, 400)\
    #         .perform()
    #     time.sleep(5)
    #     print(draggable.rect)

    # def click_to_go_forward(self):
    #     """ https://git.hust.cc/canvas-nest.js/
    #         Click the button """
    #     draggable = self.driver.find_element(By.XPATH, '/html/body/canvas')
    #     print(draggable.rect)
    #     webdriver.ActionChains(self.driver)\
    #         .move_to_element_with_offset(draggable, 50, 35)\
    #         .click()\
    #         .perform()
    #     time.sleep(10)
    #     print(draggable.rect)

    def click_to_go_forward(self):
        """ http://localhost:3000/ """
        draggable = self.driver.find_element(By.XPATH, '//*[@id="StreetView"]/div/div[1]/div/div[10]')
        print(draggable.rect)
        # webdriver.ActionChains(self.driver)\
        #     .click_and_hold(draggable)\
        #     .move_by_offset(200, 100)\
        #     .perform()
        
        # action = webdriver.ActionChains(self.driver)
        # action.click_and_hold(draggable)
        # action.move_by_offset(400, 0)
        # action.release(draggable)
        # action.perform()
        # time.sleep(1)
        # print(draggable.rect)

        # //*[@id="StreetView"]/div/div[1]/div/div[9]/svg/path[3]
        go_forward_btn = self.driver.find_element(By.XPATH,
            '//div[@class="gmnoprint"]/*[name()="svg"]/*[name()="path" and @fill="black"][1]'
            )
        action = webdriver.ActionChains(self.driver)

        action.move_to_element(go_forward_btn)
        action.click()
        action.perform()

        time.sleep(2)

        go_forward_btn = self.driver.find_element(By.XPATH,
            '//div[@class="gmnoprint"]/*[name()="svg"]/*[name()="path" and @fill="black"][2]')
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(go_forward_btn)
        action.click()
        action.perform()

        time.sleep(2)

        go_forward_btn = self.driver.find_element(By.XPATH,
            '//div[@class="gmnoprint"]/*[name()="svg"]/*[name()="path" and @fill="black"][1]')
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(go_forward_btn)
        action.click()
        action.perform()

        time.sleep(2)

        go_forward_btn = self.driver.find_element(By.XPATH,
            '//div[@class="gmnoprint"]/*[name()="svg"]/*[name()="path" and @fill="black"][2]')
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(go_forward_btn)
        action.click()
        action.perform()

        time.sleep(2)


if __name__ == "__main__":
    try:
        gsv_auto = GsvAuto()
        gsv_auto.open_website()
        gsv_auto.click_to_go_forward()
    except Exception as e:
        print(e)
    finally:
        time.sleep(5)
        gsv_auto.driver.quit()
        print('############ End ############')
