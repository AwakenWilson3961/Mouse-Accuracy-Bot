import pyautogui
import time
import keyboard

while keyboard.is_pressed('q') == False:
    location = pyautogui.locateCenterOnScreen('redball.png', confidence=0.7)
    if location is not None:
        print('Detected wanted object!')
        pyautogui.moveTo(location)
        pyautogui.click()
        time.sleep(0.1)
    else:
        print('Object not in sight!')
        time.sleep(0.1)
