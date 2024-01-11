import socket 
import json

def trapez_area_count(a, b, h):
    area = ((a+b)*h)/2
    return area

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 7777)

conn.bind(server_address)
conn.listen()

connect, address = conn.accept()

while True:
    data = connect.recv(1024)
    if not data:
        break
    vars = json.loads(data.decode())
    connect.send(str(trapez_area_count(**vars)).encode("utf-8"))

connect.close()
    