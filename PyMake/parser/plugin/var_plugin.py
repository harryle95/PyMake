# TODO : Implement state pattern for input parsing
from typing import Optional, Union

from PyMake.parser.plugin.base_plugin import ParserPlugin
from PyMake.parser.plugin.utils.exceptions import (
    InvalidPointerError,
    MissingRequiredVariableError,
    UndefinedVariableError,
)
from PyMake.parser.plugin.utils.states import ExpectOption, ExpectOptionValue
from PyMake.parser.plugin.utils.states import State
from PyMake.parser.plugin.utils.tokens import Tokenizer
from PyMake.parser.plugin.utils.type_alias import (
    DefaultType,
    NameSpaceType,
    OptionType,
    PositionalType,
    RequiredType,
    VariablesType,
)


class VarParser(ParserPlugin):
    def __init__(
        self,
        variables: VariablesType,
        positional: PositionalType,
        default: DefaultType,
        required: RequiredType,
    ) -> None:
        self.variables = variables
        self.positional = positional
        self.default = default
        self.required = required
        self.namespace = self._init_namespace()
        self._state = self._init_state()
        self._seq_vars = [v for v in self.variables if self._get_type(v) == "sequence"]

    def _init_state(self) -> State:
        if len(self.positional) == 0:
            return ExpectOption(context=self)
        return ExpectOptionValue(context=self, allow_positional=True, pointer=0)

    @staticmethod
    def _init_namespace() -> NameSpaceType:
        return {}

    def _transition(self, state: State):
        self._state = state

    # noinspection PyTypeChecker
    def _set(self, variable: str, value: Optional[str] = None) -> None:
        if self._get_type(variable) == "sequence":
            if variable not in self.namespace:
                self.namespace[variable] = []
            self.namespace[variable].append(value)
        elif self._get_type(variable) == "basic":
            self.namespace[variable] = value
        else:
            self.namespace[variable] = self.default[variable]

    def _get_type(self, variable: str) -> OptionType:
        if variable in self.variables:
            return self.variables[variable]
        raise UndefinedVariableError(
            f"Variable {variable} was not defined in the var section"
        )

    def _get_positional(self, pointer: int) -> str:
        if pointer is None:
            raise InvalidPointerError("Pointer is undefined")
        if pointer in self.positional:
            return self.positional[pointer]
        raise InvalidPointerError("Positional pointer not recognised")

    def _handle_option(self, option: str) -> None:
        self._state.handle_option(option)

    def _handle_value(self, value: str) -> None:
        self._state.handle_value(value)

    def parse(self, args: Union[str, list[str]]) -> NameSpaceType:
        self.namespace = self._init_namespace()
        self._state = self._init_state()
        tokens = Tokenizer.tokenize(args)
        for token in tokens:
            if token.is_option:
                self._handle_option(token.value)
            else:
                self._handle_value(token.value)

        # Add default values:
        for var in self.default:
            if var not in self.namespace:
                if self._get_type(var) == "basic":
                    self._set(var, str(self.default[var]))
                if self._get_type(var) == "sequence":
                    self.namespace[var] = self.default[var]

        # Validate all required:
        for var in self.required:
            if var not in self.namespace:
                raise MissingRequiredVariableError(f"Missing {var}")

        # Trim sequence utils:
        for var in self._seq_vars:
            self.namespace[var] = " ".join([str(i) for i in self.namespace[var]])

        return self.namespace
