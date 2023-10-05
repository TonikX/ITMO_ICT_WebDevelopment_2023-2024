import socket


def get_index():
    with open("res/index.html", 'r') as file:
        index = file.read()

    return f'HTTP/1.0 200 OK\nContent-Type: text/html\n\n{index}'


if __name__ == "__main__":
    HOST = "localhost"
    PORT = 1234

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(10)
        while True:
            try:
                client_socket, client_address = s.accept()
                client_socket.send(get_index().encode("UTF-8"))
            except KeyboardInterrupt:
                break
