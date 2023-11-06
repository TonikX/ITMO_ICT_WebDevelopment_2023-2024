import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 1234
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
data, addr = sock.recvfrom(1024)
print("Полученные данные:", data.decode())
MESSAGE = "Hello, client"
sock.sendto(MESSAGE.encode(), addr)
sock.close()

