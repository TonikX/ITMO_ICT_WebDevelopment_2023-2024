import socket

host = '127.0.0.1'
port = 14560
bufferSize = 1024


tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSock.connect((host, port))

subj = input('Enter the subject: ')
grade = input('Enter the grade: ')

request = "POST /subj HTTP/1.1\nHost: localhost\nContent-Type: application/x-www-form-urlencoded\nContent-Length: 38\n\n"
body = f"subj={subj}&grade={grade}"

tcpSock.send((request + body).encode('utf-8'))
response = tcpSock.recv(bufferSize).decode('utf-8')
print(response)
