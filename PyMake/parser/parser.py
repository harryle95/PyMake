# TODO : Implement state pattern for input parsing
import abc
from typing import Literal, Optional, Union

from PyMake.exceptions import InvalidPointerError, StateError, UndefinedVariableError
from PyMake.parser.tokens import Tokenizer

NameSpaceType = dict[str, Union[str, list[str]]]
OptionType = Literal['basic', 'flag', 'sequence']
DefaultType = Union[int, float, str, list[int], list[float], list[str]]


class State(abc):
    def __init__(
            self,
            context: "VarParser",
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
            raise StateError("State that allows positional argument can not have a variable")
        if self.allow_positional is True and self.pointer is None:
            raise StateError("State that allows positional argument must have a valid positional pointer")
        if self.pointer >= len(self.context.positional):
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
            raise ValueError(f"Variable redefinition: {option}")
        option_type = self.context.get_type(option)
        if option_type in ["basic", "sequence"]:
            self.context.transition(
                ExpectValue(context=self.context, variable=option)
            )
        else:
            self.context.transition(
                ExpectOption(context=self.context, variable=option)
            )

    def handle_value(self, value: str) -> None:
        raise ValueError(f"Invalid positional argument: {value}. Expecting a keyword argument")


class ExpectValue(State):
    def handle_option(self, option: str) -> None:
        raise ValueError(f"Invalid keyword argument: {option}. Expecting a value argument")

    def handle_value(self, value: str) -> None:
        self.context.set(self.variable, value)
        if self.context.get_type(self.variable) == "sequence":
            self.context.transition(
                ExpectOptionValue(context=self.context, variable=self.variable)
            )
        else:
            self.context.transition(
                ExpectOption(context=self.context, variable=self.variable)
            )


class ExpectOptionValue(ExpectOption):

    def handle_value(self, value: str) -> None:
        if self.allow_positional:
            self.handle_positional(value)
        else:
            # Only valid state here is if variable is of sequence type
            assert self.context.get_type(self.variable) == "sequence"
            self.context.set(self.variable, value)

    def handle_positional(self, value: str) -> None:
        # Set value to pointer's variable and advance pointer
        variable = self.context.get_positional(self.pointer)
        self.context.set(variable, value)
        self.pointer += 1


class VarParser:
    def __init__(
            self,
            variables: dict[str, OptionType],
            positional: dict[int, str],
            default: dict[str, DefaultType],
            required: list[str], ) -> None:
        self.variables = variables
        self.positional = positional
        self.default = default
        self.required = required
        self.namespace = self._init_namespace()
        self._state = self._init_state()

    def _init_state(self) -> State:
        if len(self.positional) == 0:
            return ExpectOption(context=self)
        return ExpectOptionValue(context=self, allow_positional=True, pointer=0)

    def _init_namespace(self) -> NameSpaceType:
        return {}

    def transition(self, state: State):
        self._state = state

    def set(self, variable: str, value: str) -> None:
        if self.variables[variable] == "sequence":
            if not (variable in self.namespace):
                self.namespace[variable] = []
            self.namespace[variable].append(value)
        elif self.variables[variable] == "basic":
            self.namespace[variable] = value
        else:
            raise ValueError("Flag variable does not accept value")

    def get_type(self, variable: str) -> OptionType:
        if variable in self.variables:
            return self.variables[variable]
        raise UndefinedVariableError(f"Variable '{variable}' was not defined in the var section")

    def get_positional(self, pointer: int) -> str:
        if pointer is None:
            raise InvalidPointerError(f"Pointer is undefined")
        if pointer in self.positional:
            return self.positional[pointer]
        raise InvalidPointerError(f"Positional pointer not recognised")

    def handle_option(self, option: str) -> None:
        self._state.handle_option(option)

    def handle_value(self, value: str) -> None:
        self._state.handle_value(value)

    def parse(self, args: Union[str, list[str]]) -> None:
        self.namespace = self._init_namespace()
        tokens = Tokenizer.tokenize(args)
        for token in tokens:
            if token.is_option:
                self.handle_option(token.value)
            else:
                self.handle_value(token.value)
