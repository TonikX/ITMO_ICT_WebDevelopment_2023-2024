import socket
HOST = '127.0.0.1'
SERVER_PORT = 14900
BUFF_SIZE = 16384

if __name__ == '__main__':
    server_address = (HOST, SERVER_PORT)
    conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP

    message = 'Hello, server!'
    try:
        conn.sendto(message.encode('utf-8'), server_address)
        response = conn.recv(BUFF_SIZE)
        print(f'Received response from server: {response.decode("utf-8")}')
    except ConnectionResetError:
        print("Received no response from server, try again later")

    conn.close()


