This repository contains a socket server-client Network.
The Client reads serial input (data from an array of sensors) from /ttyUSB0 and sends it to the server which uses the incoming data to create a database. The network is used to transmit and store real-time sensor data on the server.

The datais transferred using zigbee. A zigbee on an arduino transmits the data and another on the rpi receives it.
AUTHOR: Rakshit Raj (rakshitraj)
