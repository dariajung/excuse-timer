[excuse-timer](http://excuseti.me)
============

An app to call yourself to get out of things.

Written for the [hackNY fall 2013 hackathon.](http://hackny.org)

This app uses Python, Flask, MongoDB, and Twilio.

If you want to run this / look at code / contribute
---------

```
$ git clone git@github.com:dariajung/excuse-timer.git
$ cd /path-to/excuse-timer
$ virtualenv ENV
$ cd ENV
$ source bin/activate
$ pip install -r requirements.txt
```

How does it work?
------------------

Text __424-229-9993__ a time. You will receive a call at that time, at which you may 
feign surprise/shock/whatever emotion to get out of your obligations.


####Examples of things you can text to the app include:

* tomorrow at 11:45am
* in 5 minutes
* 5 pm PST
* 2 hours from now
* eod
* next saturday 4 pm
* 3 hours before noon

