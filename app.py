from flask import Flask
from flask import request
from credentials import account_id, token_id
from twilio.rest import TwilioRestClient
from flask.ext.pymongo import PyMongo
from flask import render_template

app = Flask(__name__)
app.config['DEBUG'] = True
mongo = PyMongo(app)

@app.route("/")
def index():
        return render_template('index.html')

@app.route('/msg', methods=['POST'])
def receive_msg():
    number = request.args.get('From', None)
    message = request.args.get('Body', None)
    return "Hello"

if __name__ == "__main__":
	app.run()
