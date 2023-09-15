import re

from PyMake.console.builder.abc_builder import DictDefaultModel, PATTERN
from PyMake.decorators import validate_raise_exception
from PyMake.exceptions import InvalidEnvType

EnvType = dict[str, str | int | float] | None


@validate_raise_exception(InvalidEnvType)
class EnvModel(DictDefaultModel):
    data: EnvType
    _reference: list[str] = []
    _envs: dict[str, str] = {}
    _default: dict[str, str] = {}
    _interpolated: list[str] = []

    def build(self):
        if self.data:
            for key, value in self.data.items():
                value = str(value).strip()
                match = re.findall(PATTERN, value)
                if match:
                    self._reference.extend(match)
                    self._interpolated.append(key)
                else:
                    self._default[key] = value

    @property
    def reference(self) -> list[str]:
        return self._reference

    @property
    def default(self) -> dict[str, str]:
        return self._default

    @property
    def interpolated(self) -> list[str]:
        return self._interpolated
