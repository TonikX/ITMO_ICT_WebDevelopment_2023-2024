import socket
import threading
import json

def WaitForMessage(conn):
    while True:
        try:
            data = conn.recv(1024)
            if data:
                print(f"\n{data.decode('utf-8')}")
        except:
            break
    conn.close()

HOST = 'localhost'
PORT = 8081

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

header = b'POST /subject HTTP/1.1\r\nHost: localhost\r\nAccept: text/html\r\nContent-Type: application/json\r\n' # темплейт
# {"capabilities": {}, "desiredCapabilities": {}}
message = 1
while message:
    th = threading.Thread(target=WaitForMessage, args=(s,))
    th.start()
    key = input('Дисциплина: ') # ждем ввода предмета и оценки
    value = input('Оценка: ')
    son_of_j = json.dumps({key: value}) # создаем json
    request = header + f"Content-Length: {len(son_of_j)}\r\n\r\n".encode() + json.dumps({key: value}).encode('utf-8')
    s.send(request)
s.close()