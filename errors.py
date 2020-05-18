class NewException(Exception):
    """
    NewException base class
    """
    def __init__(self, expression=None, message=None):
        super().__init__()
        self.__expression = expression
        self.__message = message

    def what(self) -> str:
        return str(self.__expression) + " - " + self.__message

    def __str__(self):
        return str(self.__expression) + " - " + self.__message


class EmptyTableNameException(NewException):
    """
    EmptyTableNameException class
    """
    def __init__(self, expression="", message="Nazwa Tabeli nie może być pusta!"):
        super().__init__(expression, message)


class NoTableChosenException(NewException):
    """
    NoTableChosenException class
    """
    def __init__(self, expression="", message="Tabela nie została wybrana!"):
        super().__init__(expression, message)


class NoRowChosenException(NewException):
    """
    NoRowChosenException class
    """
    def __init__(self, expression="", message="Wiersz nie został wybrany!"):
        super().__init__(expression, message)


class EmptyColumnNameException(NewException):
    """
    EmptyColumnNameException class
    """
    def __init__(self, expression="", message="Nazwa kolumny nie może być pusta!"):
        super().__init__(expression, message)


class NoColumnTypeChosenException(NewException):
    """
    NoColumnTypeChosenException class
    """
    def __init__(self, expression="", message='Wybierz typ danych!'):
        super().__init__(expression, message)


class NoColumnTableException(NewException):
    """
    NoColumnTableException class
    """
    def __init__(self, expression="", message='Liczba kolumn nie może być równa zero!'):
        super().__init__(expression, message)


class BadEnteredTypeException(NewException):
    """
    BadEnteredTypeException class
    """
    def __init__(self, expression="", message="zły typ danych!"):
        super().__init__(expression, message)


class BadLambdaExpressionException(NewException):
    """
    BadLambdaExpressionException class
    """
    def __init__(self, expression="", message="złe wyrażenie lambda!"):
        super().__init__(expression, message)
