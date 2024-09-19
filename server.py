# from flask import Flask, request, jsonify
# import os
# from dotenv import load_dotenv
# from groq import Groq

# app = Flask(__name__)

# load_dotenv()

# key = os.getenv("GROQ_API_KEY")
# print("The key is ", key)
# # Initialize the Groq client with your API key
# client = Groq(
#     api_key=os.getenv("GROQ_API_KEY"),
# )

# # Define the model to use
# MODEL_NAME = "llama3-8b-8192"  # Replace with your model name

# @app.route('/chat', methods=['POST'])
# def chat():
#     user_message = request.json.get('message')
    
#     try:
#         # Generate response using Groq
#         chat_completion = client.chat.completions.create(
#             messages=[{"role": "user", "content": user_message}],
#             model=MODEL_NAME,
#         )
#         response = chat_completion.choices[0].message.content
#     except Exception as e:
#         response = f"Error generating response: {str(e)}"
    
#     return jsonify({'message': response})

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask
from app.routes import auth_bp, chat_bp, journal_bp, resource_bp, playlist_bp

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(chat_bp, url_prefix='/api')
app.register_blueprint(journal_bp, url_prefix='/api')
app.register_blueprint(resource_bp, url_prefix='/api')
app.register_blueprint(playlist_bp, url_prefix='/api')

if __name__ == "__main__":
    app.run(debug=True)
