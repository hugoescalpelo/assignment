# Node-Red Documentation

Node-Red is an open source visual programming tool based in data flow. It will be used as app server.

## Installation
The following stepps will install Node-Red locally.

1. Install [NodeJS](https://github.com/nodesource/distributions#ubuntu-versions).
    ```
    sudo apt-get update
    sudo apt install nodejs
    sudo apt install npm
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