# Project Name
CAR DIRTINESS AND DAMAGE DETECTION WITH SPECIFICATION

# Purpose
Car maintenance is really a hectic task when it comes to waiting for longer duration hence we can automate this task by recommending users based on their car condition

# Requirements
- Tensorflow
- Flask
- PIL
- matplotlib
- requests
- scipy
- torch
- pandas

# How to run this code
```
git clone https://github.com/Mak-3/Car-Dirtiness-and-Damage-detection
cd Car-Dirtiness-and-Damage-detection
python flask_app.py
open in localhost
```

# output
![Screenshot (14)](https://user-images.githubusercontent.com/75625675/212541145-287ca291-f6ef-4f7b-8e09-f379cb03f828.png)
![Screenshot (24)](https://user-images.githubusercontent.com/75625675/212541862-b306dca6-2b0d-4969-9967-e598c29597e8.png)
![Screenshot (28)](https://user-images.githubusercontent.com/75625675/212541874-a0a5292f-84cb-4197-b640-bf7c9f60b242.png)

# Types of output
YOLOv5 will return image if damaged with bounding boxes namely of 4 possibilities 
- Scratch
- Glass broken
- Deformation
- Broken

VGG16 will return output in String format in the cmd as either "messy" or "clean"
