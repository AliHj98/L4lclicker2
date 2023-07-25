import pyautogui
import time
pyautogui.FAILSAFE = True #Move mouse to top left to active failsafe
x = 0

while x  < 100 :

  #CYCLE 1

  pyautogui.moveTo(620,725,1) #move to first 
  pyautogui.PAUSE = 1

  pyautogui.click()  #open first post
  pyautogui.PAUSE = 2
  

  time.sleep(4)
  y = pyautogui.locateOnScreen('likeinsta.png') #locate first like
  if y != None :
    y1 = pyautogui.center(y) #center mouse
    
    pyautogui.click(y1) #like first post

    pyautogui.moveTo(1342,205,1) #move to close tab
    pyautogui.PAUSE = 0.2

    pyautogui.click()  #close tab
    pyautogui.PAUSE = 0.2
    pyautogui.moveTo(608,680,1) #confirm first 
    pyautogui.PAUSE = 0.2

    pyautogui.click()  #confirm 1
    pyautogui.PAUSE = 0.2



  else:
    
    pyautogui.moveTo(1342,205,1) #move to close tab
    pyautogui.PAUSE = 0.2
    pyautogui.click()  #close tab
    pyautogui.PAUSE = 1

    pyautogui.moveTo(608,680,1) #confirm first 
    pyautogui.PAUSE = 0.2
    pyautogui.click()  #confirm 1
    pyautogui.PAUSE = 0.2
  
    pyautogui.moveTo(609,694, 0.5) #report problem
    pyautogui.click()
    pyautogui.moveTo(745,520,0.5) #broken link
    pyautogui.click()
    pyautogui.moveTo(1146,780,0.5) #report 
    pyautogui.click()

    


  
  #CYCLE 2

  pyautogui.moveTo(863,726,1) #move to second 
  pyautogui.PAUSE = 1

  pyautogui.click()  #open second post
  pyautogui.PAUSE = 2
  

  time.sleep(4)
  z = pyautogui.locateOnScreen('likeinsta.png') #locate second like
  if  z !=None :
    z1 = pyautogui.center(z) #center mouse

    pyautogui.click(z1) #like second post

    pyautogui.moveTo(1342,205,1) #move to close tab
    pyautogui.PAUSE = 0.2
    pyautogui.click()  #close tab
    pyautogui.PAUSE = 0.2

    pyautogui.moveTo(861,680,1) #confirm first 
    pyautogui.PAUSE = 0.2

    pyautogui.click()  #confirm 1
    pyautogui.PAUSE = 0.2


  else :

    pyautogui.moveTo(1342,205,1) #move to close tab
    pyautogui.PAUSE = 0.2
    pyautogui.click()  #close tab
    pyautogui.PAUSE = 1

    pyautogui.moveTo(608,680,1) #confirm first 
    pyautogui.PAUSE = 0.2
    pyautogui.click()  #confirm 1
    pyautogui.PAUSE = 0.2

    pyautogui.moveTo(863,694, 0.5) #report problem
    pyautogui.click()
    pyautogui.moveTo(745,520,0.5) #broken link
    pyautogui.click()
    pyautogui.moveTo(1146,780,0.5) #report 
    pyautogui.click()
    



  x=x+1




