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
