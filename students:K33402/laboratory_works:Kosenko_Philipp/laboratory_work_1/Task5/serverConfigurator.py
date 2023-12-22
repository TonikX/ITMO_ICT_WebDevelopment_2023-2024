from socket import *


class ServerConfigurator:
    host: str
    port: int
    host_info = (str, int)
    socket: socket

    def default_configuration(self):
        self.host = 'localhost'
        self.port = 10000
        return (self.host, self.port)

    def config_udp(self):
        self.socket = socket(AF_INET, SOCK_DGRAM)
        self.socket.bind(self.host_info)
        return self.socket

    def config_tcp(self):
        server_socket = socket(AF_INET, SOCK_STREAM)
        server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        server_socket.bind((self.host, self.port))
        server_socket.listen()
        return server_socket