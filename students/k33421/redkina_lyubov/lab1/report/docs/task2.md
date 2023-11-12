# task 2
###server.py
    # Импортируем модуль socket для работы с сокетами
    import socket
    
    # Функция для вычисления площади трапеции
    def calculate_trapezoid_area(base1, base2, height):
        # Формула для вычисления площади трапеции
        return 0.5 * (base1 + base2) * height
    
    # Создаем сокет TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Привязываем сокет к локальному адресу и порту
    sock.bind(('localhost', 8080))
    
    # Ожидаем только одно подключение
    sock.listen(1)
    
    print("server is runnig")
    
    while True:
        # Принимаем подключение от клиента и для порядка выводим информацию о клиенте
        connection, client_address = sock.accept()
        print(f"Подключено клиентом: {client_address}")
    
        try:
            # Получаем данные от клиента
            data = connection.recv(1024)
            decoded_data = data.decode("utf-8")
    
            # Разбиваем строку на три числа
            base1, base2, height = map(float, decoded_data.split(','))
    
            # Вычисляем площадь трапеции
            result = calculate_trapezoid_area(base1, base2, height)
    
            # Отправляем результат клиенту
            connection.send(str(result).encode())
            print(f"Отправлен результат {result} клиенту: {client_address}")
        except ValueError:
            print("Ошибка: Некорректные данные от клиента.")
            break
    
        # Закрываем соединение с клиентом
        connection.close()
    
###client.py
    # Импортируем модуль socket для работы с сокетами
    import socket
    
    # Создаем сокет TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Устанавливаем соединение с сервером
    sock.connect(('localhost', 8080))
    
    try:
        # Вводим основания и высоту трапеции с клавиатуры
        base1 = float(input("Введите длину первого основания: "))
        base2 = float(input("Введите длину второго основания: "))
        height = float(input("Введите высоту трапеции: "))
    
        # Отправляем числа серверу в виде строки с разделителями
        data_to_send = f"{base1},{base2},{height}"
        sock.send(data_to_send.encode())
    
        # Получаем ответ от сервера
        data = sock.recv(1024)
        decoded_data = data.decode("utf-8")
        print("Площадь трапеции, вычисленная сервером:", decoded_data)
    except ValueError:
        print("Ошибка: Введите корректные числа.")
    
    # Закрываем сокет клиента
    sock.close()

![](task2.png)