import getopt
import sys
import socket
import time


subs = "s1"
host = "127.0.0.1"
port = 0
filepath = "subscriber1.txt"

# Insertion of the instances(subscriber id, host, subscriber port, file) in order the subscriber starts to run.
opts, args = getopt.getopt(sys.argv[1:], "i:h:p:f:")

for k, v in opts:
    if k == '-i':
        subs = str(v)  # Give names such as s1, s10, s30
    if k == '-h':
        host = str(v)
    if k == '-p':
        port = int(v)
    if k == '-f':
        filepath = str(v)


def main(s, h, p, file):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect((h, p))

    print(file)
    with open(file) as f:
        text = f.read()
    for line in text.splitlines():

        for lines in line.splitlines():
            t_w, cmd, top = lines.split()
            print(t_w)
            print(cmd)
            print(top)
            time.sleep(int(t_w))
            data = s + " " + cmd + " " + top
            print(data)
            i = 0
            while True:
                sock.sendall(bytes(data + "\n", "utf-8"))
                received_1 = str(sock.recv(1024), "utf-8")
                print("Received: " + received_1)
                # It is not allowed when we have unsubscription to receive messages in this topic
                # Checking which of the two received has the topic and message about checking for subscribe
                if cmd == "sub":
                    received_2 = str(sock.recv(1024), "utf-8")
                    print("Received: " + received_2)
                    t, m = received_2.split(" ", 1)
                    if t == top:
                        print("Received msg for the topic", t, ":", m)
                i += 1
                if i == 1:
                    break

    time_wait = int(input("Give time for sub to wait:  "))
    while time_wait < 0:
        time_wait = int(input("Give time for sub to wait:  "))

    while time_wait >= 0:
        time.sleep(time_wait)
        sub_id =  str(input("Give subs id:     "))  # Give names such as s1, s10, s30, in order to input more subs
        command = str(input("Give subs command:     "))
        while command != "sub" and command != "unsub":
            command = str(input("Give subs command:     "))

        topic = str(input("Give topic for subscribe:      "))
        data = sub_id + " " + command + " " + topic
        print(data)
        i = 0
        while True:
            sock.sendall(bytes(data + "\n", "utf-8"))
            received_1 = str(sock.recv(1024), "utf-8")
            print("Received: " + received_1)
            # It is not allowed when we have unsubscription to receive messages in this topic
            # Checking which of the two received has the topic and message about checking for subscribe
            if command == "sub":
                received_2 = str(sock.recv(1024), "utf-8")
                print("Received: " + received_2)
                t, m = received_2.split(" ", 1)
                if t == topic:
                    print("Received msg for the topic", t, ":", m)
            i += 1
            if i == 1:
                break
        ans = input('\n Do you want to continue(y/n) :')
        if ans == 'y':
            time_wait = int(input("Give time for sub to wait:  "))
            while time_wait < 0:
                time_wait = int(input("Give time for sub to wait:  "))
            continue
        else:
            break


if __name__ == '__main__':

    main(subs, host, port, filepath)
