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
       
        if request.headers.get('test') == "ping":
	    print 'HI!'	
            return  'Hi!'
        if request.headers.get('test') != "push":
            print 'NoNoNONo!'
	    print request.headers.get('test')
	    return  "wrong event type"

         

run(host='10.0.1.25', port=80)
