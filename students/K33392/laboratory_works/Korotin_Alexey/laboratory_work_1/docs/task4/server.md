## Формулировка задания
Реализовать многопользовательский чат. <br/>Для применения с TCP необходимо запускать клиентские подключения **И** прием
и отправку сообщений всем юзерам на сервере в потоках. Не забудьте сохранять юзеров,
чтобы потом отправлять им сообщения.

## Задаем параметры сервера
```python
HOST_DATA = ("localhost", 1234)
BUFFER_SIZE = 2 ** 20

clients = []
```
`clients` - список подключенных клиентов

## Обработка сообщения клиента
```python
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(HOST_DATA)
    s.listen(10)

    while True:
        try:
            client_socket, client_address = s.accept()
            receive(client_socket, clients)
        except KeyboardInterrupt:
            break
```
После TCP подключения работа с клиентом осуществляется в функции `receive`
## Работа с клиентом
```python
@threaded()
def receive(client_socket: socket.socket, clients: list) -> None:
    if client_socket not in clients:
        clients.append(client_socket)

    try:
        while True:
            data = client_socket.recv(BUFFER_SIZE)

            for client in clients:
                if client != client_socket:
                    client.send(data)
    except ConnectionResetError:
        clients.remove(client_socket)
        broadcast("Один из собеседников вышел.", clients)
        print(f"{client_socket} disconnected.")
```
Декоратор `threaded` указывает на то, что обработка каждого клиента будет происходить в своем потоке.
В самом начале клиент добавляется в общий список.
Далее, сервер считывает ввод клиента и отправляет сообщение всем пользователям, кроме отправителя.
В случае, если клиент закончит работу с сервером (`ConnectionResetError`), он удаляется из списка клиентов 
и всем клиентам отправляется об этом сообщение.