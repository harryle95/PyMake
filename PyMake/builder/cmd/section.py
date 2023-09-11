import re
from typing import Any, Union

from PyMake.parser.parser import CmdParser


class CmdSection:
    def __init__(self, data: Any) -> None:
        self.referenced_vars = {}
        self.script = ""
        self.pattern = r"\$\((.*?)\)"

        if data:
            self._init(data)
        else:
            raise ValueError("CMD section cannot be blank")

    def _init(self, data: Union[list[str], str]) -> None:
        if isinstance(data, str):
            matches = re.findall(self.pattern, data)
            self.script = data
        elif isinstance(data, list):
            matches = set()
            for entry in data:
                matches.update(re.findall(self.pattern, entry))
            self.script = "\n".join(data)
        else:
            raise ValueError(
                "CMD section must be either a list of commands or a script"
            )
        self.referenced_vars = {f"$({var})": var for var in matches}

    def build(self) -> CmdParser:
        return CmdParser(
            referenced_vars=self.referenced_vars,
            script=self.script,
        )
