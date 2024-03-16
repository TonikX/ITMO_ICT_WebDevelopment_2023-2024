import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 1234))
server.listen(5)

timeout = 60

clientsocket, address = server.accept()
msg = clientsocket.recv(1024)

data = msg.decode("utf-8")
arr = data.split(" ")

if len(arr) == 2:
    answ = int(arr[0]) * int(arr[1])
    clientsocket.send(bytes(f"Square: {answ}", "utf-8"))
else:
    clientsocket.send(bytes("Incorrect", "utf-8"))

clientsocket.close()
