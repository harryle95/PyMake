import pytest
import yaml

from PyMake.console.builder.builder import Builder
from PyMake.console.parser.parser import Parser
from PyMake.exceptions import InvalidPositionalVariable, MissingRequiredVariable


@pytest.fixture(scope="function")
def target1_two_positionals():
    return InvalidPositionalVariable


@pytest.fixture(scope="function")
def target2_two_positionals():
    return MissingRequiredVariable


@pytest.fixture(scope="function")
def target3_two_positionals():
    return InvalidPositionalVariable


@pytest.fixture(scope="function")
def target4_two_positionals():
    return InvalidPositionalVariable


@pytest.fixture(scope="function")
def target5_two_positionals():
    return InvalidPositionalVariable


@pytest.fixture(scope="function")
def target6_two_positionals():
    return InvalidPositionalVariable


@pytest.fixture(scope="function")
def target7_two_positionals():
    return MissingRequiredVariable


@pytest.fixture(scope="function")
def target8_two_positionals():
    return MissingRequiredVariable


@pytest.fixture(scope="function")
def target9_two_positionals():
    return MissingRequiredVariable


@pytest.fixture(scope="function")
def target10_two_positionals():
    return MissingRequiredVariable


@pytest.fixture(scope="function")
def target11_two_positionals():
    return InvalidPositionalVariable


@pytest.fixture(scope="function")
def target12_two_positionals():
    return {
        "var1": "10",
        "var2": "Alexa",
        "var3": "3",
        "list1": "1 2 3",
        "list2": "4 5 6",
    }


@pytest.fixture(scope="function")
def target13_two_positionals():
    return InvalidPositionalVariable


@pytest.mark.parametrize(
    "yaml_str, output",
    [
        ("valid_yaml_target1_1", "target1_two_positionals"),
        ("valid_yaml_target2_1", "target2_two_positionals"),
        ("valid_yaml_target3_1", "target3_two_positionals"),
        ("valid_yaml_target4_1", "target4_two_positionals"),
        ("valid_yaml_target5_1", "target5_two_positionals"),
        ("valid_yaml_target6_1", "target6_two_positionals"),
        ("valid_yaml_target7_1", "target7_two_positionals"),
        ("valid_yaml_target8_1", "target8_two_positionals"),
        ("valid_yaml_target9_1", "target9_two_positionals"),
        ("valid_yaml_target10_1", "target10_two_positionals"),
        ("valid_yaml_target11_1", "target11_two_positionals"),
        ("valid_yaml_target12_1", "target12_two_positionals"),
        ("valid_yaml_target13_1", "target13_two_positionals"),
    ],
)
def test_two_positionals(yaml_str, output, two_positionals, request):
    yaml_str = request.getfixturevalue(yaml_str)
    data = yaml.safe_load(yaml_str)["target"]
    context = Builder(data=data)
    context.build()
    parser = Parser(context=context)
    output = request.getfixturevalue(output)
    if isinstance(output, dict):
        parser.parse(two_positionals.split())
        assert parser.namespace == output
    else:
        with pytest.raises(output):
            parser.parse(two_positionals.split())
