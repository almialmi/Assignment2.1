import socket
host = input("Enter the IP : ")
port = input("Enter the port: ")
Socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
message =input("Please enter the statement: ")
while (message!="Ctrl-C"):
        Socket.sendto(message.encode(),(host, int(port)))
        modifiedMessage, serverAddress =Socket.recvfrom(4096)
        print ("Returned text from the server: "+modifiedMessage.decode())
        print("Type Ctrl-C to quit !! ")
        # it is UDP create connection in every time
        host = input("Enter the IP : ")
        port = input("Enter the port: ")
        message =input("Please enter the statement: ")

print("sorry it is quit!!!!!")

Socket.close() 
 
