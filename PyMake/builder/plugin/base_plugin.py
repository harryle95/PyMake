import abc
from typing import Any

from PyMake.parser.plugin.base_plugin import ParserPlugin


class BuilderPlugin(abc.ABC):
    @abc.abstractmethod
    def __init__(self, data: Any):
        pass

    @abc.abstractmethod
    def build(self) -> ParserPlugin:
        return NotImplemented
