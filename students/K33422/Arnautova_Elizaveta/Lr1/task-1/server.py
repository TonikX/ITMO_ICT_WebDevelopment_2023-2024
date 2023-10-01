import socket
HOST = '127.0.0.1'
SERVER_PORT = 14900
BUFF_SIZE = 16384

if __name__ == '__main__':
    server_address = (HOST, SERVER_PORT)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as conn:  # UDP
        conn.bind(server_address)  # открытие сокета
        print('Server is waiting...')

        timeout = 30
        while True:
            conn.settimeout(timeout)
            try:
                data, client_address = conn.recvfrom(BUFF_SIZE)  # получение данных
            except socket.timeout:
                print('Time is out. {0} seconds have passed'.format(timeout))
                break

            print(f'Received message from {client_address}: {data.decode("utf-8")}')  # декодирование данных

            message = 'Hello, client!'
            conn.sendto(message.encode('utf-8'), client_address)

