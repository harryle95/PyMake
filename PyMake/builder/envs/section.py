import re
from typing import Any


class EnvSection:
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
                raise TypeError(f"Sequence type value not allowed for envs vars: {k}")
            v = str(v)
            match = re.findall(self.pattern, v)
            if match:
                self.referenced_vars[k] = match[0]
            else:
                self.declared_vars[k] = v
