import pytest
from pydantic_core import ValidationError

from PyMake.builder.block import BasicBlock, FlagBlock, SequenceBlock


@pytest.fixture(scope="function")
def valid_basic_str():
    return "var1"


@pytest.fixture(scope="function")
def valid_basic_str_output():
    return ["var1"], [None], [True], [0]


@pytest.fixture(scope="function")
def invalid_flag_str():
    return "var1"


@pytest.fixture(scope="function")
def valid_sequence_str():
    return "var1"


@pytest.fixture(scope="function")
def valid_sequence_str_output():
    return ["var1"], [None], [True]


@pytest.fixture(scope="function")
def valid_basic_list_1() -> list[str]:
    return ['var1', 'var2', 'var3', 'var4']


@pytest.fixture(scope="function")
def valid_basic_list_1_output():
    return ('var1', 'var2', 'var3', 'var4'), (None, None, None, None), (True, True, True, True), (0, 1, 2, 3)


@pytest.fixture(scope="function")
def valid_basic_dict_1():
    return {'var1': 1, 'var2': 2, 'var3': 3, 'var4': 4}


@pytest.fixture(scope="function")
def valid_basic_dict_1_output():
    return ('var1', 'var2', 'var3', 'var4'), (1, 2, 3, 4), (False, False, False, False), (0, 1, 2, 3)


@pytest.fixture(scope="function")
def valid_basic_dict_2():
    return {'var1': "REQUIRED", 'var2': 2, 'var3': 3, 'var4': 4}


@pytest.fixture(scope="function")
def valid_basic_dict_2_output():
    return ('var1', 'var2', 'var3', 'var4'), (None, 2, 3, 4), (True, False, False, False), (0, 1, 2, 3)


@pytest.fixture(scope="function")
def valid_basic_dict_3():
    return {'var1': 1, 'var2': 2, 'var3': "REQUIRED", 'var4': 4}


@pytest.fixture(scope="function")
def valid_basic_dict_3_output():
    return ('var1', 'var2', 'var3', 'var4'), (1, 2, None, 4), (False, False, True, False), (0, 1, 2, 3)


@pytest.fixture(scope="function")
def valid_basic_dict_4():
    return {'var1': '1', 'var2': '2', 'var3': "REQUIRED", 'var4': 'required'}


@pytest.fixture(scope="function")
def valid_basic_dict_4_output():
    return ('var1', 'var2', 'var3', 'var4'), ('1', '2', None, None), (False, False, True, True), (0, 1, 2, 3)


@pytest.fixture(scope="function")
def valid_basic_dict_5():
    return {'var1': '1.5', 'var2': 2.7, 'var3': "REQUIRED", 'var4': 'required'}


@pytest.fixture(scope="function")
def valid_basic_dict_5_output():
    return ('var1', 'var2', 'var3', 'var4'), ('1.5', 2.7, None, None), (False, False, True, True), (0, 1, 2, 3)


@pytest.fixture(scope="function")
def invalid_basic_list_1():
    return [1, 2, 'var3']


@pytest.fixture(scope="function")
def invalid_basic_list_2():
    return [{'var1': 1}, 'var2', 'var3']


@pytest.fixture(scope="function")
def invalid_basic_list_3():
    return [('var1', 1), 'var2', 'var3']


@pytest.fixture(scope="function")
def invalid_basic_list_4():
    return [{'var1': 1}, 'var2', 'var3']


@pytest.fixture(scope="function")
def invalid_basic_list_5():
    return [['var1', 'var2', 'var3', 'var4']]


@pytest.fixture(scope="function")
def invalid_flag_list_1() -> list[str]:
    return ['var1', 'var2', 'var3', 'var4']


@pytest.fixture(scope="function")
def valid_flag_dict_1():
    return {'all': "-a", 'recursive': "-R", 'size': "-s"}


@pytest.fixture(scope="function")
def valid_flag_dict_1_output():
    return ('all', 'recursive', 'size'), ('-a', '-R', '-s')


@pytest.fixture(scope="function")
def valid_sequence_dict_1():
    return {"var1": [1, 2, 3], "var2": [1.5, 2.3], "var3": ['a', 'b', 'c']}


@pytest.fixture(scope="function")
def valid_sequence_dict_1_output():
    return ["var1", "var2", "var3"], ([1, 2, 3], [1.5, 2.3], ['a', 'b', 'c']), (False, False, False)


@pytest.fixture(scope="function")
def valid_sequence_dict_2():
    return {"var1": "REQUIRED", "var2": [1.5, 2.3], "var3": ['a', 'b', 'c']}


@pytest.fixture(scope="function")
def valid_sequence_dict_2_output():
    return ["var1", "var2", "var3"], (None, [1.5, 2.3], ['a', 'b', 'c']), (True, False, False)


@pytest.fixture(scope="function")
def valid_sequence_dict_3():
    return {"var1": "REQUIRED", "var2": [1.5, 2.3], "var3": "REQUIRED"}


@pytest.fixture(scope="function")
def valid_sequence_dict_3_output():
    return ["var1", "var2", "var3"], (None, [1.5, 2.3], None), (True, False, True)


@pytest.fixture(scope="function")
def valid_sequence_dict_4():
    return {"var1": [1, 1.5, "3"], "var2": ["REQUIRED", 1.4, "2,5"]}


@pytest.fixture(scope="function")
def valid_sequence_dict_4_output():
    return ["var1"], ([1, 1.5, "3"], ['REQUIRED', 1.4, "2.5"]), (False, False)


@pytest.fixture(scope="function")
def valid_sequence_list_1():
    return ['var1', 'var2', 'var3']


@pytest.fixture(scope="function")
def valid_sequence_list_1_output():
    return ["var1", "var2", "var3"], (None, None, None), (True, True, True)


@pytest.fixture(scope="function")
def invalid_sequence_list_1():
    return [1, 2.5, True]


@pytest.fixture(scope="function")
def invalid_sequence_list_2():
    return [{"A": 1}, "B", "M"]


@pytest.fixture(scope="function")
def invalid_sequence_list_3():
    return [["A", "B"], "C", "M"]


@pytest.fixture(scope="function")
def invalid_sequence_list_4():
    return [("A", "B"), "C", "M"]


@pytest.fixture(scope="function")
def invalid_sequence_list_5():
    return [{"A", "B"}, "C", "M"]


@pytest.fixture(scope="function")
def invalid_sequence_dict_1():
    return {"A": [1, (1.5, 2), 3]}


@pytest.fixture(scope="function")
def invalid_sequence_dict_2():
    return {"A": [[1, 2, 3]]}


@pytest.fixture(scope="function")
def invalid_sequence_dict_3():
    return {"A": ((1, 2), 3)}


@pytest.fixture(scope="function")
def invalid_sequence_dict_4():
    return {"A": {1, (2, 3)}}


@pytest.fixture(scope="function")
def invalid_sequence_dict_5():
    return {"A": 2.5}


@pytest.fixture(scope="function")
def invalid_sequence_dict_6():
    return {"A": 1}


@pytest.fixture(scope="function")
def invalid_sequence_dict_7():
    return {"A": True}


@pytest.fixture(scope="function")
def invalid_sequence_dict_8():
    return {"A": "B"}


@pytest.fixture(scope="function")
def invalid_sequence_dict_9():
    return {"A": {"B": 1}}


@pytest.mark.parametrize(
    "input_arg, expected", [
        ('valid_basic_str', 'valid_basic_str_output'),
        ('valid_basic_list_1', 'valid_basic_list_1_output'),
        ('valid_basic_dict_1', 'valid_basic_dict_1_output'),
        ('valid_basic_dict_2', 'valid_basic_dict_2_output'),
        ('valid_basic_dict_3', 'valid_basic_dict_3_output'),
        ('valid_basic_dict_4', 'valid_basic_dict_4_output'),
        ('valid_basic_dict_5', 'valid_basic_dict_5_output'),
    ]
)
def test_valid_basic(input_arg, expected, request):
    arg = request.getfixturevalue(input_arg)
    names, defaults, optionals, positions = request.getfixturevalue(expected)
    block = BasicBlock(_data=arg)
    for i in range(len(names)):
        assert block.mapping[names[i]].default == defaults[i]
        assert block.mapping[names[i]].required == optionals[i]
        assert block.mapping[names[i]].position == positions[i]


@pytest.mark.parametrize(
    "input_arg", [
        "invalid_basic_list_1",
        "invalid_basic_list_2",
        "invalid_basic_list_3",
        "invalid_basic_list_4",
        "invalid_basic_list_5",
    ]
)
def test_invalid_basic(input_arg, request):
    arg = request.getfixturevalue(input_arg)
    with pytest.raises(ValidationError):
        BasicBlock(_data=arg)


@pytest.mark.parametrize(
    "input_arg, expected", [
        ('valid_flag_dict_1', 'valid_flag_dict_1_output')
    ]
)
def test_valid_flag(input_arg, expected, request):
    arg = request.getfixturevalue(input_arg)
    names, defaults = request.getfixturevalue(expected)
    block = FlagBlock(_data=arg)
    for i in range(len(names)):
        assert block.mapping[names[i]].default == defaults[i]
        assert block.mapping[names[i]].required is False


@pytest.mark.parametrize(
    "input_arg", [
        "invalid_flag_str",
        "invalid_flag_list_1",
    ]
)
def test_invalid_flag(input_arg, request):
    arg = request.getfixturevalue(input_arg)
    with pytest.raises(ValidationError):
        FlagBlock(_data=arg)


@pytest.mark.parametrize(
    "input_arg, expected", [
        ('valid_sequence_str', 'valid_sequence_str_output'),
        ('valid_sequence_list_1', 'valid_sequence_list_1_output'),
        ('valid_sequence_dict_1', 'valid_sequence_dict_1_output'),
        ('valid_sequence_dict_2', 'valid_sequence_dict_2_output'),
        ('valid_sequence_dict_3', 'valid_sequence_dict_3_output'),
        ('valid_sequence_dict_4', 'valid_sequence_dict_4_output'),
    ]
)
def test_valid_sequence(input_arg, expected, request):
    arg = request.getfixturevalue(input_arg)
    names, defaults, optionals = request.getfixturevalue(expected)
    block = SequenceBlock(_data=arg)
    for i in range(len(names)):
        assert block.mapping[names[i]].default == defaults[i]
        assert block.mapping[names[i]].required == optionals[i]


@pytest.mark.parametrize(
    "input_arg", [
        "invalid_sequence_list_1",
        "invalid_sequence_list_2",
        "invalid_sequence_list_3",
        "invalid_sequence_list_4",
        "invalid_sequence_list_5",
        "invalid_sequence_dict_1",
        "invalid_sequence_dict_2",
        "invalid_sequence_dict_3",
        "invalid_sequence_dict_4",
        "invalid_sequence_dict_5",
        "invalid_sequence_dict_6",
        "invalid_sequence_dict_7",
        "invalid_sequence_dict_8",
        "invalid_sequence_dict_9",
    ]
)
def test_invalid_sequence(input_arg, request):
    arg = request.getfixturevalue(input_arg)
    with pytest.raises(ValidationError):
        SequenceBlock(_data=arg)
