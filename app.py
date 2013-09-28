from flask import Flask
from flask import request
from credentials import account_id, token_id
from twilio.rest import TwilioRestClient
from flask.ext.pymongo import PyMongo
from flask import render_template
import parsedatetime as pdt

app = Flask(__name__)
app.config['DEBUG'] = True
mongo = PyMongo(app)
c = pdt.Constants()
p = pdt.Calendar(c)

@app.route("/")
def index():
        return render_template('index.html')

@app.route('/msg', methods=['POST'])
def receive_msg():
    number = request.args.get('From', None)
    message = request.args.get('Body', None)
    datetime = p.parse("message")
    
    return "Hello"

if __name__ == "__main__":
	app.run()
