import pyautogui
import time

while True: # Run in python shell 
    x, y = pyautogui.position()
    print(f"X: {x}, Y: {y}")
    time.sleep(1)
