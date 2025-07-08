import pyautogui
import time
import pytesseract
import keyboard

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

area= 2091, 438,950,150 
s=pyautogui.screenshot(region=area)
pyautogui.click((2286, 483))
time.sleep(1)
t = pytesseract.image_to_string(s)
time.sleep(0.5)
n = t.replace('\n', ' ')
keyboard.write(n,0)