import pytest
import yaml

from PyMake.console.builder.builder import Builder
from PyMake.console.parser.parser import Parser
from PyMake.exceptions import UndefinedKeyword


@pytest.fixture(scope="function")
def target1_list23():
    return UndefinedKeyword


@pytest.fixture(scope="function")
def target2_list23():
    return UndefinedKeyword


@pytest.fixture(scope="function")
def target3_list23():
    return UndefinedKeyword


@pytest.fixture(scope="function")
def target4_list23():
    return UndefinedKeyword


@pytest.fixture(scope="function")
def target5_list23():
    return UndefinedKeyword


@pytest.fixture(scope="function")
def target6_list23():
    return UndefinedKeyword


@pytest.fixture(scope="function")
def target7_list23():
    return UndefinedKeyword


@pytest.fixture(scope="function")
def target8_list23():
    return UndefinedKeyword


@pytest.fixture(scope="function")
def target9_list23():
    return UndefinedKeyword


@pytest.fixture(scope="function")
def target10_list23():
    return UndefinedKeyword


@pytest.fixture(scope="function")
def target11_list23():
    return UndefinedKeyword


@pytest.fixture(scope="function")
def target12_list23():
    return UndefinedKeyword


@pytest.fixture(scope="function")
def target13_list23():
    return {"list1": "1", "list2": "20 30 40", "list3": "100 200"}


@pytest.mark.parametrize(
    "yaml_str, output",
    [
        ("valid_yaml_target1_1", "target1_list23"),
        ("valid_yaml_target2_1", "target2_list23"),
        ("valid_yaml_target3_1", "target3_list23"),
        ("valid_yaml_target4_1", "target4_list23"),
        ("valid_yaml_target5_1", "target5_list23"),
        ("valid_yaml_target6_1", "target6_list23"),
        ("valid_yaml_target7_1", "target7_list23"),
        ("valid_yaml_target8_1", "target8_list23"),
        ("valid_yaml_target9_1", "target9_list23"),
        ("valid_yaml_target10_1", "target10_list23"),
        ("valid_yaml_target11_1", "target11_list23"),
        ("valid_yaml_target12_1", "target12_list23"),
        ("valid_yaml_target13_1", "target13_list23"),
    ],
)
def test_list23(yaml_str, output, list23, request):
    yaml_str = request.getfixturevalue(yaml_str)
    data = yaml.safe_load(yaml_str)["target"]
    context = Builder(data=data)
    context.build()
    parser = Parser(context=context)
    output = request.getfixturevalue(output)
    if isinstance(output, dict):
        parser.parse(list23.split())
        assert parser.namespace == output
    else:
        with pytest.raises(output):
            parser.parse(list23.split())
