import socket
import sys
import threading


class Client:
    _server: "Server"

    _client_socket: socket.socket

    _address: tuple

    _thread: threading.Thread

    _buffer_size: int = 1024

    _is_running: bool = True

    def __init__(self, server: "Server", client_socket: socket.socket, address: tuple) -> None:
        self._server = server
        self._client_socket = client_socket
        self._address = address

    def send_message_to_client(self, message: str) -> None:
        self._client_socket.send(message.encode())

    def start_receiving_messages(self) -> None:
        self._thread = threading.Thread(target=self._run)
        self._thread.start()

    def _run(self) -> None:
        self._broadcast("Joined chat")

        try:
            while True:
                if not self._is_running:
                    break

                self._try_receiving_and_broadcasting_message_from_remote_client()

        except:
            pass

        finally:
            self._shot_down_self_gracefully()

    def _try_receiving_and_broadcasting_message_from_remote_client(self) -> None:
        try:
            message = self._try_receiving_new_message()

            if not message:
                self._shot_down_self_gracefully()
                return
            else:
                self._broadcast(message)

        except socket.timeout:
            pass

    def _try_receiving_new_message(self) -> str:
        return self._client_socket.recv(self._buffer_size).decode()

    def _shot_down_self_gracefully(self):
        self._broadcast("Покинул чат")
        self.stop_receiving_messages()
        self._server.client_disconnected(self)

    def stop_receiving_messages(self) -> None:
        self._client_socket.close()
        self._is_running = False

    def _broadcast(self, message: str) -> None:
        formatted_message = f"{self._address[0]}:{self._address[1]}: {message}"
        self._server.broadcast_message(formatted_message)


class Server:
    _address: str = "127.0.0.1"

    _port: int = 8080

    _buffer_size: int = 1024

    _server_socket: socket.socket = None

    _timeout: int = 1

    _number_of_concurrent_connections: int = 10

    _clients: list[Client]

    def __init__(self) -> None:
        self._clients = []
        self._set_up_server_socket()
        print("Server is running...")

    def _set_up_server_socket(self) -> None:
        self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server_socket.bind((self._address, self._port))
        self._server_socket.settimeout(self._timeout)
        self._server_socket.listen(self._number_of_concurrent_connections)

    def start_cycle(self) -> None:
        try:
            while True:
                self._try_handling_new_client()

        finally:
            self.exit_gracefully()

    def _try_handling_new_client(self) -> None:
        try:
            client_sock, address = self._server_socket.accept()
            client = Client(self, client_sock, address)
            client.start_receiving_messages()
            self._clients.append(client)

        except socket.timeout:
            pass

    def client_disconnected(self, client: Client) -> None:
        self._clients.remove(client)

    def exit_gracefully(self) -> None:
        self.broadcast_message("Server is shutting down...")
        self._stop_clients_from_processing_new_messages()
        self._server_socket.close()
        print("Server is shutting down...")
        sys.exit(0)

    def _stop_clients_from_processing_new_messages(self) -> None:
        for client in self._clients:
            client.stop_receiving_messages()

    def broadcast_message(self, message: str) -> None:
        for client in self._clients:
            try:
                client.send_message_to_client(message)

            except:
                pass


if __name__ == "__main__":
    server = Server()
    server.start_cycle()
