import socket

msgFromClient = "Hello, Server!"
serverAddressPort = ("127.0.0.1", 2001)
bufferSize = 1024

# create UDP socket at client side
udpClientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# sent msg to server
udpClientSock.sendto(msgFromClient.encode('utf-8'), serverAddressPort)

msgFromServer = udpClientSock.recvfrom(bufferSize)
print(f'Received response from server: {msgFromServer[0].decode("utf-8")}')






