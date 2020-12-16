
import socket
import os
import time 
import sys

server = socket.socket()
port = int(os.environ.get("PORT", 12344))
print(sys.argv)
host =  "127.0.0.1"  if len(sys.argv) > 1 else "0.0.0.0"
server.bind((host, port))
print(f"###### SERVER RUNNING ON PORT {port} ({host}) ######")
server.listen()

while True:

    s, addr = server.accept()
    print("Recived request from:", addr)
    
    print(addr, " sent: ", repr(s.recv(1024)))
    
    print("Answering to:", addr)

    s.send("Hello, world! (from server)".encode())
    
    print("Answered to:", addr)

    s.close()