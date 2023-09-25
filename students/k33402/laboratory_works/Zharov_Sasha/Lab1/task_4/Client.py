import socket, threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    name = input ('Введите личный ник (меньше 10 символов): ')
    if 1 < len(name) < 10:
        break

client.connect((socket.gethostname(), 1236))
print ('подключился к серверу')
print ('Чтобы закрыть соединение с сервером нажмите Y' )


def out_datas():
    while True:
        # Введите информацию, которая будет отправлена на сервер
        outdata = input('')
        print()
        if outdata == 'Y':
            client.send(f'{name}: отключился'.encode('utf-8'))
            break

        if outdata == '':
            continue
            # Отправить на сервер
        client.send(f'{name}: {outdata}'.encode('utf-8'))
        print(f'{name}: {outdata}')

def input_datas():
    while True:
        # Принимаем информацию с сервера
        input_data = client.recv(1024)

        # Расшифровать полученную информацию
        print(input_data.decode('utf-8'))

input_thread = threading.Thread(target=input_datas, name='input')
input_thread.start()

out_thread = threading.Thread(target=out_datas, name='out')
out_thread.start()

out_thread.join()

# Закрыть соединение
print('сервер отключен')
client.close()
