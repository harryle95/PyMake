from PyMake.parser.plugin.base_plugin import NameSpaceParser
from PyMake.parser.plugin.utils.type_alias import NameSpaceType


class EnvParser(NameSpaceParser):
    def __init__(self, declared_vars: NameSpaceType, referenced_vars: NameSpaceType):
        super().__init__(referenced_vars)
        self.declared_vars = declared_vars

    @property
    def namespace(self) -> NameSpaceType:
        replaced_val = super().namespace
        default_val = {k: v for k, v in self.declared_vars.items()}
        default_val.update(replaced_val)
        return default_val
