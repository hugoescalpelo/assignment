# OpenCV documentation
OpenCV is a library that provides real-time optimized Computer Vision.

## Instalation instructions

In this case, OpenCV is not installed directly because is a dependency of deepface.

Regardless, it can be installed via PIP with the following command, but is not recommended due to posible compatibility issues.
```
pip install opencv-python
```

## Dynamic miniature

OpenCV is used in the **get-face.py** program, wich is a small program used to extract the resulting image of faces that shows similarity with the captured picture by the main App.

To run this program, locate a terminal in the following path inside this repository ```data-visualization/OpenCV/``` 

This program needs the path to the image to be extracted and the coordinates that defines the face found. The syntax of the command is:
```
python3 get-face.py [img_path] [x_min] [x_max] [y_min] [y_max]
```
This program uses a picture located in **/deepface/samples/** path. The example comand is bellow. Change the USER value for your user name.
```
python3 get-face.py /home/hugo/Documents/GitHub/data-visualization/deepface/samples/picasso.png 180 320 50 300
```
Resulting image is stored in ```/temp``` folder named processed_image.jpg.

![](https://github.com/hugoescalpelo/data-visualization/blob/main/deepface/samples/processed_image.jpg?raw=true)

## Batch miniature

OpenCV is used in the **get-minis.py** program, wich is a small program used to generate the miniatures with the extracted faces of each subject in the facial database.

Change the value of ```input_path``` variable to the target facial database folder in order to generate miniatures. 

Run the program with the following command.
```
python3 get-minis.py
```