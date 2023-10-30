import socket
import random

ServerName = '127.0.0.1'
ServerPort = 12003

try:
    ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error as err:
    print(f'Unable to establish a socket connection {err}\n')

try:
    ServerSocket.bind((ServerName, ServerPort))
    print ('The server is ready to receive your data \n')
    while True:
        ClientMessage, ClientAddress = ServerSocket.recvfrom(4096)
        print('received: ', ClientMessage)
except socket.error as err:
    print(f'Unable to bin to the server {err}\n')