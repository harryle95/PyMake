import pytest
import yaml

from PyMake.console.builder.builder import Builder
from PyMake.console.parser.parser import Parser


def get_parser(definition: str):
    data = yaml.safe_load(definition)
    context = Builder(data=data)
    yield Parser(context=context)


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
def five_positionals():
    return "10 Alexa Wikipedia localhost MoonLight"


@pytest.fixture(scope="function")
def six_positionals():
    return "10 Alexa Wikipedia localhost 3.14"


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
def five_keyword_basic_in_order():
    return "--var1 10 --var2 Alexa --var3 Wikipedia --var4 localhost --var5 MoonLight"


@pytest.fixture(scope="function")
def two_keyword_basic_out_of_order_var1_var2():
    return "--var2 Alexa --var1 10"


@pytest.fixture(scope="function")
def three_keyword_basic_out_of_order_var1_var2_var3():
    return "--var3 Wikipedia --var1 10 --var2 Alexa"


@pytest.fixture(scope="function")
def four_keyword_basic_out_of_order_4321():
    return "--var4 localhost --var3 Wikipedia --var2 Alexa --var1 10"


@pytest.fixture(scope="function")
def four_keyword_basic_out_of_order_4123():
    return "--var4 localhost --var1 10 --var2 Alexa --var3 Wikipedia"


@pytest.fixture(scope="function")
def four_keyword_basic_out_of_order_2341():
    return "--var2 Alexa --var3 Wikipedia --var4 localhost --var1 10 "


@pytest.fixture(scope="function")
def one_positional_all_option():
    return "10 --all"


@pytest.fixture(scope="function")
def two_positional_all_option():
    return "10 Alexa --all"


@pytest.fixture(scope="function")
def three_positional_all_option():
    return "10 Alexa Wikipedia --all"


@pytest.fixture(scope="function")
def four_positional_all_option():
    return "10 Alexa Wikipedia localhost --all"


@pytest.fixture(scope="function")
def four_positional_one_keyword_all_option():
    return "10 Alexa Wikipedia --var4 localhost --all"


@pytest.fixture(scope="function")
def four_positional_two_keyword_all_option_34():
    return "10 Alexa --var3 Wikipedia --var4 localhost --all"


@pytest.fixture(scope="function")
def four_positional_two_keyword_all_option_43():
    return "10 Alexa --var4 localhost --var3 Wikipedia --all"


@pytest.fixture(scope="function")
def four_positional_three_keyword_all_option_243():
    return "10 --var2 Alexa --var4 localhost --var3 Wikipedia --all"


@pytest.fixture(scope="function")
def one_positional_all_quiet_option():
    return "10 --all --quiet"


@pytest.fixture(scope="function")
def two_positional_all_quiet_option():
    return "10 Alexa --all --quiet"


@pytest.fixture(scope="function")
def three_positional_all_quiet_option():
    return "10 Alexa Wikipedia --all --quiet"


@pytest.fixture(scope="function")
def four_positional_all_quiet_option():
    return "10 Alexa Wikipedia localhost --all --quiet"


@pytest.fixture(scope="function")
def four_positional_one_keyword_all_quiet_option():
    return "10 Alexa Wikipedia --var4 localhost --all --quiet"


@pytest.fixture(scope="function")
def four_positional_two_keyword_all_op_quiet_option():
    return "10 Alexa --var3 Wikipedia --var4 localhost --all --quiet"


@pytest.fixture(scope="function")
def four_positional_two_keyword_all_quiet_option():
    return "10 Alexa --var4 localhost --var3 Wikipedia --all --quiet"


@pytest.fixture(scope="function")
def four_positional_three_keyword_all_quiet_option():
    return "10 --var2 Alexa --var4 localhost --var3 Wikipedia --all --quiet"


@pytest.fixture(scope="function")
def one_positional_list1():
    return "10 --list1 100 200 300"


@pytest.fixture(scope="function")
def two_positional_list1():
    return "10 Alexa --list1 100 200 300"


@pytest.fixture(scope="function")
def three_positional_list1():
    return "10 Alexa Wikipedia --list1 100 200 300"


@pytest.fixture(scope="function")
def four_positional_list1():
    return "10 Alexa Wikipedia localhost --list1 100 200 300"


@pytest.fixture(scope="function")
def one_positional_list1_quiet():
    return "10 --list1 100 200 300 --quiet"


@pytest.fixture(scope="function")
def two_positional_list1_quiet():
    return "10 Alexa --list1 100 200 300 --quiet"


@pytest.fixture(scope="function")
def three_positional_list1_quiet():
    return "10 Alexa Wikipedia --list1 100 200 300 --quiet"


@pytest.fixture(scope="function")
def four_positional_list1_quiet():
    return "10 Alexa Wikipedia localhost --list1 100 200 300 --quiet"


@pytest.fixture(scope="function")
def one_positional_list1_all():
    return "10 --list1 100 200 300 --all"


@pytest.fixture(scope="function")
def two_positional_list1_all():
    return "10 Alexa --list1 100 200 300 --all"


@pytest.fixture(scope="function")
def three_positional_list1_all():
    return "10 Alexa Wikipedia --list1 100 200 300 --all"


@pytest.fixture(scope="function")
def four_positional_list1_all():
    return "10 Alexa Wikipedia localhost --list1 100 200 300 --all"


@pytest.fixture(scope="function")
def one_positional_all_list1():
    return "10 --all --list1 100 200 300"


@pytest.fixture(scope="function")
def two_positional_all_list1():
    return "10 Alexa --all --list1 100 200 300"


@pytest.fixture(scope="function")
def three_positional_all_list1():
    return "10 Alexa Wikipedia --all --list1 100 200 300"


@pytest.fixture(scope="function")
def four_positional_all_list1():
    return "10 Alexa Wikipedia localhost --all --list1 100 200 300"


@pytest.fixture(scope="function")
def one_positional_list1_list2():
    return "10 --list1 100 200 300 --list2 400 500 600"


@pytest.fixture(scope="function")
def two_positional_list1_list2():
    return "10 Alexa --list1 100 200 300 --list2 400 500 600"


@pytest.fixture(scope="function")
def three_positional_list1_list2():
    return "10 Alexa Wikipedia --list1 100 200 300 --list2 400 500 600"


@pytest.fixture(scope="function")
def four_positional_list1_list2():
    return "10 Alexa Wikipedia localhost --list1 100 200 300 --list2 400 500 600"


@pytest.fixture(scope="function")
def one_positional_list1_quiet_list2():
    return "10 --list1 100 200 300 --quiet --list2 400 500 600"


@pytest.fixture(scope="function")
def two_positional_list1_quiet_list2():
    return "10 Alexa --list1 100 200 300 --quiet --list2 400 500 600"


@pytest.fixture(scope="function")
def three_positional_list1_quiet_list2():
    return "10 Alexa Wikipedia --list1 100 200 300 --quiet --list2 400 500 600"


@pytest.fixture(scope="function")
def four_positional_list1_quiet_list2():
    return (
        "10 Alexa Wikipedia localhost --list1 100 200 300 --quiet --list2 400 500 600"
    )


@pytest.fixture(scope="function")
def one_positional_list1_all_list2():
    return "10 --list1 100 200 300 --all --list2 400 500 600"


@pytest.fixture(scope="function")
def two_positional_list1_all_list2():
    return "10 Alexa --list1 100 200 300 --all --list2 400 500 600"


@pytest.fixture(scope="function")
def three_positional_list1_all_list2():
    return "10 Alexa Wikipedia --list1 100 200 300 --all --list2 400 500 600"


@pytest.fixture(scope="function")
def four_positional_list1_all_list2():
    return "10 Alexa Wikipedia localhost --list1 100 200 300 --all --list2 400 500 600"


@pytest.fixture(scope="function")
def one_positional_all_list1_list2():
    return "10 --all --list1 100 200 300 --list2 400 500 600"


@pytest.fixture(scope="function")
def two_positional_all_list1_list2():
    return "10 Alexa --all --list1 100 200 300 --list2 400 500 600"


@pytest.fixture(scope="function")
def three_positional_all_list1_list2():
    return "10 Alexa Wikipedia --all --list1 100 200 300 --list2 400 500 600"


@pytest.fixture(scope="function")
def four_positional_all_list1_list2():
    return "10 Alexa Wikipedia localhost --all --list1 100 200 300 --list2 400 500 600"
