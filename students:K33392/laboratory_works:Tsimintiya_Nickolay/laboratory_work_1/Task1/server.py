from serverConfigurator import *

configuration = ServerConfigurator()
configuration.default_configuration()
server_socket = configuration.config_udp()

conn, addr = server_socket.recvfrom(1024)
print(conn.decode())
server_socket.sendto(b"Hello, client!", addr)