import socket

# Создаем UDP-сервер
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 12345)
server_socket.bind(server_address)

while True:
    print("Ожидание сообщения от клиента...")
    data, client_address = server_socket.recvfrom(1024)
    print(f"Получено сообщение от клиента: {data.decode()}")

    response = "Hello, client"
    server_socket.sendto(response.encode(), client_address)