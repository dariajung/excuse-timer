from flask import Flask
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

if __name__ == "__main__":
	app.run()
