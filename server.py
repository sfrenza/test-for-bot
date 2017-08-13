# coding: utf-8

import warnings
import os
from flask import Flask, request
import json
#import psycopg2
from configparser import ConfigParser

from flask import Flask
from flask import request
from flask import make_response
from flask import render_template

#import chatbot
#import messenger

app = Flask(__name__)

#PAT = 'EAACVleRe26oBAJverSWgEZB1PKZAwcmBZAJwfowPNoaXWdkL8hS7Dc31VEQ5DeZAMUKxC3V9GFgLpgFZABm3XtCWUAZCqbzsZBQ4WR9itFs9mw2B37XID9Na4k2bcjjFtaCIRR2ZAgWUmkDRMyPIUnWi3dM4thsNpMUphtzOSIRGNQZDZD'
bot = None



@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/doschatbot')
def doschatbot():
    return render_template('page.html')

@app.route('/doschatbot2')
def doschatbot2():
    return render_template('page2.html')

@app.route('/aribaticket')
def doschatbot3():
    return render_template('page3.html')

@app.route('/kb')
def doschatbotkb():
    return render_template('page4.html')

@app.route('/ariba')
def doschatbotariba():
    return render_template('page5.html')

@app.route('/webhook', methods=['GET'])
def handle_verification():
  print("Handling Verification.")
  if request.args.get('hub.verify_token', '') == 'hola-mundo':
    print("Verification successful!")
    return request.args.get('hub.challenge', '')
  else:
    print("Verification failed!")
    return 'Error, wrong validation token'


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    # connect()
    intent = req["result"]["metadata"]["intentName"]
    print(intent)

    print("Request:")
    print(json.dumps(req))

    res = makeWebhookResult()

    res = json.dumps(res, indent=4)

    print(res)
    r = make_response(res)

    r.headers['Content-Type'] = 'application/json'

    return r



if __name__ == '__main__':
    # Suppress nltk warnings about not enough data
    warnings.filterwarnings('ignore', '.*returning an arbitrary sample.*',)

    app.run(port=3000, debug=True)
    