#Задание 2

Реализовать клиентскую и серверную часть приложения. Клиент запрашивает у
сервера выполнение математической операции (решение квадратного уравнения), параметры, которые вводятся с
клавиатуры. Сервер обрабатывает полученные данные и возвращает результат
клиенту. Реализовать с помощью протокола TCP.

###Реализация сервера
```python
import socket
import math

# функция принятия сообщения и записи в лог файл
def get_message():
    data = connection.recv(128).decode()
    log_file.write(f'Message from {address[0]}:{address[1]}: {data}\n')
    return data

# функция отправки сообщения
def send_message(msg):
    connection.send(msg.encode())
    log_file.write(f'Message to {address[0]}:{address[1]}: {msg}\n')

# решение уравнения
def find_roots(coefficients):
    a, b, c = map(float, coefficients.split())
    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        return 'This equation has no real roots'
    x1 = (b * (-1) + math.sqrt(discriminant)) / (2 * a)
    x2 = (b * (-1) - math.sqrt(discriminant)) / (2 * a)
    if x1 == x2:
        return f'This equation has one root: {x1}'
    else:
        return f'Roots of this equation are: {x1} and {x2}'


log_file = open("server3.log", "w")

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('localhost', 55555)) # создание и привязка сокета

socket.listen(1)
connection, address = socket.accept() #принятие подключения от клиента
send_message('Please type \'Find equation roots\' to find roots of your quadratic equation'
             '\nType \'exit\' to terminate connection')

while True:
    # взаимодействие с клиентом
    message = get_message() 

    if message == 'Find equation roots':
        send_message('Enter equation coefficients\nExample: 1 4 3')

        coefficients = get_message()
        answer = find_roots(coefficients)

        send_message(answer)
    elif message == 'exit':
        break
    else:
        send_message('No understanding')

socket.close()
```

###Реализация клиента
```python
import socket

# получение сообщения от сервера
def receive_message():
    message = socket.recv(128).decode()
    print(message)

# создание сокета и соединение с сервером
server_address = ('localhost', 55555)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(server_address) 

receive_message()

while True:
    # взаимодействие с сервером
    msg = input()
    socket.send(msg.encode())
    if msg == 'exit':
        break
    elif msg == 'Find equation roots':
        receive_message()

        coefficients = input()
        socket.send(coefficients.encode())
        receive_message()
    else:
        receive_message()

socket.close()
```

###Пример работы
![Пример задания 2](images/task2.png)

###Log файл
```log
Message to 127.0.0.1:51621: Please type 'Find equation roots' to find roots of your quadratic equation
Type 'exit' to terminate connection
Message from 127.0.0.1:51621: Find equation roots
Message to 127.0.0.1:51621: Enter equation coefficients
Example: 1 4 3
Message from 127.0.0.1:51621: 1 4 3
Message to 127.0.0.1:51621: Roots of this equation are: -1.0 and -3.0
Message from 127.0.0.1:51621: Find equation roots
Message to 127.0.0.1:51621: Enter equation coefficients
Example: 1 4 3
Message from 127.0.0.1:51621: 1 4 4
Message to 127.0.0.1:51621: This equation has one root: -2.0
Message from 127.0.0.1:51621: exit
```
