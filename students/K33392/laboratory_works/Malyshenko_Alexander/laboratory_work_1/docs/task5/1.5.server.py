import socket
from io import BufferedReader
from urllib.parse import urlparse
import urllib.parse as urlParse
import json


class Request:
	def __init__(self, method: str, target: str, version: str, headers: list[str], body: list[str], fileReader: BufferedReader):
		self.method = method
		self.target = target
		self.version = version
		self.headers = headers
		self.body = body
		self.fileReader = fileReader

	@property
	def getUrl(self) -> urlParse.ParseResult:
		return urlparse(self.target)
	
	@property
	def getPath(self):
		return self.getUrl.path
	

class Response:
	def __init__(self, status: int, reason: str, headers = None, body = None):
		self.status = status
		self.reason = reason
		self.headers = headers
		self.body = body



class HTTPServer:
	def __init__(self, host: str, port: int, name: str):
		self._host = host
		self._port = port
		self._name = name
		self._handlers = 0
		self._disciplinesGrades: dict[str, list[int]] = {"Информатика": list('5')}
		self._maxBufferLen = 1024 * 64

	def serverStart(self):
		'''
		Start server \n
		Create server socket and try to connect to client
		'''

		serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
		try:
			serverSocket.bind((self._host, self._port))
			serverSocket.listen(5)
			print(f"=== Server [{self._name}] is running ===")

			while True:
				try:
					(clientSocket, adrress) = serverSocket.accept()
					self.serveClient(clientSocket)

				except Exception as ex:
					print("=== Client connection failed ===\n", ex)

		except Exception as ex:
			print(f"=== Error when starting the server [{self._name}] ===")

		finally:
			serverSocket.close()
			print(f"=== Server [{self._name}] stopped ===")

	def serveClient(self, clientSocket: socket.socket):
		try:
			request = self.parseRequest(clientSocket)
			print(f"Received request: {request.method}, target: {request.target}")
			response = self.handleRequest(request)
			print(f"Return response: {response.reason}, status: {response.status}\n")
			self.sendResponse(clientSocket, response)

		except ConnectionResetError as conEx:
			clientSocket = False

		
		except Exception as ex:
			print(f"Failed receive request and return response")

		if clientSocket:
			clientSocket.close()

	def parseRequest(self, clientSocket: socket.socket) -> Request:
		fileReader = clientSocket.makefile('rb')
		requestString = fileReader.readline(self._maxBufferLen + 1)
		if len(requestString) > self._maxBufferLen:
			raise Exception('Too long request')
		
		requestLine = str(requestString, 'iso-8859-1')
		requestLine = requestLine.rstrip('\r\n')
		partsOfRequest = requestLine.split()
		if len(partsOfRequest) != 3:
			raise Exception('Incorrect request line')
		
		method, target, version = partsOfRequest
		if version != "HTTP/1.1":
			raise Exception("Incorrect HTTP Version")
		
		requestHeaders = self._parseRequestHeaders(fileReader)
		requestBody = self._parseRequestBody(fileReader, requestHeaders)

		
		return Request(method, target, version, requestHeaders, requestBody, fileReader)

	def _parseRequestHeaders(self, requestFileReader: BufferedReader) -> list[str]:

		headersList = []

		while True:
			requestString = requestFileReader.readline(self._maxBufferLen + 1)
			if requestString in (b"\r\n", b"\n", b""):
				break

			headersList.append(requestString.decode("iso-8859-1"))

		return headersList
	
	def _parseRequestBody(self, requestFileReader: BufferedReader, requestHeaders: list[str]) -> list[str]:
		
		length = 0
		for header in reversed(requestHeaders):
			index = header.find('Content-Length: ')
			lastIndex = index + len('Content-Length: ')
			if index != -1:
				length = int(header[lastIndex : header.find('\r')])

		if length != 0:
			body = requestFileReader.read(length)

		return body

	def handleRequest(self, request: Request):
		if request.getPath == "/disciplines" and request.method == "POST":
			return self._handlePostDiscipline(request)
		
		if request.getPath == "/disciplines" and request.method == "GET":
			return self._handleGetDiscipline()
		
		raise Exception("Not found such response")
	
	def _handlePostDiscipline(self, request: Request):
		postBody = json.loads(request.body)
		if not postBody["discipline"] in self._disciplinesGrades:
			self._disciplinesGrades[postBody["discipline"]] = []

		self._disciplinesGrades[postBody["discipline"]].append(postBody["grade"])
		responseBody = json.dumps({"Post done": True}).encode("utf-8")
		headers = [
        	("Content-Type", "application/json; charset=utf-8"),
        	("Content-Length", len(responseBody))]

		return Response(204, 'Created', headers, responseBody)
		
	def _handleGetDiscipline(self):
		requestBody = self._htmlTableGen()
		requestBody = requestBody.encode('utf-8')
		requestHeaders = [("Content-Type", "text/html; charset=utf-8"), ("Content-Length", len(requestBody))]

		return Response(200, "OK", requestHeaders, requestBody)

	def _htmlMain(self, ctx: str) -> str:
		return f"""<!DOCTYPE html>
		<head>
			<style>
				table {{ background: CadetBlue }}
				td {{ background: SkyBlue }}
			</style>
		</head>
		<body>
			{ctx}
		</body>
		</html>"""
	
	def _htmlTableGen(self) -> str:
		tableRows = []
		for discipline in self._disciplinesGrades:
			gradesString = ', '.join(list(map(str, list(self._disciplinesGrades[discipline]))))
			tableRows.append(
				f"""
				<tr>
					<td>{discipline}</td>
					<td>{gradesString}</td>
				</tr>""")
			
		tableHead = """
			<thead>
				<tr>
				<th scope="col">Discipline</th>
				<th scope="col">Grades</th>
				</tr>
			</thead>"""

		tableRows = "\n".join(tableRows)
		tableBody = f"<tbody>{tableRows}</tbody>"
		return self._htmlMain(f"<table>{tableHead}\n{tableBody}</table>")

	def sendResponse(self, clientSocket: socket.socket, response: Response):
		fileWriter = clientSocket.makefile("wb")
		status = f"HTTP/1.1 {response.status} {response.reason}\r\n"
		fileWriter.write(status.encode('iso-8859-1'))

		if response.headers:
			for key, value in response.headers:
				header = f"{key}: {value}\r\n"
				fileWriter.write(header.encode("iso-8859-1"))

		fileWriter.write(b'\r\n')

		if response.body:
			fileWriter.write(response.body)


if __name__ == "__main__":
	
	host, port = "127.0.0.1", 9090
	name = "lab5.local"

	server = HTTPServer(host, port, name)
	try:
		server.serverStart()
	except:
		pass