import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch the API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')

# Print the raw API key to check its content
print(f"Raw API Key from os.getenv: {api_key}")

# Check for invisible characters
print(f"API Key length: {len(api_key)}" if api_key else "API Key not found")

# Ensure there are no hidden characters
if api_key:
    if ' ' in api_key or '\n' in api_key or '\t' in api_key:
        print("Warning: API Key contains invisible characters")

if not api_key:
    raise ValueError("OpenAI API key not found.")
else:
    print("OpenAI API Key is correctly formatted")
