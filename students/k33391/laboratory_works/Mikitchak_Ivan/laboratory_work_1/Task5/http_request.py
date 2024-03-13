class HTTPRequest:
	def __init__(self, method, url, version, headers, body):
		self.method = method
		self.url = url
		self.version = version
		self.headers = headers
		self.body = body