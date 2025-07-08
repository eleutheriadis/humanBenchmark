import pyautogui
import mss
from PIL import Image
sct = mss.mss()

pyautogui.PAUSE = 0
region = {'top':230,'left': 2100,'width': 1000,'height':440}
color = (149,195,232)
endColor = (255, 209, 84)
pyautogui.PAUSE =0
s = sct.grab(region)
img = Image.frombytes("RGB", s.size, s.bgra, "raw", "BGRX")
end = img.getpixel((334, 375))
while end!=endColor:
    x = 40
    y=40
    found = False
    while x <s.width and found == False:
        if img.getpixel((x,y)) == color: 
                found = True
                pyautogui.click(x+2100,y+230)    
        y +=40
        if y >= s.height:
             y=40
             x +=40 
    s = sct.grab(region)
    img = Image.frombytes("RGB", s.size, s.bgra, "raw", "BGRX")
    end = img.getpixel((334, 375))
    


     