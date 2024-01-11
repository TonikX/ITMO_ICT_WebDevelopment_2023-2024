import socket
import json

a = int(input("Введите первое основание трапеции: "))
b = int(input("Введите второе основание трапеции: "))
h = int(input("Введите высоту трапеции: "))

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 7777)
conn.connect(server_address)

conn.send(json.dumps({"a": a, "b": b, "h": h}).encode("utf-8"))

data = conn.recv(1024)

print("Площадь трапеции: " + data.decode("utf-8"))

conn.close()