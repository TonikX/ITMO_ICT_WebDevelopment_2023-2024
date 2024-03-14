from dataclasses import dataclass

from task_5.model.Method import Method


# @see https://developer.mozilla.org/ru/docs/Web/HTTP/Overview#http_%D1%81%D0%BE%D0%BE%D0%B1%D1%89%D0%B5%D0%BD%D0%B8%D1%8F
@dataclass
class Request:
    method: Method
    path: str
    protocolVersion: str
    headers: dict[str, str]
    body: bytes
