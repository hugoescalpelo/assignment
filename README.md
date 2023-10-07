# Data visualization

## Objectives

This repository contains an app that does the following:

1. Face recognition
    
    **Objective**: Detect and track faces from a live webcam feed and compare them to a predefined collection of other faces.

    **Requirements**:
    - Detect faces in real-time from the webcam feed.
    - Capture a still frame of the detected face.
    - Compare the captured face to a collection of 40 other people.
    - Display the live camera feed, the extracted face, the top 5 most similar faces from the collection, and a numerical value representing their similarity (recognition score).

## Quirks and features

This app is developed considering the following:
- **Variety**: Demonstrate multiple paradigms and programming languages usage.
- **Robustness**: modularity and interoperability.
- **Reproducibility**: easy installation and configuration in multiple devices.
- **Scalability**: multiple instances of this app can be runned in same device or many devices.
- **Mantainability**: detailed documentation and version control.
- **Openness**: all tools are well known and maintainded open source projects.

## Requirements

To run this app you'll need the following:

- [Ubuntu 22.04LTS](https://ubuntu.com/download/desktop). Also can be runned in any Debain Based distro, VM or WSL system.
- [CodeProject.AI](https://hub.docker.com/r/codeproject/ai-server). This is an AI server for image recognition and will be installed via Docker Compose.
- [Docker Engine](https://docs.docker.com/engine/install/ubuntu/). This allow to install with all dependencies provided by publisher.
- An nVidia graphics card.


## Instructions

Once an Ubuntu system is set, follow this steps. Linked documentation includes details about requirements for each step.

1. Set up GPU. [Details](https://github.com/hugoescalpelo/data-visualization/blob/main/CUDA/cuda-toolkit-instructons.md)
2. Install Docker Engine. [Details](https://github.com/hugoescalpelo/data-visualization/blob/main/Docker/docker-documentation.md)
3. Enable GPU Access to containers. [Details]()
4. Set the Docker Compose file. This step will install CodeProject.AI and MySQL Server. [Details](https://github.com/hugoescalpelo/data-visualization/blob/main/Docker/docker-compose-documentation.md)
5. Create the MySQL database.
6. Set up CodeProject.AI
7. Install deepface for facial recognition.
8. Program the IP camera.
9. Install and configure Node-Red. [Details]()
10. 

## Reference

- [Notes on CUDA nVidia support - CodeProject.AI docs](https://www.codeproject.com/Articles/5322557/CodeProject-AI-Server-AI-the-easy-way)
- [CUDA Installation guide](https://gist.github.com/denguir/b21aa66ae7fb1089655dd9de8351a202)
- [cuDNN archive](https://developer.nvidia.com/rdp/cudnn-archive)
- [Install CodeProject.AI with GPU](https://youtu.be/6_jZmAt2yV4?si=QbV8ph1Ldi7IBFY6)
- [What does off means in nvidia-smi](https://forums.developer.nvidia.com/t/what-does-off-mean-in-the-output-of-nvidia-smi/37509/3)
- [GPU Persistance Mode](https://www.microway.com/hpc-tech-tips/nvidia-smi_control-your-gpus/)

<!-- 
2. Create the needed directories
3. Install compose
4. Move the configuration files
5. Set up nodeRed
6. Setup  -->


