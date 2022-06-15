# doorfront-automation

Automatically walk in Google Street View on the website ([DoorFront](https://doorfront.org/)) using **Selenium 4.2** and **ChromeDriver**.


## How to run?
1. Clone the code from: https://github.com/Qingquan-Li/doorfront-automation
2. Install [python3](https://www.python.org/downloads/)
3. In the project root directory, create a [virtual environment](https://docs.python.org/3/library/venv.html): `$ python3 -m venv .venv`
4. Activate the virtual environment: `$ source .venv/bin/activate`
5. Install dependencies: `$ pip install -r requirements.txt`
6. Download [ChromeDriver](https://chromedriver.chromium.org) to the project root path
7. Run: `$ python src/gsv_auto.py`


---


## Selenium
Documentation:
- https://www.selenium.dev/documentation/webdriver/

Python Documentations (Third Party):
- https://selenium-python.readthedocs.io/index.html


## ChromeDriver

WebDriver is an open source tool for
automated testing of webapps across many browsers.

- https://chromedriver.chromium.org


## Create a Google Maps API Key

Create a Google Maps API Key for loading
Google Street View on the website (DoorFront).
- https://developers.google.com/maps/documentation/javascript/get-api-key
