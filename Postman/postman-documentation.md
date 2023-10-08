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
You should see the Postman window. 
![](https://github.com/hugoescalpelo/data-visualization/blob/main/Images/Screenshot%20from%202023-10-07%2021-01-52.png?raw=true)
Do not close the terminal that launched Postman.
![](https://github.com/hugoescalpelo/data-visualization/blob/main/Images/Screenshot%20from%202023-10-07%2021-03-06.png?raw=true)