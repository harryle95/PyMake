from typing import Any

from pydantic import BaseModel, field_validator

from PyMake.decorators import validate_raise_exception
from PyMake.exceptions import PyMakeFormatError


@validate_raise_exception(PyMakeFormatError)
class DictDefaultModel(BaseModel):
    data: Any

    @field_validator("data")
    @classmethod
    def convert_data(cls, data: Any) -> Any:
        if data is None:
            return {}
        if isinstance(data, str):
            return {data: None}
        if isinstance(data, list):
            return {item: None for item in data}
        return data


@validate_raise_exception(PyMakeFormatError)
class ListDefaultModel(BaseModel):
    data: Any

    @field_validator("data")
    @classmethod
    def convert_data(cls, data: Any) -> Any:
        if data is None:
            return []
        return data
