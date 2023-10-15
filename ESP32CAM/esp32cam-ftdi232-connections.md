# ESP32CAM connections through FTD232 serial converter

If you use an FTD232 serial converter, wire the following.

ESP32       FTDI
5V----------5V
GND---------GND
UoT---------Rx
UoR---------Tx

## Programming wire

In order to load a program, you have to wire GPIO0 to GND and press reset button located under the board. A plastic tool is recomended.

ESP32
GPIO0-----v
GND-------<