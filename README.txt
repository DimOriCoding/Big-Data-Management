In order to run this program we open three terminals one for broker, for subscriber and publisher each. After unzip the file 
in each command line we wrote:
If for example the broker starts with the following command:
python broker.py -s 9000 -p 9090 
where 
-s indicates the port of this specific broker where subscribers will connect. The IP address of the broker is implied to be that of 
the current machine the publisher is running on. 
-p indicates the port of this specific broker where publishers will connect. Again, the IP address of the broker is implied to be that of 
the current machine the publisher is running on.
The subscriber starts with the following command:
python sub.py -i s1 -h 127.0.0.1 -p 9000 -f subscriber1.txt
-i indicates the id of this subscriber. This id will be sent to the broker so that it can keep track of the subscriber and print messages 
accordingly.
-h indicates the IP address of the broker. 
-p indicates the port of the broker 
-f is an optional parameter that indicates a file name where there are commands that the subscriber will execute once started and connected to the broker, 
before giving control to the user from the keyboard.
Correspondingly the publisher starts with the following command:
python pub.py -i p1 -h 127.0.0.1 -p 9090 -f publisher1.txt
where -i indicates the id of this publisher.This id will be sent to the broker so that it can keep track of the publisher and print messages accordingly. 
-h indicates the IP address of the broker.
 -p indicates the port of the broker 
-f is an optional parameter that indicates a file name where there are commands that the publisher will execute once started and connected to the broker, 
before giving control to the user from the keyboard.
First of all we run the broker.py from the respective command line in order to start running our project. 
After that we run the sub.py from command line and as it starts running after a while (maybe when it appears the received:OK, 
or a little bit earlier) in terminal we start to run pub.py. 

About the keyboard the most preferable way to run the sub and pub is firstly to give sub_id, time_wait , command(sub, unsub) and topic run 
them, the “received = OK” is appeared and then put the same for pub (sub_id, time_wait , command(pub) topic and message). 

Also you can run it with the same way into the keyboard but first the pub and secondly the sub.
Note: If we want to publish a message into a topic a subscriber is already subscribed (e.g s1 sub topic), 
then we have to enter the same id command and topic again (s1 sub topic), in order to confirm that the subscriber is already subscribed 
and then to recive from publisher the same or different message to the same topic (e.g p1 pub topic message).
P.S. The whole project(python files broker.py, sub.py, pub.py) has improved a little bit in order to save the topics and the messages sending from publisher to this topics and finally to forward all the messages to the subscriber that is subscribed to a specific topic. This is an additional improvement from the project objectives, because storing/remembering messages is out of the scope of this project. 
If you have any problem about source code (e.g you can not see it) or any other problem with the project please contact me on emails 
dimori@outlook.com.gr or ic121006@di.uoa.gr





