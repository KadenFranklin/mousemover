import time
import pyautogui

while True:
    x1, y1 = pyautogui.position()
    pyautogui.move(500, 0, duration=.3, tween=pyautogui.easeInOutQuad)
    x2, y2 = pyautogui.position()
    pyautogui.moveTo(x2 + 50, y2, duration=0.01, tween=pyautogui.easeInOutQuad)
    pyautogui.moveTo(x2 + 75, y2 + 43, duration=0.01, tween=pyautogui.easeInOutQuad)
    pyautogui.moveTo(x2 + 50, y2 + 86, duration=0.01, tween=pyautogui.easeInOutQuad)
    pyautogui.moveTo(x2, y2 + 86, duration=0.01, tween=pyautogui.easeInOutQuad)
    pyautogui.moveTo(x2 - 25, y2 + 43, duration=0.01, tween=pyautogui.easeInOutQuad)
    pyautogui.moveTo(x2, y2, duration=0.01, tween=pyautogui.easeInOutQuad)
    pyautogui.moveTo(x1, y1, duration=.1, tween=pyautogui.easeInOutQuad)
    time.sleep(10)
    
