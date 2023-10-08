# Postman Documentation

Postman is a plattform for testing and building APIs. In this project will be used for testing.

# Install Postman
Following instructions asume you are using Ubuntu 22.04LTS.

- Dowload Postman from [official site](https://www.postman.com/downloads/).
- Go to Downloads folder and extract files.
    ```
    cd ~/Downlaods
    tar -xzf postman-linux-x64.tar.gz
    ```
- Move the extracted Postman directory to **/opt*** folder.
    ```
    sudo mv Postman /opt
    ```
- Create a symbolic link somewhere in PATH so you can run it via Terminal.
    ```
    sudo ln -s /opt/Postman/Postman /usr/local/bin/postman
    ```
- Run Postman with following command.
    ```
    postman
    ```