import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8080))

data = sock.recv(1024)
decoded_data = data.decode("utf-8")
print("Received message:", decoded_data)

sock.close()