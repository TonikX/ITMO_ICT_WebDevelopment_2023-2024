import socket
from config import HOST, SERVER_PORT, BUFF_SIZE


if __name__ == '__main__':
    server_address = (HOST, SERVER_PORT)
    conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP

    message = 'Hello, server!'
    try:
        conn.sendto(message.encode('utf-8'), server_address)
        response = conn.recv(BUFF_SIZE)
        print(f'Received response from server: {response.decode("utf-8")}')
    except ConnectionResetError:
        print("Server not avaliable, try again later")

    conn.close()
