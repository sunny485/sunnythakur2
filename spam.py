import pyautogui
import time
time.sleep(5)
with open("sut.txt") as f:
    pyautogui.typewrite(f.read())
    pyautogui.press("enter")
