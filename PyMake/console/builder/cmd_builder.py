import re

from PyMake.console.builder.abc_builder import ListDefaultModel, PATTERN
from PyMake.decorators import validate_raise_exception
from PyMake.exceptions import InvalidCmdType

CmdType = str | list[str] | None


@validate_raise_exception(InvalidCmdType)
class CmdModel(ListDefaultModel):
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
        else:
            raise InvalidCmdType("cmd cannot be empty.")

    def _extract_reference(self, data: list[str]) -> None:
        matches = set()
        cmds = []
        for cmd in data:
            cmds.append(cmd)
            matches.update(re.findall(PATTERN, cmd))
        self._commands = list(cmds)
        self._reference = list(matches)

    @property
    def reference(self) -> list[str]:
        return self._reference

    @property
    def commands(self) -> list[str]:
        return self._commands
