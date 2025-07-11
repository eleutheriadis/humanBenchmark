import pyautogui
import mss
from PIL import Image
sct = mss.mss()
from pynput import mouse

print("Please click the TOP-LEFT corner of the region...")

coords = []

def on_click(x, y, button, pressed):
    if pressed:
        coords.append((x, y))
        print(f"Captured click at: ({x}, {y})")

        if len(coords) == 1:
            print("Now, click the BOTTOM-RIGHT corner of the region...")
        elif len(coords) == 2:
            # Stop listener after second click
            return False

# Collect two clicks
with mouse.Listener(on_click=on_click) as listener:
    listener.join()

# Calculate region from two clicks
(x1, y1), (x2, y2) = coords

region = {
    'top': min(y1, y2),
    'left': min(x1, x2),
    'width': abs(x2 - x1),
    'height': abs(y2 - y1)
}

print(f"Region set to: {region}")


pyautogui.PAUSE = 0
pyautogui.click((region["width"]/2)+region['left'],(region["height"]/2)+region['top'])
color = (149,195,232)
endpixel=(0.4*region['width'],0.8*region["height"])
endColor = (255, 209, 84)
pyautogui.PAUSE =0
s = sct.grab(region)
img = Image.frombytes("RGB", s.size, s.bgra, "raw", "BGRX")
end = img.getpixel(endpixel)
while end!=endColor:
    x = 40
    y = 40
    found = False
    while x <s.width and found == False:
        if img.getpixel((x,y)) == color: 
                found = True
                pyautogui.click(x+region["left"],y+region["top"])    
        y +=40
        if y >= s.height:
             y=40
             x +=40 
    s = sct.grab(region)
    img = Image.frombytes("RGB", s.size, s.bgra, "raw", "BGRX")
    end = img.getpixel(endpixel)
    


     