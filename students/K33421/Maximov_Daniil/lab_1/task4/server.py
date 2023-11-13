import socket
import sys
from client_thread import ClientThread

class Server:
    _address_and_port: tuple = ("127.0.0.1", 8080)

    _server_socket: socket.socket = None

    _timeout: int = 1

    _number_of_concurrent_connections: int = 10

    _clients: list[ClientThread]

    # init ------------------------------------------------------------------

    def __init__(self) -> None:
        self._clients = []
        self._set_up_server()
        print("Server is running...")

    # setup ------------------------------------------------------------------
    def _set_up_server(self) -> None:
        self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server_socket.bind(self._address_and_port)
        self._server_socket.settimeout(self._timeout)
        self._server_socket.listen(self._number_of_concurrent_connections)

    # main cycle ------------------------------------------------------------------
    def start_cycle(self) -> None:
        try:
            while True:
                print("try to connect client")
                self._try_to_get_new_client_connection()

        finally:
            self.exit()

    def _try_to_get_new_client_connection(self) -> None:
        try:
            client_sock, address = self._server_socket.accept()
            client = ClientThread(self, client_sock, address)
            self._clients.append(client)
            client.start_receiving_messages()

        except socket.timeout:
            pass

    # Exiting ------------------------------------------------------------------
    def client_disconnected(self, client: ClientThread) -> None:
        print(f'{client.address} ползователь покинул чат ')
        self._clients.remove(client)

    def exit(self) -> None:
        self.broadcast_message("...Server is shutting down...")
        self._abort_clients_reciving_messages()
        self._server_socket.close()
        print("...Server is shutting down...")
        sys.exit(0)

    def _abort_clients_reciving_messages(self) -> None:
        for client in self._clients:
            client.stop_receiving_messages()

    # broadcasting ------------------------------------------------------------------
    def broadcast_message(self, message: str) -> None:
        for client in self._clients:
            try:
                client.send_message_to_client(message)

            except:
                pass


if __name__ == "__main__":
    server = Server()
    server.start_cycle()
