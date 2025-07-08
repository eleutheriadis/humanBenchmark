import pyautogui
import time
from PIL import Image

# Define the coordinates for t and tc
t = [(50, 50), (150, 50), (300, 50), (50, 150), (150, 150), (300, 150), (50, 300), (150, 300), (300, 300)]
tc = [(2475, 335), (2585, 335), (2735, 335), (2435, 485), (2535, 485), (2685, 485), (2435, 635), (2535, 635), (2685, 635)]

# Initial click to start the process
pyautogui.click((2534, 580))
time.sleep(1)

# Define the white color and area for screenshot
white = (255, 255, 255)
area = (2385, 285, 2385 + 375, 285 + 375)  # Update coordinates to represent (left, top, right, bottom)
prev = (37, 115, 193)

# Loop for performing 68 iterations
for i in range(1, 69):
    seq = []
    for k in range(i):  # Loop to find the sequence
        found = False
        j = 0
        
        while not found:
            # Take a screenshot and use the image directly
            img = pyautogui.screenshot(region=area)
            
            # Check the pixel values
            if img.getpixel(t[j]) == white and img.getpixel(t[j]) != prev:
                if k == 0 or (k > 0 and seq[k - 1] != j):  # Ensure sequence does not repeat
                    found = True
                    seq.append(j)

            # Update previous color and increment
            prev = img.getpixel(t[j])
            j += 1
            if j > 8:
                j = 0
    
    time.sleep(1)  # Pause before clicking the sequence

    # Click the sequence found
    for j in seq:
        pyautogui.click(tc[j])
        time.sleep(0.1)  # Brief pause between clicks
