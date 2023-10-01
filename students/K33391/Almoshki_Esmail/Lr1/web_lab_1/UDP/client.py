import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(bytes("Hello, server", "utf-8"),(socket.gethostname(),1234))

