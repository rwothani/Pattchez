from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    # Here you can add logic to handle the user message
    # For now, let's just echo the message back
    response = {'message': f'You said: {user_message}'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
