import socket
import requests
import requests

url = 'http://127.0.0.1:8080'
data = {'Subject': 'Math', 'Grade': 'A'}

response = requests.post(url, data=data)
print(response.text)

# Создаем сокет сервера
server_host = "127.0.0.1"
server_port = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_host, server_port))
server_socket.listen(5)
print(f"Сервер слушает на {server_host}:{server_port}")

# База данных для хранения информации о дисциплине и оценках
grades = {}

# Функция для обработки GET запросов
def handle_get(request):
    response = "HTTP/1.1 200 OK\nContent-Type: text/html\n\n"
    response += "<html><body>"
    response += "<h1>Оценки по дисциплине</h1>"
    response += "<ul>"
    
    for subject, grade in grades.items():
        response += f"<li>{subject}: {grade}</li>"
    
    response += "</ul></body></html>"
    return response

# Функция для обработки POST запросов
def handle_post(request):
    data = request.split("\n")
    subject = None
    grade = None
    
    for line in data:
        if "Subject:" in line:
            subject = line.split(":")[1].strip()
        elif "Grade:" in line:
            grade = line.split(":")[1].strip()
    
    if subject and grade:
        grades[subject] = grade
        return "HTTP/1.1 200 OK\nContent-Type: text/html\n\nДанные сохранены"
    else:
        return "HTTP/1.1 400 Bad Request\nContent-Type: text/html\n\nНеверный формат запроса"

# Основной цикл сервера
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Подключено клиентов с адреса: {client_address}")

    request_data = client_socket.recv(1024).decode('utf-8')
    
    if "GET /" in request_data:
        response = handle_get(request_data)
    elif "POST /" in request_data:
        response = handle_post(request_data)
    else:
        response = "HTTP/1.1 404 Not Found\nContent-Type: text/html\n\nСтраница не найдена"

    client_socket.send(response.encode('utf-8'))
    client_socket.close()
