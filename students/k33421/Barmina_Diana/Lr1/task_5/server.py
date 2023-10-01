from MyHTTPServer import MyHTTPServer


if __name__ == '__main__':
    HOST = '127.0.0.1'
    SERVER_PORT = 14900
    my_server = MyHTTPServer(HOST, SERVER_PORT)
    my_server.serve_forever()