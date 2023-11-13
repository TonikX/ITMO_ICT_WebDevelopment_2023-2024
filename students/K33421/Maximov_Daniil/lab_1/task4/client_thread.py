import threading
import socket


class ClientThread:
    _server: "Server"

    _client_socket: socket.socket

    address: tuple

    _thread: threading.Thread

    _is_running: bool = True

    # init ------------------------------------------------------------------

    def __init__(self, server, client_socket: socket.socket, address: tuple) -> None:
        self._server = server
        self._client_socket = client_socket
        self.address = address

    # Sending and reciving -------------------------------------------------------------
    def send_message_to_client(self, message: str) -> None:
        self._client_socket.send(message.encode())

    def start_receiving_messages(self) -> None:
        self._thread = threading.Thread(target=self._run)
        self._thread.start()

    # running in Thread ------------------------------------------------------------------
    def _run(self) -> None:
        self._broadcast("присоединился к чату")

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
        return self._client_socket.recv(1024).decode()

    # broadcasting ------------------------------------------------------------------
    def _broadcast(self, message: str) -> None:
        formatted_message = f"{self.address[0]}:{self.address[1]}: {message}"
        self._server.broadcast_message(formatted_message)

    # Exiting ------------------------------------------------------------------
    def _shot_down_self_gracefully(self):
        if not self._is_running:
            return

        self._broadcast("Покинул чат")
        self.stop_receiving_messages()
        self._server.client_disconnected(self)

    def stop_receiving_messages(self) -> None:
        self._client_socket.close()
        self._is_running = False

