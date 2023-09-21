import socket

# Теорема Пифагора


def pythagoreantheorem(data):
    strvalue_1, strvalue_2 = data.decode("utf-8").split(",")
    try:
        value_1 = int(strvalue_1)
        value_2 = int(strvalue_2)
        answer = f"{pow(pow(value_1, 2) + pow(value_2, 2), 0.5)}"
        return answer.encode()
    except:
        return b"Incorrect data"


conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind((socket.gethostname(), 1236))
conn.listen(10)
while True:
    try:
        clientsocket, address = conn.accept()
        data = clientsocket.recv(1024)
        answer = pythagoreantheorem(data)
        clientsocket.send(answer)
    except KeyboardInterrupt:
        conn.close()
        break
