import pyautogui
import time
import pyperclip
import re
import client

def parse_messages(chat_text):
    # split text into lines, strip whitespace, and keep only non-empty lines
    lines = [l.strip() for l in chat_text.split("\n") if l.strip()]

    messages =[]

    pattern = r"\[(.*?)\]\s(.*?):\s(.*)"
    '''
    matches ->
    [time] sender: message format and extracts time, sender, and message
    '''
    # \[ (.*?) \]     → Group 1
    # \s              → space
    # (.*?):          → Group 2
    # \s              → space
    # (.*)            → Group 3

    for line in lines:
        match = re.match(pattern,line)

        # skip broken / emoji-only / system lines
        if not match:
            continue

        # list ma dict format ma haleko
        messages.append({
            "time": match.group(1),
            "sender": match.group(2),
            "text": match.group(3)

        })
    return messages

def build_history(seen_messages):

    history = ""
    for time, sender, text in seen_messages[-10:]:
        history += f"[{time}] {sender}: {text}\n"

    return history


# asks user whom to chat and copy person name
person = input("Who do you wanna chat with: ")
pyperclip.copy(person)


# click on chrome
pyautogui.click(1010,1061)
time.sleep(1)

# click on whatsapp shortcut
pyautogui.click(751,645)
time.sleep(2)

# click on login
pyautogui.click(1567,173)
time.sleep(4.5)

# click on search bar and paste the person name
pyautogui.click(206,221)
pyautogui.hotkey('ctrl','v')
time.sleep(1)

# click on person chat
pyautogui.click(313,409)
time.sleep(1)

# write and copy the 1st message
first_text = "Hello k gardai xau?"
pyperclip.copy(first_text)

# click on user chatbox
pyautogui.click(843,979)
time.sleep(1)

# paste in chatbox
pyautogui.hotkey('ctrl','v')
time.sleep(1)

# enter and click outside chatbox
pyautogui.press("enter")
time.sleep(1)
pyautogui.click(1221,927)
seen_messages = []

# select previous message to {first_text}
pyautogui.moveTo(669,224)
pyautogui.dragTo(1837,981,duration=1.0,button="left")

# copy the selected text to the clipboard and unselect text
pyautogui.hotkey('ctrl','c')
time.sleep(1)
pyautogui.click(673,224)


chat_text = pyperclip.paste()
messages = parse_messages(chat_text)

for msg in messages:

    message = (
    msg["time"],
    msg["sender"],
    msg["text"]
    )
    seen_messages.append(message)

while True:
    # copy all messages by dragging in a time of 1.2sec
    time.sleep(3)
    pyautogui.click(668,224)
    pyautogui.moveTo(669,224)
    pyautogui.dragTo(1837,981,duration=1.0,button="left")

    # copy the selected text to the clipboard and unselect text
    pyautogui.hotkey('ctrl','c')
    time.sleep(1)
    pyautogui.click(673,224)

    # paste it in a variable
    chat_text = pyperclip.paste()
    messages = parse_messages(chat_text)

    for msg in messages:

        message = (
        msg["time"],
        msg["sender"],
        msg["text"]
    )
        if message in seen_messages:
            continue
        

        seen_messages.append(message)
            

        if msg["sender"] != "Harman Bhuju":
            history = build_history(seen_messages)
            prompt = prompt = f"""
                                Conversation history:
                                {history}

                                Now reply to:
                                {msg['sender']}: {msg['text']}
                                """
            response = client.harman_assistant(prompt,person)

            pyperclip.copy(response)

            # click at chatbox
            pyautogui.click(843,979)
            time.sleep(1)

            # paste in chatbox
            pyautogui.hotkey('ctrl','v')
            time.sleep(1)

            # enter and click outside the checkbox
            pyautogui.press("enter")
            time.sleep(1)
            pyautogui.click(673,224)


        