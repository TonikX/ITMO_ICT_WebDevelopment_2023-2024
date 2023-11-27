from socket import *
if __name__ == "__main__":
    ip= '127.0.0.1'
    port = 3000

    client = socket(AF_INET, SOCK_STREAM)
    client.connect((ip, port))

    request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
    client.send(request.encode('utf-8'))

    response = client.recv(1024).decode('utf-8')
    print(response)
