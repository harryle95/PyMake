import re

from pydantic import BaseModel

from PyMake.decorators import validate_raise_exception
from PyMake.exceptions import InvalidEnvType

EnvType = dict[str, str | int | float] | None


@validate_raise_exception(InvalidEnvType)
class EnvModel(BaseModel):
    data: EnvType
    _default: dict[str, str] = {}
    _reference: dict[str, str] = {}
    _envs: dict[str, str] = {}

    def build(self):
        pattern = r"\$\((.*?)\)"
        if self.data:
            self._envs = self.data
            for key, value in self.data.items():
                value = str(value).strip()
                match = re.findall(pattern, value)
                if match:
                    self._reference[match[0]] = key
                else:
                    self._default[value] = key

    @property
    def envs(self) -> dict[str, str]:
        return self._envs

    @property
    def default(self) -> dict[str, str]:
        return self._default

    @property
    def reference(self) -> dict[str, str]:
        return self._reference
