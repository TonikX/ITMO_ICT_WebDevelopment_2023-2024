MAPPERS = dict()


def request_mapping(endpoint: str, method: str):
    def mapper(func):
        if method not in MAPPERS:
            MAPPERS[method] = dict()
        MAPPERS[method][endpoint] = func

        return func
    return mapper
