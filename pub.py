import time
import getopt
import sys
import socket


pubs =  "p1"
host = "127.0.0.1"
port = 0
filepath = "publisher1.txt"

opts, args = getopt.getopt(sys.argv[1:], "i:r:h:p:f:")

for k, v in opts:
    if k == '-i':
        pubs = str(v)  # Give names such as p1, p10, p30
    if k == '-h':
        host = str(v)
    if k == '-p':
        port = int(v)
    if k == '-f':
        filepath = str(v)


def main(p, h, po, file):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect((h, po))

    print(file)
    with open(file) as f:
        text = f.read()
    for line in text.splitlines():

        for lines in line.splitlines():
            t_w, cmd, top, msg = lines.split(" ", 3)
            print(t_w)
            print(cmd)
            print(top)
            print(msg)
            time.sleep(int(t_w))
            data = p + " " + cmd + " " + top + " " + msg
            i = 0
            while True:
                sock.sendall(bytes(data + "\n", "utf-8"))
                received_1 = str(sock.recv(1024), "utf-8")  # Message OK
                received_2 = str(sock.recv(1024), "utf-8")
                print("Received: " + received_1)
                t, m = received_2.split(" ", 1)  # message that published into the topic
                print("Received msg for the topic", t, ":", m)
                i += 1
                if i == 1:
                    break
    ans = input('\nDo you want to continue(y/n) :')
    if ans == "y":
      time_wait = int(input("Give time for pub to wait:  "))
      while time_wait < 0:
         time_wait = int(input("Give time for pub to wait:  "))

      while time_wait >= 0:
         time.sleep(time_wait)
         pub_id = str(input("Give pubs id:     "))  # Give names such as p1, p10, p30, in order to input more pubs
         command = input("Give pubs command:     ")
         while command != "pub":
            command = input("Give pubs command:     ")

         topic = input("Give topic for publish:      ")
         message = input("send message for publish:      ")
         data = (pub_id + " " + command + " " + topic + " " + message)
         print(data)
         i = 0
         while True:
            sock.sendall(bytes(data + "\n", "utf-8"))
            received_1 = str(sock.recv(1024), "utf-8")  # Message OK
            received_2 = str(sock.recv(1024), "utf-8")  # message that published into the topic
            t, m = received_2.split(" ", 1)
            print("Received: " + received_1)
            print("Received msg for the topic", t, ":", m)
            i += 1
            if i == 1:
                break
         ans = input('\n Do you want to continue(y/n) :')
         if ans == "y":
          time_wait = int(input("Give time for pub to wait:  "))
          while time_wait < 0:
            time_wait = int(input("Give time for pub to wait:  "))
          continue
         else:
           break


if __name__ == '__main__':

    main(pubs, host, port, filepath)
