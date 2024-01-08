import socket
import sys



class MyHTTPServer:
    # Параметры сервера
    def __init__(self, ip, port, codage):
        self.ip = ip
        self.port = port
        self.grades = {}
        self.codage = codage

    def serve_forever(self):
        #1. Запуск сервера на сокете, обработка входящих соединений
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.ip, self.port))
        server_socket.listen(10)
        while True:
            client_socket, addr = server_socket.accept()
            self.serve_client(client_socket)


    def serve_client(self, client_socket):
        # 2. Обработка клиентского подключения
        data = client_socket.recv(1024).decode(self.codage)
        try:
            request = self.parse_request(data)
            response = self.handle_request(request)
            if response:
                client_socket.send(response.encode('utf-8'))
        except Exception as e:
            error_msg = "HTTP/1.1 400 Bad Request\n\n"
            client_socket.send(error_msg.encode('utf-8'))
        finally:
            client_socket.close()

    def parse_request(self, data):
        # 3. функция для обработки заголовка http+запроса.
        # Python, сокет предоставляет возможность создать вокруг него некоторую обертку,
        # которая предоставляет file object интерфейс. Это дайте возможность построчно обработать запрос.
        # Заголовок всегда - первая строка. Первую строку нужно разбить на 3 элемента  (метод + url + версия протокола).
        # URL необходимо разбить на адрес и параметры (isu.ifmo.ru/pls/apex/f?p=2143 ,
        # где isu.ifmo.ru/pls/apex/f, а p=2143 - параметр p со значением 2143)
        lines = data.split('\r\n')
        headers = lines[0].split()
        print(f"Headers : {headers}, {len(headers)}")

        if len(headers) != 3:
            raise Exception("Bad request line")

        body = lines[-1]
        print(body)
        grds = {}
        if ":" in body:
            grds = {grade.split(":")[0]: grade.split(":")[1]
                    for grade in body.split(";")}
        request = {"method": headers[0], "url": headers[1],
                   "version": headers[2], "grades": grds}

        return request


    def handle_request(self, request):
        # 5. Функция для обработки url в соответствии с нужным методом.
        # В случае данной работы, нужно будет создать набор условий,
        # который обрабатывает GET или POST запрос.
        # GET запрос должен возвращать данные.
        # POST запрос должен записывать данные на основе переданных параметров.
        if request["method"] == "POST":
            for subject, grade in request["grades"].items():
                if subject not in self.grades:
                    self.grades[subject] = []
                self.grades[subject].extend(grade)
            #with open('index.html', 'r') as f:
            return f"HTTP/1.1 200 OK\n\n"
        elif request["method"] == "GET":
            response = f"HTTP/1.1 200 OK\n\n" \
                       + "<html><head><title>Grades</title></head><body>"
            response += "<table border='1'>"
            response += "<tr><th>Subject</th><th>Grades</th></tr>"
            for subject, grades in self.grades.items():
                grades_str = ", ".join(map(str, grades))
                response += f"<tr><td>{subject}</td><td>{grades_str}</td></tr>"
            response += "</table>"
            response += "</body></html>"
            return response
        else:
            return "HTTP/1.1 405 Something wrong with request\n\n"

    #def send_response(self, *):
        # 6. Функция для отправки ответа. Необходимо записать в соединение status line вида HTTP/1.1 <status_code> <reason>.
        # Затем, построчно записать заголовки и пустую строку, обозначающую конец секции заголовков.

if __name__ == '__main__':
    IP = "127.0.0.1"
    PORT = 44455
    codage = 'utf-8'
    serv = MyHTTPServer(IP, PORT, codage)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass

