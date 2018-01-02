#!/usr/bin/env python2
# coding: utf-8

from flask import Flask, session, redirect, request, url_for, render_template, jsonify

import json
import os
import sys
import subprocess
import signal
import socket
import time
import datetime
from datetime import timedelta


# renvoie l'ip sur lequel est executé le scripte.
def getIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("gmail.com", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

# on recupere le repertoir courrant
current_directory = os.getcwd()


# on cree une appllication flask
app = Flask(__name__)


# test de connexion
@app.route('/connexion', methods=['GET', 'POST'])
def connexion():
    return jsonify(results="Bienvenu dans l'interface web de falcon")


# test de connexion
@app.route('/stop', methods=['GET', 'POST'])
def stop():
    return jsonify(results="stop")

@app.route('/up', methods=['GET', 'POST'])
def up():
    return jsonify(results="up")


@app.route('/down', methods=['GET', 'POST'])
def down():
    return jsonify(results="down")



@app.route('/right', methods=['GET', 'POST'])
def right():
    return jsonify(results="right")


@app.route('/left', methods=['GET', 'POST'])
def left():
    return jsonify(results="left")

@app.route('/up_right', methods=['GET', 'POST'])
def up_right():
    return jsonify(results="up_right")


@app.route('/down_right', methods=['GET', 'POST'])
def down_right():
    return jsonify(results="down_right")



@app.route('/up_left', methods=['GET', 'POST'])
def up_left():
    return jsonify(results="up_left")


@app.route('/down_left', methods=['GET', 'POST'])
def down_left():
    return jsonify(results="down_left")

    



if __name__ == "__main__":
    app.run(host=getIp(), port=5000)
