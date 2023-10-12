# Visual Studio Code Documentation

Visual Studio Code is a code editor redefined and optimized for building and debugging modern web and cloud applications. 

Many tests and examples in this project were tested in **Visual Studio Code**. Here you can find instructions to set it up.

## Visual Studio Code Installation

Visual Studio Code was installed via **Ubuntu Software** app, which is equivalent to *Snap* installation. Manual instructions can be find in the following [link](https://code.visualstudio.com/docs/setup/linux). Debian and Ubunti instruction al cited bellow.

```
sudo apt-get install wget gpg

wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg

sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg

sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'

rm -f packages.microsoft.gpg

sudo apt install apt-transport-https

sudo apt update

sudo apt install code
```
### Adding the Python Extension

1. Open Visual Studio Code by clicking on the App icon in the menu or with a terminal.

    ```
    code .
    ```
2. Clic on the extension icon in the left bar.
3. Search for the **Python** word.
4. In the result list clic on the **Install** blue button in the result pubished by **Microsoft**.