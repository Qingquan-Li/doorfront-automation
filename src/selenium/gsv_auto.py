"""
Created: 06/12/2022 EDT (UTC-4)
Description: Run the Google Street View automatically.
"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager


class ChromeOptionsInit:
    """ Initialize chrome_options """
    # selenium.webdriver source code: from .chrome.options import Options as ChromeOptions
    chrome_options = webdriver.ChromeOptions()

    # [Add startup arguments]:

    # USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36'
    # chrome_options.add_argument('user-agent={}'.format(USER_AGENT))

    # Specify browser resolution
    # https://www.selenium.dev/documentation/en/webdriver/browser_manipulation/#set-window-size
    # https://selenium-python.readthedocs.io/api.html#selenium.webdriver.remote.webdriver.WebDriver.set_window_size
    # driver.set_window_size(1024, 768)
    # Note that there can be no spaces after the comma.
    # `window-size` can be: `--window-size`
    chrome_options.add_argument('window-size=1440,1080')

    # Hide the scroll bar, for some special web pages
    # chrome_options.add_argument('--hide-scrollbars')

    # Do not load pictures, to improve speed
    # chrome_options.add_argument('blink-settings=imagesEnabled=false')

    # Disable JavaScript
    # chrome_options.add_argument("--disable-javascript")

    # Using Chrome headless mode (without a visual interface);
    # because some systems (such as Linux) does not support visualization,
    # they will fail to start without this line.
    # chrome_options.add_argument('--headless')

    # Run with highest permission. Sandbox is a security technology of Chrome.
    chrome_options.add_argument('--no-sandbox')

    # Tell Chrome to hide webdriver traces. Test in https://bot.sannysoft.com/:
    # Test Name: WebDriver(New)  Result: present (failed)  will be: WebDriver(New)  missing (passed)
    chrome_options.add_argument('disable-blink-features=AutomationControlled')

    # [Add experimental arguments]:

    # Set developer mode, hide: Chrome is being controlled by automated test software.
    chrome_options.add_experimental_option('excludeSwitches',
                                           ['enable-automation'])
    # Hide automation extension information
    chrome_options.add_experimental_option('useAutomationExtension', False)


class GsvAuto:
    """ Run the Google Street View automatically """

    def __init__(self):
        """ Initialize """
        # self.driver = webdriver.Chrome(executable_path='./chromedriver',
        #                                options=ChromeOptionsInit.chrome_options)
        # DeprecationWarning: executable_path has been deprecated, please pass in a Service object
        # In Selenium 4, you’ll need to set the driver’s executable_path from a Service object.

        # service = Service('./chromedriver')
        # Most machines automatically update the browser, but the driver does not.
        # Use "webdriver-manager" to make sure you get the correct driver for your browser.
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service,
                                       options=ChromeOptionsInit.chrome_options)

        self.doorfront_local_url = 'http://localhost:3000/'
        self.doorfront_production_url = 'https://doorfront.org/'

    def open_website(self):
        print('Opening the website...')
        try:
            self.driver.get(self.doorfront_local_url)
            time.sleep(8)  # TODO use WebDriverWait
        except TimeoutException:
            print('Time Out!')

    def click_to_go_forward(self):
        # //*[@id="StreetView"]/div/div[1]/div/div[10]/div/canvas
        # #StreetView > div > div:nth-child(1) > div > div:nth-child(10) > div > canvas
        # <canvas width="1280" height="1280" id=""
        # class="mapsConsumerUiSceneInternalCoreScene__canvas widget-scene-canvas"
        # style="width: 640px; height: 640px;"></canvas>
        # res = self.driver.find_element(By.ID, "StreetView").rect
        # print(res)  # {'height': 640, 'width': 640, 'x': 24, 'y': 153.59375}
        
        # mouse_tracker = self.driver.find_element(By.ID, "StreetView")
        # webdriver.ActionChains(self.driver)\
        #     .move_to_element_with_offset(mouse_tracker, 662, 791)\
        #     .click()\
        #     .perform()
        # time.sleep(2)

        draggable = self.driver.find_element(By.ID, "StreetView")
        droppable = self.driver.find_element(By.ID, "MapContainer")
        webdriver.ActionChains(self.driver)\
            .drag_and_drop(draggable, droppable)\
            .perform()

if __name__ == "__main__":
    try:
        gsv_auto = GsvAuto()
        gsv_auto.open_website()
        gsv_auto.click_to_go_forward()
    except Exception as e:
        print(e)
    finally:
        time.sleep(1)
        gsv_auto.driver.quit()
        print('############ End ############')
