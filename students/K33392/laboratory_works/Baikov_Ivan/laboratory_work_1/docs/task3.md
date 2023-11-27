# Задание 3

Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ
клиент получает http-сообщение, содержащее html-страницу, которую сервер
подгружает из файла index.html.

Обязательно использовать библиотеку socket

## Ход выполнения работы

### Код server.py

```python
    from socket import *
    content = open("Task3/index.html").read()

    if __name__ == "__main__":
        ip = '127.0.0.1'
        port = 3000

        server = socket(AF_INET, SOCK_STREAM)
        server.bind((ip, port))
        server.listen()

        while True:
            try:
                print("Waiting for a connection...")
                client, addr = server.accept()
                print(f"Accepted connection from {addr}")

                response = "HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\n\n" + content

                client.send(response.encode())

                client.close()

            except KeyboardInterrupt:
                print("Server terminated by user.")
                break
            except Exception as e:
                print(f"Error: {e}")

        server.close()

```

### Код client.py

```python
    from socket import *
    if __name__ == "__main__":
        ip= '127.0.0.1'
        port = 3000

        client = socket(AF_INET, SOCK_STREAM)
        client.connect((ip, port))

        request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
        client.send(request.encode('utf-8'))

        response = client.recv(1024).decode('utf-8')
        print(response)

```

### Код index.html

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Hello, Dear client!</title>
  </head>
  <body>
    <h1>Hello, Dear client!</h1>
  </body>
</html>
```

## Результат

![Результат](images/task3.png)
