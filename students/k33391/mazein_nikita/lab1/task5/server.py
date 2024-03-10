import socket
import re
import signal

student_marks = {
    "Bob": [85],
    "Tom": [92],
    "Shlick-Shlack": [78],
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
        mark_str = ', '.join(map(str, marks))
        student_list += f'<li> {name} : {mark_str}'
    return student_list

def handle_request(request):
    print(request)
    if request.startswith("GET"):
        response_body = html_template.format(student_list=generate_student_list())
        response = f"HTTP/1.1 200 OK\r\nContent-Length: {len(response_body)}\r\n\r\n{response_body}"

    elif request.startswith("POST"):
        match = re.search(r'name=(\w+)&marks=(\d+)', request).groups()

        if match:
            post_data = match
            name, mark = post_data[0], int(post_data[1])
            if name in student_marks:
                student_marks[name].append(mark)
            else:
                student_marks[name] = []
                student_marks[name].append(mark)
            response = "HTTP/1.1 302 Found\r\nLocation: /"

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
