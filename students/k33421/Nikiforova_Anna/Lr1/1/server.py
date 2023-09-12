import socket
from config import HOST, SERVER_PORT, BUFF_SIZE


if __name__ == '__main__':
    server_address = (HOST, SERVER_PORT)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as conn:  # UDP
        conn.bind(server_address)
        print('Server is listening...')

        while True:
            data, client_address = conn.recvfrom(BUFF_SIZE)
            print(f'Received message from {client_address}: {data.decode("utf-8")}')

            message = 'Hello, client!'
            conn.sendto(message.encode('utf-8'), client_address)
