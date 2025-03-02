from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# A1000- X:  654 Y:  260
# A0100- X:  854 Y:  260
# A0010- X:  1054 Y:  260
# A0001- X:  1254 Y:  260

# B1000- X:  654 Y:  466
# B0100- X:  854 Y:  466
# B0010- X:  1054 Y:  466
# B0001- X:  1254 Y:  466

# C1000- X:  654 Y:  654
# C0100- X:  854 Y:  654
# C0010- X:  1054 Y:  654
# C0001- X:  1254 Y:  654

# D1000- X:  654 Y:  854
# D0100- X:  854 Y:  854
# D0010- X:  1054 Y:  854
# D0001- X:  1254 Y:  854



time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    print(f'clicked at x: {x} and y: {y}')


while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(654, 260)[0] < 100:
        click(654, 260)
    if pyautogui.pixel(854, 260)[0] < 100:
        click(854, 260)
    if pyautogui.pixel(1054, 260)[0] < 100:
        click(1054, 260)
    if pyautogui.pixel(1254, 260)[0] < 100:
        click(1254, 260)
    if pyautogui.pixel(654, 466)[0] < 100:
        click(654, 466)
    if pyautogui.pixel(854, 466)[0] < 100:
        click(854, 466)
    if pyautogui.pixel(1054, 466)[0] < 100:
        click(1054, 466)
    if pyautogui.pixel(1254, 466)[0] < 100:
        click(1254, 466)
    if pyautogui.pixel(654, 654)[0] < 100:
        click(654, 654)
    if pyautogui.pixel(854, 654)[0] < 100:
        click(854, 654)
    if pyautogui.pixel(1054, 654)[0] < 100:
        click(1054, 654)
    if pyautogui.pixel(1254, 654)[0] < 100:
        click(1254, 654)
    if pyautogui.pixel(654, 854)[0] < 100:
        click(654, 854)
    if pyautogui.pixel(854, 854)[0] < 100:
        click(854, 854)
    if pyautogui.pixel(1054, 854)[0] < 100:
        click(1054, 854)
    if pyautogui.pixel(1254, 854)[0] < 100:
        click(1254, 854)

