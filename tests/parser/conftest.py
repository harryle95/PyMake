import pytest

from PyMake.parser.parser import VarParser


@pytest.fixture(scope="function")
def parser_1() -> VarParser:
    return VarParser(
        variables={
            "var1": "basic",
            "var2": "basic",
            "var3": "basic",
        },
        positional={0: "var1", 1: "var2", 2: "var3"},
        default={"var1": 10, "var2": 20, "var3": 20},
        required=[]
    )


@pytest.fixture(scope="function")
def input_1():
    return "--var1 100 --var2 100 --var3 100"


@pytest.fixture(scope="function")
def input_2():
    return "100 200 300"


@pytest.fixture(scope="function")
def input_3():
    return "100 --var2 0.5 --var3 300"


@pytest.fixture(scope="function")
def input_4():
    return "100 --var3 0.5 --var2 300"

@pytest.fixture(scope="function")
def input_5():
    return "100 ABC --var3 300"


@pytest.fixture(scope="function")
def parser1_input1_output():
    return {"var1": '100', "var2": '100', "var3": '100'}


@pytest.fixture(scope="function")
def parser1_input2_output():
    return {"var1": '100', "var2": '200', "var3": '300'}


@pytest.fixture(scope="function")
def parser1_input3_output():
    return {"var1": '100', "var2": '0.5', "var3": '300'}


@pytest.fixture(scope="function")
def parser1_input4_output():
    return {"var1": '100', "var2": '300', "var3": '0.5'}

@pytest.fixture(scope="function")
def parser1_input5_output():
    return {"var1": '100', "var2": 'ABC', "var3": '300'}
