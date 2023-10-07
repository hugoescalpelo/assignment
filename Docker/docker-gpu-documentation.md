# Docker GPU documentation

In order to use GPU in Docker Compose, you need the nVidia container.

## Instructions

1. Set the nVidia Contaner Runtime Repository.

    ```
    curl -s -L https://nvidia.github.io/nvidia-container-runtime/gpgkey | \
        sudo apt-key add -
    distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
    
    curl -s -L https://nvidia.github.io/nvidia-container-runtime/$distribution/nvidia-container-runtime.list | \
        sudo tee /etc/apt/sources.list.d/nvidia-container-runtime.list

    sudo apt-get update
    ```
2. Install de nvidia-container-runtime
    ```
    apt-get install nvidia-container-runtime
    ```
3. Check the path of nvidia-container-runtime
    ```
    which nvidia-container-runtime-hook
    ```
4. Add that to the PATH by editing the .bashrc file
    ```
    sudo nano ~/.bashrc
    ```
5. Add the following command at the bottom of the file
    ```
    PATH=$PATH:/usr/bin/nvidia-container-runtime-hook
    ```
6. Reboot your system

Now, the installation of CodeProject.AI with CodeComposer shoudl use GPU correctly.

## Reference

- [Turn GPU Access with Docker Compose](https://docs.docker.com/compose/gpu-support/)
- [Access an nVidia GPU](https://docs.docker.com/config/containers/resource_constraints/#gpu)
- [nVidia Container Runtime](https://nvidia.github.io/nvidia-container-runtime/)