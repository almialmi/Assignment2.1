import socket
from socket import *
ready="The server is wating to recieve: "
host="127.0.0.1"
Port = input("Enter the port: ")
Socket = socket(AF_INET, SOCK_DGRAM)
Socket.bind((host,int(Port)))
print (ready)
while True:
    message, clientAddress =Socket.recvfrom(4096)
    if not message:
        break
    print ("The client says " + str(message))
    modifiedMessage= message.upper().decode()
    print ("Server sending: " + str(message))
    Socket.sendto(modifiedMessage.encode(), clientAddress) 
