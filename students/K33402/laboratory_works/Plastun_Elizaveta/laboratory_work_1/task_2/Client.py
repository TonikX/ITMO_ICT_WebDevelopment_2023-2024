import socket

clients_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clients_socket.connect((socket.gethostname(), 6666))

a = input("enter the height of the parallelogram:\n")
b = input("enter the parallelogram edge value:\n")
data = a + " " + b
print(type(data))
clients_socket.send(data.encode())

serverMessage, addr = clients_socket.recvfrom(1024)

print(f"Server says: {serverMessage.decode()}")

clients_socket.close()
