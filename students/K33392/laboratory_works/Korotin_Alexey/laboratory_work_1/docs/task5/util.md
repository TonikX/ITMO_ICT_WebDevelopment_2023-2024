## Utility-функции

### Декоратор `request_mapping`
```python
MAPPERS = dict()

def request_mapping(endpoint: str, method: str):
    def mapper(func):
        if method not in MAPPERS:
            MAPPERS[method] = dict()
        MAPPERS[method][endpoint] = func

        return func
    return mapper
```
Данный декоратор регистрирует декорируемую функцию как обработчик HTTP запроса 