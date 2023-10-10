import socket

servers_sockets = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servers_sockets.bind((socket.gethostname(), 6666))

while True:
    clientMessage, addr = servers_sockets.recvfrom(1024)
    print(f"Client says: {clientMessage.decode()}")
    serverMessage = "Hello Client!"
    servers_sockets.sendto(serverMessage.encode("utf-8"), addr)
    if False:
        break

servers_sockets.close()
