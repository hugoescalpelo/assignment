# Basic CodeProject.AI testing

CodeProject.AI is an Artificial Intelligence server that containerizes some basic AI tools. Follow the [README](https://github.com/hugoescalpelo/data-visualization/blob/main/README.md) instructions to set it up.

Once you have CodeProject.AI installed, you can do some basic tests. 

Go to [localhost:32168](http://localhost:32168/). You will see the status tab, where you can check if any problem as came up.

![](https://github.com/hugoescalpelo/data-visualization/blob/main/Images/Screenshot%20from%202023-10-07%2020-33-48.png?raw=true)

## Simple tests

Clic on the **CodePoject.AI Explorer** tab. A new browser tab will be oppened. Here you can do some basic tests. 

The following assumes you have available selfies. It can be from a webcam, an IP camera or any file with a face in it.

### Face detection

In vision tab, in the Face Detection Group, clic on the Browse button and provide a picture with a face in it. Then clic on the Detect Faces button and wait for the results. Here is an example of a successful test.

![](https://github.com/hugoescalpelo/data-visualization/blob/main/Images/Screenshot%20from%202023-10-07%2020-42-29.png?raw=true)

### Face Registration

In Face tab, in the Face Registration Group, write a person's name in the field **Person's Name**, clic on the Browse button in the **Select images** field and then clic on the Register Faces button in the **Final Step** field. A person's face will be be registered and a summary will be displayed.

**Note**: there is a folder with 40 faces in this repository in [/data-visualization/faces/face_db/](). Face list was suggested by Chat GPT.

![](https://github.com/hugoescalpelo/data-visualization/blob/main/Images/Screenshot%20from%202023-10-10%2015-54-07.png?raw=true)

You can also list registered faces by clicking on the List Registered Faces in Face Registration Group.

![](https://github.com/hugoescalpelo/data-visualization/blob/main/Images/Screenshot%20from%202023-10-10%2016-00-17.png?raw=true)

### Face Recognition

In the Face tab, in the Face Recognition Group, clic on the Browse button in the **Image** field, select an image and then clic on the **Recognize** button. You can also change the confidence of the algorithm in the **Minimum Recognition Confidence** field by setting a number between 0.0 and 1.0, equivalent to 0% confidence and 100% confidence respectively.

In this example we compare Spielbergs registered face with [a second one](https://github.com/hugoescalpelo/data-visualization/blob/main/faces/test_faces/spielberg2.png).

The results are the following.

![](https://github.com/hugoescalpelo/data-visualization/blob/main/Images/Screenshot%20from%202023-10-10%2017-51-23.png?raw=true)

## Optic Character Recognition

In the Image tab, in the Optical Character Recognition Group, clic on the Browse Button in the **Image** field, select an image, and then clic con the **Read Text** button. 

In this example we compare to a [picture of me](hhttps://github.com/hugoescalpelo/data-visualization/blob/main/faces/test_faces/hugo2.jpg?raw=true)holding a white card.
![](https://github.com/hugoescalpelo/data-visualization/blob/main/faces/test_faces/hugo2.jpg?raw=true)

The result of this test looks like this.
![](https://github.com/hugoescalpelo/data-visualization/blob/main/Images/Screenshot%20from%202023-10-17%2017-42-59.png?raw=true)
**Note**:To run this test, you need to [install OCR Module](https://github.com/hugoescalpelo/data-visualization/blob/main/CodeProject.AI/ocr-settings.md) first.