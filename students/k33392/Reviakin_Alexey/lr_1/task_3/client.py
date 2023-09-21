import socket

conn = socket.socket()

conn.connect((socket.gethostname(), 12355))
conn.send(b"Hello")
data = conn.recv(1000)
udata = data.decode("utf-8")
print(udata)
