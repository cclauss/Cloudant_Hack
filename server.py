#!/usr/bin/env python3
# coding: utf-8

# import dependencies
from flask import Flask
import inspect
import json
import os
import platform
import sys
import time

f'Python 3.6 or better is required'  # f-string will be a syntax error pre-3.6
START_TIME = time.time()
PORT = int(os.getenv('PORT', 8000))  # Cloud will provide a web server PORT id


# bootstrap the app
app = Flask(__name__)

# set the port dynamically with a default of 3000 for local development
port = int(os.getenv('PORT', 3000))


def platform_info():
    info = [f'On {sys.platform} running Python {sys.version}\n']
    for name, value in inspect.getmembers(platform):
        if name[0] != '_' and callable(value):
            try:
                value = value()
            except (IndexError, TypeError):
                continue
            if str(value).strip("( ,')"):
                info.append('{:>21}() = {}'.format(name, value))
    info += ['\n', json.dumps(dict(os.environ), indent=2)]
    #        '\n', json.dumps(os.environ['VCAP_APPLICATION'], indent=2)]
    return '\n'.join(info)


# our base route which just returns a string
@app.route('/')
def hello_world():
    s = '<br>' * 2 + '<pre>' + platform_info() + '</pre>'
    return 'Congratulations! Welcome to the Swisscom Application Cloud.' + s


# start the app
if __name__ == '__main__':
    print("{0} Python main starts... {0}".format('!' * 10))
    app.run(host='0.0.0.0', port=port)
