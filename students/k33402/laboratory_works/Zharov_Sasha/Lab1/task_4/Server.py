import socket, threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 1236))
server.listen(5)

client_list = list()
client_threads = list()

def accept():
    while True:
        clientsocket, address = server.accept()
        if address not in client_list:
            client_list.append(clientsocket)
        print(f'connect: {address}')

def recv_data(client):
    while True:
        try:
            input_data = client.recv(1024)

        except Exception as e:
            client_list.remove(client)
            print(f'Количество подключений: {len(client_list)}')
            break

        print(input_data.decode('utf-8'))

        for cli in client_list:
            # Перенаправить информацию от клиента и отправить ее другим клиентам
            if cli != client:
                cli.send(input_data)

def out_datas():
    while True:
        print('')
        out_data = input('')
        print()
        if out_data == 'Y':
            break
        print(f'Отправить всем: {out_data}')

    # Отправлять информацию каждому клиенту
    for cli in client_list:
        cli.send(f'Сервер: {out_data}'.encode('utf-8)'))


def input_datas():
    while True:
        for cli in client_list:
            if cli in client_threads:
                continue
            index = threading.Thread(target=recv_data, args=(cli,))
            index.start()
            client_threads.append(cli)

input_thread = threading.Thread(target=input_datas, name='input')
input_thread.start()

out_thread = threading.Thread(target=out_datas, name='out')
out_thread.start()

accept_thread = threading.Thread(target=accept(), name='accept')
accept_thread.start()

out_thread.join()

# Выключите все серверы
for client in client_list:
    client.close()
print('сервер отключен')
