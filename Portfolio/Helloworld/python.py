from twilio.rest import Client

account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

for i in range(20):
    message = client.messages.create(
        body='Hello, this is message number ' + str(i+1),
        from_='whatsapp:+14155238886',
        to='whatsapp:+1234567890'
    )
    print('Message sent: ' + message.sid)