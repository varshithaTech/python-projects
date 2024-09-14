import pyautogui
import time
#giving the python file some time before continuing
time.sleep(4)


#Mouse functions
#prints the resolution of your screen
#print(pyautogui.size())
#print(pyautogui.position())#shows the current position
#pyautogui.moveTo(100,100,3)#moves the mouse overtime (3 sec)
#pyautogui.moveRel(100,100,3)#moves the mouse to the current position


#Click functions
#it goes to the top position
# we have tripleclick(),double click(),leftclick(),rightclick().

#SCROLL FUNCTIONS
#pyautogui.scroll(-500) #scrolls down
#pyautogui.scroll(500) #scrolls up


#example mouse up and down
#pyautogui.mouseUp(300,400, button="left")
#pyautogui.mouseDown(800,400, button="left")
pyautogui.mouseDown(300,400,button="left")
pyautogui.moveTo(800,400,3)
pyautogui.mouseUp()
pyautogui.moveTo(1000,400,3)










