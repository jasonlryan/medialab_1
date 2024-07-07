from dotenv import load_dotenv
import os
import openai

from flask import Flask, render_template, request, Response, stream_with_context
from scenario_planning_chatbot import ScenarioPlanningChatbot
import json
import logging

load_dotenv()  # This loads the variables from .env

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

try:
    chatbot = ScenarioPlanningChatbot()
except ValueError as e:
    app.logger.error(f"Error initializing chatbot: {e}")
    chatbot = None

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    if not chatbot:
        app.logger.error('Chatbot not initialized. Check API key.')
        return Response(json.dumps({'error': 'Chatbot not initialized. Check API key.'}), content_type='application/json')

    user_message = request.json['message']
    app.logger.info(f"Received message: {user_message}")
    
    def generate():
        try:
            for token in chatbot.handle_input_stream(user_message):
                app.logger.debug(f"Yielding token: {token}")
                yield f"data: {json.dumps({'token': token})}\n\n"
        except Exception as e:
            app.logger.error(f"Error in generate: {e}")
            yield f"data: {json.dumps({'token': f'Error: {str(e)}'})}\n\n"

    return Response(stream_with_context(generate()), content_type='text/event-stream')

if __name__ == "__main__":
    app.run(port=5001, debug=True)
