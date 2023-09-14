import re

from pydantic import BaseModel

from PyMake.decorators import validate_raise_exception
from PyMake.exceptions import InvalidCmdType

CmdType = str | list[str] | None


@validate_raise_exception(InvalidCmdType)
class CmdModel(BaseModel):
    data: CmdType
    _reference: list[str] = []
    _commands: list[str] = []

    def build(self):
        if self.data:
            if isinstance(self.data, str):
                data = [self.data]
            else:
                data = self.data
            self._extract_reference(data)

    def _extract_reference(self, data: list[str]) -> None:
        matches = set()
        pattern = r"\$\((.*?)\)"
        cmds = []
        for cmd in data:
            cmds.append(cmd)
            matches.update(re.findall(pattern, cmd))
        self._commands = list(cmds)
        self._reference = list(matches)

    @property
    def reference(self) -> list[str]:
        return self._reference

    @property
    def commands(self) -> list[str]:
        return self._commands
