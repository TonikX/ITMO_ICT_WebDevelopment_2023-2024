import socket

# Подключаемся к серверу
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ("localhost", 12345)

message = b"Hello, server"

try:
    client_socket.sendto(message, server_address)
    data, server = client_socket.recvfrom(1024)
    print(f"Сервер ответил: {data.decode()}")

finally:
    client_socket.close()
