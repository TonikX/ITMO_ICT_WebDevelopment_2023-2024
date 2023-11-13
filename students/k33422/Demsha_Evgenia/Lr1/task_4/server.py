import socket
import threading
from collections import defaultdict

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 9090))
ThreadCount = 0
s.listen()
print('Socket is listening..')

clients = defaultdict(dict)


def receiving(*arg):
    session = arg[0]
    name = arg[1]
    while True:
        try:
            data = session.recv(2048).decode()
            if not data:
                raise Exception
            broadcast(name, data)
            mes_to_send = f'{name}: {data}'
            print(mes_to_send)
        except Exception:
            del clients[name]
            session.close()
            broadcast('localhost', f"{name} disconnected")
            print(f"{name} disconnected")
            break


def sending(*arg):
    while True:
        response = input()
        broadcast('localhost', response)


def multi_threaded_client(session, address):
    threading.Thread(target=receiving, args=(session, address)).start()


def broadcast(author, mes):
    mes_to_send = f'{author}: {mes}'
    # print(mes_to_send)
    for nm, data in clients.items():
        if nm != author:
            c_session = data['session']
            c_session.send(mes_to_send.encode())


threading.Thread(target=sending).start()

while True:
    session, (ip, port) = s.accept()
    print('Connected to: ' + ip + ':' + str(port))
    name = session.recv(2048).decode()
    while name in clients.keys():
        session.send('This name is already taken by another chat member'.encode())
        name = session.recv(2048).decode()
    else:
        threading.Thread(target=receiving, args=(session, name)).start()
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))
        clients[str(name)]['IP'] = ip
        clients[str(name)]['port'] = port
        clients[str(name)]['session'] = session
        session.send(f'Welcome to the chat, {name}'.encode())

