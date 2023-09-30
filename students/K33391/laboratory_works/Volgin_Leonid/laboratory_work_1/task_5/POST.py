import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 2002))

discipline = input('discipline: ')
grade = input('grade: ')

request = "POST /discipline HTTP/1.1\nHost: localhost\nContent-Type: application/x-www-form-urlencoded\nContent-Length: 38\n\n"
body = f"discipline={discipline}&grade={grade}"

client.send((request + body).encode("UTF-8"))

answer = client.recv(2048).decode("UTF-8")
client.close()

print(answer)