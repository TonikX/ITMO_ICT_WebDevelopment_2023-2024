import socket
import threading
HOST = '127.0.0.1'
SERVER_PORT = 14900
BUFF_SIZE = 16384

name = input("What is your name? ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, SERVER_PORT))


def input_information():
    while True:
        try:
            message = client.recv(BUFF_SIZE).decode('utf-8')
            if message == 'name':
                client.send(name.encode('utf-8'))
            else:
                print(message)

        except:
            client.close()
            break


def output_information():
    while True:
        message = input('')
        if message == 'leave':
            client.send(f'*{name} left*'.encode('utf-8'))
            client.close()
            break

        message = '{}: {}'.format(name, message)
        client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=input_information)
receive_thread.start()

write_thread = threading.Thread(target=output_information)
write_thread.start()
