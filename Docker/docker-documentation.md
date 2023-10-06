# Docker Documentation
In this document you will find instructions and detail of Docker Engine Installation for "data-visualization" test app.

## Requirements

Requirements are listed in [docker engine prerequisites documentation](https://docs.docker.com/engine/install/ubuntu/#prerequisites) and [docker engine system requirements](https://docs.docker.com/desktop/install/linux-install/#kvm-virtualization-support). The following is the most important.
- 64 bit kerned and CPU
- Virtualization compatible Processor
- KVM compatible OS
    - Install CPU tools. Run ```sudo apt install cpu-checker```
    - Check if KVM is setted. Run ```kvm-ok```
    - Check if KVM is enabled. Run ```lsmod | grep kvm```
        - You should see the following depending on your processor
            ```
            modprobe kvm_intel  # Intel processors

            modprobe kvm_amd    # AMD processors
            ```
- 4 GB of RAM
- An nVidia graphics Card

## Installation guide

Docker is installed using the [convinience script](https://docs.docker.com/engine/install/ubuntu/#install-using-the-convenience-script). Follow the next instructions.

1. Install curl if not installed ```sudo apt install curl```
2. Run the following:
```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh --dry-run
```
3. Check docker version with ```docker -version```

### Alternative installation
If the previous did not work, try [manual apt installation](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository):

1. Add Docker's official GPG key:
```
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
```
2. Add the repository to Apt sources:

```
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

3. Install de latest version

```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
### Test installation

Check if Docker is installed with the following command 

```
docker --version
```

Try the test container
```
sudo docker run hello-world
```
## Manage instructions
Following commands may need super user permissions.

Check file system size with .
```
sudo docker system df
```

Check and change service status.
```
sudo systemctl status docker
sudo systemctl start docker
sudo systemctl stop docker
sudo systemctl restart docker
```

List docker containers .
```
sudo docker ps -a
```

Start a container.
```
docker start [container_id]
```

Start all containers.
```
docker start $(docker ps -a -q)
```

Stop a container.
```
docker stop [container_id]
```

Stop all containers.
```
docker stop $(docker ps -a -q)
```

Run an specific command inside a container.
```
docker exec -it [container_id] command [options] [arguments]
```

List docker images.
```
sudo docker images
```

Delete a docker image.
```
sudo docker rmi [container_id]
```
## Install Compose

Docker Compose is a tool to define multi container apps. It will be needed. Install it with the following command:

```
sudo apt install docker-compose
```

## Troubleshooting

In case you have trouble running Docker commands, try adding your user to Docker group
```
sudo usermod -aG docker $USER
newgrp docker
```
