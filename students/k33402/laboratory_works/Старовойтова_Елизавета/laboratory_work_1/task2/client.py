import socket

serverAddressPort = ("127.0.0.1", 2005)
bufferSize = 1024

# create TCP socket at client side
tcpClientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# to attach the socket directly to the remote address
tcpClientSock.connect(serverAddressPort)

msgFromServer = tcpClientSock.recvfrom(bufferSize)
print(f'Server: {msgFromServer[0].decode("utf-8")}')

data = input()
tcpClientSock.sendall(data.encode("utf-8"))

msgFromServer = tcpClientSock.recvfrom(bufferSize)
print(f'Server: {msgFromServer[0].decode("utf-8")}')

tcpClientSock.close()
