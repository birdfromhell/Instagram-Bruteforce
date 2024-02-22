import pyautogui
import time

time.sleep(3)
x, y = pyautogui.position()

print(f"X coordinate: {x}")
print(f"Y coordinate: {y}")