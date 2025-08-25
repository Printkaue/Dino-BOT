import pyautogui
import time
import keyboard

for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

x, y = 895, 236
w, h = 30, 15


while True:
   
    screenshot = pyautogui.screenshot(region=(x, y, w, h))
    pixel = screenshot.getcolors(w*h)
    
    for count, color in pixel:
        if color != (32, 33, 36):
            keyboard.press_and_release("space")
            
        print(color)
    time.sleep(0.01)
