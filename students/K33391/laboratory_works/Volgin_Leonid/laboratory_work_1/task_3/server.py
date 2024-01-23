import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 2001))
server.listen(1)

clientSocket, clientAdress = server.accept()
response_type = "HTTP/1.0 200 OK\n"
headers = "Content-Type: text/html\n\n"

file1 = open("index.html", "r")
body =''
while True:
    line = file1.readline()
    body+=line
    if not line:
        break
file1.close()

response = response_type+headers+body
clientSocket.send(response.encode("UTF-8"))
clientSocket.close()
print(response)