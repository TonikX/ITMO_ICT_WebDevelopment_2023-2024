# Задание 3

Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ клиент получает http-сообщение,
содержащее html-страницу, которую сервер подгружает из файла index.html.

Обязательно использовать библиотеку socket

## Ход выполнения работы

### Код task3_server.py

    if __name__ == '__main__':
        import socket
    
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', 9090))
        sock.listen()
        print("Server is running on http://localhost:9090")
    
        while True:
            connection, address = sock.accept()
    
            data = connection.recv(1024)
            if not data:
                break
    
            print(data.decode("utf-8"))
    
            content = open("task3_index.html").read()
            response = "HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\n\n" + content
    
            connection.send(response.encode("utf-8"))
            connection.close()

### Код task3_client.py

    if __name__ == '__main__':
        import socket
    
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('localhost', 9090))
    
        http_request = "GET / HTTP/1.1\r\nHost: localhost:9090\r\n\r\n"
        sock.send(http_request.encode('utf-8'))
    
        while True:
            data = sock.recv(1024)
            if not data:
                break
            print(data.decode("utf-8"))
    
        sock.close()

### Код index.html

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Lab 1</title>
    </head>
    <body>
    <p>Hi!</p>
    </body>
    </html>

## Результат

![Image](src/task3.png)