from my_http_server import MyHTTPServer

host = "localhost"
port = 5555
server_name = "example.local"
server = MyHTTPServer(host, port, server_name)

raw_request = "GET / HTTP/1.1\n" \
			  "Host: example.local\n" \
			  "Languages: de,en;q=0.5\n" \
			  "\n" \
			  "discipline=Math&grade=5A"

request = server.parse_request(raw_request)
response = server.handle_request(request)
raw_response = server.convert_response(response)
print(raw_response)
