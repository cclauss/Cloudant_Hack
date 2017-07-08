#!/usr/bin/env python3
# coding: utf-8

from aiohttp import web
import aiohttp_jinja2
import asyncio
import functools
import jinja2
import os
import sys
import time
import webbrowser

f'Python 3.6 or better is required'  # f-string will be a syntax error pre-3.6
START_TIME = time.time()
PORT = int(os.getenv('PORT', 8000))  # Cloud will provide a web server PORT id

# import dependencies
from flask import Flask
import inspect
import json
import os
import platform
import sys

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
    app.run(host='0.0.0.0', port=port)

    
# =================================
    
"""
try:  # Immediately change current directory to avoid exposure of control files
    os.chdir('static_parent_dir')
except FileNotFoundError:
    pass

try:  # See if the user entered a maximum packages number on the commandline
    max_pkgs = int(sys.argv[1])
except (IndexError, ValueError):
    max_pkgs = MAX_PKGS

app = web.Application()


def done_callback(fut, app=None):  # Called when PyPI data capture is complete
    app = app or {}
    elapsed = time.time() - START_TIME
    app['packages'], app['data_datetime'] = fut.result()
    fmt = ' Gathered Python 3 support info on {:,} PyPI packages in {:.2f} seconds.'
    print(fmt.format(len(app['packages']), elapsed))


fut = asyncio.run_coroutine_threadsafe(get_packages_info(max_pkgs, START_TIME),
                                       asyncio.get_event_loop())
fut.add_done_callback(functools.partial(done_callback, app=app))


async def index_handler(request):
    # try:  # return index.html if it exists
    #    with open('index.html') as in_file:
    #        return web.Response(text=in_file.read())
    # except FileNotFoundError:
    return web.Response(text='Processing: Please wait a few seconds and then refresh this page')


@aiohttp_jinja2.template('index_db.html')
async def handler(request):
    packages = request.app.get('packages')
    if not packages:  # if data capture still ongoing, default to index.html
        return await index_handler(request)
    print('len(packages): {}'.format(len(packages)))
    max_pkgs = request.match_info.get('max_pkgs', '').split('.')[0]
    max_pkgs = ''.join(c for c in max_pkgs if c.isdigit())
    max_pkgs = max(int(max_pkgs) if max_pkgs else 0, 500)
    return build_template_values(packages[:max_pkgs],
                                 request.app.get('data_datetime'))


def run_webserver(app, port=PORT):
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(os.curdir))
    app.router.add_route('GET', '/', handler)
    app.router.add_route('GET', '/{max_pkgs}', handler)
    app.router.add_static('/static/', path='./static')
    web.run_app(app, port=PORT)


async def launch_browser(port=PORT):
    asyncio.sleep(0.2)  # give the server a fifth of a second to come up
    webbrowser.open('localhost:{}'.format(port))


if PORT == 8000:  # we are running the server on localhost
    asyncio.run_coroutine_threadsafe(launch_browser(PORT), app.loop)

run_webserver(app, port=PORT)
"""
