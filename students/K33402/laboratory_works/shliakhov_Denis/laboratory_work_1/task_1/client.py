import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.connect((socket.gethostname(), 9090))

client.send("Hello Server".encode())

serverMsg, addr = client.recvfrom(1024)

print(f"Server: {serverMsg.decode()}")

client.close()
