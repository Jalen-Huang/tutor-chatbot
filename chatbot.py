import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def chatbot():
    messages = [{"role": "system", "content": "You are a Mathematics and Computer Science tutor. You only answer to Math and Computer Science questions"}]
    while True:
        message = input("User: ")
        if message.lower() == "quit":
            break

        messages.append({"role": "user", "content": message})
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        chat_message = completion.choices[0].message.content
        print(f"Bot: {chat_message}")
        messages.append({"role": "assistant", "content": chat_message})

if __name__ == "__main__":
    print("Chat with the Math/CS tutor bot (enter 'quit' to stop).")
    chatbot()
