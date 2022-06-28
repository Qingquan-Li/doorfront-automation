"""
Automatically walk in Google Street View
and take screenshots using PyAutoGUI.

Created: June 28th EDT (UTC-4)
"""

import time

import pyautogui


gsv_img = pyautogui.screenshot(
        imageFilename = 'images/0gsv.png',
        # Get the coordinates of the mouse on the screen (macOS):
        # hot key: command + shift + 4
        # gsv top_left_corner coordinate: 24, 289
        # gsv bottom_right_corner coordinate: 664, 929
        # iMac M1 Screen bottom_right_corner Coordinate: 2239, 1259
        # iMac M1 Screen Resolution: 4480 × 2520
        # => gsv Size: (664 - 24) * 2 = 1280, (929 - 289) * 2 = 1280
        region=(48, 578, 1280, 1280)
    )
print(gsv_img)
# On a 1920 x 1080 screen,
# the screenshot() function takes roughly 100 milliseconds
time.sleep(0.3)
# Initial: Heading: 204, Pitch: 8, Zoom: 1
pyautogui.moveTo(403, 855)
pyautogui.click()
pyautogui.click()
# Waiting for GSV to render
time.sleep(1.7)

for i in range(3):
    
    gsv_img = pyautogui.screenshot(
        imageFilename = 'images/' + str(i + 1) + 'gsv.png',
        region=(48, 578, 1280, 1280)
    )
    print(gsv_img)
    
    time.sleep(0.3)
    pyautogui.click()
    time.sleep(1.7)
