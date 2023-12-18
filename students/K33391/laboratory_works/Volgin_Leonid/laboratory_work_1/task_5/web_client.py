import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 2002))
def post():
    discipline = input('discipline: ')
    grade = input('grade: ')

    request = "POST /discipline HTTP/1.1\nHost: localhost\nContent-Type: application/x-www-form-urlencoded\nContent-Length: 38\n\n"
    body = f"discipline={discipline}&grade={grade}"

    # print(request+body)
    client.send((request + body).encode("UTF-8"))

    answer = client.recv(2048).decode("UTF-8")
    print(answer)

def get():
    request = "GET /scores?subject=test HTTP/1.1\nContent-Type: text"
    client.send(request.encode("UTF-8"))

    msg = client.recv(2048).decode("UTF-8")
    print(msg)


while True:
    action = input()
    if action == "post":
        post()
    elif action == "get":
        get()
    else:
        break

client.close()
