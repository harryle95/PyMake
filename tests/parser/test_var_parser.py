import pytest

from PyMake.parser.utils.exceptions import (
    InvalidPointerError,
    InvalidValueError,
    MissingRequiredVariableError,
    UndefinedVariableError,
    VariableRedefinitionError,
)


@pytest.mark.parametrize(
    "var_parser, valid_input",
    [
        ("var_parser1", "valid_var_parser1_input1"),
        ("var_parser1", "valid_var_parser1_input2"),
        ("var_parser1", "valid_var_parser1_input3"),
        ("var_parser1", "valid_var_parser1_input4"),
        ("var_parser1", "valid_var_parser1_input5"),
        ("var_parser1", "valid_var_parser1_input6"),
        ("var_parser1", "valid_var_parser1_input7"),
        ("var_parser1", "valid_var_parser1_input8"),
        ("var_parser1", "valid_var_parser1_input9"),
        ("var_parser1", "valid_var_parser1_input10"),
        ("var_parser1", "valid_var_parser1_input11"),
        ("var_parser1", "valid_var_parser1_input12"),
        ("var_parser2", "valid_var_parser2_input1"),
        ("var_parser2", "valid_var_parser2_input2"),
        ("var_parser2", "valid_var_parser2_input3"),
        ("var_parser2", "valid_var_parser2_input4"),
        ("var_parser2", "valid_var_parser2_input5"),
        ("var_parser2", "valid_var_parser2_input6"),
        ("var_parser3", "valid_var_parser3_input1"),
        ("var_parser3", "valid_var_parser3_input2"),
        ("var_parser3", "valid_var_parser3_input3"),
        ("var_parser3", "valid_var_parser3_input4"),
    ],
)
def test_var_parser_valid(var_parser, valid_input, request):
    var_parser = request.getfixturevalue(var_parser)
    valid_input = request.getfixturevalue(valid_input)
    var_parser.parse(valid_input["args"])
    assert var_parser.namespace == valid_input["namespace"]


@pytest.mark.parametrize(
    "var_parser, invalid_input",
    [
        ("var_parser1", "invalid_var_parser1_undefined_variable_1"),
        ("var_parser1", "invalid_var_parser1_undefined_variable_2"),
        ("var_parser1", "invalid_var_parser1_undefined_variable_3"),
        ("var_parser1", "invalid_var_parser1_undefined_variable_4"),
    ],
)
def test_var_parser_undefined_var(var_parser, invalid_input, request):
    var_parser = request.getfixturevalue(var_parser)
    args = request.getfixturevalue(invalid_input)["args"]
    with pytest.raises(UndefinedVariableError):
        var_parser.parse(args)


@pytest.mark.parametrize(
    "var_parser, invalid_input",
    [
        ("var_parser1", "invalid_var_parser1_invalid_value_1"),
        ("var_parser1", "invalid_var_parser1_invalid_value_2"),
        ("var_parser2", "invalid_var_parser2_invalid_value_1"),
        ("var_parser2", "invalid_var_parser2_invalid_value_2"),
        ("var_parser2", "invalid_var_parser2_invalid_value_3"),
        ("var_parser2", "invalid_var_parser2_invalid_value_4"),
        ("var_parser2", "invalid_var_parser2_invalid_value_5"),
    ],
)
def test_var_parser_invalid_value(var_parser, invalid_input, request):
    var_parser = request.getfixturevalue(var_parser)
    args = request.getfixturevalue(invalid_input)["args"]
    with pytest.raises(InvalidValueError):
        var_parser.parse(args)


@pytest.mark.parametrize(
    "var_parser, invalid_input",
    [
        ("var_parser1", "invalid_var_parser1_variable_redefinition_1"),
        ("var_parser1", "invalid_var_parser1_variable_redefinition_2"),
    ],
)
def test_var_parser_variable_redefinition(var_parser, invalid_input, request):
    var_parser = request.getfixturevalue(var_parser)
    args = request.getfixturevalue(invalid_input)["args"]
    with pytest.raises(VariableRedefinitionError):
        var_parser.parse(args)


@pytest.mark.parametrize(
    "var_parser, invalid_input",
    [
        ("var_parser1", "invalid_var_parser1_undefined_variable_1"),
        ("var_parser1", "invalid_var_parser1_undefined_variable_2"),
        ("var_parser1", "invalid_var_parser1_undefined_variable_3"),
        ("var_parser1", "invalid_var_parser1_undefined_variable_4"),
        ("var_parser2", "invalid_var_parser2_undefined_variable_1"),
        ("var_parser2", "invalid_var_parser2_undefined_variable_2"),
    ],
)
def test_var_parser_variable_undefined(var_parser, invalid_input, request):
    var_parser = request.getfixturevalue(var_parser)
    args = request.getfixturevalue(invalid_input)["args"]
    with pytest.raises(UndefinedVariableError):
        var_parser.parse(args)


@pytest.mark.parametrize(
    "var_parser, invalid_input",
    [
        ("var_parser2", "invalid_var_parser2_missing_required_1"),
        ("var_parser2", "invalid_var_parser2_missing_required_2"),
    ],
)
def test_var_parser_missing_required(var_parser, invalid_input, request):
    var_parser = request.getfixturevalue(var_parser)
    args = request.getfixturevalue(invalid_input)["args"]
    with pytest.raises(MissingRequiredVariableError):
        var_parser.parse(args)


@pytest.mark.parametrize(
    "var_parser, pointer",
    [
        ("var_parser1", None),
        ("var_parser1", 4),
        ("var_parser3", 0),
    ],
)
def test_invalid_pointer_value(var_parser, pointer, request):
    var_parser = request.getfixturevalue(var_parser)
    with pytest.raises(InvalidPointerError):
        var_parser.get_positional(pointer)
