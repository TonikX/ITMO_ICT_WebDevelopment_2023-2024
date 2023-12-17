import socket
from numpy import polynomial 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 49001))  
sock.listen(1)

conn, adr = sock.accept()

while True:
    try:
        data = conn.recv(1024).decode("utf-8")
        data = data.split()
        a, b, c = int(data[0]), int(data[1]), int(data[2])

        if (b*b - 4*a*c) >= 0:
            pol = polynomial.Polynomial([a, b, c])
            pol = pol.roots()
            roots = str(pol[0]) + ' ' + str(pol[1])
            print('Корни найдены')
        else:
            roots = "Нет корней"
            print('Корни не найдены')
        conn.send(roots.encode())
    except:
        conn.close()
        break