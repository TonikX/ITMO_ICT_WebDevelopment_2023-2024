import socket
import threading

IP = "127.0.0.1"
PORT = 44455
codage = 'utf-8'


def receive(client_socket):
    while True:
        message = client_socket.recv(1024).decode(codage)
        print(message)


def send(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode(codage))


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, PORT))

    receive_thread = threading.Thread(target=receive, args = (client_socket, ))
    send_thread = threading.Thread(target=send, args = (client_socket, ))

    receive_thread.start()
    send_thread.start()


if __name__ == "__main__":
    main()
