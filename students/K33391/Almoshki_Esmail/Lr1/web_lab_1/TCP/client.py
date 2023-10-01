import socket

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 1234
FORMAT = "utf-8"
ADDRESS = (SERVER, PORT)
HEADER = 64


def send_massage(msg):
    encoded_msg = msg.encode(FORMAT)
    client.send(encoded_msg)
    print(client.recv(HEADER).decode(FORMAT))


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)
send_massage("0 0 6")
