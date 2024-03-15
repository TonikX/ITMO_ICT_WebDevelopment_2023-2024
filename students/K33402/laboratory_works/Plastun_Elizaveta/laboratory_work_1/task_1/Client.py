import socket

clients_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clients_socket.connect((socket.gethostname(), 6666))

clients_socket.send("Hello Server!".encode())

serverMessage, addr = clients_socket.recvfrom(1024)

print(f"Server says: {serverMessage.decode()}")

clients_socket.close()
