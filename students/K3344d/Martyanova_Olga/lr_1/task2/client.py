import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 9090)
client_socket.connect(server_address)


a = input("Enter a: ")
b = input("Enter b: ")
c = input("Enter c: ")

params = f"{a}, {b}, {c}"
client_socket.send(params.encode())

response = client_socket.recv(1024)
result = response.decode('utf-8')
print(f"Result: {result}")

client_socket.close()
