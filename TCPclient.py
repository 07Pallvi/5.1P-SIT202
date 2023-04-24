from socket import *
serverName = "192.168.108.178"
serverPort = 14268
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

message = "Hello SIT202 from Pallvi (2110994824)"
clientSocket.send(message.encode())
serverReply = clientSocket.recv(2048)
print(serverReply.decode())
clientSocket.close()