# task 1
###server.py
    # Импортируем модуль socket для работы с сокетами
    import socket

    # Создаем сокет, используя IPv4 и UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Привязываем сокет к локальному адресу и порту
    sock.bind(('localhost', 8080)) 
    
    # Принимаем данные от клиента и адрес клиента
    data, addr = sock.recvfrom(1024)
    
    # Декодируем полученные данные из байтовой строки в строку UTF-8
    decoded_data = data.decode("utf-8")
    
    # Выводим полученное сообщение на экран
    print("Recieved message:", decoded_data)
    
    # Отправляем ответное сообщение клиенту
    sock.sendto(b"Hello, client!", addr)
    
    # Закрываем сокет
    sock.close()

###client.py
    # Импортируем модуль socket для работы с сокетами
    import socket
    
    # Создаем сокет, используя IPv4 и UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Устанавливаем соединение с сервером
    sock.connect(('localhost', 8080))
    
    # Отправляем сообщение серверу ("Hello, server!") через сокет
    sock.send(b"Hello, server!")
    
    # Получаем данные от сервера
    data = sock.recv(1024)
    
    # Декодируем полученные данные из байтовой строки в строку UTF-8
    decoded_data = data.decode("utf-8")
    
    # Выводим полученное сообщение на экран
    print("Recieved message:", decoded_data)
    
    # Закрываем сокет
    sock.close()

![](task1.png)