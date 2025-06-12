# GeminiAPI-Chat

A simple Python app that connects to Google's **Gemini 2.0 Flash** model using an API key from a `.env` file, which contains your personal Gemini API Key.

## 💡 Features

- Loads your Gemini API key securely.
- Allows the user to send a prompt to Gemini and prints the response.
- Type `exit` to quit the chat.

## ❗ Requirements

- Python 3.7+
- `.env` file with your own Gemini API key.

# 🌱 Startup Guide
Clone this repository:
### In terminal set:
#### To use this repository
git clone https://github.com/Emilio-02/GeminiAPI-Chat.git  
cd GeminiAPI-Chat

#### Install dependencies:
pip install python-dotenv google-generativeai

#### Run the app:
python main.py

## 🛠 Setup Guide

### How to get a personal Gemini API Key?
#### First step is to create a Project in Google Cloud.
This link is where you'll Login with a google account:
https://console.cloud.google.com/projectcreate  
Next you will create a new project (if you don't have one yet).

#### Get your key! 
With this link: https://aistudio.google.com/apikey  
Click the button "Get API key" and you will obtain it!

### What to do with this key?
Now that you got your key, paste it in "insert_your_gemini_key" from the .env file.

## Autor
Emilio Fernando Vásquez Millar
