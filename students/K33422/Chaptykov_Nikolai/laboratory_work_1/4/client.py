import socket
import threading

def WaitForMessage(conn):
    while True:
        try:
            data = conn.recv(1024)
            if data:
                print(data.decode('utf-8'))
        except:
            break
    conn.close()

HOST = 'localhost'
PORT = 8081

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

message = 1
while message:
    th = threading.Thread(target=WaitForMessage, args=(s,))
    th.start()
    message = input()
    s.sendall(message.encode('utf-8'))

s.close()