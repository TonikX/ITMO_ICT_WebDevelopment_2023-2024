import socket

HOST = '127.0.0.1'
SERVER_PORT = 14900
BUFF_SIZE = 16384

if __name__ == '__main__':
    server_address = (HOST, SERVER_PORT)
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
    try:
        conn.connect(server_address)
        print(f'Server: {conn.recv(BUFF_SIZE).decode("utf-8")}')  # получение запроса параметров трапеции

        params = input()
        conn.sendall(params.encode('utf-8'))  # отправка серверу параметров

        print(f'Server: {conn.recv(BUFF_SIZE).decode("utf-8")}')  # выдача результата
    except ConnectionRefusedError:
        print("Server not avaliable, try again later")

    conn.close()
