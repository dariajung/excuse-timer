from flask import Flask
from credentials import account_id, token_id
from twilio.rest import TwilioRestClient
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
app.config['DEBUG'] = True
mongo = PyMongo(app)

@app.route("/")
def hello():
        return "Hello World!"

if __name__ == "__main__":
	app.run()
