import os
import subprocess
from typing import Any

from PyMake.console.helpers import build_target, parse_arg
from PyMake.exceptions import MissingTarget


def set_env(env_dict: dict[str, str]):
    """
    Set environment variable in the executing environment
    :param env_dict: mapping of environment name and value
    :return:
    """
    for name, value in env_dict.items():
        os.environ[name] = value


def run_cmd(cmd_list: list[str]):
    """
    Execute commands in command list
    :param cmd_list: list of commands
    :return:
    """
    for cmd in cmd_list:
        subprocess.run(cmd, shell=True, check=True)


def run_target(yaml_dict: dict[str, Any], args):
    if args.target not in yaml_dict:
        raise MissingTarget(f"target `{args.target}` is not defined in PyMake.yaml")

    # Build target and parse arguments
    builder = build_target(yaml_dict, args.target)
    parser = parse_arg(builder, args.args)

    # Set env
    set_env(parser.parsed_env)

    # Run commands:
    run_cmd(parser.parsed_commands)
