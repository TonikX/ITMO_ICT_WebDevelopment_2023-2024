from mathModule import MathModule
from Lab1.serverConfigurator import ServerConfigurator
from socket import *
from messages import *


class Server:
    def __init__(self):
        configuration = ServerConfigurator()
        configuration.default_configuration()
        self.socket = configuration.config_tcp()

    def run(self):
        client_socket, client_addr = self.socket.accept()
        print("Connected")
        self._send_hello(client_socket)
        equation_data = client_socket.recv(1024).decode()
        parsed_data = self._parse_equation_data(equation_data)
        answer = self._solve_equation(parsed_data)
        client_socket.sendall(answer.encode())
        client_socket.close()

    def _send_hello(self, client_socket):
        client_socket.sendall(Messages.hello_message().encode())

    def _parse_equation_data(self, data: str) -> [int]:
        return list(map(int, data.split(",")))

    def _solve_equation(self, data: [int]) -> str:
        a, b, c = data[0], data[1], data[2]
        return MathModule.solve_equation(a, b, c)


server = Server()
server.run()