class ParserError(Exception):
    pass


class InvalidElementError(ParserError):
    pass


class KeywordFormatError(ParserError):
    pass

class StateError(ParserError):
    pass

class UndefinedVariableError(ParserError):
    pass

class InvalidPointerError(ParserError):
    pass