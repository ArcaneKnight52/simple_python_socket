#client.py

import socket

#create socket instance

client_object = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
#target ip

ip_address = '127.0.0.1'
port = 5555

#recive connection
client_object.connect((ip_address,port))
data_receive = client_object.recv(1024)

#if response is not null
if data_receive :
    #Connection Succesfull
    print("CLIENT CONNECTION SUCCESFULL")
    print(data_receive.decode('utf-8'))
    
    while data_receive:
        #user input
        client_input = input().encode('utf-8')
        
        #sending req to server
        client_object.send(client_input)
        
        #receiving input from from the server
        data_receive = client_object.recv(1024)
        

        if data_receive :
            print("{}: {}".format("SERVER",data_receive.decode('utf-8')))
        