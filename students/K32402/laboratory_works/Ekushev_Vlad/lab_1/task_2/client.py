import socket

# Using TCP connection (SOCK_STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 9090)
client.connect(server_address)

baseA = float(input('Length of the first base: '))
baseB = float(input('Length of the second base: '))
height = float(input('Height of the trapezoid: '))

SEP = ';'
data = SEP.join(map(str, [baseA, baseB, height]))
client.send(data.encode())
res = client.recv(1024).decode()
print(f'Area of the trapezoid: {res}')
client.close()
