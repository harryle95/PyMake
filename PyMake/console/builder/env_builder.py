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

    def build(self):
        pattern = r"\$\((.*?)\)"
        if self.data:
            for key, value in self.data.items():
                value = str(value).strip()
                match = re.findall(pattern, value)
                if match:
                    self._reference[key] = match[0]
                else:
                    self._default[key] = value

    @property
    def default(self) -> dict[str, str]:
        return self._default

    @property
    def reference(self) -> dict[str, str]:
        return self._reference
