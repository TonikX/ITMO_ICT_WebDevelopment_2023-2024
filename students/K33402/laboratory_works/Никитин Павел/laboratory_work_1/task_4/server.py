import socket, threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 1236))
server.listen(5)

client_list = list()
client_threads = list()


def connect_user():
    while True:
        client_socket, address = server.accept()
        if address not in client_list:
            client_list.append(client_socket)
            index = threading.Thread(target=add_user_message, args=(client_socket,))
            index.start()
            client_threads.append(client_socket)
        print(f"connect: {address}")


def add_user_message(user):
    while True:
        # noinspection PyBroadException
        try:
            input_data = user.recv(1024)

        except Exception:
            client_list.remove(user)
            break

        print(input_data.decode("utf-8"))

        # Перенаправить информацию от клиента и отправить ее другим клиентам
        for cli in client_list:
            if cli != user:
                cli.send(input_data)


accept_thread = threading.Thread(target=connect_user(), name="accept")
accept_thread.start()

# Выключите все серверы
for client in client_list:
    client.close()
print("сервер отключен")