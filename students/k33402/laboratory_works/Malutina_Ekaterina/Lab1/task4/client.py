import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    name = input('Enter nickname (less 10 symbols): ')
    if 1 < len(name) < 10:
        break

client.connect((socket.gethostname(), 1236))
print('connected')
print('To close press Z')


def out_datas():
    while True:
        outdata = input('')
        print()
        if outdata == 'Y':
            client.send(f'{name}: disconnected'.encode('utf-8'))
            break

        if outdata == '':
            continue
        client.send(f'{name}: {outdata}'.encode('utf-8'))
        print(f'{name}: {outdata}')


def input_datas():
    while True:
        input_data = client.recv(1024)
        print(input_data.decode('utf-8'))


input_thread = threading.Thread(target=input_datas, name='input')
input_thread.start()

out_thread = threading.Thread(target=out_datas, name='out')
out_thread.start()

out_thread.join()

print('server closed')
client.close()
