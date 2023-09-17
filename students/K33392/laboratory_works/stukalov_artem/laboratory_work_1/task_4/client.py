import socket
from threading import Thread, Lock
from typing import Union

HOST = "127.0.0.1"
PORT = 3000
RECV_SIZE = 2048
PROMT_MESSAGE = "Your message: "

Address = tuple[str, int]


class Client:
    def __init__(self, address: Address, name: str):
        self.__address = address
        self.__name = name
        self.__connection: Union[None, socket.socket] = None

    def start(self):
        self.__connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__connection.connect(self.__address)

        listener_thread = Thread(target=self.__listen_for_messages, daemon=True)
        listener_thread.start()

        self.__send_message(self.__name)
        self.__wait_for_input()

    def __stop(self):
        if not self.__connection:
            return

        self.__connection.close()
        print(f"Session stopped, bye")

    def __wait_for_input(self):
        if not self.__connection:
            return

        while True:
            try:
                message = input(PROMT_MESSAGE)
                if len(message) == 0:
                    continue

                self.__send_message(message)
                if message == "/exit":
                    self.__stop()
                    break
            except KeyboardInterrupt:
                self.__stop()
                break

    def __listen_for_messages(self):
        if not self.__connection:
            return

        while True:
            try:
                message = self.__connection.recv(RECV_SIZE).decode()
                if len(message) == 0:
                    self.__stop()
                    break

                print(f"\r{message}\n{PROMT_MESSAGE}", end="")
            except Exception as error:
                print(f"Failed to get message from server with error: {error}")
                break

    def __send_message(self, message: str):
        if not self.__connection:
            return
        self.__connection.send(message.encode())


if __name__ == "__main__":
    client = Client((HOST, PORT), input("Your name: "))
    client.start()
