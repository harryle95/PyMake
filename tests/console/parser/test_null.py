import pytest
import yaml

from PyMake.console.builder.builder import Builder
from PyMake.console.parser.parser import Parser
from PyMake.exceptions import MissingRequiredVariable


@pytest.fixture(scope="function")
def target1_null():
    return {}


@pytest.fixture(scope="function")
def target2_null():
    return MissingRequiredVariable


@pytest.fixture(scope="function")
def target3_null():
    return MissingRequiredVariable


@pytest.fixture(scope="function")
def target4_null():
    return {}


@pytest.fixture(scope="function")
def target5_null():
    return MissingRequiredVariable


@pytest.fixture(scope="function")
def target6_null():
    return {"list1": "1 2 3"}


@pytest.fixture(scope="function")
def target7_null():
    return MissingRequiredVariable


@pytest.fixture(scope="function")
def target8_null():
    return MissingRequiredVariable


@pytest.fixture(scope="function")
def target9_null():
    return MissingRequiredVariable


@pytest.fixture(scope="function")
def target10_null():
    return MissingRequiredVariable


@pytest.fixture(scope="function")
def target11_null():
    return MissingRequiredVariable


@pytest.fixture(scope="function")
def target12_null():
    return {
        "var1": "1",
        "var2": "2",
        "var3": "3",
        "list1": "1 2 3",
        "list2": "4 5 6",
    }


@pytest.fixture(scope="function")
def target13_null():
    return MissingRequiredVariable


@pytest.mark.parametrize(
    "yaml_str, output",
    [
        ("valid_yaml_target1_1", "target1_null"),
        ("valid_yaml_target2_1", "target2_null"),
        ("valid_yaml_target3_1", "target3_null"),
        ("valid_yaml_target4_1", "target4_null"),
        ("valid_yaml_target5_1", "target5_null"),
        ("valid_yaml_target6_1", "target6_null"),
        ("valid_yaml_target7_1", "target7_null"),
        ("valid_yaml_target8_1", "target8_null"),
        ("valid_yaml_target9_1", "target9_null"),
        ("valid_yaml_target10_1", "target10_null"),
        ("valid_yaml_target11_1", "target11_null"),
        ("valid_yaml_target12_1", "target12_null"),
        ("valid_yaml_target13_1", "target13_null"),
    ],
)
def test_null(yaml_str, output, null_arg, request):
    yaml_str = request.getfixturevalue(yaml_str)
    data = yaml.safe_load(yaml_str)["target"]
    context = Builder(data=data)
    context.build()
    parser = Parser(context=context)
    output = request.getfixturevalue(output)
    if isinstance(output, dict):
        parser.parse(null_arg.split())
        assert parser.namespace == output
    else:
        with pytest.raises(output):
            parser.parse(null_arg.split())
