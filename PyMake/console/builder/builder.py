from functools import cached_property
from typing import Any, Literal

from pydantic import BaseModel

from PyMake.console.builder.cmd_builder import CmdModel
from PyMake.console.builder.env_builder import EnvModel
from PyMake.console.builder.var_builder import VarKeyWord, VarModel
from PyMake.decorators import validate_raise_exception
from PyMake.exceptions import PyMakeFormatError, UndefinedReference

Elements = Literal["env", "var", "cmd"]
TargetType = dict[Elements, Any]


@validate_raise_exception(PyMakeFormatError)
class Builder(BaseModel):
    data: TargetType
    var: VarModel = VarModel(data=None)
    env: EnvModel = EnvModel(data=None)
    cmd: CmdModel = CmdModel(data=None)

    def build(self):
        # Parse build recipe
        self.var = VarModel(data=self.data.get("var"))
        self.env = EnvModel(data=self.data.get("env"))
        self.cmd = CmdModel(data=self.data.get("cmd"))
        # Build
        self.var.build()
        self.env.build()
        self.cmd.build()
        # Validate reference
        self.validate_variables()

    def validate_env_reference(self) -> None:
        for reference in self.env.reference:
            if reference not in self.var.vars:
                raise UndefinedReference(f"env has an undefined reference: {reference}")

    def validate_cmd_reference(self) -> None:
        for reference in self.cmd.reference:
            if reference not in self.var.vars:
                raise UndefinedReference(f"cmd has an undefined reference: {reference}")

    def validate_variables(self):
        self.validate_env_reference()
        self.validate_cmd_reference()

    @property
    def positional(self) -> list[str]:
        return self.var.positional

    @property
    def default(self) -> dict[str, str]:
        return self.var.default

    @property
    def flag(self) -> dict[str, str]:
        return self.var.flag

    @property
    def required(self) -> list[str]:
        return self.var.required

    @property
    def vars(self) -> list[str]:
        return self.var.vars

    @property
    def envs(self) -> dict[str, str]:
        return self.env.data

    @property
    def commands(self) -> list[str]:
        return self.cmd.commands

    @cached_property
    def type_map(self) -> dict[str, VarKeyWord]:
        return self.var.type_map
