from task_5.server.MyHTTPServer import MyHTTPServer

if __name__ == '__main__':
    server = MyHTTPServer("localhost", 9090)
    server.init()
