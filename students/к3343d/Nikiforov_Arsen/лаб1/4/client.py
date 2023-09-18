import socket
import threading

class Client:
    def __init__(self, host = '127.0.0.1', port = 55555):
        self.nickname = input("Enter your nickname: ")
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))  # Подключение к серверу по указанному адресу и порту

    def receive(self):
        while True:
            try:
                message = self.client.recv(1024).decode('ascii')  # Прием сообщения от сервера
                if message == 'NICK':
                    self.client.send(self.nickname.encode('ascii'))  # Отправка своего никнейма серверу
                else:
                    print(message)  # Вывод сообщения от сервера
            except:
                print("An error occurred!")
                self.client.close()
                break
            
    def write(self):
        while True:
            message = f'{self.nickname}: {input("")}'  # Ввод сообщения с указанием своего никнейма
            self.client.send(message.encode('ascii'))  # Отправка сообщения серверу

    def run(self):
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()  # Запуск потока для приема сообщений от сервера

        write_thread = threading.Thread(target=self.write)
        write_thread.start()    # Запуск потока для отправки сообщений на сервер

client = Client()
client.run()
