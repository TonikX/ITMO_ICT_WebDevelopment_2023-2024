import socket
import pickle
import math


def run():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 9090))
    sock.listen(1)

    while True:
        conn, addr = sock.accept()

        data = conn.recv(1024)

        if not data:
            break

        a, b = pickle.loads(data)

        if not a or not b:
            conn.send('a and b must be present and be type of number'.encode('utf-8'))

        res = math.sqrt(float(a)**2 + float(b)**2)

        conn.send(str(res).encode('utf-8'))

        conn.close()


if __name__ == '__main__':
    run()
