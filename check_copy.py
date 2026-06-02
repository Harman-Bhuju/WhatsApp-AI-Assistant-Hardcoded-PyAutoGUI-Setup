import pyautogui
import time
import pyperclip

# click on chrome
pyautogui.click(1010,1061)
time.sleep(1)

while True:
    # select previous message to {first_text}
    pyautogui.moveTo(668,224)
    pyautogui.dragTo(1837,981,duration=1.0,button="left")

    # copy the selected text to the clipboard and unselect text
    pyautogui.hotkey('ctrl','c')
    pyautogui.click(1222,861)
    time.sleep(1)

    chat_text = pyperclip.paste()
    print(chat_text,"\n\n")