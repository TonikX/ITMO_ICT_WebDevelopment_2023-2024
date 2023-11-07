from util.decorator import threaded
import socket


def broadcast(message: str, clients: list) -> None:
    for client in clients:
        client.send(message.encode("UTF-8"))


@threaded()
def receive(client_socket: socket.socket, clients: list) -> None:
    if client_socket not in clients:
        clients.append(client_socket)

    try:
        while True:
            data = client_socket.recv(BUFFER_SIZE)

            for client in clients:
                if client != client_socket:
                    client.send(data)
    except ConnectionResetError:
        clients.remove(client_socket)
        broadcast("Один из собеседников вышел.", clients)
        print(f"{client_socket} disconnected.")


if __name__ == "__main__":
    HOST_DATA = ("localhost", 1234)
    BUFFER_SIZE = 2 ** 20

    clients = []

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(HOST_DATA)
        s.listen(10)

        while True:
            try:
                client_socket, client_address = s.accept()
                receive(client_socket, clients)
            except KeyboardInterrupt:
                break
