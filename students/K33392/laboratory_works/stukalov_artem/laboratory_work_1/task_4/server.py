import socket
from threading import Thread, Lock
from typing import Dict, Union
from loguru import logger

HOST = "127.0.0.1"
PORT = 3000
RECV_SIZE = 2048
MAX_PENDING_CONNECTIONS = 10

Address = tuple[str, int]


class Client:
    def __init__(self, connection: socket.socket, address: Address):
        self.connection = connection
        self.addres = address
        self.name = ""
        self.is_ready = False


class SocketChatServer:
    def __init__(self, address: Address):
        self.__addres = address
        self.__clients: Dict[int, Client] = {}
        self.__server: Union[None, socket.socket] = None
        self.__broadcast_lock = Lock()
        self.__clients_lock = Lock()

    def start(self):
        try:
            logger.info("Starting server...")
            self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__server.bind(self.__addres)
            self.__server.listen(MAX_PENDING_CONNECTIONS)
            logger.info(
                f"Server started successfully on {self.__addres[0]}:{self.__addres[1]}"
            )

            accept_connections_thread = Thread(target=self.__accept_connections)
            accept_connections_thread.start()
            accept_connections_thread.join()
        except KeyboardInterrupt:
            print("KeyboardInterrupt in start")
            self.__stop()

    def broadcast(self, message: str):
        logger.info(f"Broadcasting message: {message}")
        with self.__broadcast_lock:
            for client in self.__clients.values():
                if not client.is_ready:
                    continue
                try:
                    client.connection.send(message.encode())
                except Exception as error:
                    logger.info(
                        f"Failed to broadcast message({message}) with error:\n {error}"
                    )

    def __accept_connections(self):
        if not self.__server:
            return

        logger.info("Listening for connections...")
        while True:
            (connection, address) = self.__server.accept()
            logger.info(f"Got connection from clinet {address[0]}:{address[1]}")

            client = Client(connection, address)
            with self.__clients_lock:
                self.__clients[address[1]] = client

            client_thread = Thread(
                target=self.__handle_clinet_messages, args=(client,), daemon=True
            )
            client_thread.start()

    def __stop(self):
        if not self.__server:
            return

        for client_id in list(self.__clients.keys()):
            self.__close_client_connection(client_id)
        self.__server.close()
        logger.info("Server stopped...")

    def __handle_clinet_messages(self, client: Client):
        clinet_name = client.connection.recv(RECV_SIZE).decode()
        client.name = clinet_name
        client.is_ready = True
        logger.info(f"Got clinet({client.addres}) name: {clinet_name}")

        self.broadcast(self.__get_join_message(client))
        while True:
            try:
                message = client.connection.recv(RECV_SIZE).decode()
                logger.info(f"Got client({client.addres}) message: {message}")

                if message == "/exit" or len(message) == 0:
                    self.__close_client_connection(client.addres[1])
                    break
                else:
                    self.broadcast(f"<{client.name}>: {message}")
            except Exception as error:
                logger.info(f"Failed to recv client message with error:\n {error}")

    def __close_client_connection(self, client_id: int):
        client = self.__clients[client_id]
        client.connection.close()
        client.is_ready = False
        logger.info(f"Close client connection {client.addres}")
        with self.__clients_lock:
            self.__clients.pop(client.addres[1])
        self.broadcast(self.__get_leave_message(client))

    def __get_join_message(self, client: Client):
        return f"User <{client.name}> joined chat"

    def __get_leave_message(self, client: Client):
        return f"User <{client.name}> leaved chat"


if __name__ == "__main__":
    chat_server = SocketChatServer((HOST, PORT))
    chat_server.start()
