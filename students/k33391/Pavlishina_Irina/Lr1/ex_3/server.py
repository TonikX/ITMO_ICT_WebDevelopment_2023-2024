import socket
import threading


def chat(client_socket):
    while True:
        client_socket.recv(1000)
        response_type = 'HTTP/1.0 200 OK\n'
        headers = 'Content-Type: text/html\n\n'
        with open('index.html', 'r') as f:
            body = f.read()

        response = response_type + headers + body
        client_socket.send(response.encode('utf-8'))


def main():
    TCP_PORT = 8080
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', TCP_PORT))
    server_socket.listen(5)

    while True:
        try:
            client_socket, client_address = server_socket.accept()
            thread = threading.Thread(target=chat, args=(client_socket, ))
            thread.start()

        except KeyboardInterrupt:
            server_socket.close()
            break


if __name__ == "__main__":
    main()