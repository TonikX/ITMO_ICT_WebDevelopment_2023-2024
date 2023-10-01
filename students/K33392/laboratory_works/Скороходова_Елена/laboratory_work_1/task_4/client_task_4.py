import socket
import threading


def send_message(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode())


def receive_message(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            print("Ошибка при получении сообщения")
            break


def main():
    host = 'localhost'
    port = 1221

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    send_thread = threading.Thread(target=send_message, args=(client,))
    receive_thread = threading.Thread(target=receive_message, args=(client,))

    send_thread.start()
    receive_thread.start()


if __name__ == "__main__":
    main()
