from my_http_server import MyHTTPServer

if __name__ == "__main__":
	host = "localhost"
	port = 5555
	name = "example.local"
	my_server = MyHTTPServer(host, port, name)
	my_server.serve_forever()