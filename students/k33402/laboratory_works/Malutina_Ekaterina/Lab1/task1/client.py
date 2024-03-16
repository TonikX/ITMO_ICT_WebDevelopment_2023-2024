import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = "Hello, server"
client.sendto(msg.encode("utf-8"), (socket.gethostname(), 1234))

data = client.recvfrom(1024)
server_msg = data[0]

print(server_msg.decode("utf-8"))

client.close()
