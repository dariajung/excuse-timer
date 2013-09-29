from pymongo import MongoClient
from datetime import datetime
from twilio.rest import TwilioRestClient
from credentials import account_id, token_id
from time import sleep

client = MongoClient()
messages = client['excuse-timer'].messages
client = TwilioRestClient(account_id, token_id)

while True:
    for message in messages.find({"time":{"$lt":datetime.now()}}):
        try:
            call = client.calls.create(to=message['from'], from_='+14242299993', url='http://zencephalon.com:5000/twilio')
        except:
            print "an error occurred"
        finally:
            messages.remove(message)
        print call.sid
        print message
    sleep(60)
