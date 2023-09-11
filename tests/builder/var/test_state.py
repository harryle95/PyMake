import pytest

from PyMake.exceptions import StateError
from PyMake.parser.parser import ExpectOption, VarParser


@pytest.fixture(scope="function")
def context_with_position() -> VarParser:
    return VarParser(
        variables={"var1": "basic"},
        positional={0: "var1"},
        default={"var1": 10},
        required=[],
    )


@pytest.fixture(scope="function")
def context_no_position() -> VarParser:
    return VarParser(
        variables={"var1": "flag"}, positional={}, default={"var1": "-a"}, required=[]
    )


def test_invalid_state_variable_allow_positional(context_with_position):
    with pytest.raises(StateError):
        ExpectOption(
            context=context_with_position,
            variable="var1",
            allow_positional=True,
            pointer=0,
        )


def test_invalid_state_allow_position_pointer_none(context_with_position):
    with pytest.raises(StateError):
        ExpectOption(
            context=context_with_position,
            variable=None,
            allow_positional=True,
            pointer=None,
        )


def test_invalid_state_invalid_pointer(context_with_position):
    with pytest.raises(StateError):
        ExpectOption(
            context=context_with_position,
            variable=None,
            allow_positional=True,
            pointer=10,
        )


def test_init_state_positional(context_with_position):
    assert context_with_position._state.allow_positional is True
    assert context_with_position._state.pointer == 0


def test_init_state_no_positional(context_no_position):
    assert context_no_position._state.allow_positional is False
    assert context_no_position._state.pointer is None
