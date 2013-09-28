from flask import Flask
from flask import request
from credentials import account_id, token_id
from twilio.rest import TwilioRestClient
from flask.ext.pymongo import PyMongo
from flask import render_template
import parsedatetime.parsedatetime as pdt
from time import mktime
from datetime import datetime

app = Flask(__name__)
app.config['DEBUG'] = True
mongo = PyMongo(app)
p = pdt.Calendar()

@app.route("/")
def index():
        return render_template('index.html')

@app.route('/msg')
def receive_msg():
    number = request.args.get('From', None)
    message = request.args.get('Body', None)
    print request.args
    print message
    print number
    dt = p.parse(message)
    dt = datetime.fromtimestamp(mktime(dt))
    mongo.db.messages.insert({"from": number, "time": dt})
    return "Hello"

if __name__ == "__main__":
	app.run(host='0.0.0.0')
