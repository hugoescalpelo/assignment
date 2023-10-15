# ESP32CAM documentation
ESP32CAM is a ESP32 based microcontroller with a OV2640 camera. A modified version of Camera Web Server example is loaded to the micro controller.

Its modificatons consist in camera model, SSID name, network password, static IP, default resolution and reboot directive whenever wifi connection is lost.

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
    - Set up pyserial, needed for serial communication. Run the following commands, you can ommit previous components like installation of Git, Python or PIP.
        ```
        sudo usermod -a -G dialout $USER
        sudo apt-get install git
        wget https://bootstrap.pypa.io/get-pip.py
        sudo python3 get-pip.py
        sudo pip3 install pyserial
        mkdir -p ~/Arduino/hardware/espressif
        cd ~/Arduino/hardware/espressif
        git clone https://github.com/espressif/arduino-esp32.git esp32
        cd esp32/tools
        python3 get.py
        ```
        Around 2.5 GB will be donwloaded. Time will vary depending on your Internet speed connection and system capabilities.
    - Reboot your system.
3. Connect an ESP32CAM board already mounted in a USB base or throug a FTDI232 Converter. Connection instructions are in [this file](https://github.com/hugoescalpelo/data-visualization/blob/main/ESP32CAM/esp32cam-ftdi232-connections.md).
4. Select ESP32CAM board.
    - Clic on the *Select Board* drop down menu.
    - Clic on the *Select other board and port...* option.
    - Search for AI Thinker ESP32-CAM board.
    - Select port, usually /dev/ttyS0
5. Open the CameraWebServer.ino file
    - Clic on the file menu and then clic the Open option.
    - Search for the CameraWebServer.ino file located in **data-visualization/ESP32CAM/CameraWebServer/** path in this repository.
6. Check network settings. The following commands assume your PC is in the same network your ESP32CAM will be.
    - Run the ```ip addr``` command to check your IP. In my case, my IP is ```192.168.1.68``` at ```enp5s0``` interface.
    - Check used network with arp -a command
        ```
        sudo arp -a
        ```
        In my network the answer is:
        ```
        _gateway (192.168.1.254) at b8:d6:f6:7d:0f:ef [ether] on enp5s0
        ? (172.18.0.2) at 02:42:ac:12:00:02 [ether] on br-6b01c40054f0
        ? (192.168.1.81) at b4:b2:91:74:fa:a9 [ether] on enp5s0
        ```
    - Notice the gateway is ```192.168.1.254```, this will be used later.
    - Install ```arp-scan``` with ```sudo apt install arp-scan```
    - Check available IPs within your network segment. For me, the command was 
        ```
        sudo arp-scan --interface=enp5s0 192.168.1.0/24
        ```
    - Choose an availabe IP, which means an IP that is not listed. I will choose ```192.168.1.110```
    - Find your subnet mask. Install ```net-tools``` with ```sudo apt install net-tools``` command and run ```sudo ifconfig | grep -i mask```. My results were the following
        ```
        inet 172.18.0.1  netmask 255.255.0.0  broadcast 172.18.255.255
        inet 172.19.0.1  netmask 255.255.0.0  broadcast 172.19.255.255
        inet 172.17.0.1  netmask 255.255.0.0  broadcast 172.17.255.255
        inet 192.168.1.68  netmask 255.255.255.0  broadcast 192.168.1.255
        inet 127.0.0.1  netmask 255.0.0.0
        ```
        So, for my IP (```192.168.1.68```), subnet mask will be ```255.255.255.0```
7. Update the network settings in **CameraWebServer.ino** program.
    - Set your WiFi network name in **ssid** variable inside the quotation marks.
    - Set your WiFi password in **password** variable inside the quotation marks.
    - Set an available IP in **local_IP** variable, comma separated.
    - Set your gateway IP in **gateway** variable, comma separated.
    - Set your subnet mask in **subnet** variable, comma separated.
8. Save changes with Ctrl+S
9. Set communication speed by clicking on serial monitor button located at upper right corner of Arduino IDE and then select **115200 baud** at the speed dropdown meny in the upper right corner of the Serial Monitor area located at the bottom of the Arduino IDE.
10. Set the ESP32CAM in programming mode by doing the following depending on your programming tool:
    - ESP32CAM base: no action needed.
    - FTID232: Wire GPIO0 with GND in the ESP32CAM, press Reset button under the ESP32CAM. A message will appear in serial monitor stating that a program upload is expected. Once the program is loaded, disconnect GPIO0 from GND and press Reset button.
11. Clic on the Uplaod button to load the program. Progress messages will be displayed.
12. Test the connection. Open the selected IP. A settings page will be updated. Clic on the Start Stream button. A streaming will be displayed.



## Reference
- [Arduino 2 Ubuntu Instructios](https://www.youtube.com/watch?v=JeD3nz0__nc)
- [Espressif **arduino-esp32** install instructions](https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html)
- [Get network settings 1](https://www.techrepublic.com/article/how-to-scan-for-ip-addresses-on-your-network-with-linux/)
- [Get network settings 2](https://devconnected.com/how-to-get-your-ip-address-on-linux/)