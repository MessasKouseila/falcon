#!/usr/bin/env python2
# coding: utf-8

from flask import Flask, request, jsonify
from urllib import urlopen
from pandas.compat import StringIO
from werkzeug.utils import secure_filename
import Image
import json
import os
import sys
import subprocess
import signal
import socket
import time
import datetime
from datetime import timedelta
import tensorflow as tf
from collections import OrderedDict


# renvoie l'ip sur lequel est executé le scripte.
def getIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("gmail.com", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

TF_PATH = "../falcon/tensorFlow/"
# on recupere le repertoir courrant
current_directory = os.getcwd()

UPLOAD_FOLDER = "../falcon/images/"
LOCAL_IMAGE = "/dev/shm/mjpeg/cam.jpg"
PATH_IMAGE = LOCAL_IMAGE

# on cree une appllication flask
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def uploadPhoto():
    url = "http://10.3.141.1:8000/html/cam_pic.php"
    formats = {'image/jpeg': 'JPEG', 'image/png': 'PNG', 'image/gif': 'GIF'}

    response = urlopen(url)
    image_type = response.info().get('Content-Type')
    
    try:
        format = formats[image_type]
    except KeyError:
        raise ValueError('Not a supported image format')

    file = StringIO(response.read())
    img = Image.open(file)

    filename = secure_filename(url.rpartition('/')[-1])
    filename = filename + ".jpeg"
    img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename), format=format)

    image_path = UPLOAD_FOLDER + filename
    return image_path

@app.route('/localPhoto', methods=['GET', 'POST'])
def localPhoto():
    print("Appelle local")
    photo(LOCAL_IMAGE)
    
@app.route('/photo', methods=['GET', 'POST'])
def photo(image = None):
    print("Appelle distant")
    PATH = ""
    result = {'banane' : 0, 'chaise' : 0, 'chaussure' : 0, 'main' : 0, 'smartphone' : 0}
    if image == None:
        PATH = uploadPhoto()
    else:
        PATH = image

    image_data = tf.gfile.FastGFile(PATH, 'rb').read()

    # holt labels aus file in array 
    label_lines = [line.rstrip() for line 
                    in tf.gfile.GFile(TF_PATH + "tf_files/retrained_labels.txt")]
    # !! labels befinden sich jeweils in eigenen lines -> keine aenderung in retrain.py noetig -> falsche darstellung im windows editor !!
                    
    # graph einlesen, wurde in train.sh -> call retrain.py trainiert
    with tf.gfile.FastGFile(TF_PATH + "tf_files/retrained_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')	

    with tf.Session() as sess:
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        predictions = sess.run(softmax_tensor, \
                {'DecodeJpeg/contents:0': image_data})
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

        # output
        for node_id in top_k:
            human_string = label_lines[node_id]
            score = predictions[0][node_id]
            result[human_string] = score
        result_final = {}
        for i in result:
            result_final[i] = round(result[i] * 100, 2)
        result_final = OrderedDict(sorted(result_final.items(), key=lambda t: t[1]))
        find = result_final.popitem()

    return jsonify(results="TF : " + str(find[0]))

if __name__ == "__main__":
    app.run(host=getIp(), port=4522, debug=True)
