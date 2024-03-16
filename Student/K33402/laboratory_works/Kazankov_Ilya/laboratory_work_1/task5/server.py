import socket
import threading

class WebServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.disciplines_data = {}
    
    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print('Сервер ожидает подключения клиентов...')
        
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f'Подключен клиент: {client_address}')
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()
    
    def handle_client(self, client_socket):
        try:
            request_data = client_socket.recv(1024).decode('utf-8')
            
            if "GET /" in request_data:
                self.handle_get_request(client_socket)
            elif "POST /" in request_data:
                request_body = request_data.split('\r\n\r\n')[1]
                self.handle_post_request(client_socket, request_body)
        except Exception as e:
            print(f'Ошибка при обработке запроса: {str(e)}')
        finally:
            client_socket.close()
    
    def handle_get_request(self, client_socket):
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        response += "<html><body>"
        response += "<h1>Список оценок по дисциплинам:</h1>"
        for discipline, grades in self.disciplines_data.items():
            response += f"<p>{discipline}: {', '.join(grades)}</p>"
        response += "</body></html>"
        client_socket.send(response.encode('utf-8'))
    
    def handle_post_request(self, client_socket, data):
        try:
            data = data.split('&')
            discipline = data[0].split('=')[1]
            grade = data[1].split('=')[1]
            if discipline in self.disciplines_data:
                self.disciplines_data[discipline].append(grade)
            else:
                self.disciplines_data[discipline] = [grade]
            response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
            response += "<html><body>"
            response += "<h1>Данные успешно добавлены</h1>"
            response += "<p><a href='/'>Вернуться к списку оценок</a></p>"
            response += "</body></html>"
            client_socket.send(response.encode('utf-8'))
        except Exception as e:
            print(f'Ошибка при обработке POST запроса: {str(e)}')
            response = "HTTP/1.1 500 Internal Server Error\r\n\r\n"
            client_socket.send(response.encode('utf-8'))

if __name__ == "__main__":
    web_server = WebServer('localhost', 12413)
    web_server.start()