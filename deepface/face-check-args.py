# Import libraries
from deepface import DeepFace
import pandas as pd
import random
import time
import argparse

verbose=False
# Parser
parser = argparse.ArgumentParser()
parser.add_argument("img_src", help="Image to find in face database")
parser.add_argument("db_path", help="Path to face database")
args = parser.parse_args()

### Inicio del programa
df = DeepFace.find (img_path = args.img_src, db_path = args.db_path, enforce_detection = "false")
#print (df)
#json_view = df.to_json(orient="index")
#json_view = df.to_json()
df = pd.concat(df, ignore_index=True)
json_view = df.to_json()
print (json_view)
