import pyautogui as h
import time
print("Welcome to the simple Python Googler")
x = input("Please enter what would you like to Google about? ")
time.sleep(2)
h.click(1254,66)
h.typewrite("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
h.press("enter")
time.sleep(0.5)
h.hotkey("alt", "space")
h.typewrite("Notepad")
time.sleep(0.5)
h.press("enter")
time.sleep(1.5)
h.typewrite("The power of Python")
h.press("enter")
h.typewrite("Got em")
h.press("enter")
h.press("enter")
h.typewrite("Okie now for the actual Google Result : ")
time.sleep(5)
h.hotkey("alt", "space")
h.press("backspace")
h.typewrite(x)
time.sleep(1.5)
h.press("enter")
print("Volla!")