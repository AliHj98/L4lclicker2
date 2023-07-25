import pyautogui

x = 0

while x  < 3 :
  pyautogui.moveTo(620,725,1) #move to first 
  pyautogui.PAUSE = 0.2

  pyautogui.click()  #open first post
  pyautogui.PAUSE = 0.2

  pyautogui.moveTo(1023,600,1) #move to first like
  pyautogui.PAUSE = 5

  pyautogui.click()  #like post
  pyautogui.PAUSE = 1

  pyautogui.moveTo(1342,205,1) #move to close tab
  pyautogui.PAUSE = 0.2

  pyautogui.click()  #close tab
  pyautogui.PAUSE = 0.2

  pyautogui.moveTo(608,680,1) #confirm first 
  pyautogui.PAUSE = 0.2

  pyautogui.click()  #confirm 1
  pyautogui.PAUSE = 0.2

  pyautogui.moveTo(862,723,1) #move to second 
  pyautogui.PAUSE = 0.2

  pyautogui.click()  #click
  pyautogui.PAUSE = 0.2

  pyautogui.moveTo(1023,600,1) #move to second like
  pyautogui.PAUSE = 5

  pyautogui.click()  #like post
  pyautogui.PAUSE = 0.2

  pyautogui.moveTo(1342,205,1) #move to close tab
  pyautogui.PAUSE = 0.2

  pyautogui.click()  #close tab
  pyautogui.PAUSE = 0.2

  pyautogui.moveTo(860,680,1) #move to confirm second
  pyautogui.PAUSE = 0.2

  pyautogui.click()  #confrim
  pyautogui.PAUSE = 0.2
  x=x+1




