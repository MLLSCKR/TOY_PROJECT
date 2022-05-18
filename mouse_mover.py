import pyautogui
from time import sleep

display_size = pyautogui.size()

for i in range (1, display_size.width, 400):
    for j in range(1, display_size.height, 400):
        pyautogui.moveTo(i, j)
        sleep(1)