import socket
import threading


def handle_messages(connection: socket.socket):
    while True:
        try:
            message = connection.recv(1024)
            if message is not None and message != b"":
                print(message.decode("utf-8"))
        except Exception:
            connection.close()


def send_to_chat(connection: socket.socket):
    while True:
        try:
            message = input("Введите ваше сообщение")
            if message != "Quit":
                connection.send(message.encode("utf-8"))
            else:
                connection.send(message.encode("utf-8"))
                print("Bye")
                connection.close()
                break
        except OSError:
            break


if __name__ == "__main__":
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    _socket.connect(("localhost", 9090))

    handleThread = threading.Thread(target=handle_messages, args=[_socket], name="Handle thread")
    handleThread.start()
    sendToChatThread = threading.Thread(target=send_to_chat, args=[_socket], name="Send to chat thread")
    sendToChatThread.start()
