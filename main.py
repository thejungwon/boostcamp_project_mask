from flask import Flask, render_template, request
import base64
import cv2
import numpy as np
import json
from inference import infernece

app = Flask(__name__)

def face_recognize(frame):
    cascade_file = "haarcascade_frontalface_alt2.xml"
    cascade = cv2.CascadeClassifier(cascade_file)
    img = frame
    face_list = cascade.detectMultiScale(img, minSize=(150,150))
    if len(face_list) == 0:
        return {"result":"failure"}
    for (x,y,w,h) in face_list:
        #얼굴 하나만 디텍트
        break
    return {"result":"success", "x":str(x), "y":str(y), "w":str(w), "h":str(h)}

def mask_recognize(frame):
    classes = {
        0:["Wear","Male","under 30"],
        1:["Wear","Male","between 30 and 60"],
        2:["Wear","Male","over 60"],
        3:["Wear","Female","under 30"],
        4:["Wear","Female","between 30 and 60"],
        5:["Wear","Female","over 60"],
        6:["Incorrect","Male","under 30"],
        7:["Incorrect","Male","between 30 and 60"],
        8:["Incorrect","Male","over 60"],
        9:["Incorrect","Female","under 30"],
        10:["Incorrect","Female","between 30 and 60"],
        11:["Incorrect","Female","over 60"],
        12:["Not Wear","Male","under 30"],
        13:["Not Wear","Male","between 30 and 60"],
        14:["Not Wear","Male","over 60"],
        15:["Not Wear","Female","under 30"],
        16:["Not Wear","Female","between 30 and 60"],
        17:["Not Wear","Female","over 60"],
        }

    return classes[infernece([frame])[0]]

@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/face_detect", methods=["POST"])
def face_detect():
    image_b64 = request.json['image']
    image_b64=image_b64.split(",")[1]
    binary = base64.b64decode(image_b64)
    image = np.asarray(bytearray(binary), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    data=face_recognize(image)
    return json.dumps(data)

@app.route("/mask_detect", methods=["POST"])
def mask_detect():
    image_b64 = request.json['image']
    image_b64=image_b64.split(",")[1]
    binary = base64.b64decode(image_b64)
    image = np.asarray(bytearray(binary), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    data=mask_recognize(image)
    return json.dumps(data)





if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6006, debug=True)