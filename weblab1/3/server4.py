import socket


def get_message():
    data = connection.recv(128).decode()
    log_file.write(f'Message from {address[0]}:{address[1]}: {data}\n')
    return data


def send_message(msg):
    connection.send(msg.encode())
    log_file.write(f'Message to {address[0]}:{address[1]}: {msg}\n')


log_file = open("server4.log", "w")

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('localhost', 55555))

socket.listen(1)
connection, address = socket.accept()

html_file = open('index.html', 'rb')
connection.sendall(b"HTTP/1.1 200 OK\r\n\r\n" + html_file.read())

socket.close()
