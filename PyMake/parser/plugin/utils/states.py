from __future__ import annotations

import abc
from typing import Optional, TYPE_CHECKING

from PyMake.parser.plugin.utils.exceptions import (
    InvalidValueError,
    StateError,
    VariableRedefinitionError,
)

if TYPE_CHECKING:
    from PyMake.parser.plugin.var_plugin import VarParser


class State(abc.ABC):
    def __init__(
        self,
        context: VarParser,
        variable: Optional[str] = None,
        allow_positional: bool = False,
        pointer: Optional[int] = None,
    ) -> None:
        self.context = context
        self.variable = variable
        self.allow_positional = allow_positional
        self.pointer = pointer
        self._validate_state()

    def _validate_state(self):
        if self.variable and self.allow_positional is True:
            raise StateError(
                "State that allows positional argument can not have a variable"
            )
        if self.allow_positional is True and self.pointer is None:
            raise StateError(
                "State that allows positional argument must have a valid positional "
                "pointer"
            )
        if self.pointer and self.pointer >= len(self.context.positional):
            raise StateError("Invalid pointer value")

    @abc.abstractmethod
    def handle_option(self, option: str) -> None:
        pass

    @abc.abstractmethod
    def handle_value(self, value: str) -> None:
        pass


class ExpectOption(State):
    def handle_option(self, option: str) -> None:
        if option in self.context.namespace:
            raise VariableRedefinitionError(f"Variable redefinition: {option}")
        option_type = self.context._get_type(option)
        if option_type in ["basic", "sequence"]:
            self.context._transition(ExpectValue(context=self.context, variable=option))
        else:
            self.context._set(option)
            self.context._transition(
                ExpectOption(context=self.context, variable=option)
            )

    def handle_value(self, value: str) -> None:
        raise InvalidValueError(
            f"Invalid positional argument: {value}. Expecting a keyword argument"
        )


class ExpectValue(State):
    def handle_option(self, option: str) -> None:
        raise InvalidValueError(
            f"Invalid keyword argument: {option}. Expecting a value argument"
        )

    def handle_value(self, value: str) -> None:
        self.context._set(self.variable, value)
        if self.context._get_type(self.variable) == "sequence":
            self.context._transition(
                ExpectOptionValue(context=self.context, variable=self.variable)
            )
        else:
            self.context._transition(
                ExpectOption(context=self.context, variable=self.variable)
            )


class ExpectOptionValue(ExpectOption):
    def handle_value(self, value: str) -> None:
        if self.allow_positional:
            self.handle_positional(value)
        else:
            # Only valid state here is if variable is of sequence type
            assert self.context._get_type(self.variable) == "sequence"
            self.context._set(self.variable, value)

    def handle_positional(self, value: str) -> None:
        # Set value to pointer's variable and advance pointer
        variable = self.context._get_positional(self.pointer)
        self.context._set(variable, value)
        self.pointer += 1
        if self.pointer in self.context.positional:
            self.context._transition(
                ExpectOptionValue(
                    context=self.context, allow_positional=True, pointer=self.pointer
                )
            )
        else:
            self.context._transition(ExpectOption(context=self.context))
