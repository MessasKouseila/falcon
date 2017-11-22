#!/usr/bin/env python2
# coding: utf-8

from flask import Flask, session, redirect, request, url_for, render_template, jsonify

import json, os, sys, subprocess, signal, socket
import time, datetime
from datetime import timedelta


# renvoie l'ip sur lequel est executé le scripte. 
def getIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("gmail.com",80))
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


if __name__ == "__main__":
    app.run(host=getIp(), port=5000)