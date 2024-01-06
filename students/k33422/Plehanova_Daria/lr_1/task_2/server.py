import socket


def pif(a, b):
    return a ** 2 + b ** 2


if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
        conn.bind(('127.0.0.1', 8888))
        conn.listen()
        while True:
            client_conn, addr = conn.accept()
            with client_conn:
                print(f'Connected by {addr}')
                client_conn.sendall(b'Enter a, b: ')
                data = client_conn.recv(1024)
                data = data.decode()
                try:
                    a, b = map(float, data.split(', '))
                    output = f"{pif(a, b)}"
                except ValueError:
                    output = 'Invalid input'
                client_conn.sendall(output.encode())
