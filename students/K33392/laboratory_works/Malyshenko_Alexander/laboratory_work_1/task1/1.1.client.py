import socket

clientMessage   = "Hello, Server"
bytesToSend     = str.encode(clientMessage)
serverAdress    = ("127.0.0.1", 9090)
buffer          = 1024

UDPSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
#отправляем сообщение по адресу сервера
UDPSocket.sendto(bytesToSend, serverAdress)
#считываем сообщение от сервера
serverMessage = UDPSocket.recvfrom(buffer)

serverMessage = serverMessage[0].decode("utf-8")
serverMessage = "Message from Server: {}".format(serverMessage)
print(serverMessage)