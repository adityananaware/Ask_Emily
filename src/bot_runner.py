# ask_emily_chatbot/src/bot_runner.py
from main import main

while True:
    user_input = input("You: ")
    response = main(user_input)
    print(f"Emily: {response}")
