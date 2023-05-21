from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from chatbot.twilio_chatgpt import chatbot_response, send_message
app = Flask(__name__)

@app.route('/')
def index():
    return 'All is well'

@app.route('/twilio/receiveMessage', methods=['POST'])
def receiveMessage():
    try:
        # Extract incomng parameters from Twilio
        message = request.form['Body']
        sender_id = request.form['From']
        # Get response from Openai
        result = chatbot_response(message)
        if result['status'] == 1:
            print(result)
            print(sender_id)
            send_message(sender_id, result['response']['content'])
        else:
            print('chatgpt error')
    except:
        pass
    return 'OK', 200

