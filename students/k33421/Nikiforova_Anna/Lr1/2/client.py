import socket
from config import HOST, SERVER_PORT, BUFF_SIZE


if __name__ == '__main__':
    server_address = (HOST, SERVER_PORT)
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
    try:
        conn.connect(server_address)

        response = conn.recv(BUFF_SIZE)
        print(f'Server: {response.decode("utf-8")}')

        coefficients = input()
        conn.sendall(coefficients.encode('utf-8'))

        response = conn.recv(BUFF_SIZE)
        print(f'Server: {response.decode("utf-8")}')
    except ConnectionRefusedError:
        print("Server not avaliable, try again later")

    conn.close()
