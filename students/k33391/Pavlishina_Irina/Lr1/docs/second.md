# Практическое задание 2

Реализовать клиентскую и серверную часть приложения. Клиент запрашивает у
сервера выполнение математической операции, параметры, которые вводятся с
клавиатуры. Сервер обрабатывает полученные данные и возвращает результат
клиенту. Варианты:
- a. Теорема Пифагора
- **b. Решение квадратного уравнения.**
- c. Поиск площади трапеции.
- d. Поиск площади параллелограмма.


Обязательно использовать библиотеку socket
Реализовать с помощью протокола TCP


### Сервер

###### Импорты и глобальные переменные

```
import socket
import threading
    
PORT = 8080
```

###### Тело сервера

```
def main():

    PORT = 8080
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', PORT))
    server_socket.listen(10)

    while True:

        try:
            client_socket, client_address = server_socket.accept()
            thread = threading.Thread(target=chat, args=([client_socket, client_address], ))
            thread.start()

        except KeyboardInterrupt:
            server_socket.close()
            break
```

###### Обработка подключения

```
def parce_string(string):
    return string.split()
    
def chat(client):

    while True:
        client_socket = client[0]
        client_address = client[1]

        data = client_socket.recv(65536).decode('utf-8')
        a, b, c = parce_string(data)
        x1, x2 = quadratic_equation(int(a), int(b), int(c))
        ans = f"X1= {x1}, X2= {x2}"
        client_socket.sendto(ans.encode(), client_address)
```

###### Расчет ответа
```
def quadratic_equation(a, b, c):

    x1 = (-b+(b**2 - 4*a*c)**(1/2))/(2*a)
    x2 = (-b-(b**2 - 4*a*c)**(1/2))/(2*a)
    return x1, x2

```

### Клиент

###### Импорты и глобальные переменные

```
import socket
import threading
import time
    
PORT = 8080
```


###### Тело клиента

```
def main():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', PORT))

    listen = threading.Thread(target=listen_chat, args=(client_socket,))
    listen.start()

    write = threading.Thread(target=write_chat, args=(client_socket,))
    write.start()
```

###### Отправка сообщений серверу

```
def write_chat(client_socket):
    while True:
        client_socket.sendall(f'{random.randint(-100, 100)} {random.randint(-100, 100)} {random.randint(-100, 100)}'
                              .encode('utf-8'))
        time.sleep(1)
```

###### Получение ответа от сервера

```
def listen_chat(client_socket):
    while True:
        ans = client_socket.recv(1024).decode('utf-8')
        print(ans)
```
