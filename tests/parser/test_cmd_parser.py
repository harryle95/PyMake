import pytest

from PyMake.parser.utils.exceptions import MissingRequiredVariableError


@pytest.mark.parametrize(
    "cmd_parser, valid_input",
    [
        ("cmd_parser1", "valid_cmd_parser1_input1"),
        ("cmd_parser2", "valid_cmd_parser2_input1"),
        ("cmd_parser2", "valid_cmd_parser2_input2"),
    ],
)
def test_valid_input(cmd_parser, valid_input, request):
    cmd_parser = request.getfixturevalue(cmd_parser)
    valid_input = request.getfixturevalue(valid_input)
    namespace = cmd_parser.parse(valid_input["var_ns"])
    assert namespace == valid_input["cmd_ns"]
    section_script = [
        item.strip()
        for item in cmd_parser.parsed_script.split("\n")
        if item.strip() != ""
    ]
    expected_script = [
        item.strip() for item in valid_input["script"].split("\n") if item.strip() != ""
    ]
    assert section_script == expected_script


@pytest.mark.parametrize(
    "cmd_parser, invalid_input",
    [
        ("cmd_parser1", "invalid_cmd_parser1_input2"),
        ("cmd_parser3", "invalid_cmd_parser3_input1"),
        ("cmd_parser3", "invalid_cmd_parser3_input2"),
    ],
)
def test_invalid_input(cmd_parser, invalid_input, request):
    cmd_parser = request.getfixturevalue(cmd_parser)
    invalid_input = request.getfixturevalue(invalid_input)
    with pytest.raises(MissingRequiredVariableError):
        cmd_parser.parse(invalid_input["var_ns"])
