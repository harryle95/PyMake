import pytest
import yaml

from PyMake.builder.plugin.cmd_plugin import CmdSection
from PyMake.builder.plugin.env_plugin import EnvSection
from PyMake.builder.plugin.var_plugin import VarSection
from PyMake.parser.plugin.var_plugin import VarParser


############################# PARSER 1 TEST ITEMS ######################################
@pytest.fixture(scope="function")
def var_parser1() -> VarParser:
    data = """
    basic:
        var1: 100
        var2: 100
        var3: 100
    """
    data = yaml.safe_load(data)
    section = VarSection(data)
    yield section.build()


@pytest.fixture(scope="function")
def valid_var_parser1_input1():
    return {"args": "1 2 3", "namespace": {"var1": "1", "var2": "2", "var3": "3"}}


@pytest.fixture(scope="function")
def valid_var_parser1_input2():
    return {
        "args": "1 2 --var3 3",
        "namespace": {"var1": "1", "var2": "2", "var3": "3"},
    }


@pytest.fixture(scope="function")
def valid_var_parser1_input3():
    return {
        "args": "1 --var3 3 --var2 2",
        "namespace": {"var1": "1", "var2": "2", "var3": "3"},
    }


@pytest.fixture(scope="function")
def valid_var_parser1_input4():
    return {
        "args": "--var1 1 --var2 2 --var3 3",
        "namespace": {"var1": "1", "var2": "2", "var3": "3"},
    }


@pytest.fixture(scope="function")
def valid_var_parser1_input5():
    return {
        "args": "--var1 1 --var3 3 --var2 2",
        "namespace": {"var1": "1", "var2": "2", "var3": "3"},
    }


@pytest.fixture(scope="function")
def valid_var_parser1_input6():
    return {
        "args": "--var1 1 --var2 2",
        "namespace": {"var1": "1", "var2": "2", "var3": "100"},
    }


@pytest.fixture(scope="function")
def valid_var_parser1_input7():
    return {
        "args": "--var1 1 --var3 3",
        "namespace": {"var1": "1", "var2": "100", "var3": "3"},
    }


@pytest.fixture(scope="function")
def valid_var_parser1_input8():
    return {
        "args": "--var1 1",
        "namespace": {"var1": "1", "var2": "100", "var3": "100"},
    }


@pytest.fixture(scope="function")
def valid_var_parser1_input9():
    return {
        "args": "--var3 3",
        "namespace": {"var1": "100", "var2": "100", "var3": "3"},
    }


@pytest.fixture(scope="function")
def valid_var_parser1_input10():
    return {"args": "", "namespace": {"var1": "100", "var2": "100", "var3": "100"}}


@pytest.fixture(scope="function")
def valid_var_parser1_input11():
    return {"args": "1", "namespace": {"var1": "1", "var2": "100", "var3": "100"}}


@pytest.fixture(scope="function")
def valid_var_parser1_input12():
    return {"args": "1 2", "namespace": {"var1": "1", "var2": "2", "var3": "100"}}


@pytest.fixture(scope="function")
def invalid_var_parser1_undefined_variable_1():
    return {
        "args": "--utils 1 2",
    }


@pytest.fixture(scope="function")
def invalid_var_parser1_undefined_variable_2():
    return {
        "args": "--var1 2 --var4",
    }


@pytest.fixture(scope="function")
def invalid_var_parser1_undefined_variable_3():
    return {
        "args": "--flag1",
    }


@pytest.fixture(scope="function")
def invalid_var_parser1_undefined_variable_4():
    return {
        "args": "--sequence1 1 2 3 4",
    }


@pytest.fixture(scope="function")
def invalid_var_parser1_invalid_value_1():
    return {
        "args": "--var1 2 3",
    }


@pytest.fixture(scope="function")
def invalid_var_parser1_invalid_value_2():
    return {
        "args": "1 --var2 2 3",
    }


@pytest.fixture(scope="function")
def invalid_var_parser1_variable_redefinition_1():
    return {
        "args": "1 --var1 2",
    }


@pytest.fixture(scope="function")
def invalid_var_parser1_variable_redefinition_2():
    return {
        "args": "--var1 1 --var1 2",
    }


############################# PARSER 2 TEST ITEMS ######################################
@pytest.fixture(scope="function")
def var_parser2() -> VarParser:
    data = """
    basic:
        var1: 100
        var2: REQUIRED
        var3: 100
    flag:
        flag1: "-A"
    sequence:
        seq1: [1,2,3,4,5]
    """
    data = yaml.safe_load(data)
    section = VarSection(data)
    yield section.build()


@pytest.fixture(scope="function")
def valid_var_parser2_input1():
    return {
        "args": "1 2 3",
        "namespace": {"var1": "1", "var2": "2", "var3": "3", "seq1": "1 2 3 4 5"},
    }


@pytest.fixture(scope="function")
def valid_var_parser2_input2():
    return {
        "args": "1 2 3 --flag1 --seq1 1 1 1",
        "namespace": {
            "var1": "1",
            "var2": "2",
            "var3": "3",
            "seq1": "1 1 1",
            "flag1": "-A",
        },
    }


@pytest.fixture(scope="function")
def valid_var_parser2_input3():
    return {
        "args": "1 2 --flag1 --seq1 1 1",
        "namespace": {
            "var1": "1",
            "var2": "2",
            "var3": "100",
            "seq1": "1 1",
            "flag1": "-A",
        },
    }


@pytest.fixture(scope="function")
def valid_var_parser2_input4():
    return {
        "args": "1 2 --seq1 1 1 --flag1",
        "namespace": {
            "var1": "1",
            "var2": "2",
            "var3": "100",
            "seq1": "1 1",
            "flag1": "-A",
        },
    }


@pytest.fixture(scope="function")
def valid_var_parser2_input5():
    return {
        "args": "1 2 --seq1 1 1",
        "namespace": {"var1": "1", "var2": "2", "var3": "100", "seq1": "1 1"},
    }


@pytest.fixture(scope="function")
def valid_var_parser2_input6():
    return {
        "args": "1 2 --seq1 1 1 --var3 110 --flag1",
        "namespace": {
            "var1": "1",
            "var2": "2",
            "var3": "110",
            "seq1": "1 1",
            "flag1": "-A",
        },
    }


@pytest.fixture(scope="function")
def invalid_var_parser2_missing_required_1():
    return {
        "args": "1 --seq1 1 1 --var3 110 --flag1",
    }


@pytest.fixture(scope="function")
def invalid_var_parser2_missing_required_2():
    return {
        "args": "",
    }


@pytest.fixture(scope="function")
def invalid_var_parser2_undefined_variable_1():
    return {
        "args": "--var2 100 --var4 1000",
    }


@pytest.fixture(scope="function")
def invalid_var_parser2_undefined_variable_2():
    return {
        "args": "--utils 100 --var1 1000",
    }


@pytest.fixture(scope="function")
def invalid_var_parser2_invalid_value_1():
    return {
        "args": "--var2 100 1000",
    }


@pytest.fixture(scope="function")
def invalid_var_parser2_invalid_value_2():
    return {
        "args": "--var1 1 10",
    }


@pytest.fixture(scope="function")
def invalid_var_parser2_invalid_value_3():
    return {"args": "--var1 --var2 100"}


@pytest.fixture(scope="function")
def invalid_var_parser2_invalid_value_4():
    return {"args": "--seq1 --var2 100"}


@pytest.fixture(scope="function")
def invalid_var_parser2_invalid_value_5():
    return {"args": "--var2 100 --flag1 100"}


############################# PARSER 3 TEST ITEMS ######################################
@pytest.fixture(scope="function")
def var_parser3() -> VarParser:
    data = """
    flag:
        flag1: "-A"
    sequence:
        seq1: [1,2,3,4,5]
    """
    data = yaml.safe_load(data)
    section = VarSection(data)
    yield section.build()


@pytest.fixture(scope="function")
def valid_var_parser3_input1():
    return {"args": "", "namespace": {"seq1": "1 2 3 4 5"}}


@pytest.fixture(scope="function")
def valid_var_parser3_input2():
    return {"args": "--flag1", "namespace": {"seq1": "1 2 3 4 5", "flag1": "-A"}}


@pytest.fixture(scope="function")
def valid_var_parser3_input3():
    return {
        "args": "--seq1 1 2 3 --flag1",
        "namespace": {"seq1": "1 2 3", "flag1": "-A"},
    }


@pytest.fixture(scope="function")
def valid_var_parser3_input4():
    return {
        "args": "--flag1 --seq1 1 2 3",
        "namespace": {"seq1": "1 2 3", "flag1": "-A"},
    }


############################# ENV PARSERS ##############################################
@pytest.fixture(scope="function")
def env_parser1():
    data = """
    env:
        env1: 10
        env2: 8080
        env3: $(var2)
    """
    section = EnvSection(yaml.safe_load(data)["env"])
    yield section.build()


@pytest.fixture(scope="function")
def valid_env_parser1_input1():
    var_namespace = {"var1": "10", "var2": "20", "var3": 100}
    env_namespace = {"env1": "10", "env2": "8080", "env3": "20"}
    return {"var_ns": var_namespace, "env_ns": env_namespace}


@pytest.fixture(scope="function")
def valid_env_parser1_input2():
    var_namespace = {"var2": "localhost"}
    env_namespace = {"env1": "10", "env2": "8080", "env3": "localhost"}
    return {"var_ns": var_namespace, "env_ns": env_namespace}


@pytest.fixture(scope="function")
def valid_env_parser1_input3(var_parser1):
    args = "--var2 MySQL"
    var_namespace = var_parser1.parse(args)
    env_namespace = {"env1": "10", "env2": "8080", "env3": "MySQL"}
    return {"var_ns": var_namespace, "env_ns": env_namespace}


@pytest.fixture(scope="function")
def invalid_env_parser1_input1():
    var_namespace = {}
    return {"var_ns": var_namespace}


@pytest.fixture(scope="function")
def invalid_env_parser1_input2(var_parser3):
    var_namespace = var_parser3.parse("")
    return {"var_ns": var_namespace}


############################# CMD PARSERS ##############################################
@pytest.fixture(scope="function")
def cmd_parser1():
    data = """
    cmd:
        - sqlcmd -S $(HOST),$(PORT) -U $(USER) -P $(PASSWORD) -C
        - python runserver.py --host=$(HOST) --port=$(PORT)
    """
    section = CmdSection(yaml.safe_load(data)["cmd"])
    yield section.build()


@pytest.fixture(scope="function")
def cmd_parser2():
    data = """
        cmd:
            python runserver.py
    """
    section = CmdSection(yaml.safe_load(data)["cmd"])
    yield section.build()


@pytest.fixture(scope="function")
def cmd_parser3():
    data = """
        cmd: "#bin/bash

            cd $(FOLDER_DIR)

            source $(VENV_PATH) activate

            python runserver.py --host=$(HOST) --port=$(PORT) --db=$(DB)

            python send_log.py --email=$(EMAIL_ADDR) --level=$(debug_level)
            "
    """
    section = CmdSection(yaml.safe_load(data)["cmd"])
    yield section.build()


@pytest.fixture(scope="function")
def valid_cmd_parser1_input1():
    var_namespace = {
        "HOST": "localhost",
        "USER": "SA",
        "PASSWORD": "Password@123456",
        "PORT": "8080",
        "DB": "TestDB",
        "DRIVER": "psycopg",
    }
    cmd_namespace = {
        "$(HOST)": "localhost",
        "$(USER)": "SA",
        "$(PASSWORD)": "Password@123456",
        "$(PORT)": "8080",
    }
    script = """
    sqlcmd -S localhost,8080 -U SA -P Password@123456 -C
    python runserver.py --host=localhost --port=8080
    """
    return {"var_ns": var_namespace, "cmd_ns": cmd_namespace, "script": script}


@pytest.fixture(scope="function")
def valid_cmd_parser2_input1():
    var_namespace = {
        "HOST": "localhost",
        "USER": "SA",
        "PASSWORD": "Password@123456",
        "PORT": "8080",
        "DB": "TestDB",
        "DRIVER": "psycopg",
    }
    cmd_namespace = {}
    script = """python runserver.py"""
    return {"var_ns": var_namespace, "cmd_ns": cmd_namespace, "script": script}


@pytest.fixture(scope="function")
def valid_cmd_parser2_input2(var_parser1):
    args = "--var2 MySQL"
    var_namespace = var_parser1.parse(args)
    cmd_namespace = {}
    script = """python runserver.py"""
    return {"var_ns": var_namespace, "cmd_ns": cmd_namespace, "script": script}


@pytest.fixture(scope="function")
def invalid_cmd_parser1_input2(var_parser1):
    args = "--var2 MySQL"
    var_namespace = var_parser1.parse(args)
    return {"var_ns": var_namespace}


@pytest.fixture(scope="function")
def invalid_cmd_parser3_input1(var_parser1):
    var_namespace = {
        "HOST": "localhost",
        "USER": "SA",
        "PASSWORD": "Password@123456",
        "PORT": "8080",
        "DB": "TestDB",
        "DRIVER": "psycopg",
    }
    return {"var_ns": var_namespace}


@pytest.fixture(scope="function")
def invalid_cmd_parser3_input2(var_parser1):
    args = "--var2 MySQL"
    var_namespace = var_parser1.parse(args)
    return {"var_ns": var_namespace}
