import socket

host = 'localhost'
port = 9090
addr = (host,port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(addr)

request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
s.sendall(request.encode('utf-8'))

response = b""
while True:
    try:
        data = s.recv(1024)
    except:
        break
    response += data

s.close()

http_response = response.decode('utf-8')

head, body = http_response.split('\r\n', 1)
print(head)
print(body)