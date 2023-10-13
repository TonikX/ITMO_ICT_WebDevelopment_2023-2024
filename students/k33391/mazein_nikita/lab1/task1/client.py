import socket

# Create a UDP socket object
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('localhost', 1337))

# Send data to server
data = bytes('Hello, server!', 'utf-8')
s.send(data)
print('Sent data to server:', data.decode('utf-8'))

# Receive data from server
data = s.recv(1024)
print('Received data from server:', data.decode('utf-8'))