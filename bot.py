from twilio.rest import Client
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

# authenticate twilio account
sid = 'ACdba8ef83477eac5a6cf5a0f6aec8360f'
authToken = 'aa9bc8f833c1e20b303475d9d6c32c1a'
client = Client(sid, authToken)

message = client.messages.create(to='whatsapp:+919061735329',
                                 from_='whatsapp:+14155238886',
                                 body='This is from Carolene')


app = Flask(__name__)
@app.route('/twilio-webhook', methods=['POST'])
def twilio_webhook():
    user_msg = request.values.get('Body', '').lower()
    response = bot(user_msg)
    return str(response)


# logic of the response
def bot(user_msg):
    # Creating object of MessagingResponse
    response = MessagingResponse()
    msg = response.message()
    msg.body('this is what you said:'+ user_msg)


    return str(response)