import socket

host = '127.0.0.1'
port = 14560
bufferSize = 1024


tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSock.connect((host, port))

request = "GET /scores?subj=test HTTP/1.1\nContent-Type: text"
tcpSock.send(request.encode('utf-8'))

response = tcpSock.recv(bufferSize).decode('utf-8')
print(response)
