#!/usr/bin/env python
import io
import os
import re
import sys
import json
import subprocess
import requests
#import ipaddress
import logging
from bottle import route, run, request, abort, auth_basic, parse_auth

global cleared
cleared = False

def check_pass():
    auth = request.headers.get('Authorization')
    username, password = parse_auth(auth)
    auth_pass = False
    print "checking"
    if username == 'thioden':
        auth_pass = True
        cleared = True
    return auth_pass

@route("/", method=['GET', 'POST'])
def index():
    if check_pass():
        if request.method == 'GET':
            return ' Nothing to see here, move along ...'

        elif request.method == 'POST':
           
            if request.headers.get('service') == "ping":
    	        print 'HI!'	
                return  'Hi!'
            if request.headers.get('name').lower() == 'dono':
                return "Whoop Whoop, it worked"
            if request.headers.get('name').lower() != 'dono':
                return "Make the value for the name header \"dono\" "  

            if request.headers.get('service') != "push":
                print 'NoNoNONo!'
    	        print request.headers.get('test')
    	    return  "wrong event type"
    return "Go away Dono, stop spamming me"
         

run(host='10.0.1.25', port=80)
