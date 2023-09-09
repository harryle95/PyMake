import pytest
import yaml
from pydantic_core import ValidationError

from PyMake.builder.var.section import VarSection


@pytest.fixture(scope="function")
def valid_yaml_1():
    raw = """
    basic:
        var1: 10
        var2: 100
        var3: 1000
    flag:
        flag1: '-l'
        flag2: '-a'
    sequence:
        seq1: [1,2,3]
        seq2: [4,5,6]
    """
    variables = {
        "var1": "basic",
        "var2": "basic",
        "var3": "basic",
        "flag1": "flag",
        "flag2": "flag",
        "seq1": "sequence",
        "seq2": "sequence"
    }
    defaults = {
        "var1": 10,
        "var2": 100,
        "var3": 1000,
        "flag1": '-l',
        "flag2": '-a',
        "seq1": [1, 2, 3],
        "seq2": [4, 5, 6]
    }
    positional = {
        0: "var1",
        1: "var2",
        2: "var3"
    }
    required = []
    return {"raw": raw, "variables": variables, "defaults": defaults, "positional": positional, "required": required}


@pytest.fixture(scope="function")
def valid_yaml_2():
    raw = """
    basic:
        var1: REQUIRED
        var2: 100
        var3: REQUIRED
    flag:
        flag1: '-l'
        flag2: '-a'
    sequence:
        seq1: [1,2,3]
        seq2: REQUIRED
    """
    variables = {
        "var1": "basic",
        "var2": "basic",
        "var3": "basic",
        "flag1": "flag",
        "flag2": "flag",
        "seq1": "sequence",
        "seq2": "sequence"
    }
    defaults = {
        "var2": 100,
        "flag1": '-l',
        "flag2": '-a',
        "seq1": [1, 2, 3],
    }
    positional = {
        0: "var1",
        1: "var2",
        2: "var3"
    }
    required = ['var1', 'var3', 'seq2']
    return {"raw": raw, "variables": variables, "defaults": defaults, "positional": positional, "required": required}


@pytest.fixture(scope="function")
def valid_yaml_3():
    raw = """
    basic:
        - var1
        - var2
        - var3
    flag:
        flag1: '-l'
        flag2: '-a'
    sequence:
        - seq1 
        - seq2
    """
    variables = {
        "var1": "basic",
        "var2": "basic",
        "var3": "basic",
        "flag1": "flag",
        "flag2": "flag",
        "seq1": "sequence",
        "seq2": "sequence"
    }
    defaults = {
        "flag1": '-l',
        "flag2": '-a',
    }
    positional = {
        0: "var1",
        1: "var2",
        2: "var3"
    }
    required = ['var1', 'var2', 'var3', 'seq1', 'seq2']
    return {"raw": raw, "variables": variables, "defaults": defaults, "positional": positional, "required": required}


@pytest.fixture(scope="function")
def valid_yaml_4():
    raw = """
    basic: var1
    flag:
        flag1: '-l'
        flag2: '-a'
    sequence: seq1
    """
    variables = {
        "var1": "basic",
        "flag1": "flag",
        "flag2": "flag",
        "seq1": "sequence",
    }
    defaults = {
        "flag1": '-l',
        "flag2": '-a',
    }
    positional = {
        0: "var1",
    }
    required = ['var1', 'seq1']
    return {"raw": raw, "variables": variables, "defaults": defaults, "positional": positional, "required": required}


@pytest.fixture(scope="function")
def valid_yaml_5():
    raw = """
    sequence: seq1
    basic: var1
    flag:
        flag1: '-l'
        flag2: '-a'
    
    """
    variables = {
        "var1": "basic",
        "flag1": "flag",
        "flag2": "flag",
        "seq1": "sequence",
    }
    defaults = {
        "flag1": '-l',
        "flag2": '-a',
    }
    positional = {
        0: "var1",
    }
    required = ['var1', 'seq1']
    return {"raw": raw, "variables": variables, "defaults": defaults, "positional": positional, "required": required}


@pytest.fixture(scope="function")
def valid_yaml_6():
    raw = """
    sequence: seq1
    basic: var1
    """
    variables = {
        "var1": "basic",
        "seq1": "sequence",
    }
    defaults = {
    }
    positional = {
        0: "var1",
    }
    required = ['var1', 'seq1']
    return {"raw": raw, "variables": variables, "defaults": defaults, "positional": positional, "required": required}


@pytest.fixture(scope="function")
def valid_yaml_7():
    raw = """
    basic: var1
    """
    variables = {
        "var1": "basic",
    }
    defaults = {
    }
    positional = {
        0: "var1",
    }
    required = ['var1']
    return {"raw": raw, "variables": variables, "defaults": defaults, "positional": positional, "required": required}


@pytest.fixture(scope="function")
def valid_yaml_8():
    raw = """
    sequence: seq1
    """
    variables = {
        "seq1": "sequence",
    }
    defaults = {
    }
    positional = {
    }
    required = ['seq1']
    return {"raw": raw, "variables": variables, "defaults": defaults, "positional": positional, "required": required}


@pytest.fixture(scope="function")
def valid_yaml_9():
    raw = """
    flag: 
        var1: "-l"
    """
    variables = {
        "var1": "flag",
    }
    defaults = {
        "var1": "-l"
    }
    positional = {
    }
    required = []
    return {"raw": raw, "variables": variables, "defaults": defaults, "positional": positional, "required": required}


@pytest.fixture(scope="function")
def valid_yaml_10():
    raw = """
    sequence: 
        seq1: [1,2,3]
    """
    variables = {
        "seq1": "sequence",
    }
    defaults = {
        "seq1": [1, 2, 3]
    }
    positional = {
    }
    required = []
    return {"raw": raw, "variables": variables, "defaults": defaults, "positional": positional, "required": required}


@pytest.fixture(scope="function")
def valid_yaml_11():
    raw = """
    basic: 
        var1: 1
        var2: 10
    """
    variables = {
        "var1": "basic",
        "var2": "basic"
    }
    defaults = {
        "var1": 1,
        "var2": 10
    }
    positional = {
        0: "var1",
        1: "var2"
    }
    required = []
    return {"raw": raw, "variables": variables, "defaults": defaults, "positional": positional, "required": required}


@pytest.fixture(scope="function")
def valid_yaml_12():
    raw = """
    basic:
    """
    variables = {
    }
    defaults = {
    }
    positional = {
    }
    required = []
    return {"raw": raw, "variables": variables, "defaults": defaults, "positional": positional, "required": required}


@pytest.fixture(scope="function")
def valid_yaml_13():
    raw = """
    flag:
    """
    variables = {
    }
    defaults = {
    }
    positional = {
    }
    required = []
    return {"raw": raw, "variables": variables, "defaults": defaults, "positional": positional, "required": required}


@pytest.fixture(scope="function")
def valid_yaml_14():
    raw = """
    sequence:
    """
    variables = {
    }
    defaults = {
    }
    positional = {
    }
    required = []
    return {"raw": raw, "variables": variables, "defaults": defaults, "positional": positional, "required": required}


@pytest.fixture(scope="function")
def valid_yaml_15():
    raw = """
    flag:
    basic:
    sequence:
    """
    variables = {
    }
    defaults = {
    }
    positional = {
    }
    required = []
    return {"raw": raw, "variables": variables, "defaults": defaults, "positional": positional, "required": required}


@pytest.fixture(scope="function")
def valid_yaml_16():
    raw = """
    """
    variables = {
    }
    defaults = {
    }
    positional = {
    }
    required = []
    return {"raw": raw, "variables": variables, "defaults": defaults, "positional": positional, "required": required}


@pytest.fixture(scope="function")
def invalid_validation_yaml_1():
    raw = """
    basic: 
        var1: [1, 2, 3]
    """
    return {"raw": raw}


@pytest.fixture(scope="function")
def invalid_validation_yaml_2():
    raw = """
    basic: 
        var1: {var2: 10}
    """
    return {"raw": raw}


@pytest.fixture(scope="function")
def invalid_validation_yaml_3():
    raw = """
    basic: 
        var1: 
            var2: 10
            var3: 100
    """
    return {"raw": raw}


@pytest.fixture(scope="function")
def invalid_validation_yaml_4():
    raw = """
    flag:
        var1
    """
    return {"raw": raw}


@pytest.fixture(scope="function")
def invalid_validation_yaml_5():
    raw = """
    sequence:
        var1: {var2: 100}
    """
    return {"raw": raw}


@pytest.fixture(scope="function")
def invalid_value_yaml_1():
    raw = """
    basic: 
        var1: 10
    flag: 
        var1: "-a"
    """
    return {"raw": raw}


@pytest.fixture(scope="function")
def invalid_value_yaml_2():
    raw = """
    basic: 
        var1: 10
    sequence:
        var1: [1,2,3]
    """
    return {"raw": raw}


@pytest.fixture(scope="function")
def invalid_value_yaml_3():
    raw = """
    flag: 
        var1: "-a"
    sequence:
        var1: [1,2,3]
    """
    return {"raw": raw}


@pytest.fixture(scope="function")
def invalid_value_yaml_4():
    raw = """
    option: 
        var1: "-a"
    sequence:
        seq1: [1,2,3]
    """
    return {"raw": raw}


@pytest.fixture(scope="function")
def invalid_value_yaml_5():
    raw = """
    base: 
        var1: "-a"
    sequence:
        seq1: [1,2,3]
    """
    return {"raw": raw}


@pytest.mark.parametrize(
    "test_suite", [
        "valid_yaml_1",
        "valid_yaml_2",
        "valid_yaml_3",
        "valid_yaml_4",
        "valid_yaml_5",
        "valid_yaml_6",
        "valid_yaml_7",
        "valid_yaml_8",
        "valid_yaml_9",
        "valid_yaml_10",
        "valid_yaml_11",
        "valid_yaml_12",
        "valid_yaml_13",
        "valid_yaml_14",
        "valid_yaml_15",
        "valid_yaml_16"
    ]
)
def test_valid_yaml(test_suite, request):
    test_dict = request.getfixturevalue(test_suite)
    vars = yaml.safe_load(test_dict['raw'])
    section = VarSection(vars)
    assert section.required == test_dict['required']
    assert section.variables == test_dict['variables']
    assert section.positional == test_dict['positional']
    assert section.default == test_dict['defaults']


@pytest.mark.parametrize(
    "test_suite", [
        "invalid_validation_yaml_1",
        "invalid_validation_yaml_2",
        "invalid_validation_yaml_3",
        "invalid_validation_yaml_4",
        "invalid_validation_yaml_5",
    ]
)
def test_invalid_validation_yaml(test_suite, request):
    test_dict = request.getfixturevalue(test_suite)
    vars = yaml.safe_load(test_dict['raw'])
    with pytest.raises(ValidationError):
        section = VarSection(vars)


@pytest.mark.parametrize(
    "test_suite", [
        "invalid_value_yaml_1",
        "invalid_value_yaml_2",
        "invalid_value_yaml_3",
        "invalid_value_yaml_4",
        "invalid_value_yaml_5"
    ]
)
def test_invalid_value_yaml(test_suite, request):
    test_dict = request.getfixturevalue(test_suite)
    vars = yaml.safe_load(test_dict['raw'])
    with pytest.raises(ValueError):
        section = VarSection(vars)
