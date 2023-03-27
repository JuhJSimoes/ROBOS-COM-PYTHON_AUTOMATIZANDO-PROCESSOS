import pyautogui
import time

"""picX, picY = pyautogui.locateCenterOnScreen('minimizar.PNG',confidence=0.8) # type: ignore
print(picX, picY)
pyautogui.click(picX, picY, duration=3)

playX, playY = pyautogui.locateCenterOnScreen('win.PNG', confidence=0.8)  # type: ignore
print(playX, playY)
pyautogui.click(playX, playY, duration=3)"""


playX, playY = pyautogui.locateCenterOnScreen('abrir_nova.PNG', confidence=0.8)  # type: ignore
print(playX, playY)
pyautogui.click(playX, playY)
time.sleep(1)


playX, playY = pyautogui.locateCenterOnScreen('google.PNG', confidence=0.8)  # type: ignore
print(playX, playY)
pyautogui.click(playX, playY)


pyautogui.typewrite('https://chat.openai.com/chat')
#pyautogui.KEYBOARD_KEYS
pyautogui.press('enter')
time.sleep(1)

playX, playY = pyautogui.locateCenterOnScreen('ChatGPT.PNG', confidence=0.8)  # type: ignore
print(playX, playY)
pyautogui.click(playX, playY)
pyautogui.press('enter')

pyautogui.typewrite('a história do fisiculturismo')
pyautogui.press('enter')
