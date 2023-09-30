import socket


def process_request():

    with open('index.html', 'r') as file:
        html = file.read()

    response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + html

    return response


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12345)
server_socket.bind(server_address)

server_socket.listen(1)

while True:
    print("Ожидание подключения клиента...")
    client_socket, client_address = server_socket.accept()

    print("Подключение от", client_address)

    request = client_socket.recv(1024).decode()

    response = process_request()

    client_socket.send(response.encode())

    client_socket.close()
