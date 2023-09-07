class ParserError(Exception):
    pass


class InvalidElementError(ParserError):
    pass


class KeywordFormatError(ParserError):
    pass
