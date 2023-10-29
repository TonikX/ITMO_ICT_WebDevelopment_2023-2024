import socket

# Загружаем содержимое HTML-файла
with open("index.html", "r") as file:
    html_content = file.read()

# Создаем HTTP-сервер
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8080)
server_socket.bind(server_address)

server_socket.listen(1)
print("Сервер запущен. Ожидание подключения клиента...")

while True:
    client_connection, client_address = server_socket.accept()
    print(f"Подключение от клиента {client_address}")

    http_response = f"HTTP/1.1 200 OK\r\nContent-Length: {len(html_content)}\r\n\r\n{html_content}"
    client_connection.sendall(http_response.encode())
    client_connection.close()
