import pytest
import yaml

from PyMake.console.builder.builder import Builder
from PyMake.console.parser.parser import Parser


@pytest.fixture(scope="function")
def parser():
    definition = """
    target:
        var:
            basic:
                usr: db_app_dev
                password: Password@123456
                db: TestDB
                port: 1433
                driver: pyodbc
                provider: mssql
                host: 172.0.0.1
            option:
                all: "-a"
        env:
            engine: $(provider)+$(driver)
            url: $(usr):$(password)@$(host):$(port)/$(db)
        cmd:
           - ls $(all)
           - python script1.py --usr $(usr) --password $(password) 
           - python script2.py --host $(host) --db $(db) --port $(port)
    """
    definition = yaml.safe_load(definition)["target"]
    builder = Builder(data=definition)
    builder.build()
    parser = Parser(context=builder)
    return parser


@pytest.fixture(scope="function")
def io_set1():
    return {
        "arg": "--usr SA --password 123456 --host localhost".split(),
        "env": {
            "engine": "mssql+pyodbc",
            "url": "SA:123456@localhost:1433/TestDB",
        },
        "cmd": [
            "ls",
            "python script1.py --usr SA --password 123456",
            "python script2.py --host localhost --db TestDB --port 1433",
        ],
    }


@pytest.fixture(scope="function")
def io_set2():
    return {
        "arg": "--all".split(),
        "env": {
            "engine": "mssql+pyodbc",
            "url": "db_app_dev:Password@123456@172.0.0.1:1433/TestDB",
        },
        "cmd": [
            "ls -a",
            "python script1.py --usr db_app_dev --password Password@123456",
            "python script2.py --host 172.0.0.1 --db TestDB --port 1433",
        ],
    }


@pytest.mark.parametrize("target", ["io_set1", "io_set2"])
def test_interpolate(parser, target, request):
    target = request.getfixturevalue(target)
    parser.parse(target["arg"])
    assert parser.interp_env == target["env"]
    assert [item.command for item in parser.interp_cmd] == target["cmd"]
