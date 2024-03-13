import socket


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(('localhost', 9998))
        a = input('Введите высоту параллелограмма: ')
        b = input('Введите длину стороны параллелограмма: ')
        data = a + ',' + b
        client.send(data.encode('utf-8'))
        print('Площадь параллелограмма равна: ' + client.recv(1024).decode('utf-8'))
    except Exception as e:
        print('Error: ', str(e))
    finally:
        client.close()


if __name__ == '__main__':
    main()




