import threading
import socket
from http_request import HTTPRequest
from http_response import HTTPResponse

class MyHTTPServer:
	def __init__(self, host, port, server_name):
		self._host = host
		self._port = port
		self._server_name = server_name
		self.grades = {}

	def serve_forever(self):
		# Create a server socket and put in into listening mode
		serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		serv_sock.bind((self._host, self._port))
		serv_sock.listen()

		# Serve clients forever
		while True:
			# Accept a client connection
			conn, addr = serv_sock.accept()

			print(f"New client: {addr}")

			# Serve the client
			threading.Thread(target=self.serve_client, args=[conn, addr]).start()

		serv_sock.close()

	def serve_client(self, conn, addr):
		# Recieve a raw text of client's request
		raw_request = self.recieve_raw_request(conn)

		# Parse the raw text into a request object
		# If the text format was incorrect we get None
		request = self.parse_request(raw_request)

		# Create a response object based on the request object
		response = self.handle_request(request)

		# Convert the respone into raw text
		raw_response = self.convert_response(response)

		# Send the response text to the client
		self.send_raw_response(conn, raw_response)

		# Close the connection
		conn.close()

		print(f"Client {addr} served!")

	def recieve_raw_request(self, conn):
		# Recieve the request text
		return conn.recv(4096).decode()

	def parse_request(self, raw_request):
		# Split raw request text into a list of lines
		lines = raw_request.split("\n")

		# Request is not empty guard check
		if len(lines) == 0:
			return None

		# Split the first line into request line words
		request_params = lines[0].split(" ")

		# Request line contains three values guard check
		if len(request_params) != 3:
			return None
		method, url, version = list(map(lambda word: word.strip(), request_params))

		# A headers dictionary
		headers = {}

		# A pointer for the separator line
		separator_line = None

		# Parse the headers section
		for i in range(1, len(lines)):
			# If the line is not empty consider it as a header
			# Otherwise consider it as a separator line
			if len(lines[i].strip()) > 0:
				header_words = list(map(lambda word: word.strip(), lines[i].split(":")))

				# Incorrect header format guard check
				if len(header_words) < 2:
					return None

				# The first header word is the header name and the rest
				# of the header words is the header value
				key, value = header_words[0], ":".join(header_words[1:])
				headers[key] = value
			else:
				separator_line = i
				break

		# The rest of the message starting from the line
		# right after the separator is the body
		body = "".join(lines[separator_line + 1:]) if separator_line else None

		return HTTPRequest(method, url, version, headers, body)

	def handle_request(self, request):
		# None corresponds to a bad request
		if request is None:
			return self.handle_bad_request()

		# All version except for HTTP/1.1 are not supported
		if request.version != "HTTP/1.1":
			return self.handle_version_is_not_supported()

		# The only accessible resource on the server is its root
		if request.url != "/":
			return self.handle_not_found()

		# The only allowed methods are GET and POST
		if request.method == "GET":
			return self.handle_get_request(request)
		elif request.method == "POST":
			return self.handle_post_request(request)
		else:
			return self.handle_method_not_allowed()

	def handle_bad_request(self):
		return HTTPResponse(400, "Bad Request")

	def handle_version_is_not_supported(self):
		return HTTPResponse(505, "HTTP Version Not Supported")

	def handle_not_found(self):
		return HTTPResponse(404, "Not Found")

	def handle_method_not_allowed(self):
		return HTTPResponse(405, "Method Not Allowed", {"Allow": "GET, POST"})

	def handle_get_request(self, request):
		import grades_generator

		# Generate a page with the table
		body = grades_generator.generate(self.grades)

		return HTTPResponse(200, "OK", request.headers, body)

	def handle_post_request(self, request):
		import re

		# The expression contained in the body matches the pattern guard check
		if not re.match("^discipline=.*&grade=.*$", request.body):
			return self.handle_bad_request()

		# Parse the values provided by the user
		discipline, grade = map(lambda statement: statement.split("=")[1], request.body.split("&"))

		# If discipline is already present in the table
		# append a new grade to the corresponding entry
		# Otherwise create a new entry
		if discipline in self.grades:
			self.grades[discipline].append(grade)
		else:
			self.grades[discipline] = [grade]

		return HTTPResponse(201, "CREATED", request.headers)

	def convert_response(self, response):
		response_elements = []
		status_line = f"HTTP/1.1 {response.status} {response.reason}"
		response_elements.append(status_line)
		if response.headers:
			headers_lines = "\n".join([f"{key}: {value}" for key, value in response.headers.items()])
			response_elements.append(headers_lines)
		response_elements.append("")
		if response.body:
			response_elements.append(response.body)
		return "\n".join(response_elements)

	def send_raw_response(self, conn, raw_response):
		conn.send(raw_response.encode())