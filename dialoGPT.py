from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def main():
    print("Loading model and tokenizer, please wait...")
    tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
    model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-small")

    chat_history_ids = None

    print("Chatbot ready! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # ✅ Rule-based custom responses
        if any(greet in user_input.lower() for greet in ["good morning", "morning", "gm"]):
            print("Bot: Good morning! How can I help you today?")
            continue
        elif "your name" in user_input.lower():
            print("Bot: I'm a chatbot powered by AI.")
            continue
        elif any(farewell in user_input.lower() for farewell in ["bye", "goodbye", "see you"]):
            print("Bot: Goodbye! Have a great day.")
            continue
        elif any(greet in user_input.lower() for greet in ["hello", "hi", "hey"]):
            print("Bot: Hello! How can I assist you today?")
            continue

        # Encode the user input and add end-of-string token
        new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')

        # Append to chat history if exists (maintain context)
        bot_input_ids = torch.cat([chat_history_ids, new_input_ids], dim=-1) if chat_history_ids is not None else new_input_ids

        # Generate a response (AI)
        attention_mask = torch.ones(bot_input_ids.shape, dtype=torch.long)
        chat_history_ids = model.generate(
            bot_input_ids,
            attention_mask=attention_mask,
            max_length=1000,
            pad_token_id=tokenizer.eos_token_id
        )

        # Decode the output to text and skip special tokens
        bot_response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)

        print("Bot:", bot_response)

if __name__ == "__main__":
    main()
