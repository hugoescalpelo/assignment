# Docker Compose Documentation

Docker compose is a tool to define multi container applicatons. We will use it to implement:

- [CodeProject.AI](https://www.codeproject.com/Articles/5322557/CodeProject-AI-Server-AI-the-easy-way) Server
- [MySQL Server](https://ubuntu.com/server/docs/databases-mysql)

## Instructions

This repository has the YAML file needed to define this portion of the "data-visualization" test app. To run it, run the following commands.

1. Create a directory for composer files.
    ```
    mkdir -p ~/DockerCompose
    ```
2. Create volumes directories.
    ```
    mkdir -p ~/DockerVolumes/MySQL/config
    mkdir -p ~/DockerVolumes/MySQL/data
    mkdir -p ~/DockerVolumes/codeproject/etc/ai
    mkdir -p ~/DockerVolumes/codeproject/opt/ai
    ```
3. Move the ```compose.yaml``` file in this repository to the DockerCompose directory. This step assumes you cloned this repository via GitHub Desktop and its stored in the default directory: ```~/Documents/GitHub```. For this case, you can run the following command to move said file.

    ```
    cp ~/Documents/GitHub/data-visualization/Docker/compose.yaml ~/DockerCompose/compose.yaml
    ```
    **Note**: Edit the MySQL password.
4. Set the terminal to the ```compose.yaml``` file with ```cd ~/DockerCompose``` and run the compose file. This will install or update the containers. This will take some time depending on your connection and systen capabilities.
    ```
    sudo docker compose up -d
    ```
    **Note**: This will download around 12GB. Be sure you have the needed disk space.
5. Check the status of your containers with ```sudo docker ps -a```

At this point, CodeProject.AI and MySQL shoudl be running.

## Test installation

### CodePorjectAI
In a browser, open [localhost:32168](http://localhost:32168/). You should see the CodeProjectAI status local webpage.

![](https://github.com/hugoescalpelo/data-visualization/blob/main/Images/Screenshot%20from%202023-10-06%2002-07-28.png?raw=true)

### MySQL

Get into the MySQL CLI:
```
sudo docker exec -it [id_del_contenedor] mysql -u root -p
```
Use the setted passwrod. Default password is **my-secret-pw**
