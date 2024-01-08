import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 49001))  
sock.listen(1)

while True:
    conn, adr = sock.accept()
    data = conn.recv(1024).decode("utf-8")
    
    if not data:
        print('Какая-то ошибка')
        break

    with open('C:/Users/nic03/5sem/WebProgramming/lab_1/task3/index.html', 'r') as file:
        html_page = file.read()

    resp = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{html_page}\r\n"
    conn.send(resp.encode("utf-8"))


conn.close()