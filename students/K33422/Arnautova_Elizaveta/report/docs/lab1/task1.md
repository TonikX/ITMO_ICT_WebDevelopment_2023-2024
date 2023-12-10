**Задание:** реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу сообщение «Hello, server». Сообщение должно отразиться на стороне сервера.
Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно отобразиться у клиента.
Обязательно использовать библиотеку socket. Реализовать с помощью протокола UDP.

**Код сервера:**
```python
import socket
HOST = '127.0.0.1'
SERVER_PORT = 14900
BUFF_SIZE = 16384

if __name__ == '__main__':
    server_address = (HOST, SERVER_PORT)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as conn:  # UDP
        conn.bind(server_address)  # открытие сокета
        print('Server is waiting...')

        timeout = 30
        while True:
            conn.settimeout(timeout)
            try:
                data, client_address = conn.recvfrom(BUFF_SIZE)  # получение данных
            except socket.timeout:
                print('Time is out. {0} seconds have passed'.format(timeout))
                break

            print(f'Received message from {client_address}: {data.decode("utf-8")}')  # декодирование данных

            message = 'Hello, client!'
            conn.sendto(message.encode('utf-8'), client_address)



```

**Код клиента:**
```python
import socket
HOST = '127.0.0.1'
SERVER_PORT = 14900
BUFF_SIZE = 16384

if __name__ == '__main__':
    server_address = (HOST, SERVER_PORT)
    conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP

    message = 'Hello, server!'
    try:
        conn.sendto(message.encode('utf-8'), server_address)
        response = conn.recv(BUFF_SIZE)
        print(f'Received response from server: {response.decode("utf-8")}')
    except ConnectionResetError:
        print("Received no response from server, try again later")

    conn.close()



```

**Скринкаст:**

Клиент-серверное взаимодействие:

На стороне клиента:
![](/screenshots/1-client.png)

На стороне сервера:
![](/screenshots/1-server.png)