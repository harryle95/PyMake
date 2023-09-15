import pytest
import yaml

from PyMake.console.builder.builder import Builder
from PyMake.console.parser.parser import Parser
from PyMake.exceptions import MissingRequiredVariable, UndefinedKeyword


@pytest.fixture(scope="function")
def target1_var13_list1():
    return UndefinedKeyword


@pytest.fixture(scope="function")
def target2_var13_list1():
    return UndefinedKeyword


@pytest.fixture(scope="function")
def target3_var13_list1():
    return UndefinedKeyword


@pytest.fixture(scope="function")
def target4_var13_list1():
    return UndefinedKeyword


@pytest.fixture(scope="function")
def target5_var13_list1():
    return UndefinedKeyword


@pytest.fixture(scope="function")
def target6_var13_list1():
    return UndefinedKeyword


@pytest.fixture(scope="function")
def target7_var13_list1():
    return {"var1": "10", "var2": "2", "var3": "Wikipedia", "list1": "10 20 30"}


@pytest.fixture(scope="function")
def target8_var13_list1():
    return {"var1": "10", "var2": "2", "var3": "Wikipedia", "list1": "10 20 30"}


@pytest.fixture(scope="function")
def target9_var13_list1():
    return MissingRequiredVariable


@pytest.fixture(scope="function")
def target10_var13_list1():
    return MissingRequiredVariable


@pytest.fixture(scope="function")
def target11_var13_list1():
    return UndefinedKeyword


@pytest.fixture(scope="function")
def target12_var13_list1():
    return {
        "var1": "10",
        "var2": "2",
        "var3": "Wikipedia",
        "list1": "10 20 30",
        "list2": "4 5 6",
    }


@pytest.fixture(scope="function")
def target13_var13_list1():
    return UndefinedKeyword


@pytest.mark.parametrize(
    "yaml_str, output",
    [
        ("valid_yaml_target1_1", "target1_var13_list1"),
        ("valid_yaml_target2_1", "target2_var13_list1"),
        ("valid_yaml_target3_1", "target3_var13_list1"),
        ("valid_yaml_target4_1", "target4_var13_list1"),
        ("valid_yaml_target5_1", "target5_var13_list1"),
        ("valid_yaml_target6_1", "target6_var13_list1"),
        ("valid_yaml_target7_1", "target7_var13_list1"),
        ("valid_yaml_target8_1", "target8_var13_list1"),
        ("valid_yaml_target9_1", "target9_var13_list1"),
        ("valid_yaml_target10_1", "target10_var13_list1"),
        ("valid_yaml_target11_1", "target11_var13_list1"),
        ("valid_yaml_target12_1", "target12_var13_list1"),
        ("valid_yaml_target13_1", "target13_var13_list1"),
    ],
)
def test_var13_list1(yaml_str, output, var13_list1, request):
    yaml_str = request.getfixturevalue(yaml_str)
    data = yaml.safe_load(yaml_str)["target"]
    context = Builder(data=data)
    context.build()
    parser = Parser(context=context)
    output = request.getfixturevalue(output)
    if isinstance(output, dict):
        parser.parse(var13_list1.split())
        assert parser.namespace == output
    else:
        with pytest.raises(output):
            parser.parse(var13_list1.split())
