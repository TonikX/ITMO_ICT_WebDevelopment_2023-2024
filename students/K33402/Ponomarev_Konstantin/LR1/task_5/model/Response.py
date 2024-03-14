from dataclasses import dataclass
from http import HTTPStatus


# @see https://developer.mozilla.org/ru/docs/Web/HTTP/Overview#http_%D1%81%D0%BE%D0%BE%D0%B1%D1%89%D0%B5%D0%BD%D0%B8%D1%8F
@dataclass
class Response:
    protocolVersion: str
    headers: dict[str, str]
    body: bytes
    status: int

    def to_byte(self):
        headers_str = "\n".join(f"{header_key}: {header_value}" for header_key, header_value in self.headers.items())
        return f"{self.protocolVersion} {self.status} {HTTPStatus(self.status).phrase}\n{headers_str}\n\n".encode() + self.body
