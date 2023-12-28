import socket
import threading

PORT = 8080

def listen_chat(client_socket):
    while True:
        response = client_socket.recv(1024).decode('utf-8')
        print(response)


def write_chat(client_socket):
    while True:
        client_socket.send(b"GET / HTTP/1.0\r\nHost:localhost\r\n\r\n")


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', PORT))

    listen = threading.Thread(target=listen_chat, args=(client_socket,))
    listen.start()

    write = threading.Thread(target=write_chat, args=(client_socket,))
    write.start()


if __name__ == "__main__":
    main()