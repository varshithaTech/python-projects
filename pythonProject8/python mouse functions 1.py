import pyautogui
import time
time.sleep(8)
pyautogui.mouseDown(300,400,button="left")
pyautogui.moveTo(800,400,3)
pyautogui.mouseUp()
pyautogui.moveTo(1000,400,3)

