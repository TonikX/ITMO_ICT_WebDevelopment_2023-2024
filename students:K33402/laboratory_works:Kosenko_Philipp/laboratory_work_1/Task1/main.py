import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 1234
MESSAGE = "Hello, server"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))
data, addr = sock.recvfrom(1024)
print("Ответ сервера:", data.decode())
sock.close()





