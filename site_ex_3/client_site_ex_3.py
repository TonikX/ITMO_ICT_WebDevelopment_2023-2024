import socket

def receive_html_page(server_host, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))

    response = b""
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        response += data

    client_socket.close()
    return response

def main():
    server_host = "127.0.0.1"  # IP-адрес сервера
    server_port = 8080  # Порт сервера

    html_response = receive_html_page(server_host, server_port)

    # Печать HTTP-ответа
    print(html_response.decode('utf-8'))

if __name__ == "__main__":
    main()
