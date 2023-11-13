import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 8080))

question = client_socket.recv(1024).decode()
print(question)
user_input = input()

client_socket.send(user_input.encode())
result = client_socket.recv(1024).decode()
print(result)

client_socket.close()