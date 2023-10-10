# Node-Red Documentation

Node-Red is an open source visual programming tool based in data flow. It will be used as app server.

This document assumes you are using the ESP32CAM video server as IP Camera, but it can be substituted for any USB camera or IP Camera.

## Installation
The following stepps will install Node-Red locally.

1. Install [NodeJS](https://github.com/nodesource/distributions#ubuntu-versions).
    ```
    sudo apt-get update

    sudo apt-get install -y ca-certificates curl gnupg

    sudo mkdir -p /etc/apt/keyrings

    curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg

    NODE_MAJOR=20

    echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | sudo tee /etc/apt/sources.list.d/nodesource.list

    sudo apt-get update

    sudo apt-get install nodejs -y
    ```
2. Install [Node-Red](https://nodered.org/docs/getting-started/local).
    ```
    sudo npm install -g --unsafe-perm node-red
    ```
3. Run Node-Red with the following command ```node-red```
4. Go to [localhost:1880](http://localhost:1880). You will see the Node-Red GUI.

## Add the needed external nodes
This app uses additional nodes provided by the community.

1. Clic on the hamburger menu and select Manage Palette option.
2. In the Install tab search for **node-red-dashboard** and clic on install.

## Import the application
The aplication is provided in this repository as a JSON file.

1. Clic on the hamburger menu and select import option.
2. Select File Import Option and browse for the **flows.json** file in **/data-visualization/NodeRed/** directory.
3. Update the following nodes to match your system:
    - The **http request** node called **get picture** in the Camera Cheker group. In the Method field select **GET**, in the URL field writhe the **Capture** URL from an IP camera in the same network you are working, in the Return field select **a binary buffer**.
    - The **function** node called **Add name** in Camera Checker group. Updathe the path in the string assigned to *msg.filename*, it has to be an absolue path to where you want to storage the picture from the web camera to detect a face.
    - The **write file** node called **write file** in the Camera Checker group. In the field Filename, select *msg.* and write **filename** as object variable, in the Action field select *Overwrite File*, check the *Create directory if it doesn't exist* checkbox.
    - The **exec** node called **curl call** in the Camera Checker group. Update the command ```curl --location 'http://localhost:32168/v1/vision/face' --form 'image=@"/home/hugo/Pictures/detect.jpg"' --form 'min_confidence="0.4"'``` to match the absolute path to the face detection file and the URL to your **CodeProject.AI Server**.
    - The **template** node in Camera Checker. Update the URL to your IP Camera stream URL at the top and the bottom of the code.
    - The **http request** node called **Get photo** in the Capture Photo Group. Update the URL to your IP camera capture picture URL, be sure Method field is set to **GET** and return field is set to **a binary buffer**.
    - The **function** node called **Add name** in the Capture Photo group. Update the string assigned to *msg.filename* to have an absolute path to where the Photos will be saved when an user clics on the *Capture* button.

## Reference

- [NodeJS package installation instructions](https://github.com/nodesource/distributions#installation-instructions)
- [Node-Red standar installation instructions](https://nodered.org/docs/getting-started/local)
