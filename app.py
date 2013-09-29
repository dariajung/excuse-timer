from flask import Flask
from flask import request
from flask import Response
from credentials import account_id, token_id
from twilio.rest import TwilioRestClient
from flask.ext.pymongo import PyMongo
from flask import render_template
import parsedatetime.parsedatetime as pdt
from time import mktime
from datetime import datetime
import twilio.twiml

app = Flask('excuse-timer')
app.config['DEBUG'] = True
mongo = PyMongo(app)
p = pdt.Calendar()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/msg')
def receive_msg():
    number = request.args.get('From', None)
    message = request.args.get('Body', None)
    (dt, hello) = p.parse(message)
    dt = datetime.fromtimestamp(mktime(dt))
    mongo.db.messages.insert({'from': number, "time": dt})

@app.route('/ad', methods=['POST'])
def save_ad():
    ad = request.form['ad']
    mongo.db.ad.insert({'ad': ad})

@app.route('/twilio', methods=['GET', 'POST'])
def text_msg():
    resp = twilio.twiml.Response()
    ad = mongo.db.ad.find_one()
    resp.say("This is your Excuse Time call. " + ad['ad'])

    return str(resp)

if __name__ == "__main__":
	app.run(host='0.0.0.0')
