# Deepface documentation

Deepface is a lightweight face recognition and facial attribute analysis (age, gender, emotion and race) framework for python.

In this project, will be used for facial recognition in a database of 40 people.

## Instructions

### Requirements
Deepface needs Python 3 and PIP. Check it with the following instructions.
```
python3 --version
pip --version
```
I f you dont have it, you can install it with the following commands.
```
sudo apt install python3
sudo apt install python3-pip
```

### Install deepface

In order to install deepface, use the following command.
```
pip install deepface
```
Now you can import deepface library in a Python program.
```
from deepface import DeepFace
```
### MQTT
THe program used to integrate deepface results into an App uses MQTT to send results. Lthe library used is [paho-mqtt](https://pypi.org/project/paho-mqtt/). To install it, run the following commad.
```
pip install paho-mqtt
```
### CUDA

Deepface is compatible with CUDA, its usage is optional. You can find instructions to set it up in the [cuda-toolkit-instructions.md](https://github.com/hugoescalpelo/data-visualization/blob/main/CUDA/cuda-toolkit-instructons.md) file in this repository.
## Testing
 
 Sample funciton tests are in [deepface-testing.md](https://github.com/hugoescalpelo/data-visualization/blob/main/deepface/deepface-testing.md) file in this repository.

## Reference

- [serengil/deepface Github](https://github.com/serengil/deepface).