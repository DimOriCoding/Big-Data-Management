# Big-Data-Management
This folder was created as part of the "Big Data Management" course of the "Information and Communication Technologies" master's program of the Department of Informatics and Telecommunications of the National and Kapodistrian University of Athens.

The main project that is implemented through this postgraduate course, is the construction a simple publisher-subscriber (pub-sub) system. More analytically this pub-sub system consists of three basic parts (components):

[**Subscriber**]((https://github.com/DimOriCoding/Big-Data-Management/blob/main/sub.py)): that can
 also run with multiple instances
 
[**Publisher**]((https://github.com/DimOriCoding/Big-Data-Management/blob/main/pub.py)):

[**Broker**]((https://github.com/DimOriCoding/Big-Data-Management/blob/main/broker.py)):

The connection between publisher or subscriber is made through [**socket programming**](https://github.com/DimOriCoding/Big-Data-Management/blob/main/Pub-Sub%20system%20assignment%20report.pdf), which consists a way of connecting two nodes on a network to communicate with each other. One socket(node) listens on a particular port at an IP, while the other socket reaches out to the other to form a connection. The server (broker) forms the listener socket while the client (publisher, subscriber) reaches out to the server. The Python socket library provides a low-level networking interface that allows you to create and manage network connections. A socket in Python is an endpoint for sending or receiving data across a network using the socket API.

<img width="769" height="866" alt="image" src="https://github.com/user-attachments/assets/5df297a6-fdc0-48da-be38-d1d6ea0fd22e" />
