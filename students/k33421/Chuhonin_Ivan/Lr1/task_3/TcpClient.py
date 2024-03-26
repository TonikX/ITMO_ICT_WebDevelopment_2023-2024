import socket
import sys
import time


def run_tcp_client(port: int, buffer_size: int) -> None:
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', port, ))
    except OSError as msg:
        print(msg)
        sys.exit(1)

    if client is None:
        print('could not open client socket')
        sys.exit(1)

    with client:
        data = client.recv(buffer_size)
        print("Client:\n", data.decode('utf-8'))
        time.sleep(3.0)
        # get html again
        hi = 'hi'.encode('utf-8')
        client.sendall(hi)
        data = client.recv(buffer_size)
        print("Client:\nx2\n" + data.decode('utf-8'))
        time.sleep(1.0)
        # stop it
        stop = 'stop'.encode('utf-8')
        client.sendall(stop)
