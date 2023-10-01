**Задание:** Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ клиент получает http-сообщение, содержащее html-страницу, которую сервер подгружает из файла index.html. 

**Код сервера:**
```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '127.0.0.1'
PORT = 14902
sock.bind((HOST, PORT))
sock.listen(1)
print(f"Сервер запущен на http://{HOST}:{PORT}")

with open('index.html', 'rb') as file:
    html_content = file.read()

while True:
    clientsocket, address = sock.accept()
    request_data = clientsocket.recv(1024)
    response_headers = "HTTP/1.1 200 OK\nContent-Type: text/html\n\n"

    clientsocket.sendall(response_headers.encode('utf-8') + html_content)

    clientsocket.close()

```

**index.html:**
```python
<!DOCTYPE html>
<html>
    <head>
        <title>Web task 3</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f2f2f2;
                text-align: center;
                padding: 100px;
            }
            h1 {
                color: #333;
            }
            h3 {
                color: #666;
            }
        </style>
    </head>
    <body>

    <h1 align="center">Hello, world!</h1>
    <h3 align="center">The 3rd task is working!</h3>

    </body>
</html>
```

**Скринкаст:**

Клиент-серверное взаимодействие:

На стороне клиента:
![](/screenshots/3-client.png)

На стороне сервера:
![](/screenshots/3-server.png)