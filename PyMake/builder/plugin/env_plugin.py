import re
from typing import Any

from PyMake.builder.plugin.base_plugin import BuilderPlugin
from PyMake.parser.plugin.env_plugin import EnvParser


class EnvSection(BuilderPlugin):
    def __init__(self, data: Any) -> None:
        self.declared_vars = {}
        self.referenced_vars = {}
        self.pattern = r"\$\((.*?)\)"

        if data:
            self._init(data)

    def _init(self, data: Any) -> None:
        if not (isinstance(data, dict)):
            raise ValueError("Env section must be defined as a dictionary")
        for k, v in data.items():
            if not isinstance(v, str) and hasattr(v, "__len__"):
                raise TypeError(f"Sequence type value not allowed for env vars: {k}")
            v = str(v)
            match = re.findall(self.pattern, v)
            if match:
                self.referenced_vars[k] = match[0]
            else:
                self.declared_vars[k] = v

    def build(self) -> EnvParser:
        return EnvParser(
            declared_vars=self.declared_vars,
            referenced_vars=self.referenced_vars,
        )
