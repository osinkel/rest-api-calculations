#!/usr/bin/env python
import socketserver
import sys

sys.path.append('../')
from config import HOST, SOCKET_PORT
from controllers.operation_controller import add_to_db


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024).decode('utf-8').split()
        operator, n1, n2 = '', '', ''
        try:
            operator, n1, n2 = data[0], data[1], data[2]
        except IndexError:
            print('Wrong number of variables!')
        self.request.sendall(add_to_db(operator, n1, n2).encode('utf-8'))


if __name__ == '__main__':
    with socketserver.TCPServer((HOST,SOCKET_PORT), MyTCPHandler) as server:
        server.serve_forever()
