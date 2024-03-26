import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Создаем сокет
server_address = ('localhost', 2222)
server_socket.bind(server_address)

print(f"Сервер слушает)")

while True:
    data, client_address = server_socket.recvfrom(1024) # Ждемc
    print(f"Получено от клиента ({client_address}): {data.decode()}")
    server_socket.sendto(b"Hello, client", client_address) # наконец я нашёл применение к этому префексу :D
