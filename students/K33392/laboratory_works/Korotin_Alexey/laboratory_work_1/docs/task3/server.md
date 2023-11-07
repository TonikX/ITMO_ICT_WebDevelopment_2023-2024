## Формулировка задания
Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ
клиент получает http-сообщение, содержащее html-страницу, которую сервер
подгружает из файла `index.html`.
## Задаем параметры сервера
```python
HOST = "localhost"
PORT = 1234
```
## Обработка запросов клиента
```python
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(10)
    while True:
        try:
            client_socket, client_address = s.accept()
            client_socket.send(get_index().encode("UTF-8"))
        except KeyboardInterrupt:
            break
```
Валидный HTTP ответ формируется в функции `get_index`
```python
def get_index():
    with open("res/index.html", 'r') as file:
        index = file.read()

    return f'HTTP/1.0 200 OK\nContent-Type: text/html\n\n{index}'
```
В данной функции происходит считывание содержимого файла `index.html`,
составляется структура HTTP ответа:

- Response code: **200 OK**
- Content-Type: **text/html**
