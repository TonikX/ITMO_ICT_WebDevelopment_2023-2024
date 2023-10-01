import socket

def sendResponse(connection):
	status = 'HTTP/1.1 200 OK\r\n'
	header = 'Content-Type: text/html\r\n'
	
	ms =  status + header + "\r\n"
	
	htmlFile = open("lab1/task3/index.html", 'r')
	for string in htmlFile:
		ms += string

	connection.send(ms.encode("utf-8"))

PORT = 14900

IP = socket.gethostbyname(socket.gethostname())

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


listener.bind((IP, PORT))
listener.listen(10)

while True:
	connection, adrress = listener.accept()
	try:
		sendResponse(connection)
		if connection:
			connection.close()

	except Exception as ex:
		print("=== Client connection failed ===\n", ex)
