import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("localhost", 9090))

subj = input('Enter the subject: ')
grade = input('Enter the grade: ')

request = "POST /subj HTTP/1.1\nHost: localhost\nContent-Type: text\n"
body = f"subj={subj}&grade={grade}"

conn.send((request + body).encode('utf-8'))
response = conn.recv(1024).decode('utf-8')
print(response)