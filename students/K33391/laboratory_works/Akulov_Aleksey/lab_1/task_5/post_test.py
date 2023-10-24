import socket


def test_post_request():
    IP = "127.0.0.1"
    PORT = 44455

    grades = {
        'Math2': '4',
        'PE': '5',
        'Eng': '2'
    }

    data = ';'.join([f"{key}:{value}" for key, value in grades.items()])

    headers = f"POST / HTTP/1.1\r\nContent-Length: {len(data)}\r\n\r\n{data}"

    test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    test_socket.connect((IP, PORT))
    test_socket.sendall(headers.encode())
    response = test_socket.recv(1024)

    print("Response:\n", response.decode())


if __name__ == "__main__":
    test_post_request()
