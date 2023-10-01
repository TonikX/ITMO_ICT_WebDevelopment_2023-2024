import socket
import threading


def handle_messages(connection: socket.socket):
    message = connection.recv(1024)
    while message is not None and message != b'':
        print(f"\n{message.decode()}", end="")
    _socket.close()
    print("Bye!")


if __name__ == "__main__":
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    _socket.connect(("localhost", 9090))

    t = threading.Thread(target=handle_messages, args=(_socket,))
    t.start()

    while True:
        try:
            _socket.send(input("Write your messages at console: "))
        except OSError:
            break
