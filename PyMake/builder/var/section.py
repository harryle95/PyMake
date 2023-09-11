from typing import Any

from PyMake.builder.var.block import BasicBlock, FlagBlock, SequenceBlock
from PyMake.parser.parser import VarParser

FACTORY = {"basic": BasicBlock, "flag": FlagBlock, "sequence": SequenceBlock}


class VarSection:
    def __init__(self, data: Any):
        self.variables = {}
        self.positional = {}
        self.required = []
        self.default = {}
        if data:
            self._add_blocks(data)

    def _add_blocks(self, data):
        if not isinstance(data, dict):
            raise ValueError("Var section must be defined as a dictionary")
        unhandled_key = [k for k in data if k not in FACTORY]
        if len(unhandled_key) != 0:
            raise ValueError(f"Unexpected block in var section: {unhandled_key}")
        for (k, v) in FACTORY.items():
            if k in data and data[k]:
                self.__setattr__(k, v(_data=data[k]))
            else:
                self.__setattr__(k, None)

        for k in FACTORY.keys():
            self._update_parser_elements(k)

    def build(self) -> VarParser:
        return VarParser(
            variables=self.variables,
            positional=self.positional,
            required=self.required,
            default=self.default,
        )

    def _update_parser_elements(self, container_type: str) -> None:
        container = self.__getattribute__(container_type)
        if container is None:
            return
        for key, value in container.mapping.items():
            if key in self.variables:
                raise ValueError("Variable defined in different blocks")
            self.variables[key] = container_type
            if hasattr(value, "position"):
                self.positional[value.position] = key
            if value.required:
                self.required.append(key)
            if value.default:
                self.default[key] = value.default
