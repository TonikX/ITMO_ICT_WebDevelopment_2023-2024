import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((socket.gethostname(), 1234))
msg, address = s.recvfrom(1234)

print(msg.decode("utf-8"))

