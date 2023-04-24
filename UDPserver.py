from socket import *
serverPort = 13331
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The Server is listening")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    data = message.decode()
    no_of_char = str(len(data))
    print("Number of characters received by client:", no_of_char)
    sendmessage = "No. of characters in the message: " + no_of_char + "\nMessage: " + data.upper()
    serverSocket.sendto(sendmessage.encode(), clientAddress)