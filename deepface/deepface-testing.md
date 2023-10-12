# Deepface testing

In this document you will find how to test deepface.

## Requirements
1. Deepface needs to be installed, you can find instructions in the [deepface-documentation.md](https://github.com/hugoescalpelo/data-visualization/blob/main/deepface/deepface-documentation.md) file in this repository.

2. This examples were tested using Visual Studio Code, you can find instructions to install it and set it up in the [visualstudiocode-documentation.md](https://github.com/hugoescalpelo/data-visualization/blob/main/VisualStudioCode/visualstudiocode-documentation.md) file.

## Warning!
This examples need to download the analysis models the first time they run. A download will be performed, so you need Internet connection. The download size is 500Mb to 1GB per test.

Download an execution time will vary depending on your PC technical capabilities and speed connection.

## Facial attribute analysis

This program analyzes a picture with Hugo Escalpelo face in *samples* folder and returns age, face coordinates, gender, race and emotion.

You need to update the value of *img_path* variable to the path of the image in this repository in your system, since relative directories are not implemented and different systems may use diferent directory structure.

Open the [facial-analysis.py](https://github.com/hugoescalpelo/data-visualization/blob/main/deepface/facial-analysis.py) program with **Visual Studio Code** and then clic in the **Run** icon or run it in a terminal where the .py is, using the following command.
```
python3 facial-analysis.py
```
Result is a JSON describing age, face coordinates, gender, race and emotion.
```
Analysis results are: 
[
   {
      "age":30,
      "region":{
         "x":195,
         "y":130,
         "w":254,
         "h":254
      },
      "gender":{
         "Woman":0.18008240731433034,
         "Man":99.81991648674011
      },
      "dominant_gender":"Man",
      "race":{
         "asian":42.49655261615232,
         "indian":7.832079102520889,
         "black":3.5013476610986984,
         "white":14.457813767064438,
         "middle eastern":6.8431023861826885,
         "latino hispanic":24.86910223180665
      },
      "dominant_race":"asian",
      "emotion":{
         "angry":3.6864694207906723,
         "disgust":0.0007324741545744473,
         "fear":2.8725260868668556,
         "happy":20.290490984916687,
         "sad":1.7638105899095535,
         "surprise":0.4909480456262827,
         "neutral":70.89502215385437
      },
      "dominant_emotion":"neutral"
   }
]
```
## Face Check

This program compares two pictures with Hugo Escalpelo face in *samples* folder and returns states if the person in both pictures are the same.

You need to update the value of *img1_path* and *img2_path* variables to the path of the images in this repository in your system, since relative directories are not implemented and different systems may use diferent directory structure.

Open the [face-check.py](https://github.com/hugoescalpelo/data-visualization/blob/main/deepface/facial-analysis.py) program with **Visual Studio Code** and then clic in the **Run** icon or run it in a terminal where the .py is, using the following command.
```
python3 face-check.py
```
Result is a JSON describing similarity
```
Results
{
   "verified":true,
   "distance":0.04372681046238813,
   "threshold":0.4,
   "model":"VGG-Face",
   "detector_backend":"opencv",
   "similarity_metric":"cosine",
   "facial_areas":{
      "img1":{
         "x":195,
         "y":130,
         "w":254,
         "h":254
      },
      "img2":{
         "x":99,
         "y":48,
         "w":148,
         "h":148
      }
   
```

