from dotenv import load_dotenv
from flask import request, jsonify
from . import chat_bp
from groq import Groq

load_dotenv()


# Initialize Groq client (adjust as needed for environment variables)
client = Groq(api_key='YOUR_API_KEY')

@chat_bp.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    
    # Send the message to Groq and get response
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": user_message}],
        model="llama3-8b-8192"
    )
    
    reply = response.choices[0].message.content
    return jsonify({"reply": reply})
