import socket
import re
import signal

port = 2448
enc = "utf-8"

student_marks = {
    "Zahar": [9],
    "Alexei": [88],
    "Maksim": [33]
}

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Points</title>
</head>
<body>
    <h1>Student Points</h1>
    <ul>
        {student_list}
    </ul>
<form method="post" action="/">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>
    <br><br>
    <label for="marks">Points:</label>
    <input type="number" id="marks" name="marks" required>
    <br><br>
    <input type="submit" value="Submit">
</form>
</body>
</html>
"""

def generate_student_list():
    student_list = ""
    for name, marks in student_marks.items():
        mark_str = ", ".join(map(str, marks))
        student_list += f"<li> {name} : {mark_str}"
    return student_list

def handle_request(request):
    print(request)
    if request.startswith("GET"):
        response_body = html_template.format(student_list=generate_student_list())
        response = f"HTTP/1.1 200 OK\r\nContent-Length: {len(response_body)}\r\n\r\n{response_body}"

    elif request.startswith("POST"):
        match = re.search(r"name=(\w+)&marks=(\d+)", request).groups()

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
    server_socket.bind(("localhost", port))
    server_socket.listen(5)
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    print("Server is listening on port ", port)

    while True:
        client_socket, client_address = server_socket.accept()
        print("Accepted connection from: ", client_address)

        request = client_socket.recv(1024).decode(enc)
        response = handle_request(request)
        client_socket.sendall(response.encode(enc))
        client_socket.close()

if __name__ == "__main__":
    main()
