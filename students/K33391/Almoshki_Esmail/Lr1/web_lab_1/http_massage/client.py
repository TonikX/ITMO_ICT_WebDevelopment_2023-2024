import socket, webbrowser

FORMAT = 'utf-8'
PORT = 8888
HOST = socket.gethostbyname(socket.gethostname())
ADDRESS = (HOST, PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:



    s.connect(ADDRESS)
    headers = [
        'GET / HTTP/1.1',
        'Host: www.geeksforgeeks.org',
        'Connection: keep-alive',
        'Accept: text/text',
        '\n'
    ]
    content = "\n".join(headers)
    s.send(content.encode(FORMAT))
    result = s.recv(14233)
    print(result.decode(FORMAT))
    ready  = result.decode()
    webbrowser.open_new_tab(ready)