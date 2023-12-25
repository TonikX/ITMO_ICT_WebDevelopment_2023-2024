import socket

BUFFER = 2048

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 8080))

discipline = input('Введите название предмета: ')
grade = input('Введите оценку: ')

request = "POST /discipline HTTP/1.1\nHost: localhost\nContent-Type: application/x-www-form-urlencoded\nContent-Length: 38\n\n"
body = f"subject={discipline}&grade={grade}"

sock.send((request + body).encode())

response = sock.recv(BUFFER).decode()
print(response)