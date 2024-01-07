import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 8080))

discipline = input('Введите предмет: ')
grade = input('Введите отметку: ')

request = "POST /discipline HTTP/1.1\nHost: localhost\nContent-Type: application/x-www-form-urlencoded\nContent-Length: 38\n\n"
body = f"discipline={discipline}&grade={grade}"

sock.send((request + body).encode())

response = sock.recv(2*1024).decode()
print(response)