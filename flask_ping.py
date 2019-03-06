#!/usr/bin/env python

from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

ms = 0

@app.before_request
def time_request():
  global ms
  dt = datetime.now()
  ms = dt.microsecond

@app.route("/ping", methods=["GET"])
def ping_requests():
  dt_now = datetime.now()
  time_diff = dt_now.microsecond - ms
  return jsonify({
    'message': 'pong ' + 'from ' + str(request.remote_addr) + " " + str(time_diff) + 'ms'
  })
    
app.run(host='0.0.0.0', port=8000)
                            
