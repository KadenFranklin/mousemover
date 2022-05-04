import time
import pyautogui


def check_if_move(x, y):
	time.sleep(2)
	xx, yy = pyautogui.position()
	if x == xx or y == yy:
		return None
	else:
		check_if_move(xx, yy)


while True:
	x1, y1 = pyautogui.position()
	check_if_move(x1, y1)
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
