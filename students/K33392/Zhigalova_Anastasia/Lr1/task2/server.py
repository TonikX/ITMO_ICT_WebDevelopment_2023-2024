import socket

host = 'localhost'
port = 9090
addr = (host, port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(addr)

s.listen()

while True:
        conn, addr = s.accept()
        print('Received new connection from', addr)

        conn.send(b'Enter 2 integers separated by a space')

        data = conn.recv(1024)
        a, b = list(map(int, data.decode('utf-8').split()))
        result = (a**2 + b**2)**0.5
        conn.sendall(str(result).encode('utf-8'))
        conn.close()