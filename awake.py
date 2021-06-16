import time
import pyautogui


def main():
    counter: int = 0
    while(True):
        x, y = pyautogui.position()
        time.sleep(1)
        x1, y1 = pyautogui.position()
        if x1 == x and y1 == y:
            counter += 1
        else:
            counter = 0
        while(counter > 5) :
            pyautogui.move(100, 0, duration=1, tween=pyautogui.easeInOutQuad)
            pyautogui.moveTo(x, y, duration=1, tween=pyautogui.easeInOutQuad)
            counter = 0