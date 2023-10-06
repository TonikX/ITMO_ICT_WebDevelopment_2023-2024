import socket
import threading
# как хранятся студенты?
# делаете threading на сервере? Да, каждое следующее сообщение обрабатывается в thread

# Функция обработки соединений с клиентами
def connection(sockets, addrs, niknames):
    while True:
        # Принимаем соединение от клиента и добавляем его сокет в список
        clsocket, addr = s.accept()
        sockets.append(clsocket)
        addrs.append(addr)
        msg = clsocket.recv(1000)
        niknames.append(msg.decode())
        print('Подключился клиент', addr)

# Функция для получения сообщений от одного клиента и отправки их всем остальным клиентам
def get(sock, addrs, sockets, niknames):
    while True:
        try:
            msg = sock.recv(1000)
            print(f"от {sock} было получено сообщение {msg}")
        except Exception as e:
            # Если возникает ошибка при получении сообщения, удаляем клиентский сокет и выходим из цикла
            sockets.remove(sock)
            print(f"Ох хо кажется была ошибка про получении сообщения от {sock}")
            break
        # Пересылаем сообщение от одного клиента всем остальным клиентам
        for soc in sockets:
            if soc != sock:
                string_1 = niknames[sockets.index(sock)] + ': ' +msg.decode()
                soc.send(bytes(string_1, 'utf-8'))
                print(f"Переслали сообщение {msg} пользователю {soc}")

# Функция для создания отдельных потоков для каждого клиента
def make_threads(sockets, addrs, threads):
    while True:
        for soc in sockets:
            if soc in threads:
                continue
            print(f"Ого мы создаём поток! для {soc}")
            # Создаем новый поток для клиента и передаем ему соответствующий сокет
            t = threading.Thread(target=get, args=(soc, addrs, sockets, niknames))
            t.start()
            threads.append(soc)

# Создаем серверный сокет
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем серверный сокет к хосту (этому компьютеру) и порту 2020
s.bind((socket.gethostname(), 1010))

# Начинаем слушать порт, принимая до 10 клиентских соединений
s.listen(10)

# Создаем список для хранения клиентских сокетов и список для хранения потоков
sockets = []
addrs = []
niknames = []
threads = []

# Создаем поток для обработки новых соединений
t1 = threading.Thread(target=connection, args=(sockets, addrs, niknames, ))
t1.start()

# Создаем поток для создания потоков для каждого клиента
t2 = threading.Thread(target=make_threads, args=(sockets, addrs, threads,))
t2.start()

# Ожидаем завершения потока t2
t2.join()
