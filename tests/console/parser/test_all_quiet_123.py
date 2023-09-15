import pytest
import yaml

from PyMake.console.builder.builder import Builder
from PyMake.console.parser.parser import Parser
from PyMake.exceptions import UndefinedKeyword


@pytest.fixture(scope="function")
def target1_all_quiet():
    return UndefinedKeyword


@pytest.fixture(scope="function")
def target2_all_quiet():
    return UndefinedKeyword


@pytest.fixture(scope="function")
def target3_all_quiet():
    return UndefinedKeyword


@pytest.fixture(scope="function")
def target4_all_quiet():
    return UndefinedKeyword


@pytest.fixture(scope="function")
def target5_all_quiet():
    return UndefinedKeyword


@pytest.fixture(scope="function")
def target6_all_quiet():
    return UndefinedKeyword


@pytest.fixture(scope="function")
def target7_all_quiet():
    return UndefinedKeyword


@pytest.fixture(scope="function")
def target8_all_quiet():
    return UndefinedKeyword


@pytest.fixture(scope="function")
def target9_all_quiet():
    return {
        "var1": "10",
        "var2": "Alexa",
        "var3": "Wikipedia",
        "all": "-all",
        "quiet": "-quiet",
        "list1": "10 20 30",
        "list2": "40 50 60",
    }


@pytest.fixture(scope="function")
def target10_all_quiet():
    return {
        "var1": "10",
        "var2": "Alexa",
        "var3": "Wikipedia",
        "all": "-all",
        "quiet": "-quiet",
        "list1": "10 20 30",
        "list2": "40 50 60",
    }


@pytest.fixture(scope="function")
def target11_all_quiet():
    return UndefinedKeyword


@pytest.fixture(scope="function")
def target12_all_quiet():
    return UndefinedKeyword


@pytest.fixture(scope="function")
def target13_all_quiet():
    return UndefinedKeyword


@pytest.mark.parametrize(
    "yaml_str, output, all_quiet_variant",
    [
        ("valid_yaml_target1_1", "target1_all_quiet", "quiet_all_var123"),
        ("valid_yaml_target2_1", "target2_all_quiet", "quiet_all_var123"),
        ("valid_yaml_target3_1", "target3_all_quiet", "quiet_all_var123"),
        ("valid_yaml_target4_1", "target4_all_quiet", "quiet_all_var123"),
        ("valid_yaml_target5_1", "target5_all_quiet", "quiet_all_var123"),
        ("valid_yaml_target6_1", "target6_all_quiet", "quiet_all_var123"),
        ("valid_yaml_target7_1", "target7_all_quiet", "quiet_all_var123"),
        ("valid_yaml_target8_1", "target8_all_quiet", "quiet_all_var123"),
        ("valid_yaml_target9_1", "target9_all_quiet", "quiet_all_var123"),
        ("valid_yaml_target10_1", "target10_all_quiet", "quiet_all_var123"),
        ("valid_yaml_target11_1", "target11_all_quiet", "quiet_all_var123"),
        ("valid_yaml_target12_1", "target12_all_quiet", "quiet_all_var123"),
        ("valid_yaml_target13_1", "target13_all_quiet", "quiet_all_var123"),
        ("valid_yaml_target1_1", "target1_all_quiet", "quiet_all_var132"),
        ("valid_yaml_target2_1", "target2_all_quiet", "quiet_all_var132"),
        ("valid_yaml_target3_1", "target3_all_quiet", "quiet_all_var132"),
        ("valid_yaml_target4_1", "target4_all_quiet", "quiet_all_var132"),
        ("valid_yaml_target5_1", "target5_all_quiet", "quiet_all_var132"),
        ("valid_yaml_target6_1", "target6_all_quiet", "quiet_all_var132"),
        ("valid_yaml_target7_1", "target7_all_quiet", "quiet_all_var132"),
        ("valid_yaml_target8_1", "target8_all_quiet", "quiet_all_var132"),
        ("valid_yaml_target9_1", "target9_all_quiet", "quiet_all_var132"),
        ("valid_yaml_target10_1", "target10_all_quiet", "quiet_all_var132"),
        ("valid_yaml_target11_1", "target11_all_quiet", "quiet_all_var132"),
        ("valid_yaml_target12_1", "target12_all_quiet", "quiet_all_var132"),
        ("valid_yaml_target13_1", "target13_all_quiet", "quiet_all_var132"),
        ("valid_yaml_target1_1", "target1_all_quiet", "quiet_all_var321"),
        ("valid_yaml_target2_1", "target2_all_quiet", "quiet_all_var321"),
        ("valid_yaml_target3_1", "target3_all_quiet", "quiet_all_var321"),
        ("valid_yaml_target4_1", "target4_all_quiet", "quiet_all_var321"),
        ("valid_yaml_target5_1", "target5_all_quiet", "quiet_all_var321"),
        ("valid_yaml_target6_1", "target6_all_quiet", "quiet_all_var321"),
        ("valid_yaml_target7_1", "target7_all_quiet", "quiet_all_var321"),
        ("valid_yaml_target8_1", "target8_all_quiet", "quiet_all_var321"),
        ("valid_yaml_target9_1", "target9_all_quiet", "quiet_all_var321"),
        ("valid_yaml_target10_1", "target10_all_quiet", "quiet_all_var321"),
        ("valid_yaml_target11_1", "target11_all_quiet", "quiet_all_var321"),
        ("valid_yaml_target12_1", "target12_all_quiet", "quiet_all_var321"),
        ("valid_yaml_target13_1", "target13_all_quiet", "quiet_all_var321"),
        ("valid_yaml_target1_1", "target1_all_quiet", "quiet_all_var_list1_321_list2"),
        ("valid_yaml_target2_1", "target2_all_quiet", "quiet_all_var_list1_321_list2"),
        ("valid_yaml_target3_1", "target3_all_quiet", "quiet_all_var_list1_321_list2"),
        ("valid_yaml_target4_1", "target4_all_quiet", "quiet_all_var_list1_321_list2"),
        ("valid_yaml_target5_1", "target5_all_quiet", "quiet_all_var_list1_321_list2"),
        ("valid_yaml_target6_1", "target6_all_quiet", "quiet_all_var_list1_321_list2"),
        ("valid_yaml_target7_1", "target7_all_quiet", "quiet_all_var_list1_321_list2"),
        ("valid_yaml_target8_1", "target8_all_quiet", "quiet_all_var_list1_321_list2"),
        ("valid_yaml_target9_1", "target9_all_quiet", "quiet_all_var_list1_321_list2"),
        (
            "valid_yaml_target10_1",
            "target10_all_quiet",
            "quiet_all_var_list1_321_list2",
        ),
        (
            "valid_yaml_target11_1",
            "target11_all_quiet",
            "quiet_all_var_list1_321_list2",
        ),
        (
            "valid_yaml_target12_1",
            "target12_all_quiet",
            "quiet_all_var_list1_321_list2",
        ),
        (
            "valid_yaml_target13_1",
            "target13_all_quiet",
            "quiet_all_var_list1_321_list2",
        ),
    ],
)
def test_all_quiet(yaml_str, output, all_quiet_variant, request):
    yaml_str = request.getfixturevalue(yaml_str)
    all_quiet_variant = request.getfixturevalue(all_quiet_variant)
    data = yaml.safe_load(yaml_str)["target"]
    context = Builder(data=data)
    context.build()
    parser = Parser(context=context)
    output = request.getfixturevalue(output)
    if isinstance(output, dict):
        parser.parse(all_quiet_variant.split())
        assert parser.namespace == output
    else:
        with pytest.raises(output):
            parser.parse(all_quiet_variant.split())
