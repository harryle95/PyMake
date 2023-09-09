from typing import Any, Literal

from PyMake.builder.var.block import BasicBlock, FlagBlock, SequenceBlock
from PyMake.parser.parser import VarParser

FACTORY = {
    'basic': BasicBlock,
    'flag': FlagBlock,
    'sequence': SequenceBlock
}


class VarSection:
    def __init__(self, data: Any):
        if not isinstance(data, dict):
            raise ValueError("Var section must be defined as a dictionary")
        unhandled_key = [k for k in data if k not in FACTORY]
        if len(unhandled_key) != 0:
            raise ValueError(f"Unexpected block in var section: {unhandled_key}")
        for (k, v) in FACTORY.items():
            if k in data:
                self.__setattr__(k, v(_data=data[k]))
            else:
                self.__setattr__(k, None)
        self.vars = []
        self.positional = {}
        self.required = []
        self.default = {}
        for k in FACTORY.keys():
            self._update_vars(k)

    def build(self) -> VarParser:
        return VarParser(
            variables=self.vars,
            positional=self.positional,
            required=self.required,
            default=self.default,
        )

    def _update_vars(
            self,
            container_type: Literal['basic', 'flag', 'sequence']
    ) -> None:
        container = self.__getattribute__(container_type)
        if container is None:
            return
        for key, value in container.mapping.items():
            if key in vars:
                raise ValueError("Variable defined in different blocks")
            self.vars[key] = container_type
            if hasattr(container, "position"):
                self.positional[key] = value.position
            if value.required:
                self.required.append(key)
            if value.default:
                self.default[key] = value.default
