"""
Created: 06/12/2022 EDT (UTC-4)
Description: Run the Google Street View automatically.
"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException


class SeleniumInit:
    """ Initialize Selenium with ChromeDriver """
    # selenium.webdriver source code: from .chrome.options import Options as ChromeOptions
    chrome_options = webdriver.ChromeOptions()

    # Add startup arguments
    USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    chrome_options.add_argument('user-agent={}'.format(USER_AGENT))
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

    # add experimental arguments
    # Set developer mode, hide: Chrome is being controlled by automated test software.
    chrome_options.add_experimental_option('excludeSwitches',
                                           ['enable-automation'])
    # 使浏览器隐藏自动化扩展信息
    chrome_options.add_experimental_option('useAutomationExtension', False)


class GsvAuto:
    """ Run the Google Street View automatically """

    def __init__(self):
        """ Initialize """
        # macOS:
        self.driver = webdriver.Chrome(executable_path='/Users/quan/code/doorfront-automation/chromedriver',
                                       options=SeleniumInit.chrome_options)
        # Windwos OS：chromedriver -> chromedriver.exe
        # DeprecationWarning: executable_path has been deprecated, please pass in a Service object

        self.doorfront_local_url = 'http://localhost:3000/'
        self.doorfront_production_url = 'https://doorfront.org/'

    def open_website(self):
        print('Opening the website...')
        try:
            self.driver.get(self.doorfront_local_url)
            time.sleep(5)
        except TimeoutException:
            print('Time Out!')


if __name__ == "__main__":
    try:
        GsvAuto().open_website()
    except Exception as e:
        print(e)
    finally:
        time.sleep(1)
        GsvAuto().driver.quit()
        print('############ End ############')
