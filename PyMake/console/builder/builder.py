from typing import Any, Literal

from pydantic import BaseModel

from PyMake.console.builder.cmd_builder import CmdModel
from PyMake.console.builder.env_builder import EnvModel
from PyMake.console.builder.var_builder import VarModel
from PyMake.decorators import validate_raise_exception
from PyMake.exceptions import PyMakeFormatError, UndefinedReference

Elements = Literal["env", "var", "cmd"]
PyMakeType = dict[str, dict[Elements, Any]]


@validate_raise_exception(PyMakeFormatError)
class Builder(BaseModel):
    data: PyMakeType
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

    def validate_reference(self, model: EnvModel | CmdModel, name: str) -> None:
        for reference in model.reference:
            if reference not in self.var.vars:
                raise UndefinedReference(
                    f"{name} has an undefined reference: {reference}"
                )

    def validate_variables(self):
        self.validate_reference(self.env)
        self.validate_reference(self.cmd)
