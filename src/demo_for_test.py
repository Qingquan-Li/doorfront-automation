import time

import pyautogui as pg

x_coordinate = pg.prompt(text="Enter the x-coordinate of the forward arrow",
                         title="x-coordinate of the forward arrow",
                         default="403")
x_coordinate = int(x_coordinate)


y_coordinate = pg.prompt(text="Enter the y-coordinate of the forward arrow",
                         title="y-coordinate of the forward arrow",
                         default="855")
y_coordinate = int(y_coordinate)

print(x_coordinate, y_coordinate)
