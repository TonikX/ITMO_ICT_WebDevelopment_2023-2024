import socket
import sys
from func import LocateCalculate, CheckMessage

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

    data = conn.recv(1024)
    reply = data.decode('utf-8')
    message = 'Pythagorator 3000k\nInsert data like "leg leg hypothenus" using space as separator, mark unknown as "0", e.g. 0 3 25'
    conn.sendall(message.encode('utf-8'))
    temp = CheckMessage(reply)
    if temp:
        msg = f"The input is: {reply}\nX = {LocateCalculate(temp)}"
        conn.sendto(msg.encode('utf-8'), addr)
        print(f"sent to {addr}")

    conn.close()