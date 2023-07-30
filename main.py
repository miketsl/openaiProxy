# Import the Flask module and create an app running at http://localhost:5000
from flask import Flask, jsonify, request 
import asyncio
from EdgeGPT.EdgeGPT import Chatbot,ConversationStyle # Import the Chatbot class from EdgeGPT
app = Flask(__name__)

# OpenAI chat completion endpoint
@app.route('/v1/chat/completions', methods=['POST'])
@app.route('/chat/completions', methods=['POST'])
async def chat_completions():
    print("in chat completions")
    data=request.json
    print(data)
    messages=data.get('messages')
    prompt=""
    for message in messages:
        prompt+=f"{message['role']}: {message['content']}\n"
    # Generate a response using the ask method of the Chatbot instance 
    response = await bot.ask(prompt=prompt, conversation_style=ConversationStyle.creative, simplify_response=False) 
    messages_left = response["item"]["throttling"]["maxNumUserMessagesInConversation"] - response["item"]["throttling"].get("numUserMessagesInConversation",0)
    if messages_left == 0:
        raise Exception("Max messages reached")
    for msg in reversed(response["item"]["messages"]):
        if msg.get("adaptiveCards") and msg["adaptiveCards"][0]["body"][0].get("text"):
            message = msg
            break

    response = {
        "choices": [
            {
                "finish_reason": "stop",
                "index": 0,
                "message": {
                    "content": message["text"],
                    "role": "assistant"
                }
            }
        ],
        "created": 1677664795,
        "id": "chatcmpl-7QyqpwdfhqwajicIEznoc6Q47XAyW",
        "model": "gpt-3.5-turbo-0613",
        "object": "chat.completion",
        "usage": {
            "completion_tokens": 17,
            "prompt_tokens": 57,
            "total_tokens": 74
        }
    }
    print(response)
    return jsonify(response)

# OpenAI edit completion endpoint
#@app.route('/v1/edits', methods=['POST'])
#@app.route('/edits', methods=['POST'])
#def edits():
    #return "edits"

# OpenAI completion endpoint
#@app.route('/v1/completions', methods=['POST'])
#@app.route('/completions', methods=['POST'])
#@app.route('/v1/engines/<string:model>/completions', methods=['POST'])
#def completions():
    #return "completions"

# OpenAI models endpoint
#@app.route('/v1/models', methods=['POST'])
#@app.route('/models', methods=['POST'])
#def models(task_id):
#    return "models"

@app.route('/', defaults={'path': ''},methods=['GET','POST'])
@app.route('/<path:path>',methods=['GET','POST'])
def catch_all(path):
    json=request.json
    #headers=request.headers
    path=request.path

    return jsonify(json=json,path=path)

async def create_chatbot():
    bot = await Chatbot.create()
    return bot

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    bot=asyncio.run(create_chatbot())
    app.run(debug=True)
