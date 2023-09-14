import pytest
import yaml

from PyMake.console.builder.builder import Builder


@pytest.mark.parametrize(
    "str_input, target",
    [
        ("valid_yaml_target1_1", "output_yaml_target1_1_11"),
        ("valid_yaml_target1_2", "output_yaml_target1_1_11"),
        ("valid_yaml_target1_3", "output_yaml_target1_1_11"),
        ("valid_yaml_target1_4", "output_yaml_target1_1_11"),
        ("valid_yaml_target1_5", "output_yaml_target1_1_11"),
        ("valid_yaml_target1_6", "output_yaml_target1_1_11"),
        ("valid_yaml_target1_7", "output_yaml_target1_1_11"),
        ("valid_yaml_target1_8", "output_yaml_target1_1_11"),
        ("valid_yaml_target1_9", "output_yaml_target1_1_11"),
        ("valid_yaml_target1_10", "output_yaml_target1_1_11"),
        ("valid_yaml_target1_11", "output_yaml_target1_1_11"),
        ("valid_yaml_target2_1", "output_yaml_target2_1_3"),
        ("valid_yaml_target2_2", "output_yaml_target2_1_3"),
        ("valid_yaml_target2_3", "output_yaml_target2_1_3"),
        ("valid_yaml_target3_1", "output_yaml_target3_1"),
        ("valid_yaml_target4_1", "output_yaml_target4_1"),
        ("valid_yaml_target5_1", "output_yaml_target5_1_2"),
        ("valid_yaml_target5_2", "output_yaml_target5_1_2"),
        ("valid_yaml_target6_1", "output_yaml_target6_1"),
        ("valid_yaml_target7_1", "output_yaml_target7_1"),
        ("valid_yaml_target8_1", "output_yaml_target8_1_3"),
        ("valid_yaml_target8_2", "output_yaml_target8_1_3"),
        ("valid_yaml_target8_3", "output_yaml_target8_1_3"),
        ("valid_yaml_target9_1", "output_yaml_target9_1_9"),
        ("valid_yaml_target9_2", "output_yaml_target9_1_9"),
        ("valid_yaml_target9_3", "output_yaml_target9_1_9"),
        ("valid_yaml_target9_4", "output_yaml_target9_1_9"),
        ("valid_yaml_target9_5", "output_yaml_target9_1_9"),
        ("valid_yaml_target9_6", "output_yaml_target9_1_9"),
        ("valid_yaml_target9_7", "output_yaml_target9_1_9"),
        ("valid_yaml_target9_8", "output_yaml_target9_1_9"),
        ("valid_yaml_target9_9", "output_yaml_target9_1_9"),
        ("valid_yaml_target10_1", "output_yaml_target10_1_6"),
        ("valid_yaml_target10_2", "output_yaml_target10_1_6"),
        ("valid_yaml_target10_3", "output_yaml_target10_1_6"),
        ("valid_yaml_target10_4", "output_yaml_target10_1_6"),
        ("valid_yaml_target10_5", "output_yaml_target10_1_6"),
        ("valid_yaml_target10_6", "output_yaml_target10_1_6"),
        ("valid_yaml_target11_1", "output_yaml_target11_1"),
        ("valid_yaml_target12_1", "output_yaml_target12_1"),
        ("valid_yaml_target13_1", "output_yaml_target13_1"),
    ],
)
def test_valid_build(str_input, target, request):
    str_input = request.getfixturevalue(str_input)
    target = request.getfixturevalue(target)
    str_input = yaml.safe_load(str_input)["target"]
    model = Builder(data=str_input)
    model.build()
    assert set(model.vars) == set(target["vars"])
    assert set(model.required) == set(target["required"])
    assert model.default == target["default"]
    assert model.flag == target["flag"]
    assert model.envs == target["envs"]
