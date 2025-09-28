# Big-Data-Management
This folder was created as part of the "Big Data Management" course of the "Information and Communication Technologies" master's program of the Department of Informatics and Telecommunications of the National and Kapodistrian University of Athens.

The main project that is implemented through this postgraduate course, is the construction a simple publisher-subscriber (pub-sub) system. Essemtially this system is a type of an a simple client-server system and consists of three basic parts (components):

[**Subscriber**]((https://github.com/DimOriCoding/Big-Data-Management/blob/main/sub.py)): Subscriber is a program that, when started, will connect to the Broker and subscribe to one or more topics.
 
[**Publisher**]((https://github.com/DimOriCoding/Big-Data-Management/blob/main/pub.py)) Publisher (client) is a program that produce (i.e., publish) message(s) for each topic subscribed to a Subscriber and connects to the Broker in a similar way to it.

[**Broker**]((https://github.com/DimOriCoding/Big-Data-Management/blob/main/broker.py)): The Broker:
1) Connects the publishers and the subscribers together
2) Has to remember (record) all the topics that each subscriber has subscribed to
4) It should forward the message to all subscribers that have subscribed to that topic, when a publisher publishes something about a specific
 topic.

The main connection between broker, publisher and subscriber is described in the image below. We assume that there is only the Subscriber X and the Publisher 1. So, each subscription has one subscriber, with each subscriber receiving a subset of the messages or a single message. Message 1 comes from Publisher 1 and is sent to Subscriber X via Subscription X into the Topic A.


<img width="826" height="558" alt="image" src="https://github.com/user-attachments/assets/47233e43-7299-4426-81d0-c67a9bbbaf0e" />










The connection between publisher or subscriber with broker is made through [**socket programming**](https://github.com/DimOriCoding/Big-Data-Management/blob/main/Pub-Sub%20system%20assignment%20report.pdf), which consists a way of connecting two nodes on a network to communicate with each other. One socket(node) listens on a particular port at an IP, while the other socket reaches out to the other to form a connection. The broker (server) forms the listener socket while the client (publisher, subscriber) reaches out to the server. Essentially a socket in Python is an endpoint for sending or receiving data across a network using the socket API. The Python socket library provides a low-level networking interface that allows you to create and manage network connections. 

In general in order to explain better the way that sockets work, it is vital to understand the image below


<div style="display: flex; justify-content: center; align-items: center; height: 100vh;">
  <img
    width="950"
    height="550"
    alt="image"
    src="https://github.com/user-attachments/assets/5df297a6-fdc0-48da-be38-d1d6ea0fd22e"
  />
</div>









The top left-hand column represents the server (broker), the column on the right side represents the client (subscriber or publisher) 

From the server side it is observable that the API calls that the server makes to set up a “listening” socket which listens for connections from clients and consists of these methods:

.socket(): where a socket object is created

.bind(): This method binds broker to a specific IP and port so that it can listen to incoming requests on that IP and port.

.listen(): This method puts the broker into listening mode when a client connects

.accept(): When a subscriber or publisher connects, the server calls .accept() to accept, or complete, the connection.

.connect(): The subscriber or publisher calls this method to establish a connection to the server and initiate the three-way handshake. The handshake step is important because it ensures that the client (subscriber/publisher) can reach the server (broker) and vice-versa. 

.send(), .recv() By calling these methods data is exchanged (sending and receiving data) between the client and server

Additionally there is the .sendall() function from python socket library which allow to send data to a server to which the socket is connected and the server can also send data to the client using it.

.close(): This method helps client and server to close their respective connection sockets.
