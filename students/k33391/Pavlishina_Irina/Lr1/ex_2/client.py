import socket
import threading
import random
import time

"""
    
"""

PORT = 8080


def listen_chat(client_socket):
    """
    Function for listening server connection
    :param client_socket: socket of the client
    :return: Nothing
    """
    while True:
        ans = client_socket.recv(1024).decode('utf-8')
        print(ans)


def write_chat(client_socket):
    """
    Function for recieves from server connection
    :param client_socket: socket of the client
    :return: Nothing
    """
    while True:
        client_socket.sendall(f'{random.randint(-100, 100)} {random.randint(-100, 100)} {random.randint(-100, 100)}'
                              .encode('utf-8'))
        time.sleep(1)


def main():
    """
    Main function
    :return: Nothing
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', PORT))

    listen = threading.Thread(target=listen_chat, args=(client_socket,))
    listen.start()

    write = threading.Thread(target=write_chat, args=(client_socket,))
    write.start()


if __name__ == "__main__":
    main()
