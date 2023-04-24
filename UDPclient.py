from socket import *
serverName = "192.168.108.178"
serverPort = 13331
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = "Hello SIT202 from Pallvi (2110994824)"
clientSocket.sendto(message.encode(), (serverName, serverPort))
servermessage, serverAddress = clientSocket.recvfrom(2048)
print(servermessage.decode())
clientSocket.close()