import socket

serverAddressPort = ("127.0.0.1", 2001)
bufferSize = 1024
msgFromServer = "Hello, Client!"

udpServerSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# bind to address and IP
udpServerSock.bind(serverAddressPort)
print("Server is listening")

while True:
    msg, clientAddress = udpServerSock.recvfrom(bufferSize)
    print(f'Received response from client {clientAddress}:  {msg.decode("utf-8")}')
    udpServerSock.sendto(msgFromServer.encode("utf-8"), clientAddress)
