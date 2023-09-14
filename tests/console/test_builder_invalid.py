import pytest
import yaml

from PyMake.console.builder.builder import Builder
from PyMake.exceptions import PyMakeFormatError, UnrecognisedVarKeyword


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

# Invalid Option Var

# Invalid Sequence Var

# Invalid Env

# Invalid CMD

# Redefined var

# Undefined Var


# Run test cases
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
