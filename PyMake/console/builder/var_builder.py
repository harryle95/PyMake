from __future__ import annotations

from typing import Any, Literal

from PyMake.console.builder.abc_builder import DictDefaultModel
from PyMake.decorators import validate_raise_exception
from PyMake.exceptions import (
    InvalidBasicVarType,
    InvalidOptionVarType,
    InvalidSequenceVarType,
    RedefinedVariable,
    UnrecognisedVarKeyword,
)

VarKeyWord = Literal["basic", "option", "sequence"]
VarType = dict[VarKeyWord, Any] | None
AtomType = str | int | float
BasicType = str | dict[str, AtomType | None] | list[str] | None
OptionType = dict[str, str] | None
SequenceType = str | list[str] | dict[str, AtomType | list[AtomType] | None] | None


@validate_raise_exception(InvalidBasicVarType)
class BasicModel(DictDefaultModel):
    data: BasicType = {}

    @property
    def positional(self) -> list[str]:
        return [key for key in self.data]

    @property
    def default(self) -> dict[str, str]:
        return {
            key: str(value).strip()
            for key, value in self.data.items()
            if (value and str(value).strip() != "")
        }

    @property
    def required(self) -> list[str]:
        return [
            key
            for key, value in self.data.items()
            if value is None or str(value).strip() == ""
        ]


@validate_raise_exception(InvalidOptionVarType)
class OptionModel(DictDefaultModel):
    data: OptionType = {}

    @property
    def default(self) -> dict[str, str]:
        _default = {}
        for key, value in self.data.items():
            if value.strip() == "":
                raise InvalidOptionVarType(
                    f"option variables must not be empty. Error detected for: {key}"
                )
            _default[key] = value.strip()
        return _default


@validate_raise_exception(InvalidSequenceVarType)
class SequenceModel(DictDefaultModel):
    data: SequenceType = {}

    @property
    def default(self) -> dict[str, str | None]:
        _default = {}
        for key, value in self.data.items():
            if value is None:
                continue
            elif hasattr(value, "__len__"):
                _default[key] = " ".join([str(item).strip() for item in value]).strip()
            else:
                _default[key] = str(value).strip()
        return _default

    @property
    def required(self) -> list[str]:
        return [
            key
            for key, value in self.data.items()
            if value is None or str(value).strip() == ""
        ]


@validate_raise_exception(UnrecognisedVarKeyword)
class VarModel(DictDefaultModel):
    data: VarType = {}
    basic: BasicModel = BasicModel()
    option: OptionModel = OptionModel()
    sequence: SequenceModel = SequenceModel()

    def build(self):
        self.basic = BasicModel(data=self.data.get("basic", {}))
        self.option = OptionModel(data=self.data.get("option", {}))
        self.sequence = SequenceModel(data=self.data.get("sequence", {}))
        self.validate_var()

    def validate_var(self):
        """
        Check if there are common variables among basic, option and sequence
        """
        basic_keys = set(self.basic.data.keys())
        option_keys = set(self.option.data.keys())
        sequence_keys = set(self.sequence.data.keys())
        basic_option = basic_keys.intersection(option_keys)
        if basic_option:
            raise RedefinedVariable(
                f"The following variable(s) were declared in "
                f"both basic and option: {basic_option}"
            )
        basic_sequence = basic_keys.intersection(sequence_keys)
        if basic_sequence:
            raise RedefinedVariable(
                f"The following variable(s) were declared in "
                f"both basic and sequence: {basic_sequence}"
            )
        option_sequence = option_keys.intersection(sequence_keys)
        if option_sequence:
            raise RedefinedVariable(
                f"The following variable(s) were declared in "
                f"both basic and sequence: {option_sequence}"
            )

    @property
    def vars(self) -> list[str]:
        return list(
            set(self.basic.data.keys())
            | set(self.option.data.keys() | set(self.sequence.data.keys()))
        )

    @property
    def positional(self) -> list[str]:
        return self.basic.positional

    @property
    def default(self) -> dict[str, str]:
        _default = {k: v for k, v in self.basic.default.items()}
        _default.update(self.sequence.default)
        return _default

    @property
    def flag(self) -> dict[str, str]:
        return self.option.default

    @property
    def required(self) -> list[str]:
        return self.basic.required + self.sequence.required

    @property
    def type_map(self) -> dict[str, VarKeyWord]:
        type_map = {var: "basic" for var in self.basic.data}
        type_map.update({var: "option" for var in self.option.data})
        type_map.update({var: "sequence" for var in self.sequence.data})
        return type_map
