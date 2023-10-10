import socket

ip     = "127.0.0.1"
port   = 9090
buffer = 1024

TCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCPSocket.bind((ip, port))
TCPSocket.listen(1)

print(" === server is running ===\n")

def parallelogramArea(h, a):
    area = a * h
    return area

while True:
	connection, adrress = TCPSocket.accept()

	try:
		print("Connected to client IP: {}".format(adrress))
        
		while True:
			data = connection.recv(buffer)

			if not data:
				break

			data = data.decode("utf-8")
			print("Received data: {}".format(data))
			
			if data == "stop":
				break
			
			array = list(map(int, data.split()))
			answer = parallelogramArea(array[0], array[1])
			print("Send data: {}".format(answer))
			answer = str.encode(str(answer))
			connection.send(answer)

	finally:
		print("\n=== stopping the server ===")
		connection.close()
		break
