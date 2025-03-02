from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# X:  719 Y:  600 RGB: (0, 0, 0) - A
# X:  882 Y:  600 RGB: (0, 0, 0) - B
# X: 1038 Y:  600 RGB: (0, 0, 0) - C
# X: 1206 Y:  600 RGB: (0, 0, 0) - D

time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.03)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    print(f'clicked at x: {x} and y: {y}')


while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(719, 600)[0] == 0:
        click(717, 600)
    if pyautogui.pixel(882, 600)[0] == 0:
        click(880, 600)
    if pyautogui.pixel(1038, 600)[0] == 0:
        click(1036, 600)
    if pyautogui.pixel(1206, 600)[0] == 0:
        click(1204, 600)

