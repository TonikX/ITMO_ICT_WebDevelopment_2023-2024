import socket
import json

a = int(input("Enter the first base of the trapezoid: "))
b = int(input("Enter the second base of the trapezoid: "))
h = int(input("Enter the height of the trapezoid: "))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9090))
sock.send(json.dumps({"a": a, "b": b, "h": h}).encode("utf-8"))

data = sock.recv(1024)
print("The area of a trapezoid is " + data.decode("utf-8"))

sock.close()
