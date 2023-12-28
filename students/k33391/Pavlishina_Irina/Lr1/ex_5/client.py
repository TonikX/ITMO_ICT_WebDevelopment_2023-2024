import socket


def main():
    PORT = 5321

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', PORT))
    client_socket.send(b"POST /journal/add?subject=Maths&mark=4 HTTP/1.1\r\nHost:www.example.com\r\nAccept:text/html\r\n\r\n")

    #client_socket.send(b"GET /journal/subject?subject=Maths HTTP/1.1\r\nHost:www.example.com\r\nAccept:text/html\r\n\r\n")
    response = client_socket.recv(4096)
    client_socket.close()
    print(response.decode())


if __name__ == "__main__":
    main()
