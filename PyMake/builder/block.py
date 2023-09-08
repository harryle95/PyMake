from __future__ import annotations

import abc
from typing import Any, ClassVar, Generic, Literal, TypeVar, Union

from pydantic import TypeAdapter
from pydantic.dataclasses import dataclass

from PyMake.builder.atom import Atom, BasicAtom, BasicType, FlagAtom, FlagType, SequenceAtom, SequenceType

UNSET = -1

BasicBlockType = Union[list[str], dict[str, BasicType]]
FlagBlockType = dict[str, FlagType]
SequenceBlockType = Union[list[str], dict[str, Union[SequenceType, Literal['REQUIRED']]]]

T = TypeVar("T", bound=Atom)
S = TypeVar("S")


@dataclass
class Block(Generic[T, S], abc.ABC):
    _data: Union[S, str]
    class_type: ClassVar[S]

    @classmethod
    def _validate_data(cls, data: Any):
        return TypeAdapter(cls.class_type).validate_python(data)

    def __post_init__(self):
        try:
            if isinstance(self._data, str):
                self._data = [self._data]
            value = self._validate_data(self._data)
            if isinstance(value, list):
                value = {name: None for name in value}
            self._mapping = {name: self._create_atom(index, name, value[name]) for index, name in
                             enumerate(value)}
        except Exception as e:
            raise e

    @classmethod
    def _create_atom(cls, index, name, default) -> T:
        return NotImplemented

    @property
    def mapping(self) -> dict[str, T]:
        return self._mapping

    def __getattr__(self, item) -> T:
        return self._mapping[item]


class BasicBlock(Block[BasicAtom, BasicBlockType]):
    class_type = BasicBlockType

    @classmethod
    def _create_atom(cls, index: int, name: str, default: BasicType) -> BasicAtom:
        atom = BasicAtom(_name=name, _default=default)
        atom.position = index
        return atom


class FlagBlock(Block[FlagAtom, FlagBlockType]):
    class_type = FlagBlockType

    @classmethod
    def _create_atom(cls, index: int, name: str, default: FlagType) -> FlagAtom:
        atom = FlagAtom(_name=name, _default=default)
        return atom


class SequenceBlock(Block[SequenceAtom, SequenceBlockType]):
    class_type = SequenceBlockType

    @classmethod
    def _create_atom(cls, index: int, name: str, default: Union[SequenceType, Literal['REQUIRED']]) -> SequenceAtom:
        atom = SequenceAtom(_name=name, _default=default)
        return atom
