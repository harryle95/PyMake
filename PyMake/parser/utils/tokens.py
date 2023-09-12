import shlex
from typing import List, Union

from PyMake.parser.utils.exceptions import KeywordFormatError


class Token:
    """
    Represents input tokens at invocation
    """

    def __init__(self, value: str) -> None:
        self._value = value

    @property
    def is_option(self) -> bool:
        return self._value.startswith("-")

    @property
    def value(self) -> str:
        if self.is_option:
            if self._value.startswith("--") and self._value[2] != "-":
                return self._value[2:]
            if self._value.startswith("-") and self._value[1] != "-":
                return self._value[1:]
            raise KeywordFormatError(
                f"Keyword variable assignment must be prepended with either - or --. "
                f"You defined: {self._value}"
            )
        return self._value

    def __repr__(self) -> str:
        return self._value


class Tokenizer:
    @staticmethod
    def tokenize(args: Union[str, List[str]]) -> List[Token]:
        if isinstance(args, str):
            tokens = shlex.split(args)
        else:
            tokens = args
        return [Token(token) for token in tokens]
