#!/usr/bin/env python3

import socket
import sys
HOST = sys.argv[1] # IP of the Server
PORT = int(sys.argv[2]) # PORT of the Server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen()

conn, addr = sock.accept()
print('Connected by', addr)
data = conn.recv(1024)
print("received message:", data)