import pytest
import yaml

from PyMake.console.builder.builder import Builder
from PyMake.console.parser.parser import Parser
from PyMake.exceptions import InvalidKeyword, MissingPositionalValue, MultipleDefinition


@pytest.mark.parametrize(
    "arg_str, output",
    [
        ("invalid_keyword_target12_stmt1", InvalidKeyword),
        ("invalid_keyword_target12_stmt2", InvalidKeyword),
        ("invalid_keyword_target12_stmt3", InvalidKeyword),
        ("missing_positional_stmt1", MissingPositionalValue),
        ("missing_positional_stmt2", MissingPositionalValue),
        ("multiple_definition_1", MultipleDefinition),
        ("multiple_definition_2", MultipleDefinition),
        ("multiple_definition_3", MultipleDefinition),
    ],
)
def test_invalid_stmt(arg_str, output, valid_yaml_target12_1, request):
    yaml_str = valid_yaml_target12_1
    arg_str = request.getfixturevalue(arg_str)
    data = yaml.safe_load(yaml_str)["target"]
    context = Builder(data=data)
    context.build()
    parser = Parser(context=context)

    with pytest.raises(output):
        parser.parse(arg_str.split())
