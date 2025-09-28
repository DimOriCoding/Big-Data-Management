# Big-Data-Management
This folder was created as part of the "Big Data Management" course of the "Information and Communication Technologies" master's program of the Department of Informatics and Telecommunications of the National and Kapodistrian University of Athens.
Through this postgraduate course, a simple publisher-subscriber (pub-sub) system is implemented. More analytically this pub-sub system consists of three basic parts (components):

subscriber([sub.py]):

The connection between publisher or subscriber is made through socket programming which consists a way of connecting two nodes on a network to communicate with each other. One socket(node) listens on a particular port at an IP, while the other socket reaches out to the other to form a connection. The server (broker) forms the listener socket while the client (publisher, subscriber) reaches out to the server.
