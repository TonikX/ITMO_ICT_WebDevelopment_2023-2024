# Задание 3

Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ клиент получает http-сообщение,
содержащее html-страницу, которую сервер подгружает из файла index.html.

Обязательно использовать библиотеку socket

## Ход выполнения работы

### Код server.py

    import socket

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((socket.gethostname(), 9090))
    server.listen(5)
    
    while True:
        client_socket, addr = server.accept()
    
        with open('index.html') as html:
            html_content = html.read()
    
        response = f"HTTP/1.1 200 OK\r\nContent-Length: {len(html_content)}\r\n\r\n{html_content}"
        client_socket.send(response.encode())
    
        client_socket.close()

### Код client.py

    import socket

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((socket.gethostname(), 9090))
    
    request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
    client.send(request.encode())
    
    response = client.recv(1024)
    
    print(response.decode())
    
    client.close()

### Код index.html

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Hello, world!</title>
    </head>
    <body>
    
    </body>
    </html>

## Результат

![Result](images/task_3_1.png)
![Result](images/task_3_2.png)