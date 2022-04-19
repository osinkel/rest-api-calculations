#!/usr/bin/env python
import socket
import sys
sys.path.append('../')
from config import CLIENT_HOST, SOCKET_PORT


try:
    vals = sys.argv[1], sys.argv[2], sys.argv[3]
except IndexError:
    raise IndexError('Values should be as: {operarion} {number} {number}')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((CLIENT_HOST, SOCKET_PORT))
    msg = (''.join(str(x) + ' ' for x in vals)).encode("UTF-8")
    s.sendall(msg)
    data = str(s.recv(1024), 'utf-8')

print(f"Result: {data!r}")
