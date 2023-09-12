from PyMake.parser.base_plugin import NameSpaceParser

from PyMake.parser.utils.type_alias import NameSpaceType


class CmdParser(NameSpaceParser):
    def __init__(self, referenced_vars: NameSpaceType, script: str) -> None:
        super().__init__(referenced_vars)
        self.script = script

    @property
    def parsed_script(self) -> str:
        parsed = self.script
        for term, substitute in self.namespace.items():
            parsed = parsed.replace(term, substitute)
        return parsed
