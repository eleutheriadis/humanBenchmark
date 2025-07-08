import pyautogui
import pytesseract
import time
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pyautogui.click((2534,580)) #CLick start
time.sleep(1)
area=1900 ,340,1500,350
endColor = (255, 209, 84) #Yellow color of buttons
custom_config=r'--oem 3 --psm 6 outputbase digits'
score=0
retries=0
while score <69:
    color = pyautogui.pixel(2434, 620)
    if color ==endColor:
        pyautogui.click((2711 ,615)) #Click try again
        time.sleep(0.5)
        pyautogui.click((2534,580)) #Click start
        print("Retries:",retries,"Score:",score)
        retries+=1
        continue
    s = pyautogui.screenshot('petros.png',region=area)
    c = cv2.imread('petros.png')
    g = cv2.cvtColor(c,cv2.COLOR_BGR2GRAY)
    t = pytesseract.image_to_string(g,lang='digits',config=custom_config)
    n = t.replace('\n', '')
    color = pyautogui.pixel(2527 ,533) #Submit button
    while color!=endColor:
            color = pyautogui.pixel(2527 ,533)
    pyautogui.write(n,interval=0.1)
    time.sleep(0.5)
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(2)
    score +=1