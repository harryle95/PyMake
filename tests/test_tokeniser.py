from typing import List

import pytest

from PyMake.exceptions import KeywordFormatError
from PyMake.tokens import Tokenizer


@pytest.fixture(scope="function")
def valid_arg_1() -> str:
    return "--arg1 10 --arg2 100 -arg3"


@pytest.fixture(scope="function")
def valid_arg_1_values() -> List[str]:
    return ["arg1", "10", "arg2", "100", "arg3"]


@pytest.fixture(scope="function")
def valid_arg_1_options() -> List[bool]:
    return [True, False, True, False, True]


@pytest.fixture(scope="function")
def valid_arg_2() -> str:
    return "1 --arg1 10 100"


@pytest.fixture(scope="function")
def valid_arg_2_values() -> List[str]:
    return ["1", "arg1", "10", "100"]


@pytest.fixture(scope="function")
def valid_arg_2_options() -> List[bool]:
    return [False, True, False, False]


@pytest.fixture(scope="function")
def invalid_arg_1() -> str:
    return "---arg1 10 --arg2 100"


@pytest.fixture(scope="function")
def invalid_arg_2() -> str:
    return "----arg1 10"


@pytest.mark.parametrize(
    "test_input, exp_value, exp_option", [
        ("valid_arg_1", "valid_arg_1_values", "valid_arg_1_options"),
        ("valid_arg_2", "valid_arg_2_values", "valid_arg_2_options")
    ]
)
def test_valid_inputs(test_input, exp_value, exp_option, request):
    arg = request.getfixturevalue(test_input)
    tokens = Tokenizer.tokenize(arg)
    values = request.getfixturevalue(exp_value)
    options = request.getfixturevalue(exp_option)
    for i in range(len(tokens)):
        assert tokens[i].value == values[i]
        assert tokens[i].is_option == options[i]


@pytest.mark.parametrize(
    "test_input", [
        "invalid_arg_1",
        "invalid_arg_2"
    ]
)
def test_invalid_input(test_input, request):
    arg = request.getfixturevalue(test_input)
    with pytest.raises(KeywordFormatError):
        tokens = Tokenizer.tokenize(arg)
        tokens = [token.value for token in tokens]
