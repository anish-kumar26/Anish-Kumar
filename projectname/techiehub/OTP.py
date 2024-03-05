from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request
import openai

app = Flask(__name__)


account_sid = 'AC221ca32b1a5350b9823cb32ceb6cecd6'
auth_token = '239ebf18d85aa398dc3aa100704ea148'
twilio_phone_number = 'whatsapp:+14155238886'

openai.api_key = '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'

@app.route('/webhook', methods=['POST'])
def webhook():
    user_input = request.form.get('Body', '').lower()

    if user_input == 'hi':
        # Generate AI response
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt="hi",
            max_tokens=150
        )
        ai_reply = response['choices'][0]['text']


        twilio_resp = MessagingResponse()
        twilio_resp.message(ai_reply)

        return str(twilio_resp)

    return "No response for this input."

if __name__ == '__main__':
    app.run(debug=True)
