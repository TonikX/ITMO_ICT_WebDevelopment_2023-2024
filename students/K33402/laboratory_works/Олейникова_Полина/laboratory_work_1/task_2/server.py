import socket
import json


def calculate_trapezoid_area(a, b, h):
    return ((a + b) * h) / 2


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 9090))
sock.listen()
connection, address = sock.accept()

while True:
    data = connection.recv(1024)
    if not data:
        break
    params = json.loads(data.decode("utf-8"))
    res = calculate_trapezoid_area(**params)
    connection.send(str(res).encode("utf-8"))

connection.close()
