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
2. Move the ```compose.yaml``` file in this repository to the DockerCompose directory. This step assumes you cloned this repository via GitHub Desktop and its stored in the default directory: ```~/Documents/GitHub```. For this case, you can run the following command to move said file.

    ```
    mv ~/Documents/GitHub/data-visualization/Docker/compose.yaml ~/DockerCompose/compose.yaml
    ```