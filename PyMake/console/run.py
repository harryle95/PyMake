import os
import subprocess
from typing import Any

from PyMake.console.builder.cmd_builder import Command
from PyMake.console.helpers import build_target, parse_arg
from PyMake.exceptions import InvalidExecutable, MissingTarget


def set_env(env_dict: dict[str, str]):
    """
    Set environment variable in the executing environment
    :param env_dict: mapping of environment name and value
    :return:
    """
    for name, value in env_dict.items():
        os.environ[name] = value


def run_cmd(cmd_list: list[Command]):
    """
    Execute commands
    :param cmd_list: list of commands
    :return:
    """

    for cmd in cmd_list:
        if cmd.executable is None:
            subprocess.run(cmd.command, shell=True, check=True)
        else:
            if os.path.exists(cmd.executable):
                subprocess.run([cmd.executable, "-c", cmd.command], check=True)
            else:
                raise InvalidExecutable(f"#!{cmd.executable} not found")


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
