#!/usr/bin/env python3

import socket
import sys
HOST = sys.argv[1] # The server's hostname or IP address
PORT = int(sys.argv[2]) # The port used by the server
MESSAGE = b"Hello, world!"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
sock.sendto(MESSAGE, (HOST, PORT))