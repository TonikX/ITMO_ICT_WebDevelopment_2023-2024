import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 2002))

request = "GET /scores?subject=test HTTP/1.1\nContent-Type: text"
client.send(request.encode("UTF-8"))

msg = client.recv(2048).decode("UTF-8")
client.close()

print(msg)
