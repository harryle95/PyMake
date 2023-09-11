import pytest
import yaml


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
