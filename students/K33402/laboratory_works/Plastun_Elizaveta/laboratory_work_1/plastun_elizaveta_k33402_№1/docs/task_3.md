#  🗿 Задача 3
Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ
клиент получает http-сообщение, содержащее html-страницу, которую сервер
подгружает из файла index.html.

## 🥸 Реализация
1. Server.py
   
```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 9090))
s.listen(1)


def send_html_response(client_socket):
    with open('index.html', 'rb') as html_file:
        html_content = html_file.read()
        response = b"HTTP/1.1 200 OK\r\n"
        response += b"Content-Type: text/html\r\n"
        response += b"Content-Length: " + str(len(html_content)).encode() + b"\r\n"
        response += b"\r\n"
        response += html_content
        client_socket.send(response)


while True:
    client_socket, client_address = s.accept()
    print(f"Accepted connection from {client_address}")
    send_html_response(client_socket)
    client_socket.close()

```
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title></title>
</head>
<body>
<h1>🗿🗿🗿</h1>
<p>Штирлиц вышел из моря и лёг на гальку. Галька обиделась и ушла.</p>
</body>
</html>
```

## 🤡 Демонстрация работы
![html_task_3.png](img/html_task_3.png)

