# Практическое задание 1

Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу
сообщение «Hello, server». Сообщение должно отразиться на стороне сервера.
Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно
отобразиться у клиента.

- Обязательно использовать библиотеку socket

- Реализовать с помощью протокола UDP


### Сервер

###### Импорты и глобальные переменные

```
    import socket
    import threading
    
    PORT = 8080
```

###### Тело сервера

```
    def main():
        
        global PORT
    
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('', PORT))
    
        while True:
            data, addr = sock.recvfrom(1024)
            thread = threading.Thread(target=recieve, args=([data, addr, sock],))
            thread.start()
```

###### Функция обработки подключения
```
    def recieve(data):
        print(data[0])
        data[2].sendto(b"Hello, client", data[1])

```

 ### Клиент

###### Импорты и глобальные переменные

```
    import socket

    PORT = 8080
```

###### Тело клиента

```
    def main():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(b'Hello, server', ('localhost', PORT))
        data, addr = sock.recvfrom(1024)
        print(data)
```