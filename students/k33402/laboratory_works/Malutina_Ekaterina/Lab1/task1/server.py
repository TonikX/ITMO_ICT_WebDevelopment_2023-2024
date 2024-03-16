import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((socket.gethostname(), 1234))

timeout = 60

data = server.recvfrom(1024)

client_msg = data[0]
addr = data[1]

print(client_msg.decode("utf-8"))

msg = "Hello, client"
server.sendto(msg.encode("utf-8"), addr)

server.close()
