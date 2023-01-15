# Project Name
CAR DIRTINESS AND DAMAGE DETECTION WITH SPECIFICATION

# Purpose
Car maintenance is really a hectic task when it comes to waiting for longer duration hence we can automate this task by recommending users based on their car condition

# Requirements
**Tensorflow
**Flask
**PIL
**matplotlib
**requests
**scipy
**torch
**pandas

# How to run this code
git clone https://github.com/Mak-3/Car-Dirtiness-and-Damage-detection
cd Car-Dirtiness-and-Damage-detection
python flask_app.py
open in localhost

#output
![Screenshot (14)](https://user-images.githubusercontent.com/75625675/212541145-287ca291-f6ef-4f7b-8e09-f379cb03f828.png)
![Screenshot (24)](https://user-images.githubusercontent.com/75625675/212541152-bbc39b55-5b8d-47fa-88c3-e5852806c2a8.png)
![Screenshot (28)](https://user-images.githubusercontent.com/75625675/212541165-32d3aca4-882d-4c27-a18c-aef2c9c79ece.png)

# Types of output
YOLOv5 will return image if damaged with bounding boxes namely of 4 possibilities 
**Scratch
**Glass broken
**Deformation
**Broken

VGG16 will return output in String format in the cmd as either "messy" or "clean"
