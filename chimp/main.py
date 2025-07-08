import pytesseract
from PIL import ImageGrab
import pyautogui
import cv2
import numpy as np
import time

#Red value of try again button
tryAgain = 149 

score = 0

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

area=2200,220,750,440

custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789'

def take_screenshot():
    
    screenshot = pyautogui.screenshot(region=area)
    screenshot.save('screenshot.png')
    return np.array(screenshot)

def find_numbers(img):
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Use pytesseract to get data of detected text
    data = pytesseract.image_to_data(gray, config=custom_config, output_type=pytesseract.Output.DICT)
    
    numbers = []
    for i in range(len(data['text'])):
        if data['text'][i].strip().isdigit():  # Check if it's a number
            x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
            number = int(data['text'][i].strip())
            numbers.append((number, x, y, w, h))

    return sorted(numbers, key=lambda x: x[0])  # Sort by number

def click_numbers(numbers,play,score):
    for number, x, y, w, h in numbers:
        r,_,_ =pyautogui.pixel(2700,600)
        if r==tryAgain:
            play = False
            break
        r,_,_ = pyautogui.pixel(2545,580)
        if r==255:
            break
        time.sleep(0.1)

        # Calculate the center of the number to click
        center_x = x + w // 2
        center_y = y + h // 2

        # Perform the click
        pyautogui.moveTo(center_x+2200, center_y+225, duration=0.2)
        pyautogui.click()
    score +=1
    return play,score

def main():
    pyautogui.click(2534,580)
    play = True
    while play:
        img = take_screenshot()
        numbers = find_numbers(img)
        time.sleep(0.5)
        click_numbers(numbers,play,score)
        pyautogui.click(2545,580)
        print(score)
    print("Game over!")

if __name__ == "__main__":
    main()
