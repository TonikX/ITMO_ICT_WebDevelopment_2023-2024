import socket
import threading

nickname = input('Choose a nickname: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9999))



def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'Nick':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print('An error occurred.')
            client.close()
            break


def write_message():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write_message)
write_thread.start()