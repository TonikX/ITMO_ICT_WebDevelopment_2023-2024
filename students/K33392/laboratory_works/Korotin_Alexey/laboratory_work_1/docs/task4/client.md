## Формулировка задания
Реализовать многопользовательский чат. <br/>Для применения с TCP необходимо запускать клиентские подключения **И** прием
и отправку сообщений всем юзерам на сервере в потоках. Не забудьте сохранять юзеров,
чтобы потом отправлять им сообщения.

## Задаем параметры сервера
```python
DEST = ("localhost", 1234)
BUFFER_SIZE = 2 ** 20
```
## Отправка сообщений на сервер
```python
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(DEST)
    accept(s)
    while True:
        try:
            inp = input()
            s.send(inp.encode("UTF-8"))
        except KeyboardInterrupt:
            break
```
Происходит считывание ввода пользователя и отправка его на сервер
## Получение сообщений
```python
@threaded(daemon=True)
def accept(s: socket.socket):
    while True:
        data = s.recv(BUFFER_SIZE)
        if data:
            print(f"Получено сообщение: {data.decode('UTF-8')}")
```
Функция `accept` запускается в фоновом режиме и выводит сообщения на экран по мере их получения


