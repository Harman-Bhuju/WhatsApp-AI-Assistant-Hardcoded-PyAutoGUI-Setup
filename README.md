# 🤖 WhatsApp AI Assistant (Hardcoded PyAutoGUI Setup)

## Description
An automated WhatsApp chatbot that reads incoming messages and replies naturally using the Google Gemini API. It acts as a personal assistant that chats in **Nepenglish** (a mix of simple English and casual Nepali words).

> [!WARNING]
> **Personal Project Note:** This bot relies heavily on `pyautogui` for GUI automation. It uses hardcoded screen coordinates to click and drag across WhatsApp Web/Desktop. Because of this, **it works on specific points on the screen only. This script is configured specifically for my desktop resolution and setup, and it will only work on my machine out of the box.**

## Demo
https://github.com/user-attachments/assets/101b404c-6f40-424e-bc1e-82dda6f059f9

## Features
- **Auto-Replies:** Automatically reads new messages and generates contextual replies using Gemini 2.5 Flash.
- **Nepenglish Tone:** Responds in a casual and friendly tone using words like *thik cha*, *k xa*, etc.
- **GUI Automation:** Uses `pyautogui` and `pyperclip` to navigate the screen, copy chats, and paste responses.
- **Continuous Monitoring:** Runs in a loop to detect new messages and avoid replying to messages it has already seen.

## Setup Requirements
- Python 3.x
- `google-genai` for the Gemini API
- `pyautogui` for screen automation
- `pyperclip` for clipboard manipulation
- `python-dotenv` for loading environment variables

## Environment Variables
Create a `.env` file in the root directory and add your Gemini API key:
```env
gemini_api=your_api_key_here
```

## Usage
Run the script and enter the name of the person you want to chat with when prompted:
```bash
python whatsapp_msg.py
```
*Note: You would need to update the `pyautogui.click()` coordinates in the script to match your screen layout if you want to use it on another machine.*
