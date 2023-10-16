# OpenCV documentation
OpenCV is a library that provides real-time optimized Computer Vision.

## Instalation instructions

In this case, OpenCV is not installed directly because is a dependency of deepface.

Regardless, it can be installed via PIP with the following command, but is not recommended due to posible compatibility issues.
```
pip install opencv-python
```

## Testing

OpenCV is used in the **get-face.py** program, wich is a small program used to extract the resulting image of faces that shows similarity with the captured picture by the main App.

To run this program, locate a terminal in the following path inside this repository ```data-visualization/OpenCV/``` 

This program needs the path to the image to be extracted and the coordinates that defines the face found. The syntax of the command is:
```
python3 get-face.py [img_path] [x_min] [x_max] [y_min] [y_max]
```
The example comand is bellow. Change the USER value for your user name.
```
python3 get-face.py /home/hugo/Documents/GitHub/data-visualization/deepface/picasso.png 100 150 100 200
```
Resulting image is stored in ```/temp``` folder named processed_image.jpg.
