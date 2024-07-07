import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

api_keys = {
    "OPENAI_API_KEY_1": os.getenv("OPENAI_API_KEY_1"),
    "OPENAI_API_KEY_2": os.getenv("OPENAI_API_KEY_2")
}

def test_openai_api(api_key):
    openai.api_key = api_key
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Say this is a test"}
            ]
        )
        print(f"API Key is working. Response: {response['choices'][0]['message']['content'].strip()}")
    except Exception as e:
        print(f"Error with API Key {api_key[:5]}****: {e}")

if __name__ == "__main__":
    for key_name, api_key in api_keys.items():
        print(f"Testing {key_name}...")
        test_openai_api(api_key)
