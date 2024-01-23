import time
import pyautogui

time.sleep(2.5)
x, y = pyautogui.position() 
print(f'A posição atual do mouse é ({x}, {y})')
