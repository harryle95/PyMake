import pytest

from tests.console.conftest import (
    valid_yaml_target10_1,
    valid_yaml_target11_1,
    valid_yaml_target12_1,
    valid_yaml_target13_1,
    valid_yaml_target1_1,
    valid_yaml_target2_1,
    valid_yaml_target3_1,
    valid_yaml_target4_1,
    valid_yaml_target5_1,
    valid_yaml_target6_1,
    valid_yaml_target7_1,
    valid_yaml_target8_1,
    valid_yaml_target9_1,
)

__all__ = [
    "valid_yaml_target12_1",
    "valid_yaml_target13_1",
    "valid_yaml_target1_1",
    "valid_yaml_target2_1",
    "valid_yaml_target3_1",
    "valid_yaml_target7_1",
    "valid_yaml_target4_1",
    "valid_yaml_target5_1",
    "valid_yaml_target6_1",
    "valid_yaml_target8_1",
    "valid_yaml_target9_1",
    "valid_yaml_target10_1",
    "valid_yaml_target11_1",
]


# Valid Yaml Target1 Variants


@pytest.fixture(scope="function")
def valid_yaml_target1_2():
    return """
    target:
        env:
        cmd:
            python script1.py
    """


@pytest.fixture(scope="function")
def valid_yaml_target1_3():
    return """
    target:
        var:
        cmd:
            python script1.py
    """


@pytest.fixture(scope="function")
def valid_yaml_target1_4():
    return """
    target:
        cmd:
            python script1.py
        var:
            basic:
    """


@pytest.fixture(scope="function")
def valid_yaml_target1_5():
    return """
    target:
        cmd:
            python script1.py
        var:
            option:
    """


@pytest.fixture(scope="function")
def valid_yaml_target1_6():
    return """
    target:
        cmd:
            python script1.py
        var:
            option:
            basic:
    """


@pytest.fixture(scope="function")
def valid_yaml_target1_7():
    return """
    target:
        cmd:
            python script1.py
        var:
            option:
            sequence:
            basic:
    """


@pytest.fixture(scope="function")
def valid_yaml_target1_8():
    return """
    target:
        cmd:
            python script1.py
        var:
            option:
            sequence:
            basic:
        env:
    """


@pytest.fixture(scope="function")
def valid_yaml_target1_9():
    return """
    target:
        cmd:
            python script1.py
        env:
        var:
            option:
            sequence:
            basic:

    """


@pytest.fixture(scope="function")
def valid_yaml_target1_10():
    return """
    target:
        env:
        cmd:
            python script1.py
        var:
            option:
            sequence:
            basic:

    """


@pytest.fixture(scope="function")
def valid_yaml_target1_11():
    return """
    target:
        cmd: python script1.py
    """


@pytest.fixture(scope="function")
def output_yaml_target1_1_11():
    return {
        "vars": [],
        "positional": [],
        "default": {},
        "required": [],
        "flag": {},
        "commands": ["python script1.py"],
        "envs": {},
    }


## Valid YAML Target 2 variants


@pytest.fixture(scope="function")
def valid_yaml_target2_2():
    return """
    target:
        var:
            basic:
                - var1
                - var2
                - var3
                - var4
        cmd:
            python script1.py
    """


@pytest.fixture(scope="function")
def valid_yaml_target2_3():
    return """
    target:
        var:
            basic:
                var1: null
                var2: null
                var3: null
                var4: null
        cmd:
            python script1.py
    """


@pytest.fixture(scope="function")
def output_yaml_target2_1_3():
    return {
        "vars": ["var1", "var2", "var3", "var4"],
        "positional": ["var1", "var2", "var3", "var4"],
        "default": {},
        "required": ["var1", "var2", "var3", "var4"],
        "flag": {},
        "commands": ["python script1.py"],
        "envs": {},
    }


## Valid Yaml Target 3


@pytest.fixture(scope="function")
def output_yaml_target3_1():
    return {
        "vars": ["var1"],
        "positional": ["var1"],
        "default": {},
        "required": ["var1"],
        "flag": {},
        "commands": ["python script1.py"],
        "envs": {},
    }


# Valid Yaml Target 4


@pytest.fixture(scope="function")
def output_yaml_target4_1():
    return {
        "vars": ["all"],
        "positional": [],
        "default": {},
        "required": [],
        "flag": {"all": "-a"},
        "commands": ["python script1.py"],
        "envs": {},
    }


# Valid Yaml Target 5


@pytest.fixture(scope="function")
def valid_yaml_target5_2():
    return """
    target:
        var:
            sequence:
                list1: null
        cmd:
            python script1.py
    """


@pytest.fixture(scope="function")
def output_yaml_target5_1_2():
    return {
        "vars": ["list1"],
        "positional": [],
        "default": {},
        "required": ["list1"],
        "flag": {},
        "commands": ["python script1.py"],
        "envs": {},
    }


# Valid Yaml Target 6


@pytest.fixture(scope="function")
def output_yaml_target6_1():
    return {
        "vars": ["list1"],
        "positional": [],
        "default": {"list1": "1 2 3"},
        "required": [],
        "flag": {},
        "commands": ["python script1.py"],
        "envs": {},
    }


# Valid YAML Target 7


@pytest.fixture(scope="function")
def output_yaml_target7_1():
    return {
        "vars": ["var1", "var2", "var3", "list1"],
        "positional": ["var1", "var2", "var3"],
        "default": {"var1": "1", "var2": "2", "list1": "1 2 3"},
        "required": ["var3"],
        "flag": {},
        "commands": ["python script1.py"],
        "envs": {},
    }


# Valid YAML Target 8


@pytest.fixture(scope="function")
def valid_yaml_target8_2():
    return """
    target:
        var:
            basic:
                var1:
                var2: 2
                var3:
            sequence:
                list1: null
        cmd:
            python script1.py
    """


@pytest.fixture(scope="function")
def valid_yaml_target8_3():
    return """
    target:
        var:
            basic:
                var1:
                var2: 2
                var3:
            sequence:
                list1:
        cmd:
            python script1.py
    """


@pytest.fixture(scope="function")
def output_yaml_target8_1_3():
    return {
        "vars": ["var1", "var2", "var3", "list1"],
        "positional": ["var1", "var2", "var3"],
        "default": {"var2": "2"},
        "required": ["var1", "var3", "list1"],
        "flag": {},
        "commands": ["python script1.py"],
        "envs": {},
    }


# Valid Yaml Target 9


@pytest.fixture(scope="function")
def valid_yaml_target9_2():
    return """
    target:
        var:
            basic:
                var1: null
                var2: 2
                var3: null
            option:
                all: "-all"
                quiet: "-quiet"
            sequence:
                - list1
                - list2
        cmd:
            python script1.py
    """


@pytest.fixture(scope="function")
def valid_yaml_target9_3():
    return """
    target:
        var:
            basic:
                var1:
                var2: 2
                var3:
            option:
                all: "-all"
                quiet: "-quiet"
            sequence:
                - list1
                - list2
        cmd:
            python script1.py
    """


@pytest.fixture(scope="function")
def valid_yaml_target9_4():
    return """
    target:
        var:
            basic:
                var1: null
                var2: 2
                var3:
            option:
                all: "-all"
                quiet: "-quiet"
            sequence:
                list1: null
                list2: null
        cmd:
            python script1.py
    """


@pytest.fixture(scope="function")
def valid_yaml_target9_5():
    return """
    target:
        var:
            sequence:
                list1: null
                list2: null
            basic:
                var1:
                var2: 2
                var3:
            option:
                all: "-all"
                quiet: "-quiet"

        cmd:
            python script1.py
    """


@pytest.fixture(scope="function")
def valid_yaml_target9_6():
    return """
    target:
        var:
            option:
                all: "-all"
                quiet: "-quiet"
            sequence:
                list1: null
                list2: null
            basic:
                var1:
                var2: 2
                var3:
        cmd:
            python script1.py
    """


@pytest.fixture(scope="function")
def valid_yaml_target9_7():
    return """
    target:
        var:
            option:
                all: "-all"
                quiet: "-quiet"
            basic:
                var1:
                var2: 2
                var3:
            sequence:
                list1: null
                list2: null

        cmd:
            python script1.py
    """


@pytest.fixture(scope="function")
def valid_yaml_target9_8():
    return """
    target:
        var:
            sequence:
                list1: null
                list2: null
            option:
                all: "-all"
                quiet: "-quiet"
            basic:
                var1:
                var2: 2
                var3:
        cmd:
            python script1.py
    """


@pytest.fixture(scope="function")
def valid_yaml_target9_9():
    return """
    target:
        var:
            basic:
                var1: null
                var2: 2
                var3: null
            sequence:
                list1: null
                list2: null
            option:
                all: "-all"
                quiet: "-quiet"
        cmd:
            python script1.py
    """


@pytest.fixture(scope="function")
def output_yaml_target9_1_9():
    return {
        "vars": ["var1", "var2", "var3", "list1", "list2", "all", "quiet"],
        "positional": ["var1", "var2", "var3"],
        "default": {"var2": "2"},
        "required": ["var1", "var3", "list1", "list2"],
        "flag": {"all": "-all", "quiet": "-quiet"},
        "commands": ["python script1.py"],
        "envs": {},
    }


# Valid YAML Target 10


@pytest.fixture(scope="function")
def valid_yaml_target10_2():
    return """
    target:
        var:
            basic:
                var1: 10
                var2: 2
                var3: 14
            option:
                all: "-all"
                quiet: "-quiet"
            sequence:
                list1: null
                list2: null
        cmd:
            - python script1.py
            - python script2.py
        env:
            env1: $(var1)
            env2: $(var2)
    """


@pytest.fixture(scope="function")
def valid_yaml_target10_3():
    return """
    target:
        cmd:
            - python script1.py
            - python script2.py
        env:
            env1: $(var1)
            env2: $(var2)
        var:
            basic:
                var1: 10
                var2: 2
                var3: 14
            option:
                all: "-all"
                quiet: "-quiet"
            sequence:
                list1: null
                list2: null
    """


@pytest.fixture(scope="function")
def valid_yaml_target10_4():
    return """
    target:
        cmd:
            - python script1.py
            - python script2.py
        var:
            basic:
                var1: 10
                var2: 2
                var3: 14
            option:
                all: "-all"
                quiet: "-quiet"
            sequence:
                list1: null
                list2: null
        env:
            env1: $(var1)
            env2: $(var2)
    """


@pytest.fixture(scope="function")
def valid_yaml_target10_5():
    return """
    target:
        env:
            env1: $(var1)
            env2: $(var2)
        cmd:
            - python script1.py
            - python script2.py
        var:
            basic:
                var1: 10
                var2: 2
                var3: 14
            option:
                all: "-all"
                quiet: "-quiet"
            sequence:
                list1: null
                list2: null
    """


@pytest.fixture(scope="function")
def valid_yaml_target10_6():
    return """
    target:
        env:
            env1: $(var1)
            env2: $(var2)
        var:
            basic:
                var1: 10
                var2: 2
                var3: 14
            option:
                all: "-all"
                quiet: "-quiet"
            sequence:
                list1: null
                list2: null
        cmd:
            - python script1.py
            - python script2.py
    """


@pytest.fixture(scope="function")
def output_yaml_target10_1_6():
    return {
        "vars": ["var2", "quiet", "var3", "all", "list1", "list2", "var1"],
        "positional": ["var1", "var2", "var3"],
        "default": {"var1": "10", "var2": "2", "var3": "14"},
        "required": ["list1", "list2"],
        "flag": {"all": "-all", "quiet": "-quiet"},
        "commands": ["python script1.py", "python script2.py"],
        "envs": {"env1": "$(var1)", "env2": "$(var2)"},
    }


# Valid Yaml Target 11


@pytest.fixture(scope="function")
def output_yaml_target11_1():
    return {
        "vars": ["var1", "list1"],
        "positional": ["var1"],
        "default": {},
        "required": ["var1", "list1"],
        "flag": {},
        "commands": ["python script1.py", "python script2.py"],
        "envs": {},
    }


# Valid YAML Target 12


@pytest.fixture(scope="function")
def output_yaml_target12_1():
    return {
        "vars": ["var1", "var2", "var3", "list1", "list2", "all"],
        "positional": ["var1", "var2", "var3"],
        "default": {
            "var1": "1",
            "var2": "2",
            "var3": "3",
            "list1": "1 2 3",
            "list2": "4 5 6",
        },
        "required": [],
        "flag": {"all": "-a"},
        "commands": [
            "ls $(all)",
            "python script1.py $(list1)",
            "python script2.py --var3 $(var3) $(list2)",
        ],
        "envs": {"ENV1": "$(var1)", "ENV2": "$(var2)"},
    }


# Valid YAML Target 13


@pytest.fixture(scope="function")
def output_yaml_target13_1():
    return {
        "vars": ["list1", "list2", "list3"],
        "positional": [],
        "default": {
            "list1": "1",
            "list2": "1 2 3",
        },
        "required": ["list3"],
        "flag": {},
        "commands": ["echo Hello"],
        "envs": {},
    }
