import pytest
import yaml

from PyMake.console.builder.cmd_builder import get_shebang, parse_command, parse_string


def make_cmd(definition):
    return yaml.safe_load(definition)["cmd"]


@pytest.fixture(scope="function")
def string_cmd():
    definition = """
    cmd:
        echo Hello
    """
    return {
        "cmd": make_cmd(definition),
        "exec": None,
        "script": make_cmd(definition).strip(),
    }


@pytest.fixture(scope="function")
def script_cmd_bash():
    definition = """
    cmd: |
        #!/usr/bin/bash
        echo Hello
    """
    return {
        "cmd": make_cmd(definition),
        "exec": "/usr/bin/bash",
        "script": make_cmd(definition).strip(),
    }


@pytest.fixture(scope="function")
def script_cmd_python():
    definition = """
    cmd: |
        #!/usr/bin/python3
        print("Hello")
    """
    return {
        "cmd": make_cmd(definition),
        "exec": "/usr/bin/python3",
        "script": make_cmd(definition).strip(),
    }


@pytest.fixture(scope="function")
def dict_cmd_python():
    definition = """
    cmd: 
        python:
            - print("Hello")
            - print("World")
    """
    return {
        "cmd": make_cmd(definition),
        "exec": ["/usr/bin/python3", "/usr/bin/python3"],
        "script": ['print("Hello")', 'print("World")'],
    }


@pytest.fixture(scope="function")
def dict_cmd_python_string():
    definition = """
    cmd: 
        python:
            - print("Hello")
    """
    return {
        "cmd": make_cmd(definition),
        "exec": "/usr/bin/python3",
        "script": 'print("Hello")',
    }


@pytest.fixture(scope="function")
def dict_cmd_python_script():
    definition = """
    cmd: 
        python: |
             #!/usr/bin/python3.10
             print("Hello")
    """
    return {
        "cmd": make_cmd(definition),
        "exec": "/usr/bin/python3.10",
        "script": '#!/usr/bin/python3.10\nprint("Hello")',
    }


@pytest.fixture(scope="function")
def dict_cmd_python_shebang():
    definition = """
    cmd: 
        python:
            - |
                #!/usr/bin/python3
                print("Hello")
            - print("World")
    """
    return {
        "cmd": make_cmd(definition),
        "exec": ["/usr/bin/python3", "/usr/bin/python3"],
        "script": ['#!/usr/bin/python3\nprint("Hello")', 'print("World")'],
    }


@pytest.fixture(scope="function")
def dict_cmd_bash():
    definition = """
    cmd: 
        bash:
            - echo "Hello"
            - echo "World"
    """
    return {
        "cmd": make_cmd(definition),
        "exec": ["/usr/bin/bash", "/usr/bin/bash"],
        "script": ['echo "Hello"', 'echo "World"'],
    }


@pytest.fixture(scope="function")
def dict_cmd_python_bash():
    definition = """
    cmd:
        python:
            - print("Hello")
            - print("World") 
        bash:
            - echo "Hello"
            - echo "World"
    """
    return {
        "cmd": make_cmd(definition),
        "exec": [
            "/usr/bin/python3",
            "/usr/bin/python3",
            "/usr/bin/bash",
            "/usr/bin/bash",
        ],
        "script": ['print("Hello")', 'print("World")', 'echo "Hello"', 'echo "World"'],
    }


@pytest.fixture(scope="function")
def list_cmd_python_bash():
    definition = """
    cmd:
        - python:
            - print("Hello")
            - print("World") 
        - bash:
            - echo "Hello"
            - echo "World"
    """
    return {
        "cmd": make_cmd(definition),
        "exec": [
            "/usr/bin/python3",
            "/usr/bin/python3",
            "/usr/bin/bash",
            "/usr/bin/bash",
        ],
        "script": ['print("Hello")', 'print("World")', 'echo "Hello"', 'echo "World"'],
    }


@pytest.fixture(scope="function")
def list_cmd_str_python_bash():
    definition = """
    cmd:
        - |-
         #!/usr/bin/bash
         echo Hello
         echo World
        - |-
         echo World
         echo Hello
        - |-
         #!/usr/bin/python3
         print("Hello")
         print("World")
        - python:
            - print("Hello")
            - print("World") 
        - bash:
            - echo "Hello"
            - echo "World"
    """
    return {
        "cmd": make_cmd(definition),
        "exec": [
            "/usr/bin/bash",
            None,
            "/usr/bin/python3",
            "/usr/bin/python3",
            "/usr/bin/python3",
            "/usr/bin/bash",
            "/usr/bin/bash",
        ],
        "script": [
            make_cmd(
                """cmd: | 
                    #!/usr/bin/bash
                    echo Hello
                    echo World"""
            ).strip(),
            make_cmd(
                """cmd: | 
                    echo World
                    echo Hello"""
            ).strip(),
            make_cmd(
                """cmd: | 
                    #!/usr/bin/python3
                    print("Hello")
                    print("World")"""
            ).strip(),
            'print("Hello")',
            'print("World")',
            'echo "Hello"',
            'echo "World"',
        ],
    }


@pytest.mark.parametrize(
    "entry, executable",
    [
        ("#!/bin/bash", "/bin/bash"),
        ("#!/usr/bin/bash", "/usr/bin/bash"),
        ("#!/usr/bin/python3", "/usr/bin/python3"),
        ("#!/usr/bin/myexecutable", "/usr/bin/myexecutable"),
    ],
)
def test_get_shebang(entry, executable):
    assert get_shebang(entry) == executable


@pytest.mark.parametrize(
    "entry, exe, executable",
    [
        ("echo Hello World", None, None),
        (
            """
                                                    #!/bin/bash
                                                    echo Hello World
                                                    """,
            None,
            "/bin/bash",
        ),
        (
            """
                                                #!/usr/bin/python3
                                                print('Hello World')
                                                """,
            None,
            "/usr/bin/python3",
        ),
        (
            """
                                                #!/usr/bin/python3
                                                print('Hello World')
                                                """,
            "python",
            "/usr/bin/python3",
        ),
    ],
)
def test_parse_string(entry, exe, executable):
    assert parse_string(entry, exe).executable == executable


@pytest.mark.parametrize(
    "test_suite",
    [
        "string_cmd",
        "script_cmd_bash",
        "script_cmd_python",
        "dict_cmd_python",
        "dict_cmd_python_string",
        "dict_cmd_python_script",
        "dict_cmd_python_shebang",
        "dict_cmd_bash",
        "dict_cmd_python_bash",
        "list_cmd_str_python_bash",
    ],
)
def test_parse_command(test_suite, request):
    test_suite = request.getfixturevalue(test_suite)
    commands = parse_command(test_suite["cmd"])
    if len(commands) == 1:
        assert commands[0].command.strip() == test_suite["script"]
        assert commands[0].executable == test_suite["exec"]
    else:
        script = [item.command.strip() for item in commands]
        exec = [item.executable for item in commands]
        assert script == test_suite["script"]
        assert exec == test_suite["exec"]


def test_invalid_language():
    definition = """
    cmd:
        myRunnable:
            print Hello
    """
    command = make_cmd(definition)
    with pytest.raises(ValueError):
        parse_command(command)
