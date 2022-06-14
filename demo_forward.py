"""
This script demonstrates how to click the forward button on the DoorFront website.
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

        self.LOCAL_URL = 'http://localhost:3000/'

    def open_website(self):
        print('Opening the website...')
        try:
            self.driver.get(self.LOCAL_URL)
            time.sleep(2)  # TODO wait for loading all elements
        except TimeoutException:
            print('Time Out!')

    def click_to_go_forward(self):
        """ http://localhost:3000/ """
        draggable = self.driver.find_element(By.XPATH, '//*[@id="StreetView"]/div/div[1]/div/div[10]')
        print(draggable.rect)

        action = webdriver.ActionChains(self.driver)

        go_forward_btn = self.driver.find_element(By.XPATH,
            '//div[@class="gmnoprint"]/*[name()="svg"]/*[name()="path" and @fill="black"][1]')
        action.move_to_element(go_forward_btn)
        action.click()
        action.perform()
        time.sleep(2)

        go_forward_btn = self.driver.find_element(By.XPATH,
            '//div[@class="gmnoprint"]/*[name()="svg"]/*[name()="path" and @fill="black"][2]')
        action.move_to_element(go_forward_btn)
        action.click()
        action.perform()
        time.sleep(2)

        go_forward_btn = self.driver.find_element(By.XPATH,
            '//div[@class="gmnoprint"]/*[name()="svg"]/*[name()="path" and @fill="black"][1]')
        action.move_to_element(go_forward_btn)
        action.click()
        action.perform()
        time.sleep(2)

        go_forward_btn = self.driver.find_element(By.XPATH,
            '//div[@class="gmnoprint"]/*[name()="svg"]/*[name()="path" and @fill="black"][2]')
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
