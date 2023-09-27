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
    clients = []

    server_socket = socket.socket()
    server_socket.bind(('', 9092))
    server_socket.listen()


    def accept_client():
        while True:
            client_socket, addr = server_socket.accept()
            username = receive_message(client_socket)

            next_client = (client_socket, username)

            clients.append(next_client)
            print(f'{username} connected')

            next_client_thread = threading.Thread(target=get_message_from_client, args=(next_client,))
            next_client_thread.start()


    def get_message_from_client(next_client):
        client_socket, username = next_client
        while True:
            message = receive_message(client_socket)
            message_to_send = encode_message(f'{username}: {message}')

            if message:
                print(f'{username} sent {message}')
                for notify_client, u in clients:
                    if notify_client != client_socket:
                        notify_client.send(message_to_send)
                        print(f'sent {message} to {u}')
            else:
                print(f'{username} disconnected')
                clients[:] = [i for i in clients if i[0] != client_socket]
                break

    thread_accept_client = threading.Thread(target=accept_client)
    thread_accept_client.start()
