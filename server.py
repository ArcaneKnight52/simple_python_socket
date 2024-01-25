#server.py

import socket
import string
import random

#initialize the socket object
server_object = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)

#connecting to localhost

ip_address = '127.0.0.1'
port = 5555
server_object.bind((ip_address,port))
server_object.listen()

#initialize the server object and make the client listenable
connection_object, _ = server_object.accept()

if connection_object:
    #connection succesfull
    print("SERVER CONNECTED TO CLIENT SUCCESFULL!")
    
    #send inital msg to client
    connection_object.send(b"Type the message:")
    
    #receive msg from client
    data_receive = connection_object.recv(1024)
    
    while data_receive != b'stop':
        print("{}: {}".format("CLIENT MESSAGE : ",data_receive.decode('utf-8')))
        server_input = random.choice(string.ascii_letters)
        connection_object.send(server_input.encode('utf-8'))
        data_receive = connection_object.recv(1024)