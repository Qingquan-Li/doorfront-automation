import time

import pyautogui

# btn_location = pyautogui.locateOnScreen('images/pyautogui-home.png')
# print(btn_location)
# btn_point = pyautogui.center(btn_location)
# print(btn_point)

# a shortcut version to click on the
# center of where the button was found
# pyautogui.click('images/pyautogui-home.png')

# x, y = pyautogui.locateCenterOnScreen('images/pyautogui-home.png')
# pyautogui.click(x, y)

pyautogui.moveTo(420, 788)
time.sleep(1)
pyautogui.click()
pyautogui.click()

for _ in range(10):
  time.sleep(1)
  pyautogui.click()
