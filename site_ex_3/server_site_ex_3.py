import socket

def send_html_page(client_socket):
    with open("webpage.html", "rb") as file:
        html_content = file.read()
    response = "HTTP/1.1 200 OK\nContent-Type: text/html\nContent-Length: {}\n\n".format(len(html_content)).encode('utf-8')
    response += html_content
    client_socket.send(response)

def main():
    server_host = "127.0.0.1"  # IP-адрес сервера
    server_port = 8080  # Порт сервера

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_host, server_port))
    server_socket.listen(1)
    print(f"Сервер слушает на {server_host}:{server_port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Подключено клиентов с адреса: {client_address}")
        send_html_page(client_socket)
        client_socket.close()

if __name__ == "__main__":
    main()
