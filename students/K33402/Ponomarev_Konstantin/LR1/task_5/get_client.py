import socket

if __name__ == '__main__':
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _socket.connect(("localhost", 9090))
    _socket.send(b"GET /grades?subject=web HTTP/1.1\nContent-Type: text")

    answer = _socket.recv(1024 * 2).decode()
    print(answer)
