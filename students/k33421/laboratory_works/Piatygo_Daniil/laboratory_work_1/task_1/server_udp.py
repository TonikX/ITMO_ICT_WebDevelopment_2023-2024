import socket


conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
conn.bind(("127.0.0.1", 5000))

while True:
    data, addr = conn.recvfrom(1024)
    print(data.decode("utf-8"))
    conn.sendto(b"Hello, client", addr)
