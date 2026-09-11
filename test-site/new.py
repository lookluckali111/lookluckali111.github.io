import pyautogui as gui
import time

massage = input("payam ro benevis")
number = input("shomare talaphone")

time.sleep(5)

for i in range(int(number)):
    gui.typewrite(massage)
    gui.press("Enter")