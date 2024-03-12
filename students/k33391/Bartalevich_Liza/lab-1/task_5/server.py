# Импортирует модуль socket для работы с сетевыми соединениями
import socket
# Импортирует defaultdict из модуля collections для работы со словарями с автозаполнением
from collections import defaultdict


class MyHTTPServer:
    def __init__(self, host, port, server_name):
        self._host = host  # Сохраняет адрес хоста
        self._port = port  # Сохраняет номер порта
        self._server_name = server_name  # Сохраняет имя сервера
        self.grades = []  # Инициализирует список для оценок
        self.subjects = []  # Инициализирует список для предметов

    def serve_forever(self):
        serv_sock = socket.socket(
            socket.AF_INET,  # Задает семейство адресов интернета
            socket.SOCK_STREAM,  # Задает тип сокета TCP
            proto=0  # Автоматический выбор протокола
        )

        try:
            serv_sock.bind((self._host, self._port))  # Привязывает сокет к адресу и порту
            serv_sock.listen()  # Переводит сокет в режим прослушивания входящих соединений

            while True:  # Бесконечный цикл для обработки входящих соединений
                conn, _ = serv_sock.accept()  # Принимает входящее соединение
                try:
                    self.serve_client(conn)  # Обрабатывает запрос клиента
                except Exception as e:
                    print('Client serving failed', e)  # Выводит сообщение об ошибке при обслуживании клиента
        finally:
            serv_sock.close()  # Закрывает сокет сервера

    def serve_client(self, conn):
        try:
            req = self.parse_request(conn)  # Разбирает HTTP-запрос
            if req.method == 'GET':  # Проверяет, является ли метод запроса GET
                print("Get request started")
                resp = self.handle_get_request(req)  # Обрабатывает GET-запрос
            elif req.method == 'POST':  # Проверяет, является ли метод запроса POST
                print("Post req started")
                resp = self.handle_post_request(req)  # Обрабатывает POST-запрос
            else:
                # Создает ответ с ошибкой, если метод не поддерживается
                resp = self.create_response(405, 'Method Not Allowed', 'Only GET and POST methods are supported.')

            self.send_response(conn, resp)  # Отправляет ответ клиенту
        except ConnectionResetError:
            conn = None  # Обрабатывает ошибку сброса соединения
        except Exception as e:
            self.send_error(conn, e)  # Отправляет сообщение об ошибке клиенту

        if conn:
            conn.close()  # Закрывает соединение с клиентом


    def parse_request(self, conn):
        request_data = b''  # Инициализирует переменную для данных запроса
        while b'\r\n\r\n' not in request_data:  # Читает данные запроса до получения пустой строки (конец заголовков)
            data = conn.recv(1024)  # Читает данные из соединения
            if not data:
                break  # Прерывает цикл, если данные не были получены
            request_data += data  # Добавляет полученные данные к общим данным запроса

        if not request_data:
            raise ValueError('Invalid request')  # Вызывает исключение, если запрос пуст

        request_lines = request_data.decode('utf-8').split('\r\n')  # Разбивает данные запроса на строки
        method, path, _ = request_lines[0].split(' ')  # Разбирает строку запроса
        headers = {}  # Инициализирует словарь для заголовков
        for line in request_lines[1:]:  # Перебирает строки заголовков
            if ':' in line:  # Проверяет, содержит ли строка заголовок
                key, value = line.split(':', 1)  # Разбирает строку на ключ и значение заголовка
                headers[key.strip()] = value.strip()  # Добавляет заголовок в словарь

        if "?" in path:  # Проверяет, содержит ли путь параметры запроса
            params = (
                {p.split("=")[0]: p.split("=")[1] for p in path.split("?")[1].split("&")}
                    )  # Разбирает параметры запроса
        else:
            params = None  # Устанавливает параметры запроса в None, если их нет

        print(params)  # Выводит параметры запроса

        return HTTPRequest(method, path.split("?")[0], headers, params)  # Возвращает объект HTTPRequest

    def handle_get_request(self, req):
        if req.path == '/':  # Проверяет, запрашивается ли корневой путь
            response_body = '<html><body><h1>List of subjects</h1><ul>{}</ul></body></html>'  # Шаблон тела ответа
            grades_by_subject = defaultdict(list)  # Создает словарь для оценок по предметам с автозаполнением списками
            for subject, grade in zip(self.subjects, self.grades):  # Перебирает предметы и оценки
                grades_by_subject[subject].append(str(grade))  # Добавляет оценку к соответствующему предмету

            items = ''.join(
                '<li>{} - {}</li>'.format(subject, ', '.join(grades)) for subject, grades in grades_by_subject.items()
            )  # Создает список предметов и оценок для вставки в тело ответа
            response_body = response_body.format(items)  # Формирует тело ответа
            return self.create_response(200, 'OK', response_body)  # Возвращает ответ
        else:
            # Возвращает ответ с ошибкой, если путь не найден
            return self.create_response(404, 'Not Found', 'Page not found')

    def handle_post_request(self, req):
        if req.path == '/record':  # Проверяет, соответствует ли путь цели сохранения записи
            self.grades.append(req.params.get("grade"))  # Добавляет оценку в список оценок
            self.subjects.append(req.params.get("subject"))  # Добавляет предмет в список предметов
            # Возвращает ответ об успешном сохранении
            return self.create_response(200, 'OK', 'Record saved')
        else:
            # Возвращает ответ с ошибкой, если путь не найден
            return self.create_response(404, 'Not Found', 'Page not found')

    def create_response(self, status_code, status_text, body):
        response = f"HTTP/1.1 {status_code} {status_text}\r\n"  # Формирует стартовую строку ответа
        response += f"Server: {self._server_name}\r\n"  # Добавляет заголовок сервера
        response += "Content-Type: text/html\r\n"  # Устанавливает тип содержимого

        response += f"Content-Length: {len(body)}\r\n"  # Устанавливает длину содержимого
        response += "\r\n"  # Добавляет пустую строку, разделяющую заголовки и тело сообщения
        response += body  # Добавляет тело сообщения

        return response.encode('utf-8')  # Кодирует ответ в байты и возвращает

    def send_response(self, conn, resp):
        conn.sendall(resp)  # Отправляет полный ответ клиенту

    def send_error(self, conn, err):
        error_message = f"HTTP/1.1 500 Internal Server Error\r\n\r\nError: {err}"  # Формирует сообщение об ошибке
        conn.sendall(error_message.encode('utf-8'))  # Отправляет сообщение об ошибке клиенту


class HTTPRequest:
    def __init__(self, method, path, headers, params):
        self.method = method  # Сохраняет метод запроса
        self.path = path  # Сохраняет путь запроса
        self.headers = headers  # Сохраняет заголовки запроса
        self.params = params  # Сохраняет параметры запроса

    def read_body(self, length):
        body = b''  # Инициализирует переменную для тела запроса
        while len(body) < length:  # Читает тело запроса до достижения указанной длины
            data = self.conn.recv(length - len(body))  # Читает данные из соединения
            if not data:
                break  # Прерывает цикл, если данные не были получены
            body += data  # Добавляет полученные данные к телу запроса

        return body.decode('utf-8')  # Декодирует тело запроса из байтов в строку и возвращает


if __name__ == '__main__':
    host = 'localhost'  # Задает адрес хоста
    port = 8000  # Задает номер порта
    name = 'Liz_on'  # Задает имя сервера

    serv = MyHTTPServer(host, port, name)  # Создает экземпляр сервера
    print("Server listening on port", port)  # Выводит сообщение о запуске сервера
    try:
        serv.serve_forever()  # Запускает сервер для обработки запросов
    except KeyboardInterrupt:
        pass  # Позволяет остановить сервер с помощью Ctrl+C
