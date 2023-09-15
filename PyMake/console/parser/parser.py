from __future__ import annotations

import re
from typing import TYPE_CHECKING

from pydantic import BaseModel, model_validator

if TYPE_CHECKING:
    from PyMake.console.builder.builder import Builder, VarKeyWord
import abc
from PyMake.exceptions import (
    InvalidParserState,
    UndefinedKeyword,
    MultipleDefinition,
    InvalidPositionalVariable,
    InvalidKeyword,
)


class Context(BaseModel):
    build_context: Builder
    reference: str | None = None
    position: int | None = None
    use_position: bool = False
    namespace: dict[str, str] = {}

    @model_validator(model="after")
    def validate_using_position_or_reference(self) -> "Context":
        if self.reference and self.use_position is True:
            raise InvalidParserState(
                "State that uses positional argument can not have a variable"
            )
        return self

    @model_validator(model="after")
    def validate_using_position_must_have_valid_position(self) -> "Context":
        if self.use_position is True and self.position is None:
            raise InvalidParserState(
                "State that uses positional argument must have a valid pointer defined"
            )
        return self

    @model_validator(model="after")
    def validate_pointer_must_be_in_range(self) -> "Context":
        if self.position:
            if self.position < 0 or self.position > len(self.build_context.positional):
                raise InvalidParserState(
                    f"Positional pointer must have a value between 0 and "
                    f"{len(self.build_context.positional) - 1}"
                )
        return self

    def get_type(self, name: str) -> VarKeyWord:
        if name in self.build_context.type_map:
            return self.build_context.type_map[name]
        raise UndefinedKeyword(f"Variable - {name} was not declared in PyMake file")

    def set_value(self, name: str, value: str | None) -> None:
        if self.get_type(name) == "basic" and value:
            if name in self.namespace:
                raise MultipleDefinition(
                    f"Variable {name} is defined multiple times at parsing"
                )
            else:
                self.namespace[name] = str(value)
        elif self.get_type(name) == "sequence" and value:
            if name in self.namespace:
                self.namespace[name] += f" {value}"
            else:
                self.namespace[name] = f"{value}"
        else:
            self.namespace[name] = self.build_context.flag[name]


class State(abc.ABC):
    def __init__(self, context: Context, parser: Parser) -> None:
        self.context = context
        self.parser = parser

    @abc.abstractmethod
    def handle_value(self, value: str):
        pass

    @abc.abstractmethod
    def handle_keyword(self, keyword: str):
        pass


class ExpectOption(State):
    def handle_keyword(self, keyword: str) -> None:
        self.context.reference = keyword
        self.context.use_position = False
        self.context.position = None
        keyword_type = self.context.get_type(keyword)
        if keyword_type in ["basic", "sequence"]:
            self.parser.transition(
                ExpectValue(
                    context=self.context,
                    parser=self.parser,
                ),
            )
        else:
            self.context.set_value(keyword)
            self.parser.transition(
                ExpectOption(
                    context=self.context,
                    parser=self.parser,
                )
            )

    def handle_value(self, value: str) -> None:
        raise InvalidPositionalVariable(
            f"Parser expects a keyword argument. Receive positional: {value}"
        )


class ExpectValue(State):
    def handle_keyword(self, keyword: str) -> None:
        raise InvalidKeyword(f"Parser expecting a value. Receive keyword: {keyword}")

    def handle_value(self, value: str) -> None:
        self.context.set(self.context.reference, value)
        if self.context.get_type(self.context.reference) == "sequence":
            self.parser.transition(
                ExpectOptionValue(
                    context=self.context,
                    parser=self.parser,
                )
            )
        else:
            self.parser.transition(
                ExpectOption(
                    context=self.context,
                    parser=self.parser,
                )
            )


class ExpectOptionValue(ExpectOption):
    def handle_value(self, value: str) -> None:
        if self.context.use_position:
            self.handle_positional(value)
        else:
            # Only valid state here is if variable is of sequence type
            assert self.context.get_type(self.context.reference) == "sequence"
            self.context.set_value(self.context.reference, value)

    def handle_positional(self, value: str) -> None:
        # Set value to pointer's variable and advance pointer
        variable = self.context.build_context.positional[self.context.position]
        self.context.set_value(variable, value)
        self.context.position += 1
        if self.context.position < len(self.context.build_context.positional):
            self.parser.transition(
                ExpectOptionValue(
                    context=self.context,
                    parser=self.parser,
                )
            )
        else:
            self.context.use_position = False
            self.parser.transition(
                ExpectOption(
                    context=self.context,
                    parser=self.parser,
                )
            )


class Parser:
    def __init__(self, context: Builder) -> None:
        context = Context(
            build_context=context,
            use_position=True,
            position=0,
        )
        self.state = ExpectOptionValue(
            context=context,
            parser=self,
        )

    def handle_value(self, value: str) -> None:
        self.state.handle_value(value)

    def handle_keyword(self, keyword: str) -> None:
        self.state.handle_keyword(keyword)

    def transition(self, new_state: State) -> None:
        self.state = new_state

    def parse(self, args: list[str]) -> None:
        pattern = r"--(\w+)"
        for arg in args:
            match = re.findall(pattern, arg)
            if match:
                self.handle_keyword(match[0])
            else:
                self.handle_value(arg)
