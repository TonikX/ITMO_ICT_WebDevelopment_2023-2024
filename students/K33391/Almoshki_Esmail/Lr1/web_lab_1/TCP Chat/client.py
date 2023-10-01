import socket

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
HEAD = 1024
FORMAT = 'utf-8'
ADDRESS = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

nickname_request = client.recv(HEAD)
client.send(bytes("Ais ", FORMAT))
massage_request = client.recv(HEAD)
client.send(bytes("Sub Eman", FORMAT))

while True:
    massage = client.recv(HEAD).decode(FORMAT)
    print(massage)
