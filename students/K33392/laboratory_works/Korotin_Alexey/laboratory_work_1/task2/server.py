import socket
from json import loads


def solve_equation(parameters: str) -> dict:
    params = loads(parameters)
    output = {}
    try:
        D = float(params["b"]) ** 2 - 4 * float(params["a"]) * float(params["c"])
        if D < 0:
            output["solution"] = "None"
            return output
        if D == 0:
            output["solution"] = -float(params["b"]) / (2 * float(params["a"]))
            return output

        output["solution_1"] = (-float(params["b"]) - D ** 0.5) / (2 * float(params["a"]))
        output["solution_2"] = (-float(params["b"]) + D ** 0.5) / (2 * float(params["a"]))
        return output
    except Exception:
        output["error"] = "invalid parameters"
        return output


if __name__ == "__main__":
    HOST = "localhost"
    PORT = 1234
    BUFFER_SIZE = 2 ** 20

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(10)
        while True:
            try:
                client_socket, address = s.accept()

                data = client_socket.recv(BUFFER_SIZE)

                decoded_data = data.decode("UTF-8")
                print(decoded_data)

                response = solve_equation(decoded_data)

                client_socket.send(str(response).encode("UTF-8"))
            except KeyboardInterrupt:
                break
