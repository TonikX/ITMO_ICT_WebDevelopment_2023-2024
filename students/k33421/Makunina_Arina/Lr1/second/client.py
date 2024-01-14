import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5434)
client_socket.connect(server_address)

base1 = float(input("Введите значение верхней основы трапеции: "))
base2 = float(input("Введите значение нижней основы трапеции: "))
height = float(input("Введите значение высоты трапеции: "))

request = f"{base1},{base2},{height}"
client_socket.send(request.encode())
response = client_socket.recv(1024).decode()
print(f"Ответ от сервера: {response}")
client_socket.close()
