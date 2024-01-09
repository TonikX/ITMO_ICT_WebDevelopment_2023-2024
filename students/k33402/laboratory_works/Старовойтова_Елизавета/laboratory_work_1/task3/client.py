import socket

serverAddressPort = ("127.0.0.1", 8100)
bufferSize = 1024

# create TCP socket at client side
tcpClientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# to attach the socket directly to the remote address
tcpClientSock.connect(serverAddressPort)

response = tcpClientSock.recv(bufferSize)
print(f'Server: {response.decode()}')

tcpClientSock.close()
