import abc
from typing import Literal, Optional, Union

from pydantic.dataclasses import dataclass

UNSET = -1
BasicType = Union[int, float, str, None]
FlagType = str
SequenceType = list[BasicType]


@dataclass
class Atom(abc.ABC):
    """
    Interface for atom, representing the smallest unit of input to each variable

    Each atom has the following attributes/properties:
    name: variable name
    default: default value associated with the variable
    required: determine whether the value must be provided at invocation.

    Example:

    ```

    target:
        var:
            basic:
                var1: REQUIRED
                var2: 10
                var3: 100
    ```

    There are three atoms:
        - var1 with default value of None and is required
        - var2 with default value of 10 and is not required
        - var3 with default value of 100 and is not required
    """

    _name: str

    @property
    def name(self) -> str:
        return self._name

    @property
    @abc.abstractmethod
    def default(self) -> Optional[str]:
        return NotImplemented

    @property
    @abc.abstractmethod
    def required(self) -> bool:
        return NotImplemented


@dataclass
class BasicAtom(Atom):
    _default: Optional[BasicType]
    _position: int = UNSET

    @property
    def default(self) -> Optional[BasicType]:
        if self._default:
            # If default value is required, equivalent to None
            if isinstance(self._default, str) and self._default.upper() == "REQUIRED":
                return None
            return self._default
        return None

    @property
    def required(self) -> bool:
        return self.default is None

    @property
    def position(self):
        if self._position >= 0:
            return self._position
        raise ValueError("Trying to access unset position for basic variable")

    @position.setter
    def position(self, pos: int):
        if pos < 0:
            raise ValueError("Position must be positive")
        self._position = pos


@dataclass
class FlagAtom(Atom):
    _default: str

    @property
    def required(self) -> bool:
        return False

    @property
    def default(self) -> str:
        return self._default


@dataclass
class SequenceAtom(Atom):
    _default: Optional[Union[SequenceType, Literal["REQUIRED"]]]

    @property
    def default(self) -> Optional[SequenceType]:
        if self._default:
            # Allows for setting sequence var as REQUIRED
            if isinstance(self._default, str) and self._default.upper() == "REQUIRED":
                return None
            return self._default
        return None

    @property
    def required(self) -> bool:
        return self.default is None
