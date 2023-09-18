import dataclasses
import re
from typing import Literal

from PyMake.console.builder.abc_builder import ListDefaultModel, PATTERN
from PyMake.decorators import validate_raise_exception
from PyMake.exceptions import InvalidCmdType

Lang = Literal["python", "bash"]

CmdEntry = str | dict[Lang, str | list[str]]
CmdType = CmdEntry | list[CmdEntry] | None


@dataclasses.dataclass
class Command:
    command: str
    executable: str | None


def get_shebang(command: str) -> str | None:
    command = command.strip()
    pattern = "^#!\s*(.+)"
    match = re.findall(pattern, command)
    if match:
        return match[0]


def parse_string(entry: str, exe: str | None = None) -> Command:
    executable = get_shebang(entry)
    if exe is None and executable is None:
        return Command(entry, None)
    if executable:
        return Command(entry, executable)
    if exe == "python":
        return Command(entry, "python")
    if exe == "bash":
        return Command(entry, "bash")
    raise ValueError(f"Unsupported executable: {exe}")


def parse_command(entry: CmdType) -> list[Command]:
    if not isinstance(entry, list):
        entry = [entry]
    commands = []
    for item in entry:
        if isinstance(item, str):
            commands.append(parse_string(item))
        if isinstance(item, dict):
            for key, value in item.items():
                if isinstance(value, str):
                    commands.append(parse_string(value, key))
                else:
                    commands.extend(
                        [parse_string(sub_value, key) for sub_value in value]
                    )
    return commands


@validate_raise_exception(InvalidCmdType)
class CmdModel(ListDefaultModel):
    data: CmdType
    _reference: list[str] = []
    _commands: list[Command] = []

    def build(self):
        if self.data:
            self._commands = parse_command(self.data)
            self._extract_reference(self._commands)
        else:
            raise InvalidCmdType("cmd cannot be empty.")

    def _extract_reference(self, data: list[Command]) -> None:
        matches = set()
        for cmd in data:
            matches.update(re.findall(PATTERN, cmd.command))
        self._reference = list(matches)

    @property
    def reference(self) -> list[str]:
        return self._reference

    @property
    def commands(self) -> list[str]:
        return [item.command for item in self._commands]

    @property
    def executing_commands(self) -> list[Command]:
        return self._commands
