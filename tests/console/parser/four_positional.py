import pytest
import yaml

from PyMake.console.builder.builder import Builder
from PyMake.console.parser.parser import Parser
from PyMake.exceptions import InvalidPositionalVariable


@pytest.fixture(scope="function")
def target1_four_positionals():
    return InvalidPositionalVariable


@pytest.fixture(scope="function")
def target2_four_positionals():
    return {"var1": "10", "var2": "Alexa", "var3": "Wikipedia", "var4": "localhost"}


@pytest.fixture(scope="function")
def target3_four_positionals():
    return InvalidPositionalVariable


@pytest.fixture(scope="function")
def target4_four_positionals():
    return InvalidPositionalVariable


@pytest.fixture(scope="function")
def target5_four_positionals():
    return InvalidPositionalVariable


@pytest.fixture(scope="function")
def target6_four_positionals():
    return InvalidPositionalVariable


@pytest.fixture(scope="function")
def target7_four_positionals():
    return InvalidPositionalVariable


@pytest.fixture(scope="function")
def target8_four_positionals():
    return InvalidPositionalVariable


@pytest.fixture(scope="function")
def target9_four_positionals():
    return InvalidPositionalVariable


@pytest.fixture(scope="function")
def target10_four_positionals():
    return InvalidPositionalVariable


@pytest.fixture(scope="function")
def target11_four_positionals():
    return InvalidPositionalVariable


@pytest.fixture(scope="function")
def target12_four_positionals():
    return InvalidPositionalVariable


@pytest.fixture(scope="function")
def target13_four_positionals():
    return InvalidPositionalVariable


@pytest.mark.parametrize(
    "yaml_str, output",
    [
        ("valid_yaml_target1_1", "target1_four_positionals"),
        ("valid_yaml_target2_1", "target2_four_positionals"),
        ("valid_yaml_target3_1", "target3_four_positionals"),
        ("valid_yaml_target4_1", "target4_four_positionals"),
        ("valid_yaml_target5_1", "target5_four_positionals"),
        ("valid_yaml_target6_1", "target6_four_positionals"),
        ("valid_yaml_target7_1", "target7_four_positionals"),
        ("valid_yaml_target8_1", "target8_four_positionals"),
        ("valid_yaml_target9_1", "target9_four_positionals"),
        ("valid_yaml_target10_1", "target10_four_positionals"),
        ("valid_yaml_target11_1", "target11_four_positionals"),
        ("valid_yaml_target12_1", "target12_four_positionals"),
        ("valid_yaml_target13_1", "target13_four_positionals"),
    ],
)
def test_four_positionals(yaml_str, output, four_positionals, request):
    yaml_str = request.getfixturevalue(yaml_str)
    data = yaml.safe_load(yaml_str)["target"]
    context = Builder(data=data)
    context.build()
    parser = Parser(context=context)
    output = request.getfixturevalue(output)
    if isinstance(output, dict):
        parser.parse(four_positionals.split())
        assert parser.namespace == output
    else:
        with pytest.raises(output):
            parser.parse(four_positionals.split())
