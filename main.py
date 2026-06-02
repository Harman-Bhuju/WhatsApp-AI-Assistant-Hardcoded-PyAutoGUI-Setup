from dotenv import load_dotenv
import pyautogui

load_dotenv

while True:
     a = pyautogui.position() 
     print(a)