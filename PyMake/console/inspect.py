from textwrap import indent
from typing import Any

from PyMake.console import Builder, Parser
from PyMake.console.helpers import build_target, parse_arg
from PyMake.exceptions import MissingTarget


def print_var(builder: Builder, parser: Parser | None):
    print("\nVariables Inspection")
    if parser:
        print("bound values: ")
        for name, value in parser.namespace.items():
            print(indent(name + ": " + value, "  "))
    else:
        print("basic variables: ")
        print(indent(" ".join([var for var in builder.var.basic.data]), "  "))
        print("option variables: ")
        for name, value in builder.var.option.data.items():
            print(indent(name + ": " + value, "  "))
        print("sequence variables: ")
        print(indent(" ".join([var for var in builder.var.sequence.data]), "  "))
        print("positional variables: ")
        print(indent(" ".join([var for var in builder.var.positional]), "  "))
        print("required variables: ")
        print(indent(" ".join([var for var in builder.var.required]), "  "))
        print("default values: ")
        for name, value in builder.default.items():
            print(indent(name + ": " + value, "  "))


def print_env(builder: Builder, parser: Parser | None):
    print("\nEnvironment Inspection")
    if parser:
        print("bound values: ")
        for name, value in parser.parsed_env.items():
            print(indent(name + ": " + value, "  "))
    else:
        print("env variables: ")
        for name, value in builder.envs.items():
            print(indent(name + ": " + value, "  "))


def print_cmd(builder: Builder, parser: Parser | None):
    print("\nCommand Inspection")
    if parser:
        print("bound command(s): ")
        for cmd in parser.parsed_commands:
            print(indent(cmd, "  "))
    else:
        print("command(s): ")
        for cmd in builder.commands:
            print(indent(cmd, "  "))


def inspect_target(yaml_dict: dict[str, Any], args):
    if args.target not in yaml_dict:
        raise MissingTarget(f"target `{args.target}` is not defined in PyMake.yaml")
    print(f"Inspection target: {args.target}")
    print("$(var) means referencing the value of var")
    # If no specific option is provided, show everything
    if not (args.env or args.var or args.cmd):
        args.var = True
        args.env = True
        args.cmd = True

    # Build target and parse arguments
    builder = build_target(yaml_dict, args.target)
    parser = parse_arg(builder, args.args) if args.args else None

    # Print variables
    if args.var:
        print_var(builder, parser)
    if args.env:
        print_env(builder, parser)
    if args.cmd:
        print_cmd(builder, parser)
