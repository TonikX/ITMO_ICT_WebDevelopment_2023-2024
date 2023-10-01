import socket


def generate_http_response():
    with open('index.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    http_response = "HTTP/1.1 200 OK\r\n"
    http_response += "Content-Type: text/html; charset=UTF-8\r\n"
    http_response += f"Content-Length: {len(html_content.encode('utf-8'))}\r\n"
    http_response += "\r\n"

    http_response += html_content

    return http_response


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 8080)
    server_socket.bind(server_address)
    server_socket.listen(1)
    print("Ожидание подключения клиента...")
    client_socket, client_address = server_socket.accept()
    print(f"Подключен клиент: {client_address}")
    while True:
        try:
            request = client_socket.recv(1024).decode('utf-8')
            http_response = generate_http_response()
            client_socket.send(http_response.encode('utf-8'))
            client_socket.close()
            break
        except Exception as e:
            print(f"Ошибка: {str(e)}")
            break

    server_socket.close()


if __name__ == '__main__':
    main()