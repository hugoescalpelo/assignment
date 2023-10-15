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
2. Add ESP32 boards to Arduino IDE.
    - Open Arduino IDE
    - Clic on File menu, Prefrences option and paste the following URL in Additional Boards Manager URLs textbox.
        ```
        https://espressif.github.io/arduino-esp32/package_esp32_index.json
        ```
    - If previous URLs are present, clic de double square enlarge button and add the URL in a new line.
    - Clic Ok button.
    - Clic on Boards Manager icon at left bar.
    - Search for ESP32 and install **esp32 by Espressif Systems** boards. Around 450 MB will be downlaoded. Installation time depends on your system capabilities and internet speed connection.
4. Connect an ESP32CAM board already mounted in a USB base or throug a FTDI232 Converter. Connection instructions are in [this file](https://github.com/hugoescalpelo/data-visualization/blob/main/ESP32CAM/esp32cam-ftdi232-connections.md).
3. Select ESP32CAM board.
    - Clic on the *Select Board* drop down menu.
    - Clic on the *Select other board and port...* option.
    - Search for AI Thinker ESP32-CAM board.





    ## Reference

    - [Arduino 2 Ubuntu Instructios](https://www.youtube.com/watch?v=JeD3nz0__nc)
    - [Espressif **arduino-esp32** install instructions](https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html)
