import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8080)
server_socket.bind(server_address)


server_socket.listen(1)
print("Сервер ожидает подключения клиента...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Подключен клиент с адресом: {client_address}")

    try:
        with open("index.html", "r") as file:
            html_content = file.read()
        http_response = f"HTTP/1.1 200 OK\nContent-Length: {len(html_content)}\n\n{html_content}"
        client_socket.send(http_response.encode('utf-8'))

    except Exception as e:
        print(f"Ошибка при обработке запроса: {e}")

    finally:
        client_socket.close()


