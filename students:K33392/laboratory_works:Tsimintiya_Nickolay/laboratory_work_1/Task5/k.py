class K:
    @staticmethod
    def getMethod() -> str:
        return "GET"

    @staticmethod
    def postMethod() -> str:
        return "POST"

    class Responses:
        @staticmethod
        def ok() -> str:
            return "OK"

        @staticmethod
        def notFound() -> str:
            return "Not found"