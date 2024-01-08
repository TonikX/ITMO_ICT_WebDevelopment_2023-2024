import socket, sys, threading

SEP = '__SEP__'

def send():
    while True:
        try:
            sys.stdout.write(f'[{username}] (me): ')
            sys.stdout.flush()
            message = input()
            server.send(message.encode())
        except Exception as e:
            print(str(e))

def receive():
    while True:
        try:
            msg = server.recv(1024)
            USER, MESSAGE = msg.decode().split(SEP)

            if (USER == username):
                continue
            else:
                sys.stdout.write(f'\n[{USER}]: {MESSAGE}\n[{username}] (me): ')
                sys.stdout.flush()
        except:
            break


username = input('Enter username: ')
server_address = ('localhost', 9090)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(server_address)
server.send(username.encode())

send_thread = threading.Thread(target=send)
receive_thread = threading.Thread(target=receive)
send_thread.start()
receive_thread.start()