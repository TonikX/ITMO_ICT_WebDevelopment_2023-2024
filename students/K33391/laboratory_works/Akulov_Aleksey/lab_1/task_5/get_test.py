import socket

IP = "127.0.0.1"
PORT = 44455


def test_get_request():
    request = f"GET / HTTP/1.1\r\nHost: {IP}\r\n\r\n"

    test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    test_socket.connect((IP, PORT))
    test_socket.sendall(request.encode())
    response = test_socket.recv(1024)

    print("Response:\n", response.decode())


if __name__ == "__main__":
    test_get_request()
