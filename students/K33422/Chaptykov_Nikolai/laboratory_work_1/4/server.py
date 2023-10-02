import socket
import sys
import threading

clients = []

def Emojify(addr):
    emoji = b"\\" + f"U0001F{addr % 1000}".encode()
    return emoji.decode('unicode_escape')

def SendToAll(msg):
    for i in clients:
        i.send(msg)

def WaitForMessage(addr, conn):
    clients.append(conn)
    while True:
        try:
            data = conn.recv(1024)
            code = Emojify(addr[1])
            message = f"\n[{addr[1]}] {code} says: {data.decode('utf-8')}"
            SendToAll(message.encode('utf-8'))
        except:
            clients.remove(conn)
            SendToAll(f"{code} Disconnected".encode('utf-8'))
            break
    conn.close()

HOST = 'localhost'
PORT = 8081
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Error Code : ' + str(msg[0]) + ' Message ' + msg[1])

s.listen(10)
while True:
    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
    th = threading.Thread(target=WaitForMessage, args=(addr, conn))
    th.start()