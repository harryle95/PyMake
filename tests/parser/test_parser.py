import pytest

from PyMake.exceptions import InvalidPointerError, InvalidValueError, MissingRequiredVariableError, \
    UndefinedVariableError, \
    VariableRedefinitionError


@pytest.mark.parametrize(
    "parser, valid_input", [
        ("parser1", "valid_parser1_input1"),
        ("parser1", "valid_parser1_input2"),
        ("parser1", "valid_parser1_input3"),
        ("parser1", "valid_parser1_input4"),
        ("parser1", "valid_parser1_input5"),
        ("parser1", "valid_parser1_input6"),
        ("parser1", "valid_parser1_input7"),
        ("parser1", "valid_parser1_input8"),
        ("parser1", "valid_parser1_input9"),
        ("parser1", "valid_parser1_input10"),
        ("parser1", "valid_parser1_input11"),
        ("parser1", "valid_parser1_input12"),
        ("parser2", "valid_parser2_input1"),
        ("parser2", "valid_parser2_input2"),
        ("parser2", "valid_parser2_input3"),
        ("parser2", "valid_parser2_input4"),
        ("parser2", "valid_parser2_input5"),
        ("parser2", "valid_parser2_input6"),
        ("parser3", "valid_parser3_input1"),
        ("parser3", "valid_parser3_input2"),
        ("parser3", "valid_parser3_input3"),
        ("parser3", "valid_parser3_input4"),
    ]
)
def test_parser_valid(parser, valid_input, request):
    parser = request.getfixturevalue(parser)
    valid_input = request.getfixturevalue(valid_input)
    parser.parse(valid_input['args'])
    assert parser.namespace == valid_input['namespace']


@pytest.mark.parametrize(
    "parser, invalid_input", [
        ("parser1", "invalid_parser1_undefined_variable_1"),
        ("parser1", "invalid_parser1_undefined_variable_2"),
        ("parser1", "invalid_parser1_undefined_variable_3"),
        ("parser1", "invalid_parser1_undefined_variable_4"),
    ]
)
def test_parser_undefined_var(parser, invalid_input, request):
    parser = request.getfixturevalue(parser)
    args = request.getfixturevalue(invalid_input)['args']
    with pytest.raises(UndefinedVariableError):
        parser.parse(args)


@pytest.mark.parametrize(
    "parser, invalid_input", [
        ("parser1", "invalid_parser1_invalid_value_1"),
        ("parser1", "invalid_parser1_invalid_value_2"),
        ("parser2", "invalid_parser2_invalid_value_1"),
        ("parser2", "invalid_parser2_invalid_value_2"),
        ("parser2", "invalid_parser2_invalid_value_3"),
        ("parser2", "invalid_parser2_invalid_value_4"),
        ("parser2", "invalid_parser2_invalid_value_5"),
    ]
)
def test_parser_invalid_value(parser, invalid_input, request):
    parser = request.getfixturevalue(parser)
    args = request.getfixturevalue(invalid_input)['args']
    with pytest.raises(InvalidValueError):
        parser.parse(args)


@pytest.mark.parametrize(
    "parser, invalid_input", [
        ("parser1", "invalid_parser1_variable_redefinition_1"),
        ("parser1", "invalid_parser1_variable_redefinition_2"),
    ]
)
def test_parser_variable_redefinition(parser, invalid_input, request):
    parser = request.getfixturevalue(parser)
    args = request.getfixturevalue(invalid_input)['args']
    with pytest.raises(VariableRedefinitionError):
        parser.parse(args)


@pytest.mark.parametrize(
    "parser, invalid_input", [
        ("parser1", "invalid_parser1_undefined_variable_1"),
        ("parser1", "invalid_parser1_undefined_variable_2"),
        ("parser1", "invalid_parser1_undefined_variable_3"),
        ("parser1", "invalid_parser1_undefined_variable_4"),
        ("parser2", "invalid_parser2_undefined_variable_1"),
        ("parser2", "invalid_parser2_undefined_variable_2"),
    ]
)
def test_parser_variable_undefined(parser, invalid_input, request):
    parser = request.getfixturevalue(parser)
    args = request.getfixturevalue(invalid_input)['args']
    with pytest.raises(UndefinedVariableError):
        parser.parse(args)


@pytest.mark.parametrize(
    "parser, invalid_input", [
        ("parser2", "invalid_parser2_missing_required_1"),
        ("parser2", "invalid_parser2_missing_required_2"),
    ]
)
def test_parser_missing_required(parser, invalid_input, request):
    parser = request.getfixturevalue(parser)
    args = request.getfixturevalue(invalid_input)['args']
    with pytest.raises(MissingRequiredVariableError):
        parser.parse(args)


@pytest.mark.parametrize(
    "parser, pointer", [
        ("parser1", None),
        ("parser1", 4),
        ("parser3", 0),
    ]
)
def test_invalid_pointer_value(parser, pointer, request):
    parser = request.getfixturevalue(parser)
    with pytest.raises(InvalidPointerError):
        parser.get_positional(pointer)
