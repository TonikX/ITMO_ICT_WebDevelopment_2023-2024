from serverConfigurator import ServerConfigurator

class Server:
    def __init__(self):
        configuration = ServerConfigurator()
        configuration.default_configuration()
        self.socket = configuration.config_tcp()

    def run(self):
        client_socket, client_addr = self.socket.accept()
        print("Connected")
        request = client_socket.recv(1024)
        self._response(client_socket)

    def _response(self, client_socket):
        file_content = open("index.html", "r").read().encode()
        wfile = client_socket.makefile("wb")
        status_line = f'HTTP/1.1 {200} {"kek"}\r\n'
        wfile.write(status_line.encode('iso-8859-1'))
        wfile.write(file_content)

        wfile.flush()
        wfile.close()


server = Server()
server.run()