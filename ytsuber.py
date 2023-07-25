import pyautogui
import time
pyautogui.FAILSAFE = True

x = 0

while x  < 100 :
  pyautogui.moveTo(620,725,0.5) #move to first 
  pyautogui.PAUSE = 1

  pyautogui.click()  #open first video
  pyautogui.PAUSE = 1
  
  pyautogui.moveTo(1301,208,0.5) #put to full screen
  pyautogui.PAUSE = 1

  pyautogui.click()  #full screen
  pyautogui.PAUSE = 1

  time.sleep(3)
  y = pyautogui.locateOnScreen('ytsub.png', confidence = 0.9) #locate first like

  if y != None :
    y1 = pyautogui.center(y) #center mouse

    pyautogui.click(y1) #like first post

  pyautogui.moveTo(1900,10,1) #move to close tab
  pyautogui.PAUSE = 0.2

  pyautogui.click()  #close tab
  pyautogui.PAUSE = 1

  pyautogui.moveTo(608,680,1) #confirm first 
  pyautogui.PAUSE = 0.2

  pyautogui.click()  #confirm 1
  pyautogui.PAUSE = 0.2

  pyautogui.moveTo(863,726,1) #move to second 
  pyautogui.PAUSE = 1

  pyautogui.click()  #open second post
  pyautogui.PAUSE = 2
  
  pyautogui.moveTo(1301,208,0.5) #put to full screen
  pyautogui.PAUSE = 1

  pyautogui.click()  #full screen
  pyautogui.PAUSE = 1

  time.sleep(3)
  z = pyautogui.locateOnScreen('ytsub.png', confidence = 0.9) #locate second like
  if z!=None:
    z1 = pyautogui.center(z) #center mouse

    pyautogui.click(z1) #like second post

  pyautogui.moveTo(1900,10,1) #move to close tab
  pyautogui.PAUSE = 0.2

  pyautogui.click()  #close tab
  pyautogui.PAUSE = 1

  pyautogui.moveTo(860,680,1) #move to confirm second
  pyautogui.PAUSE = 0.2

  pyautogui.click()  #confrim
  pyautogui.PAUSE = 0.2


  x=x+1