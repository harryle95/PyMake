# TODO : Implement state pattern for input parsing
import abc
from typing import Literal, Union

from PyMake.parser.tokens import Token

NameSpaceType = dict[str, str]
OptionType = Literal['basic', 'flag', 'sequence']
DefaultType = Union[int, float, str, list[int], list[float], list[str]]




class VarParser:
    pass
