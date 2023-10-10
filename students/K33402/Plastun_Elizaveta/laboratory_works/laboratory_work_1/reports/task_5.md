#  🗿 Задача 1 
Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу сообщение «Hello, server». Сообщение должно отразиться на стороне сервера. Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно отобразиться у клиента.

## 🥸 Реализация
1. Server.py
   
```python
import socket
import re

students_marks = {
    "glista": 0,
}
html = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Marks</title>
</head>
<body>
    <h1>Student Marks</h1>
    <table border width="400">
    <tr>
  <td>     Student name     </td>
  <td>     Mark     </td>
  <tr>
  {student_list}
  </table>
<div style="height: 30px;">
</div>
<form method="post" action="/">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>
    <label for="marks">Marks:</label>
    <input type="number" id="marks" name="marks" required>
    <input type="submit" value="add">
</form>
</body>
</html>
"""


def student_table_html():
    part_of_html = ""
    for name, marks in students_marks.items():
        part_of_html += f"<tr><td>{name}</td><td>{marks}</td></tr>"
    return part_of_html


def handle_request(request):
    print(request)
    if request.startswith("GET"):
        response_body = html.format(student_list=student_table_html())
        response = f"HTTP/1.1 200 OK\r\nContent-Length: {len(response_body)}\r\n\r\n{response_body}"
    elif request.startswith("POST"):
        name, mark = re.search(r'name=(\w+)&marks=(\d+)', request).groups()
        if name and mark:
            students_marks[name] = int(mark)
            response = "HTTP/1.1 302 Found\r\nLocation: /"
        else:
            response = "HTTP/1.1 400 Bad Request\r\nContent-Length: 0\r\n\r\n"
    else:
        response = "HTTP/1.1 400 Bad Request\r\nContent-Length: 0\r\n\r\n"

    return response


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9998))
    server_socket.listen(5)

    while True:
        client_socket, client_address = server_socket.accept()
        request = client_socket.recv(1024).decode('utf-8')
        response = handle_request(request)
        client_socket.sendall(response.encode('utf-8'))
        client_socket.close()


if __name__ == "__main__":
    main()

```


## 🤡 Демонстрация работы
![task_5.1.png](/Users/elizaveta/ITMO_ICT_WebDevelopment_2023-2024/students/K33402/Plastun_Elizaveta/laboratory_works/laboratory_work_1/reports/img/task_5.1.png)
![task_5.2.png](/Users/elizaveta/ITMO_ICT_WebDevelopment_2023-2024/students/K33402/Plastun_Elizaveta/laboratory_works/laboratory_work_1/reports/img/task_5.2.png)
![task_5.3.png](/Users/elizaveta/ITMO_ICT_WebDevelopment_2023-2024/students/K33402/Plastun_Elizaveta/laboratory_works/laboratory_work_1/reports/img/task_5.3.png)

