class Request:
    def __init__(self, client, method, options):
        self.client = client
        self.method = method
        self.options = options

