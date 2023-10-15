### Mosquitto

This test assumes you are running mosquitto via Docker Compose.

## Check if mosquitto is running

To check if mosquitto is running you need ```net-tools``` installed. Install it with ```sudo apt install net-tools```. Check if mosquitto is running in port 1883 with following command.
```
netstat -an | grep 1883
```

## Basic testing

To test a connection you will need two terminal windows. 

In the first, make a subscription to a test topic. For this you will need the mosquitto container ID, get it with ```sudo docker ps -a```
```
sudo docker exec -it [container-id] mosquitto_sub -h localhost -t mosquitto/test
```
In the secont terminal window, publish with following command.
```
sudo docker exec -it [container-id] mosquitto_pub -h localhost -t mosquitto/test -m "Hello Mosquitto"
```

The message "Hello Mosquitto" will appear in the subscription window.