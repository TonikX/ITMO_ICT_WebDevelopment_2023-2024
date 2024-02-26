import socket

ip     = "127.0.0.1"
port   = 9090
buffer = 1024

serverMessage  = "Hello, client"
bytesToSend    = str.encode(serverMessage)
# Создание сокета сервера, type=socket.SOCK_DGRAM - UDP протокол
UDPSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPSocket.bind((ip, port))
print(" === server is running ===")

while True:
    #получеам сообщение от клиента и его адрес
    message, address = UDPSocket.recvfrom(buffer)

    if not message:
        break
    
    message = message.decode("utf-8")
    clientMessage = "Message from Client: {}".format(message)
    print(clientMessage)
    #отправляем сообщение по адресу клиента
    UDPSocket.sendto(bytesToSend, address)