import socket

if __name__ == '__main__':
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(("127.0.0.1", 14900))
    response = conn.recv(16384).decode('utf-8')
    print('From server: ' + response)
