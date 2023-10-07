# CUDA Toolkit Instructions

Cuda Toolkit provides an environment to run and develop GPU-accelerated applications.

For the "data-visualization" test app, CodeProject.AI server will be used through Docker Engine for computer vision apps. In order to use an nVidia GPU, CUDA Toolkit has to be installed.

This requires a nVidia GPU capable PC.

## Instructions

**Note**: this will download around 12GB.

Install nVidia Drivers 516.x or below. I recommend 515.x
```
sudo apt-get update
sudo apt-get install nvidia-driver-515
```
Reboot the system.

Install CUDA Toolkit.
```
sudp apt install nvidia-cuda-toolkit
```

Download cuDNN .deb file from [here](https://developer.nvidia.com/rdp/cudnn-download). You will need an Nvidia account. Select the cuDNN version for the appropriate CUDA version, which is the version that appears when you run:
```
nvcc --version
```

Go to the download folder and install the cuDNN.
```
sudo apt install ./<filename.deb>
```

At the end, terminal will suggest a command to install the GPG Key. For me was:
```
sudo cp /var/cudnn-local-repo-ubuntu2204-8.9.4.25/cudnn-local-72322D7F-keyring.gpg /usr/share/keyrings/
```

My cuDNN version is 8, adapt the following to your version:
```
sudo apt update
sudo apt install libcudnn8
sudo apt install libcudnn8-dev
sudo apt install libcudnn8-samples
```

Test if nVidia GPU is enabled. Run the following command.
```
nvidia-smi
```
If nVidia hardware is installed, you will see something similar to the following:

![](https://github.com/hugoescalpelo/data-visualization/blob/main/Images/Screenshot%20from%202023-10-06%2000-49-01.png?raw=true)

Turn GPU ON with following command.
```
sudo nvidia-smi -pm 1
```
It should  look like this.
![](https://github.com/hugoescalpelo/data-visualization/blob/main/Images/Screenshot%20from%202023-10-06%2020-44-59.png?raw=true)

## Troubleshooting

Uninstall commands
```
sudo apt-get remove --auto-remove nvidia-cuda*
sudo rm -rf /usr/local/cuda*
sudo ldconfig
sudo apt-get remove --purge '^nvidia-.*'
```
Restart system.