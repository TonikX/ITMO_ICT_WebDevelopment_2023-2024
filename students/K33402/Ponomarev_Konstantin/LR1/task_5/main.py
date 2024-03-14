from task_5.server.MyHTTPServer import MyHTTPServer

if __name__ == '__main__':
    server = MyHTTPServer("localhost", 8888)
    server.init()
