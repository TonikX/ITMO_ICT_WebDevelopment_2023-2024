import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 2222)

client_socket.connect(server_address) # У нас же TCP)

while True:
    base = float(input("Введите длину основания параллелограмма: "))
    height = float(input("Введите высоту параллелограмма: "))

    message = f"{base},{height}"
    client_socket.sendall(message.encode())

    data = client_socket.recv(1024) # ждёмс...
    print(data.decode())

