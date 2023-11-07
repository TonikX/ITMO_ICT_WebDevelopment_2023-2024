Title: TCP Server

## Формулировка задания

Реализовать клиентскую и серверную часть приложения. Клиент запрашивает у
сервера выполнение математической операции, параметры, которые вводятся с
клавиатуры. Сервер обрабатывает полученные данные и возвращает результат
клиенту. Варианты:
- Теорема Пифагора
- Решение квадратного уравнения.
- Поиск площади трапеции.
- Поиск площади параллелограмма.

Коротин Алексей 336666 - 10ый номер по списку группы, следовательно, номер варианта - 2.

## Задаем параметры сервера 
```python
HOST = "localhost"
PORT = 1234
BUFFER_SIZE = 2 ** 20
```

## Функция решения квадратного уравнения
```python
def solve_equation(parameters: str) -> dict:
    params = loads(parameters)
    output = {}
    try:
        D = float(params["b"]) ** 2 - 4 * float(params["a"]) * float(params["c"])
        if D < 0:
            output["solution"] = "None"
            return output
        if D == 0:
            output["solution"] = -float(params["b"]) / (2 * float(params["a"]))
            return output

        output["solution_1"] = (-float(params["b"]) - D ** 0.5) / (2 * float(params["a"]))
        output["solution_2"] = (-float(params["b"]) + D ** 0.5) / (2 * float(params["a"]))
        return output
    except Exception:
        output["error"] = "invalid parameters"
        return output
```
Функция преобразует входную json-строку в объект. 
Далее - вычисление решений квадратного уравнения (сообщение об ошибках, если они есть)
## Обработка запроса клиента
```python
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(10)
    while True:
        try:
            client_socket, address = s.accept()

            data = client_socket.recv(BUFFER_SIZE)

            decoded_data = data.decode("UTF-8")
            print(decoded_data)

            response = solve_equation(decoded_data)

            client_socket.send(str(response).encode("UTF-8"))
        except KeyboardInterrupt:
            break
```
Сервер получает сообщение от клиента и вызывает функцию решения квадратного уравнения.
Далее - возвращает json-строку клиенту
## Формат ответа
### Неверные входные данные
```json
{
  "error": "error description"
}
```
### Уравнение имеет одно решение (или ни одного решения)
```json
{
  "solution": "float or None"
}
```
### Уравнение имеет два различных решение
```json
{
  "solution_1": "float",
  "solution_2": "float"
}
```