# OCR Settings
In this document you will find instructions to activate OCR module in CodeProject.AI Server. Check the instructions of the main [README.md](https://github.com/hugoescalpelo/data-visualization/blob/main/README.md) get the server running.

## Module activation

Module activation in CodeProject.AI Server is very easy.
1. Open a web browser and go to dashboard page of CodeProject.AI Server, usually [localhost:32168](http://localhost:32168/).
2. Clic on the *Install Modules* tab.
3. Find the **Optical Character Recognition** module and clic on **Install** button. This will instal the module. Ypu can check progress in **Status** tab. During installation, some red colored messages will appear. Do not worry. This is normal

To check the module was succesfully installed, a green bar should be seen at the bottom of the **Status** tab.

![](https://github.com/hugoescalpelo/data-visualization/blob/main/Images/Screenshot%20from%202023-10-17%2017-03-57.png?raw=true)

## Troubleshooting

Its posible that depending on container version of **CodeProject.AI Server** you need to manually set the dependencies needed to run OCR module inside de container. This is needed when OCR module is not started, you can identify it by checking the **Status** tab and verifying the color of the module is red instead of green.

Following instructions are based in *requirements.linux.txt* file found in the OCR module folder inside the modules volume defined in the Docker Compose File. For this project, the file is located in following path:
```
/opt/codeproject/ai/OCR/requirements.linux.txt
```

In this file is stated the following.
```
#! Python3.9

# We'll specify the exact version because we have a patch for one of the files
# Note that this is a different version of PaddlePaddle than Windows uses
paddlepaddle==2.4.0rc0    # Installing PaddelPaddle, the Deep Learning platform

## We also need to specify the exact version for paddleocr in Linux because 
## v2.6.0.2 and 2.6.0.3 fail to build (lanms-neo fails to build, which is required)
paddleocr==2.6.1.3        # Installing PaddleOCR, the OCR toolkit based on PaddlePaddle

# Do these after paddlepaddle because paddlepaddle requires specific versions 
imutils                   # Installing imutils, the image utilities library
Pillow<10.0.0             # Installing Pillow, a Python Image Library

opencv-python             # Installing OpenCV, the Computer Vision library for Python
numpy>=1.23.3             # Installing NumPy, a package for scientific computing

# end of file
```

This means executin the following commands:
```
sudo docker exec -it [container_id] pip install paddlepaddle==2.4.0rc0
sudo docker exec -it [container_id] pip install paddleocr==2.6.1.3
sudo docker exec -it [container_id] pip install imutils
sudo docker exec -it [container_id] pip install Pillow
sudo docker exec -it [container_id] pip install opencv-python
sudo docker exec -it [container_id] pip install numpy
```

You can check the container ID of **CodeProject.AI Server** with the following command:
```
sudo docker ps -a
```

After running this comands, go back to the **CodeProject.AI Server** dashboard, go to the **Install Modules**, then clic on the Uninstall button for Opticar Character Recognition moule, wait the uninstalling process to finish and then clic on the Install button again. This might take a while.

This shoud allow you to correctly install OCR Module.