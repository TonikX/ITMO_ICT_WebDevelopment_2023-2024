import socket
import threading


HEADER_LENGTH = 10


def encode_message(msg):
    header = f'{len(msg):<{HEADER_LENGTH}}'.encode('utf-8')
    message = msg.encode('utf-8')

    return header + message


def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)

        if not message_header:
            return False

        message_length = int(message_header.decode('utf-8').strip())

        return client_socket.recv(message_length).decode('utf-8')

    except:
        return False


if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 9092))

    name = input('enter your name =>')
    client_socket.send(encode_message(name))

    def send_messages():
        while True:
            message = input()
            client_socket.send(encode_message(message))
            
    def receive_messages():
        while True:
            message = receive_message(client_socket)
            if message:
                print(message)


    send_messages_thread = threading.Thread(target=send_messages)
    send_messages_thread.start()

    receive_messages_thread = threading.Thread(target=receive_messages)
    receive_messages_thread.start()
