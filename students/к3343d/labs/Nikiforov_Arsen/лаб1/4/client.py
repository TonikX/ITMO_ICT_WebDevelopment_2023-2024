import socket
import threading

class Client:
    def __init__(self, host='127.0.0.1', port=55555):
        self.nickname = input("Введите ваш никнейм: ")
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))

    def receive(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                if message == 'NICK':
                    self.client.send(self.nickname.encode('utf-8'))
                else:
                    print(message)
            except:
                print("Произошла ошибка!")
                self.client.close()
                break

    def write(self):
        while True:
            message = input("")
            if message.lower() == 'quit':  # Проверка на команду "quit" для выхода
                self.client.send('quit'.encode('utf-8'))
                break
            else:
                message_to_send = f'{self.nickname}: {message}'
                self.client.send(message_to_send.encode('utf-8'))

    def run(self):
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

        write_thread = threading.Thread(target=self.write)
        write_thread.start()

client = Client()
client.run()
