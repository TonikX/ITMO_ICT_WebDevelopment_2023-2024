# Задание 3

Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ клиент получает http-сообщение, содержащее html-страницу, которую сервер подгружает из файла index.html.

Использовать библиотеку socket.

# Выполнение

```python
import socket

def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "Файл не найден"

s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s_address = ('localhost', 12413)
s_socket.bind(s_address)

s_socket.listen(1)
print('Сервер ожидает подключения клиента...')

while True:
    c_socket, c_address = s_socket.accept()
    print(f'Подключено клиентом {c_address}')

    try:
        html_content = read_file('index.html')
        request = c_socket.recv(1024)
        http_response = f"HTTP/1.1 200 OK\r\n Content type:html \r\n Content-Length: {len(html_content)}\r\n\r\n{html_content}"
        c_socket.sendall(http_response.encode('utf-8'))
    except Exception as e:
        print(f'Ошибка: {str(e)}')
    finally:
        c_socket.close()
```

Данный код представляет собой простой TCP-сервер на языке Python, который использует модуль socket для уст
ановления соединения с клиентами. Сервер привязывается к локальному хосту и порту 12413, ожидая подключения клиентов. При подключен
ии клиента сервер выводит сообщение о подключении в консоль и начинает ожидать запросов от клиента.

При получении соединения программа считывает данные, отправленные клиентом, и отправляет ответ, содержащий ответ следующего формата:
```
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8

<содержимое файла index.html>
```

![Пример изображения](3.png)

![Пример изображения](4.png)