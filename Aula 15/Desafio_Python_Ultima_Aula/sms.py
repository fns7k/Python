# Criar um programa em Python que mande SMS automaticamente
# pip install twilio
# pip install python-dotenv
#   // senha
import os
from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='',
  to='+',
  body='oi'
)

print(message.sid)