from typing import Any, Type

from pydantic import ValidationError

from .exceptions import PyMakeError


def validate_raise_exception(exception: Type[PyMakeError]):
    def decorator(decorated):
        decorated_init = decorated.__init__

        def __init__(__pydantic_self__, **data: Any) -> None:
            try:
                decorated_init(__pydantic_self__, **data)
            except ValidationError:
                raise exception("invalid section data type")

        decorated.__init__ = __init__
        return decorated

    return decorator
