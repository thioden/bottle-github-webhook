#!/usr/bin/env python
import io
import os
import re
import sys
import json
import subprocess
import requests
import ipaddress
import logging
from bottle import route, run, request, abort


@route("/", method=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return ' Nothing to see here, move along ...'

    elif request.method == 'POST':
       
        if request.header.get('') == "ping":
            return json.dumps({'msg': 'Hi!'})
        if request.header.get() != "push":
            return json.dumps({'msg': "wrong event type"})

        repos = json.loads(io.open('repos.json', 'r').read())

        payload = request.json
        repo_meta = {
            'name': payload['repository']['name'],
            'owner': payload['repository']['owner']['name'],
        }
        

run(host='10.0.1.25', port=80, debug=debug, server=server)
