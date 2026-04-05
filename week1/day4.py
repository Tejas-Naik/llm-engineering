from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

messages = [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "Hi! I'm Tejas!"}
    ]

GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
google_api_key = os.getenv("GOOGLE_API_KEY")

gemini = OpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)

should_continue = True
while should_continue:
    user_input = input("\n\nYou: ")
    messages.append({"role": "user", "content": user_input})
    response = gemini.chat.completions.create(model="gemini-2.5-flash-lite", messages=messages)
    print("\n\nAssistant: " + response.choices[0].message.content)
    if user_input.lower() == "quit":
        should_continue = False
    else:
        messages.append({"role": "assistant", "content": response.choices[0].message.content})

print("Goodbye!")
# Memory Illusion (No model has memory or remembers previous messages)
# We can create the illusion of memory by adding the assistant's response to the messages list
# This will allow the assistant to remember the previous messages and respond accordingly
# This is a simple way to create the illusion of memory
# It is not a real memory, but it is a simple way to create the illusion of memory
# It is not a real memory, but it is a simple way to create the illusion of memory
