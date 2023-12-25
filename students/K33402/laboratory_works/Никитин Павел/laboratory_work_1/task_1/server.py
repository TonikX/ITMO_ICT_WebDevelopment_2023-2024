import socket

# Создаем UDP сервер
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ("localhost", 12345)

server_socket.bind(server_address)
print("Сервер ожидает сообщения...")

while True:
    data, client_address = server_socket.recvfrom(1024)
    print(f"Получено сообщение от клиента: {data.decode()}")

    response = b"Hello, client"
    server_socket.sendto(response, client_address)
