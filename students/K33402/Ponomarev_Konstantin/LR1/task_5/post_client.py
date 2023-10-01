import socket

if __name__ == '__main__':
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _socket.connect(("localhost", 9090))
    _socket.send(b"POST /subject?name=web&grade=5 HTTP/1.1\nContent-Type: application/x-www-form-urlencoded")
    print(_socket.recv(1024 * 4).decode())
