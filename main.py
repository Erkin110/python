
import pyautogui 

import os
print(os.name)


print (pyautogui.position())

def download_access_con():
	pyautogui.moveTo(71, 374, 0.5)
	pyautogui.click(button='left')
	pyautogui.PAUSE = 1.5
	pyautogui.moveTo(178, 109, 0.5)
	pyautogui.click(button='left')
	pyautogui.PAUSE = 1.5
	pyautogui.moveTo(501, 111, 0.5)
	pyautogui.click(button='left')
	pyautogui.PAUSE = 1
	pyautogui.moveTo(900, 551, 0.5)
	pyautogui.click(button='left')
	pyautogui.PAUSE = 5




def statistics():
	pyautogui.moveTo(100, 450, 0.5) 
	pyautogui.click(button='left')
	pyautogui.PAUSE = 1.5
	pyautogui.moveTo(251, 71, 0.5)
	pyautogui.click(button='left')
	pyautogui.PAUSE =2
	pyautogui.moveTo(305, 112, 0.5)
	pyautogui.click(button='left')
	pyautogui.PAUSE =2
	pyautogui.hotkey('Win','Up')
	pyautogui.PAUSE =2
	pyautogui.moveTo(92, 37, 0.5)
	pyautogui.click(button='left')
	pyautogui.PAUSE = 2
	pyautogui.typewrite(["enter"])
	pyautogui.PAUSE = 5
	pyautogui.typewrite(["enter"])
	pyautogui.PAUSE = 2
	pyautogui.hotkey('alt','f4')
	print('OK')

	pass
download_access_con()
statistics()


