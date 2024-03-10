# Задача
Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ
клиент получает http-сообщение, содержащее html-страницу, которую сервер
подгружает из файла index.html.

## Реализация
1. server.py

```python
import socket
import signal

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 1337))
s.listen(1)
signal.signal(signal.SIGINT, signal.SIG_DFL)

def send_html_response(client_socket):
    with open('index.html', 'rb') as html_file:
        html_content = html_file.read()
        response = b"HTTP/1.1 200 OK\r\n"
        response += b"Content-Type: text/html\r\n"
        response += b"Content-Length: " + str(len(html_content)).encode() + b"\r\n"
        response += b"\r\n"
        response += html_content

        client_socket.send(response)

while True:
    try:
        print("Waiting for a connection...")
        client_socket, client_address = s.accept()
        print(f"Accepted connection from {client_address}")
        request = client_socket.recv(1024)
        print(request.decode())

        send_html_response(client_socket)
        client_socket.close()

    except KeyboardInterrupt:
        print("Server terminated by user.")
        break
```

2. index.html

```html
<html>
        <head>
          <title>My Page</title>
          <style>
            body {
              background-image: url('https://i.stack.imgur.com/J5xAl.gif');
              background-size: cover;
              background-repeat: no-repeat;
            }
          </style>
        </head>
        <body>
          <h1>Welcome to My Page</h1>
          <p>Click the button below to see some cute dogs:</p>
          <button onclick="showDogs()">Click Dogs</button>
          <button onclick="removeDogs()">Remove Dogs</button>
          <script>
            function showDogs() {
              const images = [
                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/cute-cat-photos-1593441022.jpg?crop=0.670xw:1.00xh;0.167xw,0&resize=640:*',
                'https://bit.ly/fcc-relaxing-cat',
                'https://www.everypaw.com/.imaging/mte/everypaw/blog/dam/all-things-pet/buying-a-kitten-heres-what-you-should-look-out-for/buying-a-kitten.jpg/jcr:content/buying-a-kitten.jpg'
              ];
      
              for (const image of images) {
                const imgElement = document.createElement('img');
                imgElement.src = image;
                document.body.appendChild(imgElement);
              }
              alert('Caugth Ya, DogLovers!')
            }
      
            function removeDogs() {
              const images = document.querySelectorAll('img');
              for (const image of images) {
                image.remove();
              }
            }
          </script>
        </body>
</html>
```

## Демонстрация работы

![task31](https://github.com/pol3et/ITMO_ICT_WebDevelopment_2023-2024/assets/80038191/f1ff155b-b3f5-4195-879a-8d2a2d84852d)

![task32](https://github.com/pol3et/ITMO_ICT_WebDevelopment_2023-2024/assets/80038191/f02cd7fc-7108-477a-80b3-713bc4582e61)


