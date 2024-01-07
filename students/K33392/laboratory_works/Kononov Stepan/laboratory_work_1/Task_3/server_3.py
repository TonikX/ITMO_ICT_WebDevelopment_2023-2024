import socket

HDRS_404 = 'HTTP/1.1 404 Not Found\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
HDRS_200 = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'

SERVER_PORT = 2000


def start_server():
    print("Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind(('127.0.0.1', SERVER_PORT))
        server.listen(1)
        print(f'Server is listening on port {SERVER_PORT}')

        while True:
            print("Waiting for incoming connection...")
            client_socket, address = server.accept()
            print(f"Accepted connection from {address}")

            try:
                handle_client_request(client_socket)
            except Exception as e:
                print(f"Error handling client request: {e}")

    except KeyboardInterrupt:
        server.close()
        print("Server shutdown")
    except Exception as e:
        print(f"Server error: {e}")


def handle_client_request(client_socket):
    data = client_socket.recv(1024).decode('utf-8')
    content = load_page_from_get_request(data)
    client_socket.send(content)
    client_socket.shutdown(socket.SHUT_WR)
    client_socket.close()


def load_page_from_get_request(request_data):
    path = request_data.split(' ')[1]
    try:
        with open('views' + path, 'rb') as file:
            response = file.read()
        return HDRS_200.encode('utf-8') + response
    except FileNotFoundError:
        return (HDRS_404 + "Sorry...").encode('utf-8')


if __name__ == '__main__':
    start_server()
