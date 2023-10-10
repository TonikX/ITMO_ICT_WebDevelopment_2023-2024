# Задание №4

Реализовать двухпользовательский или многопользовательский чат. Реализация
многопользовательского часа позволяет получить максимальное количество
баллов. Необходимо исользовать библиотеку socket.

## Выполнение задания
### Серверная часть

```py
import socket
from threading import Thread

class Server:
	def __init__(self, host, port, name):
		self._host = host
		self._port = port
		self._name = name
		self.addresses = set()
		self.clients = set()
		self.serverSocket = 0

	def createSocket(self):
		# Создание сокета сервера, type=socket.SOCK_STREAM - TCP протокол
		self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			self.serverSocket.bind((self._host, self._port))
			# Ограничиваем количетсво клиентов, которое может подключиться
			self.serverSocket.listen()

			while True:
				# Принимаем соединение от клиента: сокет и адресс
				connection, addrress = self.serverSocket.accept()
				# Добавляем адрес и сокет клиента в список
				self.clients.add(connection)
				self.addresses.add(addrress)
				print(f"Client {addrress} connected")

				#запуск мултипотока
				thread = Thread(target = self.takeConnections, args = (connection, ))
				thread.daemon = True
				thread.start()

		finally:
			# Закрываем подключение
			self.serverSocket.close()
			print("=== Socket close ===")

	def takeConnections(self, clientConnection: socket.socket):
		'''
		Получает сообщение от пользователя и выводит его всем пользователям
		'''
		while True:
			try:
				message = clientConnection.recv(1024).decode()

			except Exception as ex:
				print(f"Error when try read message: {ex}")
				self.clients.remove(clientConnection)
			
			for client in self.clients:
				client.send(message.encode())


if __name__ == "__main__":
	
	host, port = "127.0.0.1", 9090
	name = "test.local"

	server = Server(host, port, name)
	try:
		server.createSocket()
	except:
		pass
```

### Клиентская часть

```py
import socket
from threading import Thread
from datetime import datetime
import random

serverAdress    = ("127.0.0.1", 9090)
buffer          = 1024
name = random.choice(('Alex', 'Petya', 'Vasya', 'Timur', 'Ivan', 'Katya '))
# Создаем TCP сокет
TCPSocket = socket.socket()
# Подключаемся к серверу
TCPSocket.connect(serverAdress)
print("=== connected to the server ===\n")

def takeMessages(socket: socket.socket):
    while True:
        # Получем данные от сервера
        message = socket.recv(buffer).decode()
        print(f"\n{message}")

try:
    #запускаем мультипоток для получения сообщений с сервера
    thread = Thread(target = takeMessages, args = (TCPSocket, ))
    thread.daemon = True
    thread.start()

    while True:
        sendedMessage = input()
        
        if sendedMessage == "quit()":
            break

        timeOfMessage = datetime.now().strftime('%H:%M')
        sendedMessage = f"[{timeOfMessage}] {name}: {sendedMessage}"
        #отправляем сообщение серверу формата [дата] имя: ctx
        TCPSocket.send(sendedMessage.encode())
 
finally:
    print("\n=== Closing socket ===")
    TCPSocket.close()
```

## Примеры

Запуск сервера, подлкючение 3-х пользователей
![Пример задания 4.1](pic/task4_startServer&AddClients.png)
Отправка/получение сообщений от пользователей
![Пример задания 4.2](pic/task4_clientsMessages.png)
