from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# X:  949 Y:  623

time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('q') == False:
        click(949, 623)
    

