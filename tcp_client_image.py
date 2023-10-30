import socket
import pickle
import numpy as np
import cv2

ServerName = 'localhost'
ServerPort = 12001

ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    ClientSocket.connect((ServerName, ServerPort))
except socket.error as err:
    print(f'Unable to connect to the server {err}')

image = cv2.imread("image.png")

ClientSocket.send(pickle.dumps(image))
ModifiedMessage = ClientSocket.recv(4096)
print(f'Response From Server:  {str(ModifiedMessage.decode())}')
ClientSocket.close()