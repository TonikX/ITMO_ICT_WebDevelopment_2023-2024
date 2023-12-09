import socket

HOST = "127.0.0.1"
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    prompt = sock.recv(1024).decode()
    print(prompt)
    payload = input()
    sock.send(payload.encode())
    res = sock.recv(1024).decode()
    print(res)