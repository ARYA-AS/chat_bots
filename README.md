# 🤖 Chatbot Collection — Rule-Based and AI-Powered

This repository contains two types of chatbots written in Python. Ideal for beginners exploring both traditional rule-based logic and transformer-based AI chat systems.

---

## 🟢 1. Rule-Based Chatbot (`rule_based_chatbot.py`)

A simple chatbot that responds to greetings like "hello", "bye", and "good morning" using predefined logic.

### Features:
- Pure Python logic (no external libraries)
- Quick response using string matching
- Great as a beginner's chatbot example

---

## 🔵 2. AI + Rule-Based Chatbot (`ai_chatbot_dialoGPT/`)

This chatbot combines rule-based responses with **AI-generated replies** using Hugging Face’s [`microsoft/DialoGPT-small`](https://huggingface.co/microsoft/DialoGPT-small) model.

### Features:
- Responds instantly to greetings and common phrases using if-else logic
- Uses a powerful transformer model for general conversation
- Maintains short conversation context using chat history

### How to Run:
```bash
cd ai_chatbot_dialoGPT
pip install -r requirements.txt
python chatbot.py
