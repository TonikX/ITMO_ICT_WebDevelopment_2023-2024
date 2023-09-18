import socket


conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 5000))

operation = input("Enter operation (cathetus/hypotenuse or c/h): ")
while operation not in ("cathetus", "c", "hypotenuse", "h"):
    operation = input("Invalid operation. Try again: ")
if operation in ("c", "h"):
    operation = "cathetus" if operation == "c" else "hypotenuse"
while True:
    if operation == "cathetus":
        a = input("Enter cathetus: ")
        b = input("Enter hypotenuse: ")
    else:
        a = input("Enter cathetus: ")
        b = input("Enter cathetus: ")
    try:
        a = float(a)
        b = float(b)
        break
    except ValueError:
        print("Invalid input. Try again.")

conn.send(bytes(f"{operation} {a} {b}", encoding="utf-8"))
result = conn.recv(1024).decode("utf-8")
print(f"Result: {result}")
