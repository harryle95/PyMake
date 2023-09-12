import abc
from typing import Any

from PyMake.parser.utils.exceptions import MissingRequiredVariableError
from PyMake.parser.utils.type_alias import NameSpaceType


class ParserPlugin(abc.ABC):
    @abc.abstractmethod
    def parse(self, args: Any) -> NameSpaceType:
        return NotImplemented


class NameSpaceParser(ParserPlugin):
    def __init__(self, referenced_vars: NameSpaceType):
        self.referenced_vars = referenced_vars
        self.referenced_value = self._init_value()

    @staticmethod
    def _init_value() -> NameSpaceType:
        return {}

    @property
    def namespace(self) -> NameSpaceType:
        return {k: self.referenced_value[v] for k, v in self.referenced_vars.items()}

    def parse(self, args: NameSpaceType) -> NameSpaceType:
        for env_var, ref_var in self.referenced_vars.items():
            if ref_var not in args:
                raise MissingRequiredVariableError(
                    f"Required var {ref_var} not provided"
                )
            # Note that ref_val should be a string now
            ref_val = args[ref_var]
            self.referenced_value[ref_var] = ref_val
        return self.namespace
