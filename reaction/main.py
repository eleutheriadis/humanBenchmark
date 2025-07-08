import pyautogui
import time

pyautogui.PAUSE = 0

while True:
    _, g, _ = pyautogui.pixel(*pyautogui.position())
    if g == 128:
        pyautogui.click()
        time.sleep(0.1)