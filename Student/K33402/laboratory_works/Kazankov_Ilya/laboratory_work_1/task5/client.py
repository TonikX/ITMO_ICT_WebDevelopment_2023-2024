import socket

def send_get_request():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12413)
    
    try:
        client_socket.connect(server_address)
        
        request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
        client_socket.send(request.encode('utf-8'))
        
        response = client_socket.recv(1024).decode('utf-8')
        print(response)
    except Exception as e:
        print(f'Ошибка при отправке GET запроса: {str(e)}')
    finally:
        client_socket.close()

def send_post_request(discipline, grade):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12413)
    
    try:
        client_socket.connect(server_address)
        
        data = f"discipline={discipline}&grade={grade}"
        request = f"POST / HTTP/1.1\r\nHost: localhost\r\nContent-Length: {len(data)}\r\n\r\n{data}"
        client_socket.send(request.encode('utf-8'))
        
        response = client_socket.recv(1024).decode('utf-8')
        print(response)
    except Exception as e:
        print(f'Ошибка при отправке POST запроса: {str(e)}')
    finally:
        client_socket.close()

if __name__ == "__main__":
    while True:
        print("Выберите действие:")
        print("1. Отправить GET запрос (получить список оценок)")
        print("2. Отправить POST запрос (добавить оценку)")
        print("3. Выйти")
        
        choice = input("Введите номер действия: ")
        
        if choice == "1":
            send_get_request()
        elif choice == "2":
            discipline = input("Введите название дисциплины: ")
            grade = input("Введите оценку: ")
            send_post_request(discipline, grade)
        elif choice == "3":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")