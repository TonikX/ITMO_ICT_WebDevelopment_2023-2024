import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((socket.gethostname(), 9090))

while True:
    clientMsg, addr = server.recvfrom(1024)

    if clientMsg.decode() == "shut":
        break

    print(f"Client : {clientMsg.decode()}")

    serverMsg = "Hello, client!"
    server.sendto(serverMsg.encode("utf-8"), addr)

server.close()
