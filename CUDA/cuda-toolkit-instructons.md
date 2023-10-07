# CUDA Toolkit Instructions

Cuda Toolkit provides an environment to run and develop GPU-accelerated applications.

For the "data-visualization" test app, CodeProject.AI server will be used through Docker Engine for computer vision apps. In order to use an nVidia GPU, CUDA Toolkit has to be installed.

This requires a nVidia GPU capable PC.

## Instructions

Test if nVidia GPU is enabled. Run the following command.
```
nvidia-smi
```
If nVidia hardware is installed, you will see something similar to the following:

![](https://github.com/hugoescalpelo/data-visualization/blob/main/Images/Screenshot%20from%202023-10-06%2000-49-01.png?raw=true)

## Manual installation

1. Search for the nVidia driver below 525.x
    [Search nVidia Linux Driver x64 515.x](https://www.nvidia.com/Download/Find.aspx?lang=en-us)
2. Right clic on the .run file and select properties. In permissions tab, activate Run as Program.
3. Open a terminal in the downlaod directory and run as root:
```

```


## Troubleshooting

Uninstall commands
```
sudo apt-get remove --auto-remove nvidia-cuda*
sudo rm -rf /usr/local/cuda*
sudo ldconfig
sudo apt-get remove --purge '^nvidia-.*'
```
Restart system.