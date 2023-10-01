import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 9090))

discipline = input('Введите название предмета: ')
mark = input('Введите оценку: ')

request = "POST /discipline HTTP/1.1\nHost: localhost\nContent-Type: " \
          "application/x-www-form-urlencoded\nContent-Length: 38\n\n"
body = f"subject={discipline}&mark={mark}"

sock.send((request + body).encode())

response = sock.recv(1024).decode()
print(response)
