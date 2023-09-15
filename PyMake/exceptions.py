class PyMakeError(Exception):
    pass


class PyMakeFormatError(PyMakeError):
    pass


class UnrecognisedVarKeyword(PyMakeFormatError):
    pass


class InvalidBasicVarType(PyMakeFormatError):
    pass


class InvalidOptionVarType(PyMakeFormatError):
    pass


class InvalidSequenceVarType(PyMakeFormatError):
    pass


class InvalidEnvType(PyMakeFormatError):
    pass


class InvalidCmdType(PyMakeFormatError):
    pass


class RedefinedVariable(PyMakeFormatError):
    pass


class UndefinedReference(PyMakeFormatError):
    pass


class ParseError(PyMakeError):
    """
    Errors encountered while parsing inputs from CLI
    """

    pass


class InvalidPositionalVariable(ParseError):
    """
    Errors encountered when a positional value is encountered where a keyword is
    expected
    """

    pass


class UndefinedKeyword(ParseError):
    """
    Errors encountered when an undeclared keyword is encountered at parsing
    """

    pass


class MissingRequiredVariable(ParseError):
    """
    Errors encountered when a required variable is not provided at parsing
    """

    pass


class InvalidKeyword(ParseError):
    """
    Errors encountered when a keyword variable is placed where a positional value is
    expected
    """

    pass


class MultipleDefinition(ParseError):
    """
    Errors encountered when a variable is defined multiple time at parsing
    """

    pass


class InvalidParserState(ParseError):
    """
    Internal error that should not be seen by user. When state declaration/transition
    is incorrect
    """

    pass
