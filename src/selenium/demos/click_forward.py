"""
This program demonstrates how to click the forward button on the DoorFront website.
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
            time.sleep(2)  # TODO use WebDriverWait
        except TimeoutException:
            print('Time Out!')

    def click_to_go_forward(self):
        """ Click the go forward button """
        action = webdriver.ActionChains(self.driver)

        number = 1
        for _ in range(3):
            if number == 1:
                go_forward_btn = self.driver.find_element(By.XPATH,
                    '//div[@class="gmnoprint"]/*[name()="svg"]/*[name()="path" and @fill="black"][1]')
                action.click(go_forward_btn)
                action.perform()
                time.sleep(2)
                number += 1
            if number == 2:
                go_forward_btn = self.driver.find_element(By.XPATH,
                    '//div[@class="gmnoprint"]/*[name()="svg"]/*[name()="path" and @fill="black"][2]')
                action.click(go_forward_btn)
                action.perform()
                time.sleep(2)
                number -= 1


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
