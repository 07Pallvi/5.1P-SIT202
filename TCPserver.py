from socket import *
serverPort = 14268
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is listening")

while True:
    connectClientSocket, addr = serverSocket.accept()
    message = connectClientSocket.recv(2048)
    data = message.decode()
    no_of_char = str(len(data))
    print("Number of characters received by client:", no_of_char)
    sendmessage = "No. of characters in the message: " + no_of_char + "\nMessage: " + data.upper()
    connectClientSocket.send(sendmessage.encode())
