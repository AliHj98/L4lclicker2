
import pyautogui
import time

x = 0

while x  < 1 :
  pyautogui.moveTo(620,725,1) #move to first 
  pyautogui.PAUSE = 1

  pyautogui.click()  #open first post
  pyautogui.PAUSE = 2
  

  time.sleep(3)
  y = pyautogui.locateOnScreen('likeinsta.png') #locate first like
  y1 = pyautogui.center(y) #center mouse

  pyautogui.click(y1) #like first post

  

  x= x+1