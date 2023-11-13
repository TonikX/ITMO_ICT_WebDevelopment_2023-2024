import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 9090))
send_data = "Gamarjoba Server!"
sock.send(send_data.encode())

receive_data = sock.recv(1024)
print(receive_data.decode())
sock.close()

