def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"
    elif "your name" in user_input:
        return "I am a simple chatbot."
    elif "bye" in user_input:
        return "Goodbye! Have a nice day."
    else:
        return "Sorry, I don't understand."

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    print("Bot:", chatbot_response(user_input))
