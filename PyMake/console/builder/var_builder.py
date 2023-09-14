from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel

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
BasicType = dict[str, AtomType | None] | list[str] | None
OptionType = dict[str, str] | None
SequenceType = list[str] | dict[str, AtomType | list[AtomType] | None] | None


@validate_raise_exception(InvalidBasicVarType)
class BasicModel(BaseModel):
    basic: BasicType = None

    @property
    def positional(self) -> list[str]:
        if self.basic:
            return [key for key in self.basic]
        return []

    @property
    def default(self) -> dict[str, str]:
        if self.basic:
            return {
                key: str(value).strip()
                for key, value in self.basic.items()
                if (value and str(value).strip() != "")
            }
        return {}

    @property
    def required(self) -> list[str]:
        if self.basic:
            return [
                key
                for key, value in self.basic.items()
                if value is None or str(value).strip() == ""
            ]
        return []


@validate_raise_exception(InvalidOptionVarType)
class OptionModel(BaseModel):
    option: OptionType = None

    @property
    def default(self) -> dict[str, str]:
        _default = {}
        if self.option:
            for key, value in self.option.items():
                if value.strip() == "":
                    raise InvalidOptionVarType(
                        f"option variables must not be empty. Error detected for: {key}"
                    )
                _default[key] = value.strip()
        return _default


@validate_raise_exception(InvalidSequenceVarType)
class SequenceModel(BaseModel):
    sequence: SequenceType = None

    @property
    def default(self) -> dict[str, str]:
        _default = {}
        if self.sequence:
            for key, value in self.sequence.items():
                if isinstance(value, str):
                    _default[key] = value
                elif hasattr(value, "__len__"):
                    _default[key] = " ".join(
                        [str(item).strip() for item in value]
                    ).strip()
                else:
                    _default[key] = str(value).strip()
        return _default

    @property
    def required(self) -> list[str]:
        if self.sequence:
            return [
                key
                for key, value in self.sequence.items()
                if value is None or str(value).strip() == ""
            ]
        return []


@validate_raise_exception(UnrecognisedVarKeyword)
class VarModel(BaseModel):
    data: VarType
    basic: BasicModel = BasicModel()
    option: OptionModel = OptionModel()
    sequence: SequenceModel = SequenceModel()

    def build(self):
        if self.data:
            self.basic = BasicModel(basic=self.data.get("basic"))
            self.option = OptionModel(option=self.data.get("option"))
            self.sequence = SequenceModel(sequence=self.data.get("sequence"))
            self.validate_var()

    def validate_var(self):
        """
        Check if there are common variables among basic, option and sequence
        """
        basic_keys = set(self.basic.basic.keys())
        option_keys = set(self.option.option.keys())
        sequence_keys = set(self.sequence.sequence.keys())
        basic_option = basic_keys.intersection(option_keys)
        if basic_option:
            raise RedefinedVariable(
                f"The following variables were declared in "
                f"both basic and option: {basic_option}"
            )
        basic_sequence = basic_keys.intersection(sequence_keys)
        if basic_sequence:
            raise RedefinedVariable(
                f"The following variables were declared in "
                f"both basic and sequence: {basic_sequence}"
            )
        option_sequence = option_keys.intersection(sequence_keys)
        if option_sequence:
            raise RedefinedVariable(
                f"The following variables were declared in "
                f"both basic and sequence: {option_sequence}"
            )

    @property
    def vars(self) -> list[str]:
        return list(
            set(self.basic.basic.keys())
            | set(self.option.option.keys() | set(self.sequence.sequence.keys()))
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


if __name__ == "__main__":
    import yaml

    data = """
    var:
        basic:
            var1: 1
            var2: 2
            var3: 3
        option:
            all: "-a"
        sequence:
            var4: [1,2,3,4]
    """
    data = yaml.safe_load(data)["var"]
    var = VarModel(data=data)
    var.build()
    print("End")
