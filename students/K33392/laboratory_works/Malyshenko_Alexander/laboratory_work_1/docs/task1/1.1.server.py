import socket

ip     = "127.0.0.1"
port   = 9090
buffer = 1024

serverMessage  = "Hello, client"
bytesToSend    = str.encode(serverMessage)
UDPSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPSocket.bind((ip, port))

print(" === server is running ===")

while True:
    message, address = UDPSocket.recvfrom(buffer)

    if not message:
        break
    
    message = message.decode("utf-8")
    clientMessage = "Message from Client: {}".format(message)
    print(clientMessage)
    UDPSocket.sendto(bytesToSend, address)