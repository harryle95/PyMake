# TODO : Implement state pattern for input parsing
import abc
from typing import Literal, Optional, Union

from PyMake.exceptions import (
    InvalidPointerError,
    InvalidValueError,
    MissingRequiredVariableError,
    StateError,
    UndefinedVariableError,
    VariableRedefinitionError,
)
from PyMake.parser.tokens import Tokenizer

NameSpaceType = dict[str, Union[str, list[str]]]
OptionType = Literal["basic", "flag", "sequence"]
DefaultType = Union[int, float, str, list[int], list[float], list[str]]
EnvType = dict[str, str]


class State(abc.ABC):
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
        option_type = self.context.get_type(option)
        if option_type in ["basic", "sequence"]:
            self.context.transition(ExpectValue(context=self.context, variable=option))
        else:
            self.context.set(option)
            self.context.transition(ExpectOption(context=self.context, variable=option))

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
        if self.pointer in self.context.positional:
            self.context.transition(
                ExpectOptionValue(
                    context=self.context, allow_positional=True, pointer=self.pointer
                )
            )
        else:
            self.context.transition(ExpectOption(context=self.context))


class VarParser:
    def __init__(
        self,
        variables: dict[str, OptionType],
        positional: dict[int, str],
        default: dict[str, DefaultType],
        required: list[str],
    ) -> None:
        self.variables = variables
        self.positional = positional
        self.default = default
        self.required = required
        self.namespace = self._init_namespace()
        self._state = self._init_state()
        self._seq_vars = [v for v in self.variables if self.get_type(v) == "sequence"]

    def _init_state(self) -> State:
        if len(self.positional) == 0:
            return ExpectOption(context=self)
        return ExpectOptionValue(context=self, allow_positional=True, pointer=0)

    @staticmethod
    def _init_namespace() -> NameSpaceType:
        return {}

    def transition(self, state: State):
        self._state = state

    def set(self, variable: str, value: Optional[str] = None) -> None:
        if self.get_type(variable) == "sequence":
            if variable not in self.namespace:
                self.namespace[variable] = []
            self.namespace[variable].append(value)
        elif self.get_type(variable) == "basic":
            self.namespace[variable] = value
        else:
            self.namespace[variable] = self.default[variable]

    def get_type(self, variable: str) -> OptionType:
        if variable in self.variables:
            return self.variables[variable]
        raise UndefinedVariableError(
            f"Variable {variable} was not defined in the var section"
        )

    def get_positional(self, pointer: int) -> str:
        if pointer is None:
            raise InvalidPointerError("Pointer is undefined")
        if pointer in self.positional:
            return self.positional[pointer]
        raise InvalidPointerError("Positional pointer not recognised")

    def handle_option(self, option: str) -> None:
        self._state.handle_option(option)

    def handle_value(self, value: str) -> None:
        self._state.handle_value(value)

    def parse(self, args: Union[str, list[str]]) -> NameSpaceType:
        self.namespace = self._init_namespace()
        self._state = self._init_state()
        tokens = Tokenizer.tokenize(args)
        for token in tokens:
            if token.is_option:
                self.handle_option(token.value)
            else:
                self.handle_value(token.value)

        # Add default values:
        for var in self.default:
            if var not in self.namespace:
                if self.get_type(var) == "basic":
                    self.set(var, str(self.default[var]))
                if self.get_type(var) == "sequence":
                    self.namespace[var] = self.default[var]

        # Validate all required:
        for var in self.required:
            if var not in self.namespace:
                raise MissingRequiredVariableError(f"Missing {var}")

        # Trim sequence var:
        for var in self._seq_vars:
            self.namespace[var] = " ".join([str(i) for i in self.namespace[var]])

        return self.namespace


class EnvParser:
    def __init__(self, declared_vars: EnvType, referenced_vars: EnvType):
        self.declared_vars = declared_vars
        self.referenced_vars = referenced_vars
        self.referenced_value = self._init_value()

    @staticmethod
    def _init_value() -> EnvType:
        return {}

    def parse(self, var_namespace: NameSpaceType):
        for env_var, ref_var in self.referenced_vars.items():
            if ref_var not in var_namespace:
                raise MissingRequiredVariableError(
                    f"Required env var {ref_var} not provided"
                )
            # Note that ref_val should be a string now
            ref_val = var_namespace[ref_var]
            self.referenced_value[ref_var] = ref_val
        return self.namespace

    @property
    def namespace(self) -> NameSpaceType:
        replaced_val = {
            k: self.referenced_value[v] for k, v in self.referenced_vars.items()
        }
        default_val = {k: v for k, v in self.declared_vars.items()}
        default_val.update(replaced_val)
        return default_val
