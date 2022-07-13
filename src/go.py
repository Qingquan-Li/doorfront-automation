"""
Automatically walk in Google Street View
and take screenshots using PyAutoGUI.

You need to change the values below the TODO comment.
Because the default values are tested on an Apple iMac,
you must change the defaults for the program to run correctly
on you computer.

Comments start with # or three double-quotes.
"""

import time

import pyautogui

""" Take the first screenshot before click the forward arrow.
The screenshot will be saved to the images folder. """
gsv_img = pyautogui.screenshot(
    imageFilename = 'images/1gsv.png',
    # TODO: Replace the top-left and bottom-right coordinates
    # of the google street view (GSV) on your computer.
    # Argument1: GSV top-left x-coordinate
    # Argument2: GSV top-left y-coordinate
    # Argument3: GSV bottom-right x-coordinate
    # Argument4: GSV bottom-right y-coordinate
    region=(48, 579, 1280, 1280)
)
print("Taking the #1 screenshot...")


""" On a 1920 x 1080 screen, the screenshot() function
takes roughly 100 milliseconds """
time.sleep(0.3)

# TODO: Replace the x-coordinate and y-coordinate
# of the forward arrow on google street view (GSV).
# Argument1: GSV forward arrow x-coordinate
# Argument2: GSV forward arrow y-coordinate
pyautogui.moveTo(403, 855)


""" Click the forward arrow to forward! """
pyautogui.click()
pyautogui.click()
""" Waiting for google street view to render. """
time.sleep(1.7)


###########################################################


# TODO: Replace the value in range().
# If set to 3, the forward arrow will be clicked 3 times here and you will
# get 4 screenshots (we get the first screenshot at the beginning).
for i in range(3):
    """ Here's a for-loop that loops over what we did above! """
    gsv_img = pyautogui.screenshot(
        imageFilename = 'images/' + str(i + 2) + 'gsv.png',
        # TODO: Replace the top-left and bottom-right coordinates
        # of the google street view (GSV) on your computer.
        # Argument1: GSV top-left x-coordinate
        # Argument2: GSV top-left y-coordinate
        # Argument3: GSV bottom-right x-coordinate
        # Argument4: GSV bottom-right y-coordinate
        # The 4 parameters are the same as in line 23 above.
        region=(48, 579, 1280, 1280)
    )

    print(f"Taking the #{i + 2} screenshot...")
    time.sleep(0.3)
    pyautogui.click()
    time.sleep(1.7)
