import pyautogui


position = pyautogui.position()


pyautogui.click(x=1766, y=1055,interval=0.20)
pyautogui.click(x=1614, y=768, interval=0.20)
pyautogui.click(x=1766, y=1057)

pyautogui.dragTo(position)