import threading
import sys
import socket
import getopt

connections = []  # list that keeps track of the connections between broker-publisher and broker-subscriber
host = "127.0.0.1"
s_port = 0
p_port = 0
t_m = "football CR7 is a great player"  # we assume that the time waiting is 0 and the name of publisher the same
# with this we give when we start to run from the terminal

# Insertion of the instances(s_port,p_port) in order the broker starts to run.
opts, args = getopt.getopt(sys.argv[1:], "s:p:")

for k, v in opts:
    if k == '-s':
        s_port = int(v)
    if k == '-p':
        p_port = int(v)


def pubthread(ho, p_po):
    # connection between broker and publisher through socket creation
    pub_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    pub_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    pub_sock.bind((ho, p_po))
    pub_sock.listen(10)
    print("Broker listening pubs on %s %d" % (ho, p_po))

    conn, addr = pub_sock.accept()

    print("Pub connected :" + addr[0] + ":" + str(addr[1]))

    if len(connections) < 2:  # Firstly we run the subthread and after the pubthread
        connections.append(conn)
    while True:
        try:
            data = connections[1].recv(1024).strip()
            data = data.decode('utf-8')  # In order to get rid of the b-prefix on the string
            print("Received from Pub:" + str(data))
            p_id, c, t, mess = data.split(" ", 3)
            print(p_id, c, t, mess)  # In our case we only have one publisher
            # Messages are of the form: This is the first message, without commas
            global t_m
            t_m = t + " " + mess
            if c == "pub":
                publishes = {}
                publishes.update({t: mess})  # Publishing a message to a topic
                print(publishes)
                connections[1].sendall(bytes("OK", "utf-8"))
                connections[1].sendall(bytes(t_m, "utf-8"))
        except Exception:
            print("Pub Disconnected")
            break


def subthread(ho, s_po):
    # connection between broker and subscriber through socket creation
    sub_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sub_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sub_sock.bind((ho, s_po))
    sub_sock.listen(10)
    print("Broker listening subs on %s %d" % (ho, s_po))

    conn, addr = sub_sock.accept()

    print("Sub connected :" + addr[0] + ":" + str(addr[1]))

    if len(connections) < 2:
        connections.append(conn)

    topics = []  # Keep track of the topics that subscribers want to subscribe
    subscribes = {}  # The broker keeps track of how many topics a subscriber has subscribed
    subs = []  # Keep track of how many subscribers are inserted to our system

    while True:
        try:
            data = connections[0].recv(1024).strip()
            data = data.decode('utf-8')  # In order to get rid of the b-prefix on the string
            print("Received from Sub:" + str(data))
            s_id, cmd, top = data.split()
            if subs.count(s_id) >= 1:
                subs.append(s_id)
                if subs[len(subs)-2] == subs[len(subs)-1]:
                    print(s_id, cmd, top)
                else:
                    topics.clear()
                    subscribes.clear()
                    print(s_id, cmd, top)
            if subs.count(s_id) == 0:
                subs.append(s_id)
                topics.clear()
                subscribes.clear()
                print(s_id, cmd, top)
            if cmd == "sub":
                if topics.count(top) == 0:
                    subs_topics = {}
                    topics.append(top)
                    subs_topics.update({top: s_id})  # subscription
                    subscribes.update({s_id: topics})
                    print("The subscriber", s_id, "subscribes into the topic", top)
                    print(subscribes)
                    connections[0].sendall(bytes("OK", "utf-8"))
                    connections[0].sendall(bytes(t_m, "utf-8"))# Broker sends topic and message to the subscriber
                else:
                    print("\n YOU ARE ALREADY SUBSCRIBED")
                    print(subscribes)
                    connections[0].sendall(bytes("OK", "utf-8"))
                    connections[0].sendall(bytes(t_m, "utf-8"))  # Broker sends topic and message to the subscriber
            if cmd == "unsub":
                if topics.count(top) != 0:
                    topics = [x for x in topics if x != top]
                    subscribes.update({s_id: topics})
                    print(subscribes)
                    connections[0].sendall(bytes("OK", "utf-8"))
                    print("The subscriber", s_id, "is unsubscribed from the topic", top)
                else:
                    print("\n NO UNSUBSCRIBE")
                    connections[0].sendall(bytes("OK", "utf-8"))
        except Exception:
            print("Sub Disconnected")
            break


def main(h, s, p):
    # The IP address of the broker
    print(h)
    # The ports that the subscriber and the publisher
    print("Subscribers port connection:", s, "Publishers port connection:", p)

    try:
        threading.Thread(target=subthread, args=(h, s)).start()
        threading.Thread(target=pubthread, args=(h, p)).start()



    except KeyboardInterrupt as msg:
        sys.exit(0)


if __name__ == '__main__':

    main(host, s_port, p_port)
