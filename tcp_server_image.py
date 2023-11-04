import socket
import os
import pickle
import cv2


ServerPort = 12001

try:
    ServerSocket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print(f'Unable to establish a socket connection {err}\n')

try:
    ServerSocket.bind(('localhost', ServerPort))
except socket.error as err:
    print(f'Unable to bind to the server {err}\n')

ServerSocket.listen(1)

print('The server is ready to receive your data \n')

while True:
    ConnectionSocket, Address = ServerSocket.accept()
    ClientMessage = ConnectionSocket.recv(4096)
    data = pickle.loads(ClientMessage)
    cv2.imwrite("image_2.png",data)
    ConnectionSocket.close()