import pyautogui
import time

pyautogui.click((2534,580))
time.sleep(1)
area = (2385, 285,375,375)
s = pyautogui.screenshot(region=area)
colorTile = (37, 115, 193)
bgColor = (43, 135, 209)
white = (255,255,255)
for i in range(1,69):
    r = bgColor
    lines = 0
    x = 0
    length = 0
    start = 0
    while x<375:
        pixel = s.getpixel((x,10))
        if start !=0 and pixel == bgColor and r!=bgColor and length==0:
            length = x-start
        if  pixel==bgColor and start==0:
            start = x
        if pixel != r and pixel!=bgColor:
            lines +=1
        r=s.getpixel((x,10))
        x +=1
    x=10
    click = [[False]*lines for _ in range(1,lines+1)]
    line =0
    while line<lines:
        y=10
        row =0
        while row<lines:
            pixel = s.getpixel((x,y))
            if pixel == white:
                click[line][row] = True
            y+=length
            row +=1
        x +=length
        line +=1
    time.sleep(1)
    line = 0
    x=10
    while line<lines:
        y=10
        row = 0
        while row<lines:
            if click [line][row] == True:
                pyautogui.click((x+2385-10,y+285-10))
            y +=length
            row +=1
        x +=length
        line +=1
    time.sleep(2)
    s = pyautogui.screenshot('petros.png',region=area)
    

