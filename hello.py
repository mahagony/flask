#!/usr/bin/env python

import socket
from flask import Flask
app = Flask(__name__)

@app.route('/hi')
def hello_world():
    s = 'this is not working ' + socket.gethostname()
    return s

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
