print("Debug: Starting scenario_planning_chatbot.py")
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch the API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')

# Debug prints to check the environment variable
print(f"Raw API Key from os.getenv: {api_key}")
if not api_key:
    raise ValueError("OpenAI API key not found.")
print("OpenAI API Key:", api_key[:5] + "..." + api_key[-5:])  # Print a truncated version of the API key for security

class ScenarioPlanningChatbot:
    def __init__(self):
        self.conversation_history = []
        openai.api_key = api_key  # Set the OpenAI API key

    def handle_input_stream(self, user_input):
        self.conversation_history.append({"role": "user", "content": user_input})
        
        messages = [
            {"role": "system", "content": "You are an AI assistant for marketing campaign scenario planning. You can help with creating new campaigns, inputting parameters, generating scenarios, and providing recommendations."},
            *self.conversation_history
        ]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            stream=True
        )

        collected_messages = []
        for chunk in response:
            if chunk['choices'][0]['delta'].get('content'):
                content = chunk['choices'][0]['delta']['content']
                collected_messages.append(content)
                yield content

        full_reply_content = ''.join(collected_messages)
        self.conversation_history.append({"role": "assistant", "content": full_reply_content})
