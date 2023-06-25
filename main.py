# Import the Flask module and create an app running at http://localhost:5000
from flask import Flask, jsonify, request
app = Flask(__name__)

# OpenAI chat completion endpoint
@app.route('/v1/chat/completion', methods=['POST'])
@app.route('/chat/completions', methods=['POST'])
def chat_completions():
    return "chat completions"

# OpenAI edit completion endpoint
@app.route('/v1/edits', methods=['POST'])
@app.route('/edits', methods=['POST'])
def edits():
    return "edits"

# OpenAI completion endpoint
@app.route('/v1/completions', methods=['POST'])
@app.route('/completions', methods=['POST'])
@app.route('/v1/engines/<string:model>/completions', methods=['POST'])
def completions():
    return "completions"

# OpenAI models endpoint
@app.route('/v1/models', methods=['POST'])
@app.route('/models', methods=['POST'])
def models(task_id):
    return "models"

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)