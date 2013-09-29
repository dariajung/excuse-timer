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
    (dt, hello) = p.parse(message)
    print dt
    print hello
    dt = datetime.fromtimestamp(mktime(dt))
    mongo.db.messages.insert({"from": number, "time": dt})
    return "Hello"

@app.route('/twilio', methods=['GET', 'POST'])
def call_msg():
	resp = twilio.twiml.Response()
	resp.say("Record your monkey howl after the tone.")
	esp.record(maxLength="30", action="/handle-recording")

	return str(resp)

@app.route("/handle-recording", methods=['GET', 'POST'])
def handle_recording():
    """Play back the caller's recording."""
 
    recording_url = request.values.get("RecordingUrl", None)
 
    resp = twilio.twiml.Response()
    resp.say("Thanks for recording a message. Listen to your recorded message.")
    resp.play(recording_url)
    resp.say("Goodbye.")
    return str(resp)

if __name__ == "__main__":
	app.run(host='0.0.0.0')
