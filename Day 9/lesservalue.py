class LesserValueError(Exception):
    def __init__(self, message, statusCode=500):
        super().__init__(message)
        self.message = message
        self.statusCode = statusCode
