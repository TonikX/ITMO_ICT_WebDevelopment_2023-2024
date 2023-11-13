import socket

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(('', 2000))

data, clientAdress = server.recvfrom(4096)
print(data.decode("UTF-8"))

server.sendto(bytes("Hello, Client", "UTF-8"),clientAdress)
server.close()