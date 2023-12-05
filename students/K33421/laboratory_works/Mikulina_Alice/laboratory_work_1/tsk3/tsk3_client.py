import socket

def get_html():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8080))
    request = 'GET / HTTP/1.0\r\n\r\n'
    client_socket.sendall(request.encode())
    response = client_socket.recv(1024).decode()
    print(response)
    client_socket.close()

get_html()