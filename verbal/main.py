import pyautogui
import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
pyautogui.click((2534,580))
def clickSeen():
    pyautogui.click(2503, 526)
def clickNew():
    pyautogui.click(2653, 523)

area = (2250, 419,1000,50)
words = []
custom_config = r'--oem 3 --psm 7'
for _ in range(6900):
    s = pyautogui.screenshot('petros.png',region=area)
    c = cv2.imread('petros.png')
    p = cv2.bitwise_not(c)
    t = pytesseract.image_to_string(p,config=custom_config)
    if t not in words:
        words.append(t)
        clickNew()
    else:
        clickSeen()
        


    
