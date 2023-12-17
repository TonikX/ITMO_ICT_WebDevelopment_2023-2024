import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 49001))


data, adr = sock.recvfrom(1024)
print(data.decode("utf-8"))
response = b"Message received. Hello client!"
sock.sendto(response, adr)

sock.close()