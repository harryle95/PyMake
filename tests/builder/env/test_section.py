import pytest
import yaml

from PyMake.builder.envs.section import EnvSection


@pytest.fixture(scope="function")
def env_valid_input1():
    definition = """
    envs:
        USERNAME: db_app_dev
        PORT: 1433
        HOST: $(hostname)
        PASSWORD: $(password)
    """
    data = yaml.safe_load(definition)["envs"]
    declared_vars = {"USERNAME": "db_app_dev", "PORT": "1433"}
    referenced_vars = {"HOST": "hostname", "PASSWORD": "password"}
    return {
        "data": data,
        "declared_vars": declared_vars,
        "referenced_vars": referenced_vars,
    }


@pytest.fixture(scope="function")
def env_valid_input2():
    definition = """
    envs:
    """
    data = yaml.safe_load(definition)["envs"]
    declared_vars = {}
    referenced_vars = {}
    return {
        "data": data,
        "declared_vars": declared_vars,
        "referenced_vars": referenced_vars,
    }


@pytest.fixture(scope="function")
def env_valid_input3():
    definition = """
    envs:
        USERNAME: $(username)
        PORT: $(port)
        HOST: $(hostname)
        PASSWORD: $(password)
    """
    data = yaml.safe_load(definition)["envs"]
    declared_vars = {}
    referenced_vars = {
        "HOST": "hostname",
        "PASSWORD": "password",
        "USERNAME": "username",
        "PORT": "port",
    }
    return {
        "data": data,
        "declared_vars": declared_vars,
        "referenced_vars": referenced_vars,
    }


@pytest.fixture(scope="function")
def env_valid_input4():
    definition = """
    envs:
        OS: Linux
        VERSION: 1.0.4
        PLATFORM: AWS
    """
    data = yaml.safe_load(definition)["envs"]
    declared_vars = {"OS": "Linux", "VERSION": "1.0.4", "PLATFORM": "AWS"}
    referenced_vars = {}
    return {
        "data": data,
        "declared_vars": declared_vars,
        "referenced_vars": referenced_vars,
    }


@pytest.fixture(scope="function")
def env_invalid_value_error1():
    definition = """
    envs:
        - USERNAME
        - PASSWORD
        - PORT
        - ID
    """
    data = yaml.safe_load(definition)["envs"]
    return {
        "data": data,
    }


@pytest.fixture(scope="function")
def env_invalid_value_error2():
    definition = """
    envs: [PORT, USERNAME]
    """
    data = yaml.safe_load(definition)["envs"]
    return {
        "data": data,
    }


@pytest.fixture(scope="function")
def env_invalid_type_error1():
    definition = """
    envs:
        OS: [A, B, C]
    """
    data = yaml.safe_load(definition)["envs"]
    return {
        "data": data,
    }


@pytest.fixture(scope="function")
def env_invalid_type_error2():
    definition = """
    envs:
        OS: 
            A: 1
            B: 2
    """
    data = yaml.safe_load(definition)["envs"]
    return {
        "data": data,
    }


@pytest.mark.parametrize(
    "valid_input",
    [
        "env_valid_input1",
        "env_valid_input2",
        "env_valid_input3",
        "env_valid_input4",
    ],
)
def test_valid_input(valid_input, request):
    valid_input = request.getfixturevalue(valid_input)
    section = EnvSection(valid_input["data"])
    assert section.declared_vars == valid_input["declared_vars"]
    assert section.referenced_vars == valid_input["referenced_vars"]


@pytest.mark.parametrize(
    "invalid_input",
    [
        "env_invalid_value_error1",
        "env_invalid_value_error2",
    ],
)
def test_value_error(invalid_input, request):
    invalid_input = request.getfixturevalue(invalid_input)
    with pytest.raises(ValueError):
        section = EnvSection(invalid_input["data"])


@pytest.mark.parametrize(
    "invalid_input",
    [
        "env_invalid_type_error1",
        "env_invalid_type_error2",
    ],
)
def test_type_error(invalid_input, request):
    invalid_input = request.getfixturevalue(invalid_input)
    with pytest.raises(TypeError):
        section = EnvSection(invalid_input["data"])
