import pytest
import yaml

from PyMake.builder.cmd.section import CmdSection


@pytest.fixture(scope="function")
def cmd_valid_input1():
    definition = """
    cmd:
        - sqlcmd -S $(HOST),$(PORT) -U $(USER) -P $(PASSWORD) -C
        - python runserver.py --host=$(HOST) --port=$(PORT)
    """
    data = yaml.safe_load(definition)["cmd"]
    referenced_vars = {
        "$(HOST)": "HOST",
        "$(PASSWORD)": "PASSWORD",
        "$(USER)": "USER",
        "$(PORT)": "PORT",
    }
    script = """
    sqlcmd -S $(HOST),$(PORT) -U $(USER) -P $(PASSWORD) -C
    python runserver.py --host=$(HOST) --port=$(PORT)"""
    return {"data": data, "referenced_vars": referenced_vars, "script": script}


@pytest.fixture(scope="function")
def cmd_valid_input2():
    definition = """
        cmd:
            python runserver.py
    """
    data = yaml.safe_load(definition)["cmd"]
    referenced_vars = {}
    script = "python runserver.py"
    return {"data": data, "referenced_vars": referenced_vars, "script": script}


@pytest.fixture(scope="function")
def cmd_valid_input3():
    definition = """
        cmd: "#bin/bash

            cd $(FOLDER_DIR)

            source $(VENV_PATH) activate

            python runserver.py --host=$(HOST) --port=$(PORT) --db=$(DB)

            python send_log.py --email=$(EMAIL_ADDR) --level=$(debug_level)
            "
    """
    data = yaml.safe_load(definition)["cmd"]
    referenced_vars = [
        "FOLDER_DIR",
        "VENV_PATH",
        "HOST",
        "PORT",
        "DB",
        "EMAIL_ADDR",
        "debug_level",
    ]
    script = """#bin/bash
            cd $(FOLDER_DIR)
            source $(VENV_PATH) activate
            python runserver.py --host=$(HOST) --port=$(PORT) --db=$(DB)
            python send_log.py --email=$(EMAIL_ADDR) --level=$(debug_level)
            """
    return {
        "data": data,
        "referenced_vars": {f"$({item})": item for item in referenced_vars},
        "script": script,
    }


@pytest.fixture(scope="function")
def cmd_invalid_input1():
    definition = """
    cmd:
    """
    data = yaml.safe_load(definition)["cmd"]

    return {"data": data}


@pytest.fixture(scope="function")
def cmd_invalid_input2():
    definition = """
    cmd: 1
    """
    data = yaml.safe_load(definition)["cmd"]
    return {"data": data}


@pytest.fixture(scope="function")
def cmd_invalid_input3():
    definition = """
    cmd:
        1: cd $HOME
        2: echo "Hello World from HOME"
    """
    data = yaml.safe_load(definition)["cmd"]
    return {"data": data}


@pytest.mark.parametrize(
    "valid_input",
    [
        "cmd_valid_input1",
        "cmd_valid_input2",
        "cmd_valid_input3",
    ],
)
def test_valid_input(valid_input, request):
    valid_input = request.getfixturevalue(valid_input)
    section = CmdSection(valid_input["data"])
    assert section.referenced_vars == valid_input["referenced_vars"]
    section_script = [
        item.strip() for item in section.script.split("\n") if item.strip() != ""
    ]
    expected_script = [
        item.strip() for item in valid_input["script"].split("\n") if item.strip() != ""
    ]
    assert section_script == expected_script


@pytest.mark.parametrize(
    "invalid_input",
    [
        "cmd_invalid_input1",
        "cmd_invalid_input2",
        "cmd_invalid_input3",
    ],
)
def test_value_error(invalid_input, request):
    invalid_input = request.getfixturevalue(invalid_input)
    with pytest.raises(ValueError):
        CmdSection(invalid_input["data"])
