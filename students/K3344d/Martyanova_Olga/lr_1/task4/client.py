import socket
import sys
import threading


def send_message(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12342)
client_socket.connect(server_address)
print("Welcome! You can start chatting")

send_thread = threading.Thread(target=send_message, args=(client_socket,))
send_thread.daemon = True
send_thread.start()

while True:
    try:
        data = client_socket.recv(1024)
        if not data:
            print('Server closed.')
            client_socket.close()
            sys.exit(0)
        print(data.decode('utf-8'))
    except KeyboardInterrupt:
        print('\nYou left the chat!')
        client_socket.close()
        break
