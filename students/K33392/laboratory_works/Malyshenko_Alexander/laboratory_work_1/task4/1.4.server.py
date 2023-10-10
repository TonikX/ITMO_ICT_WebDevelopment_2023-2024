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