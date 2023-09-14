from typing import Any

from pydantic import ValidationError


def validate_raise_exception(exception):
    def decorator(decorated):
        decorated_init = decorated.__init__

        def __init__(__pydantic_self__, **data: Any) -> None:
            try:
                decorated_init(__pydantic_self__, **data)
            except ValidationError:
                raise exception("Invalid data type encounter in PyMake element")

        decorated.__init__ = __init__
        return decorated

    return decorator
