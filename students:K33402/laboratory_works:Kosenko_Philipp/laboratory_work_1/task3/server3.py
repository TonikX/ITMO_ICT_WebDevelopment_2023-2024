import socket

HOST="localhost"
PORT=12123

def req_serv(c_sock):
    request=c_sock.recv(1024).decode()
    print('Received request:\n', request)
    path = request.split()[1]
    if path == '/':
        path = '/index.html'
    try:
        with open('.' + path, 'r') as file:
            content = file.read()
        response = 'HTTP/1.0 200 OK\n\n' + content
    except FileNotFoundError:
        response = 'HTTP/1.0 404 Not Found\n\nFile not found'
    c_sock.sendall(response.encode())
    c_sock.close()


def start_server():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind((HOST, PORT))
    serv.listen(1)
    print('Connected...')


    while True:
        c_sock,adres=serv.accept()
        print("conected", adres)
        req_serv(c_sock)


if __name__ == "__main__":
    start_server()