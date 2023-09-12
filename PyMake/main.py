import os
import subprocess
import sys
from pathlib import Path

import yaml

from PyMake.builder.cmd_plugin import CmdSection
from PyMake.builder.env_plugin import EnvSection
from PyMake.builder.var_plugin import VarSection


def load_PyMake_recipe() -> dict:
    file_path = Path(os.getcwd()) / "PyMake.yaml"
    if file_path.exists():
        with open(file_path, "r") as file:
            return yaml.safe_load(file)
    raise FileNotFoundError("Missing PyMake.yaml file")


def main():
    cli_input = sys.argv
    target = cli_input[1]
    args = cli_input[2:]

    # Get parser
    recipe = load_PyMake_recipe()
    if target in recipe:
        recipe = recipe[target]
    else:
        print(f"No such target: {target}")
        sys.exit(1)
    # Build parser:
    var_parser = VarSection(recipe.get("var", None)).build()
    env_parser = EnvSection(recipe.get("env", None)).build()
    cmd_parser = CmdSection(recipe.get("cmd", None)).build()

    # Build namespace:
    var_ns = var_parser.parse(args)
    env_ns = env_parser.parse(var_ns)
    cmd_parser.parse(var_ns)

    # Build environment variables:
    for key, value in env_ns.items():
        os.environ[key] = value

    # Run script:
    subprocess.run(
        cmd_parser.parsed_script,
        shell=True,
        check=True,
    )
