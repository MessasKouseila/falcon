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
from wheelEnum import WheelEnum
from ultraSonicSensor import UltraSonicSensor
# renvoie l'ip sur lequel est executé le scripte.
def getIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("gmail.com", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


moteur = WheelEnum()
capteur = UltraSonicSensor(18, 16)

# on recupere le repertoir courrant
current_directory = os.getcwd()


# on cree une appllication flask
app = Flask(__name__)


# test de connexion
@app.route('/connexion', methods=['GET', 'POST'])
def connexion():
    capteur.start()
    return jsonify(results="Bienvenu dans l'interface web de falcon")


# fait avancé le robot pendant x secondes
@app.route('/run', methods=['GET', 'POST'])
def run():
    distance = 30
    while(distance > 10):
        moteur.LEFT_DOWN.accelerate()
        moteur.LEFT_UP.accelerate()
        moteur.RIGHT_DOWN.accelerate()
        moteur.RIGHT_UP.accelerate()
        distance = capteur.getDistance()
    # obstacle    
    moteur.LEFT_DOWN.brake()
    moteur.LEFT_UP.brake()
    moteur.RIGHT_DOWN.brake()
    moteur.RIGHT_UP.brake()

if __name__ == "__main__":
    app.run(host=getIp(), port=5000)
