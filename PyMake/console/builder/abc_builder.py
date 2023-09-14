from typing import Any

from pydantic import BaseModel, field_validator


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


class ListDefaultModel(BaseModel):
    data: Any

    @field_validator("data")
    @classmethod
    def convert_data(cls, data: Any) -> Any:
        if data is None:
            return []
        return data
