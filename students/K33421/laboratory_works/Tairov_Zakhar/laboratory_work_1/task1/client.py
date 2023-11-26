import socket

HOST = "127.0.0.1"
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.sendto(b"Hello, server", (HOST, PORT))
    data, _ = sock.recvfrom(1024)
    print(f"Msg: {data.decode()}")