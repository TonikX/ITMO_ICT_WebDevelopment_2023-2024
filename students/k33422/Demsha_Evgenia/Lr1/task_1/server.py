import socket

localIP = "127.0.0.1"
localPort = 9090
bufferSize = 1024

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock = socket.socket()
sock.bind((localIP, localPort))
sock.listen()
conn, addr = sock.accept()

print('connected:', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    print(data.decode())
    conn.sendall('Gamarjoba client'.encode())

conn.close()
