import argparse
import io
import os
from PIL import Image
import torch
from flask import Flask, render_template, request, redirect
from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input
import numpy as np
from tensorflow.keras.models import load_model
from flask import Flask, render_template, request, redirect, flash, url_for
import urllib.request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if not file:
            return
        img_bytes = file.read()
        img = Image.open(io.BytesIO(img_bytes))
        results = model(img)  # inference
        results.render()  # updates results.ims with boxes and labels
        Image.fromarray(results.ims[0]).save("static/images/image0.jpg")
        filename=file.filename
        img2 = image.load_img(filename, target_size=(224, 224))
        x = image.img_to_array(img2)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        model2 = load_model('vgg_model.h5')
        preds = model2.predict(x)
        result = preds[0][0]
        image1 = Image.open('static/images/image0.jpg')
        image2 = Image.open('static/images/screenshot.jpg')
        image1_size = image1.size
        image2_size = image2.size
        new_image = Image.new('RGB',(3*image2_size[0],image2_size[1]), (250,250,250))
        new_image.paste(image1,(0,0))
        new_image.paste(image2,(image1_size[0],0))
        new_image.save("static/images/merged_image.jpg","JPEG")
        if result < preds[0][1]:
            print("messy")
        else:
            print("clean")
        
        return redirect("static/images/merged_image.jpg")

    return render_template("index.html")

@app.route('/bookappt')
def bookappt():
    return render_template('bookappt.html')

@app.route('/regform')
def regform():
    return render_template('regform.html')

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Flask app exposing yolov5 models")
    parser.add_argument("--port", default=5000, type=int, help="port number")
    args = parser.parse_args()

    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)  # force_reload = recache latest code
    model.eval()

    app.run(host="0.0.0.0", port=args.port)  # debug=True causes Restarting with stat