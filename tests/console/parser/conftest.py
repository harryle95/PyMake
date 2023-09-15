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


@pytest.fixture(scope="function")
def null_arg():
    return ""


@pytest.fixture(scope="function")
def one_positional():
    return "10"


@pytest.fixture(scope="function")
def two_positionals():
    return "10 Alexa"


@pytest.fixture(scope="function")
def three_positionals():
    return "10 Alexa Wikipedia"


@pytest.fixture(scope="function")
def four_positionals():
    return "10 Alexa Wikipedia localhost"


@pytest.fixture(scope="function")
def one_keyword_basic_in_order():
    return "--var1 10"


@pytest.fixture(scope="function")
def two_keywords_basic_in_order():
    return "--var1 10 --var2 Alexa"


@pytest.fixture(scope="function")
def three_keyword_basic_in_order():
    return "--var1 10 --var2 Alexa --var3 Wikipedia"


@pytest.fixture(scope="function")
def four_keyword_basic_in_order():
    return "--var1 10 --var2 Alexa --var3 Wikipedia --var4 localhost"


@pytest.fixture(scope="function")
def one_all():
    return "--all"


@pytest.fixture(scope="function")
def all_quiet():
    return "10 Alexa Wikipedia --all --quiet --list1 10 20 30 --list2 40 50 60"


@pytest.fixture(scope="function")
def quiet_all():
    return "10 Alexa Wikipedia --quiet --list1 10 20 30 --list2 40 50 60 --all"


@pytest.fixture(scope="function")
def quiet_all_var123():
    return (
        "--var1 10 --var2 Alexa --var3 Wikipedia --quiet --list1 10 20 30 --list2 "
        "40 50 60 --all"
    )


@pytest.fixture(scope="function")
def quiet_all_var132():
    return (
        "--var1 10 --var3 Wikipedia --var2 Alexa --quiet --list1 10 20 30 --list2 "
        "40 50 60 --all"
    )


@pytest.fixture(scope="function")
def quiet_all_var321():
    return (
        "--var3 Wikipedia --var2 Alexa --var1 10 --quiet --list1 10 20 30 --list2 "
        "40 50 60 --all"
    )


@pytest.fixture(scope="function")
def quiet_all_var_list1_321_list2():
    return (
        "--list1 10 20 30 --var3 Wikipedia --var2 Alexa --var1 10 --quiet --list2 "
        "40 50 60 --all"
    )


@pytest.fixture(scope="function")
def one_list1():
    return "--list1 10 20 30"


@pytest.fixture(scope="function")
def list_12():
    return "--list1 10 20 30 --list2 40 50 60"


@pytest.fixture(scope="function")
def var3_list1():
    return "--list1 10 20 30 --var3 Wikipedia"


@pytest.fixture(scope="function")
def var13_list1():
    return "--list1 10 20 30 --var1 10 --var3 Wikipedia"


@pytest.fixture(scope="function")
def var123_list1():
    return "--var2 Alexa --list1 10 20 30 --var1 10 --var3 Wikipedia"


@pytest.fixture(scope="function")
def list23():
    return "--list2 20 30 40 --list3 100 200"
