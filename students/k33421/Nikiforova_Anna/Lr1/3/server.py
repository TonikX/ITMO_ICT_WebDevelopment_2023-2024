import socket
from config import HOST, SERVER_PORT


def handle_client(client_socket):
    # про формат http-сообщений: https://selectel.ru/blog/http-request/
    http_response = """HTTP/1.1 200 OK
Content-Type: text/html

{}
""".format(html_content)
    client_socket.sendall(http_response.encode())
    client_socket.close()


if __name__ == '__main__':
    with open('index.html', 'r') as html_file:
        html_content = html_file.read()

    server_address = (HOST, SERVER_PORT)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
        conn.bind(server_address)
        conn.listen(10)
        print('Server is listening...')

        while True:
            client_conn, addr = conn.accept()
            print(f"Connected by {addr}")
            handle_client(client_conn)
