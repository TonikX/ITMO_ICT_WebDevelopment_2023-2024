import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("localhost", 9090))

request = "GET /scores?subj=test HTTP/1.1\nContent-Type: text"
conn.send(request.encode('utf-8'))

response = conn.recv(1024).decode('utf-8')
print(response)