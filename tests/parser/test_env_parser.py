import pytest

from PyMake.exceptions import MissingRequiredVariableError


@pytest.mark.parametrize(
    "env_parser, valid_input",
    [
        ("env_parser1", "valid_env_parser1_input1"),
        ("env_parser1", "valid_env_parser1_input2"),
        ("env_parser1", "valid_env_parser1_input3"),
    ],
)
def test_valid_input(env_parser, valid_input, request):
    env_parser = request.getfixturevalue(env_parser)
    valid_input = request.getfixturevalue(valid_input)
    assert env_parser.parse(valid_input["var_ns"]) == valid_input["env_ns"]


@pytest.mark.parametrize(
    "env_parser, invalid_input",
    [
        ("env_parser1", "invalid_env_parser1_input1"),
        ("env_parser1", "invalid_env_parser1_input2"),
    ],
)
def test_valid_input(env_parser, invalid_input, request):
    env_parser = request.getfixturevalue(env_parser)
    invalid_input = request.getfixturevalue(invalid_input)
    with pytest.raises(MissingRequiredVariableError):
        env_parser.parse(invalid_input["var_ns"])
