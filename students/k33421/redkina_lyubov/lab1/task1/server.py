import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 8080))
data, addr = sock.recvfrom(1024)
decoded_data = data.decode("utf-8")
print("Recieved message:", decoded_data)
sock.sendto(b"Hello, client!", addr)
sock.close()