import pytest
import yaml

from PyMake.console.builder.builder import Builder
from PyMake.exceptions import (
    InvalidBasicVarType,
    InvalidCmdType,
    InvalidEnvType,
    InvalidOptionVarType,
    InvalidSequenceVarType,
    PyMakeFormatError,
    RedefinedVariable,
    UnrecognisedVarKeyword,
)


# PyMake Format
@pytest.fixture(scope="function")
def pymake_format_yaml1():
    return """
    target:
        CMD:
            echo Hello
    """


@pytest.fixture(scope="function")
def pymake_format_yaml2():
    return """
    target:
        VAR:    
            basic: var1
        cmd:
            echo Hello
    """


@pytest.fixture(scope="function")
def pymake_format_yaml3():
    return """
    target:
        vars:    
            basic: var1
        cmd:
            echo Hello
    """


@pytest.fixture(scope="function")
def pymake_format_yaml4():
    return """
    target:
        envs:    
            basic: var1
        cmd:
            echo Hello
    """


@pytest.fixture(scope="function")
def pymake_format_yaml5():
    return """
    target:
        Env:    
            basic: var1
        cmd:
            echo Hello
    """


# Unrecognised Var
@pytest.fixture(scope="function")
def unrecognised_var_yaml1():
    return """
    target:
        var:
            Basic:
        cmd:
            echo Hello
    """


@pytest.fixture(scope="function")
def unrecognised_var_yaml2():
    return """
    target:
        var:
            env: 100
        cmd:
            echo Hello
    """


@pytest.fixture(scope="function")
def unrecognised_var_yaml3():
    return """
    target:
        var:
            flag:
                all: "-a"
        cmd:
            echo Hello
    """


@pytest.fixture(scope="function")
def unrecognised_var_yaml4():
    return """
    target:
        var:
            element: 10
        cmd:
            echo Hello
    """


@pytest.fixture(scope="function")
def unrecognised_var_yaml5():
    return """
    target:
        var:
            - var1
            - var2
        cmd:
            echo Hello
    """


# Invalid Basic Var
@pytest.fixture(scope="function")
def invalid_basic_yaml1():
    return """
    target:
        var:
            basic:
                var1: [1, 2, 3]
        cmd:
            echo Hello
    """


@pytest.fixture(scope="function")
def invalid_basic_yaml2():
    return """
    target:
        var:
            basic:
                var1: 
                    age: 10
                    name: X
        cmd:
            echo Hello
    """


# Invalid Option Var
@pytest.fixture(scope="function")
def invalid_option_yaml1():
    return """
    target:
        var:
            option:
                var1: [1, 2, 3]
        cmd:
            echo Hello
    """


@pytest.fixture(scope="function")
def invalid_option_yaml2():
    return """
    target:
        var:
            option:
                var1: null
        cmd:
            echo Hello
    """


@pytest.fixture(scope="function")
def invalid_option_yaml3():
    return """
    target:
        var:
            option:
                var1: 100
        cmd:
            echo Hello
    """


@pytest.fixture(scope="function")
def invalid_option_yaml4():
    return """
    target:
        var:
            option:
                var1: 
                    value: 10
                    cost: 100
        cmd:
            echo Hello
    """


@pytest.fixture(scope="function")
def invalid_option_yaml5():
    return """
    target:
        var:
            option: var1
        cmd:
            echo Hello
    """


@pytest.fixture(scope="function")
def invalid_option_yaml6():
    return """
    target:
        var:
            option: 
                - var1
                - var2
                - var3
        cmd:
            echo Hello
    """


@pytest.fixture(scope="function")
def invalid_option_yaml7():
    return """
    target:
        var:
            option: 100
        cmd:
            echo Hello
    """


@pytest.fixture(scope="function")
def invalid_option_yaml8():
    return """
    target:
        var:
            option: True
        cmd:
            echo Hello
    """


# Invalid Sequence Var
@pytest.fixture(scope="function")
def invalid_sequence_yaml1():
    return """
    target:
        var:
            sequence:
                var1: 
                    var2: 10
        cmd:
            echo Hello
    """


# Invalid Env
@pytest.fixture(scope="function")
def invalid_env_yaml1():
    return """
    target:
        env: 10
        cmd:
            echo Hello
    """


@pytest.fixture(scope="function")
def invalid_env_yaml2():
    return """
    target:
        env: var1
        cmd:
            echo Hello
    """


@pytest.fixture(scope="function")
def invalid_env_yaml3():
    return """
    target:
        env: 
            - var1
            - var2
            - var3
        cmd:
            echo Hello
    """


@pytest.fixture(scope="function")
def invalid_env_yaml4():
    return """
    target:
        env: 
            var1: [1, 2, 3]
        cmd:
            echo Hello
    """


@pytest.fixture(scope="function")
def invalid_env_yaml5():
    return """
    target:
        env: 
            var1: 
                var2: var3
        cmd:
            echo Hello
    """


# Invalid CMD
@pytest.fixture(scope="function")
def invalid_cmd_yaml1():
    return """
    target:
        cmd:
    """


@pytest.fixture(scope="function")
def invalid_cmd_yaml2():
    return """
    target:
        cmd: null
    """


@pytest.fixture(scope="function")
def invalid_cmd_yaml3():
    return """
    target:
        cmd: 
            cmd1: asd
            cmd2: asd
    """


# Redefined var
@pytest.fixture(scope="function")
def redefined_var_yaml1():
    return """
    target:
        var:
            basic:
                var1: 10
            option:
                var1: "-a"
        cmd: 
            echo Helo
    """


@pytest.fixture(scope="function")
def redefined_var_yaml2():
    return """
    target:
        var:
            basic:
                var1: 10
            sequence:
                var1: "-a"
        cmd: 
            echo Helo
    """


@pytest.fixture(scope="function")
def redefined_var_yaml3():
    return """
    target:
        var:
            option:
                var1: -b
            sequence:
                var1: "-a"
        cmd: 
            echo Helo
    """


# Undefined Var


# Run test cases
@pytest.mark.parametrize(
    "invalid_input",
    [
        "pymake_format_yaml1",
        "pymake_format_yaml2",
        "pymake_format_yaml3",
        "pymake_format_yaml4",
        "pymake_format_yaml5",
    ],
)
def test_pymake_format(invalid_input, request):
    invalid_input = request.getfixturevalue(invalid_input)
    invalid_input = yaml.safe_load(invalid_input)["target"]
    with pytest.raises(PyMakeFormatError):
        model = Builder(data=invalid_input)
        model.build()


@pytest.mark.parametrize(
    "invalid_input",
    [
        "unrecognised_var_yaml1",
        "unrecognised_var_yaml2",
        "unrecognised_var_yaml3",
        "unrecognised_var_yaml4",
        "unrecognised_var_yaml5",
    ],
)
def test_unrecognised_var(invalid_input, request):
    invalid_input = request.getfixturevalue(invalid_input)
    invalid_input = yaml.safe_load(invalid_input)["target"]
    with pytest.raises(UnrecognisedVarKeyword):
        model = Builder(data=invalid_input)
        model.build()


@pytest.mark.parametrize(
    "invalid_input",
    [
        "invalid_basic_yaml1",
        "invalid_basic_yaml2",
    ],
)
def test_invalid_basic(invalid_input, request):
    invalid_input = request.getfixturevalue(invalid_input)
    invalid_input = yaml.safe_load(invalid_input)["target"]
    with pytest.raises(InvalidBasicVarType):
        model = Builder(data=invalid_input)
        model.build()


@pytest.mark.parametrize(
    "invalid_input",
    [
        "invalid_option_yaml1",
        "invalid_option_yaml2",
        "invalid_option_yaml3",
        "invalid_option_yaml4",
        "invalid_option_yaml5",
        "invalid_option_yaml6",
        "invalid_option_yaml7",
        "invalid_option_yaml8",
    ],
)
def test_invalid_option(invalid_input, request):
    invalid_input = request.getfixturevalue(invalid_input)
    invalid_input = yaml.safe_load(invalid_input)["target"]
    with pytest.raises(InvalidOptionVarType):
        model = Builder(data=invalid_input)
        model.build()


@pytest.mark.parametrize(
    "invalid_input",
    [
        "invalid_sequence_yaml1",
    ],
)
def test_invalid_sequence(invalid_input, request):
    invalid_input = request.getfixturevalue(invalid_input)
    invalid_input = yaml.safe_load(invalid_input)["target"]
    with pytest.raises(InvalidSequenceVarType):
        model = Builder(data=invalid_input)
        model.build()


@pytest.mark.parametrize(
    "invalid_input",
    [
        "invalid_env_yaml1",
        "invalid_env_yaml2",
        "invalid_env_yaml3",
        "invalid_env_yaml4",
        "invalid_env_yaml5",
    ],
)
def test_invalid_env(invalid_input, request):
    invalid_input = request.getfixturevalue(invalid_input)
    invalid_input = yaml.safe_load(invalid_input)["target"]
    with pytest.raises(InvalidEnvType):
        model = Builder(data=invalid_input)
        model.build()


@pytest.mark.parametrize(
    "invalid_input",
    [
        "invalid_cmd_yaml1",
        "invalid_cmd_yaml2",
        "invalid_cmd_yaml3",
    ],
)
def test_invalid_cmd(invalid_input, request):
    invalid_input = request.getfixturevalue(invalid_input)
    invalid_input = yaml.safe_load(invalid_input)["target"]
    with pytest.raises(InvalidCmdType):
        model = Builder(data=invalid_input)
        model.build()


@pytest.mark.parametrize(
    "invalid_input",
    [
        "redefined_var_yaml1",
        "redefined_var_yaml2",
        "redefined_var_yaml3",
    ],
)
def test_redefined_variable(invalid_input, request):
    invalid_input = request.getfixturevalue(invalid_input)
    invalid_input = yaml.safe_load(invalid_input)["target"]
    with pytest.raises(RedefinedVariable):
        model = Builder(data=invalid_input)
        model.build()
