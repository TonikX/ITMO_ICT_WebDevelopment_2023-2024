# Задание 3

## Описание Задачи

Задача заключается в разработке серверной части приложения, которая отправляет HTTP-ответ с HTML-страницей клиенту при
его подключении. HTML-страница должна загружаться из файла `index.html`.

## Реализация

### Серверная Часть

Файл: `server.py`

Сервер использует протокол TCP для прослушивания подключений клиентов. При подключении клиента сервер загружает
HTML-страницу из файла `index.html` и отправляет её клиенту в виде HTTP-ответа.

```python
import socket

if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
        conn.bind(('127.0.0.1', 8888))
        conn.listen()
        
        print(f"Server running on http://localhost:8888/")
        
        while True:
            client_conn, addr = conn.accept()
            print('Connected by', addr)
            
            with open('index.html', 'rb') as f:
                data = f.read()
            
            client_conn.sendall(
                b'HTTP/1.1 200 OK\n'
                b'Content-Type: text/html\n\n'
                + data
            )
```

### HTML-Страница

Файл: `index.html`

Простая HTML-страница, отправляемая сервером:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hello, world!</title>
</head>
<body>
Hello, world!
</body>
</html>
```

## Выводы

Серверная часть приложения была реализована.
Сервер корректно обрабатывает подключения клиентов и отправляет HTTP-ответ с HTML-страницей. Тестирование показало, что
HTML-страница успешно отображается в веб-браузере клиента.