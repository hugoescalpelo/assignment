# ESP32CAM documentation
ESP32CAM is a ESP32 based microcontroller with a OV2640 camera. A modified version of Camera Web Server example is loaded to the micro controller.

Its modificatons consist in SSID name, network password, static IP, default resolution and reboot directive whenever wifi connection is lost.

In order to load the program provided in this repository, you need to use Arduino IDE and add ESP32 boards to the board manager. Instructions are in the next sections.

## Requirements

### Software
- [Arduino IDE](https://www.arduino.cc/en/software).


## Instructions

1. Install Arduino IDE via apt, snap, Ubuntu Software App (also snap), App Image or manually. This proyect was tested with Arduino 2.2.1 via App Image.
    - Download Arduino IDE 2.2.1 App Image from [Arduino Software](https://www.arduino.cc/en/software)
    - It's recommended to move it to a more suitable folder, home folder for example.
    - Right clic, select properties, select Permissions tab and check **Allow executing file as a program** checkbox. Then accept changes.
    - Open a terminal and install **libfuse2*
        ```
        sudo apt install libfuse2
        ```
    - Add your user to **dialout** group to allow acces to serial ports, needed to comunicate the IDE with boards.
        ```
        sudo adduser $USER dialout
        ```
    - Log out or reboot to changes had effect.
    - Double clic on Arduino 2.2.1 AppImage File to run it.