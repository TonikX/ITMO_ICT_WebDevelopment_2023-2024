import socket

HOST = "127.0.0.1"
PORT = 8080

try:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((HOST, PORT))
        while True:
            data, addr = sock.recvfrom(1024)
            print(f"Msg: {data.decode()}")
            sock.sendto(b"Hello, client", addr)
except KeyboardInterrupt:
    exit()