import pytest


@pytest.mark.parametrize(
    "parser, args, output", [
        ("parser_1", "input_1", "parser1_input1_output"),
        ("parser_1", "input_2", "parser1_input2_output"),
        ("parser_1", "input_3", "parser1_input3_output"),
        ("parser_1", "input_4", "parser1_input4_output"),
        ("parser_1", "input_5", "parser1_input5_output"),
    ]
)
def test_parser_valid(parser, args, output, request):
    parser = request.getfixturevalue(parser)
    arg = request.getfixturevalue(args)
    output = request.getfixturevalue(output)
    parser.parse(arg)
    assert parser.namespace == output
