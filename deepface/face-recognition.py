# Import Libraries
from deepface import DeepFace
import pandas as pd
import json

# Finding face
print ("Finding face")
df=pd.DataFrame();
# df = DeepFace.find(img_path = "img1.jpg", db_path = "C:/workspace/my_db")
df = DeepFace.find (img_path = "/home/hugo/Documents/GitHub/data-visualization/deepface/samples/picasso.png", db_path = "/home/hugo/Documents/GitHub/data-visualization/faces/deepface_db", enforce_detection = "false")
print ("Results ")
print (df)



