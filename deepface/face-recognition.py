# Import Libraries
from deepface import DeepFace
import pandas as pd

# Finding face
print ("Finding face")

# df = DeepFace.find(img_path = "img1.jpg", db_path = "C:/workspace/my_db")
df = DeepFace.find (img_path = "/home/hugo/Documents/GitHub/apertura-puertas-reconocimiento-facial/deepface/faces/carrie1.png", db_path = "/home/hugo/Documents/GitHub/apertura-puertas-reconocimiento-facial/deepface/my_db", enforce_detection = "false")
print ("Results ")
print (df)

# print ("Seconday similitude")
# print (df.identity[1])