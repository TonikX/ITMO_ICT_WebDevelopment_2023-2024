import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(('localhost', 8080))
sock.send(b"Hello, server!")
data = sock.recv(1024)
decoded_data = data.decode("utf-8")
print("Recieved message:", decoded_data)
sock.close()