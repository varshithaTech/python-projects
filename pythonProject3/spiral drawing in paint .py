import pyautogui
import time
time.sleep(5)
distance=300
# Simulate a mouse click at the current mouse pointer position
pyautogui.click()
while distance>0:
    pyautogui.dragRel(distance,0,1,button="left")#right drag
    distance=distance-20
    pyautogui.dragRel(0,distance,1,button="left")#down drag
    pyautogui.dragRel(-distance,0,1,button="left")#left drag
    distance=distance-20
    pyautogui.dragRel(0,-distance,1,button="left")#up drag