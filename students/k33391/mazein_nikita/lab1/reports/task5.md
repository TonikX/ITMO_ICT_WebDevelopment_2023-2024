#Задача
Необходимо написать простой web-сервер для обработки GET и POST http
запросов средствами Python и библиотеки socket.
Задание: сделать сервер, который может:
* Принять и записать информацию о дисциплине и оценке по дисциплине.
* Отдать информацию обо всех оценах по дсициплине в виде html-страницы.

##Реализация
server.py

```python
import socket
import re
import signal

student_marks = {
    "Bob": 85,
    "Tom": 92,
    "Shlick-Shlack": 78,
}

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Marks</title>
</head>
<body>
    <h1>Student Marks</h1>
    <ul>
        {student_list}
    </ul>
<form method="post" action="/">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>
    <label for="marks">Marks:</label>
    <input type="number" id="marks" name="marks" required>
    <input type="submit" value="Submit">
</form>
</body>
</html>
"""

def generate_student_list():
    student_list = ""
    for name, marks in student_marks.items():
        student_list += f"<li>{name}: {marks}</li>"
    return student_list

def handle_request(request):
    print(request)
    if request.startswith("GET"):
        response_body = html_template.format(student_list=generate_student_list())
        response = f"HTTP/1.1 200 OK\r\nContent-Length: {len(response_body)}\r\n\r\n{response_body}"
    elif request.startswith("POST"):
        match = re.search(r'name=(\w+)&marks=(\d+)', request).groups()
        print(match)
        if match:
            post_data = match
            name, marks = post_data[0], int(post_data[1])
            student_marks[name] = marks
            print(student_marks.items())
            response = "HTTP/1.1 302 Found\r\nLocation: /"  # Redirect to the main page
        else:
            response = "HTTP/1.1 400 Bad Request\r\nContent-Length: 0\r\n\r\n"
    else:
        response = "HTTP/1.1 400 Bad Request\r\nContent-Length: 0\r\n\r\n"

    return response

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 1337))
    server_socket.listen(5)
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    print("Server is listening on port 1337...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        request = client_socket.recv(1024).decode('utf-8')
        response = handle_request(request)
        client_socket.sendall(response.encode('utf-8'))
        client_socket.close()

if __name__ == "__main__":
    main()
```

##Демонстрация работы

![task51](https://github.com/pol3et/ITMO_ICT_WebDevelopment_2023-2024/assets/80038191/a27aeb46-38ae-4dcf-9b4b-ca1213eb18f0)

![task52](https://github.com/pol3et/ITMO_ICT_WebDevelopment_2023-2024/assets/80038191/23382052-82a2-411f-b408-ca17c558c730)

![task53](https://github.com/pol3et/ITMO_ICT_WebDevelopment_2023-2024/assets/80038191/207c4624-6327-47d4-a943-905230fc941b)

![task54](https://github.com/pol3et/ITMO_ICT_WebDevelopment_2023-2024/assets/80038191/9b284e6c-61a8-43b6-ad39-c14577be266a)




