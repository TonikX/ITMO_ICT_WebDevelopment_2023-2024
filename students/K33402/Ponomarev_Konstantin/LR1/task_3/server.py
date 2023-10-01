import socket


def generate_http_response():
    html_content = open('index.html', 'r', encoding='utf-8').read()

    http_header = "HTTP/1.1 200 OK\r\n"
    http_header += "Content-Type: text/html; charset=UTF-8\r\n"
    http_header += f"Content-Length: {len(html_content.encode('utf-8'))}\r\n"
    http_header += "\r\n"
    http_response = http_header + html_content
    return http_response


def init_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 9090)
    server_socket.bind(server_address)
    server_socket.listen(1)

    print("wait client...")
    client, client_address = server_socket.accept()
    print(f"Connected client: {client_address}")
    while True:
        try:
            request = client.recv(1024).decode('utf-8')
            http_response = generate_http_response()
            client.send(http_response.encode('utf-8'))
            client.close()
            break
        except Exception as e:
            print(f"ERROR: {str(e)}")
            client.send(str(e).encode("utf-8"))
            break

    server_socket.close()


if __name__ == '__main__':
    init_server()
