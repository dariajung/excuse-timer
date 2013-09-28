from pymongo import MongoClient
from datetime import datetime
from twilio.rest import TwilioRestClient
from credentials import account_id, token_id

client = MongoClient()
messages = client['excuse-timer'].messages
client = TwilioRestClient(account_id, token_id)

for message in messages.find({"time":{"$lt":datetime.now()}}):
    call = client.calls.create(to=message['from'], from_='+14242299993', url='http://excuseti.me/end_call')
    print call.sid
    print message
