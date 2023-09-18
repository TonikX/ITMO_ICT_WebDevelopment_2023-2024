import socket
import struct


def recv_msg(conn: socket.socket) -> tuple[bytes, bytes]:
    msg_header = conn.recv(4)
    if msg_header == b"":
        return
    length = struct.unpack(">I", msg_header)[0]
    return conn.recv(length)


def create_msg(msg: str):
    msg = msg.encode()
    return struct.pack(">I", len(msg)) + msg
