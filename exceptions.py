class NegativeTitlesError(Exception):
    def __init__(self, message):
        super().__init__(message)


class InvalidYearCupError(Exception):
    def __init__(self, message):
        super().__init__(message)


class ImpossibleTitlesError(Exception):
    def __init__(self, message):
        super().__init__(message)
