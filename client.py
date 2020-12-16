#!/usr/bin/env python3

import socket
import sys

if len(sys.argv) > 1:
    HOST = 'wss://gentle-dawn-03506.herokuapp.com/0.0.0.0'  # The server's hostname or IP address
    PORT = int(sys.argv[1])            # The port used by the server
else:
    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 12344            # The port used by
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("connecting to " + HOST +":"+str(PORT))
    s.connect((HOST, PORT))
    print(s)
    s.sendall("HI!!!".encode())
    data = s.recv(1024)

print('Received', repr(data))
