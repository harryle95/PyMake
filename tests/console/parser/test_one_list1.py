import pytest
import yaml

from PyMake.console.builder.builder import Builder
from PyMake.console.parser.parser import Parser
from PyMake.exceptions import MissingRequiredVariable, UndefinedKeyword


@pytest.fixture(scope="function")
def target1_one_list1():
    return UndefinedKeyword


@pytest.fixture(scope="function")
def target2_one_list1():
    return UndefinedKeyword


@pytest.fixture(scope="function")
def target3_one_list1():
    return UndefinedKeyword


@pytest.fixture(scope="function")
def target4_one_list1():
    return UndefinedKeyword


@pytest.fixture(scope="function")
def target5_one_list1():
    return {"list1": "10 20 30"}


@pytest.fixture(scope="function")
def target6_one_list1():
    return {"list1": "10 20 30"}


@pytest.fixture(scope="function")
def target7_one_list1():
    return MissingRequiredVariable


@pytest.fixture(scope="function")
def target8_one_list1():
    return MissingRequiredVariable


@pytest.fixture(scope="function")
def target9_one_list1():
    return MissingRequiredVariable


@pytest.fixture(scope="function")
def target10_one_list1():
    return MissingRequiredVariable


@pytest.fixture(scope="function")
def target11_one_list1():
    return MissingRequiredVariable


@pytest.fixture(scope="function")
def target12_one_list1():
    return {
        "var1": "1",
        "var2": "2",
        "var3": "3",
        "list1": "10 20 30",
        "list2": "4 5 6",
    }


@pytest.fixture(scope="function")
def target13_one_list1():
    return MissingRequiredVariable


@pytest.mark.parametrize(
    "yaml_str, output",
    [
        ("valid_yaml_target1_1", "target1_one_list1"),
        ("valid_yaml_target2_1", "target2_one_list1"),
        ("valid_yaml_target3_1", "target3_one_list1"),
        ("valid_yaml_target4_1", "target4_one_list1"),
        ("valid_yaml_target5_1", "target5_one_list1"),
        ("valid_yaml_target6_1", "target6_one_list1"),
        ("valid_yaml_target7_1", "target7_one_list1"),
        ("valid_yaml_target8_1", "target8_one_list1"),
        ("valid_yaml_target9_1", "target9_one_list1"),
        ("valid_yaml_target10_1", "target10_one_list1"),
        ("valid_yaml_target11_1", "target11_one_list1"),
        ("valid_yaml_target12_1", "target12_one_list1"),
        ("valid_yaml_target13_1", "target13_one_list1"),
    ],
)
def test_one_list1(yaml_str, output, one_list1, request):
    yaml_str = request.getfixturevalue(yaml_str)
    data = yaml.safe_load(yaml_str)["target"]
    context = Builder(data=data)
    context.build()
    parser = Parser(context=context)
    output = request.getfixturevalue(output)
    if isinstance(output, dict):
        parser.parse(one_list1.split())
        assert parser.namespace == output
    else:
        with pytest.raises(output):
            parser.parse(one_list1.split())
