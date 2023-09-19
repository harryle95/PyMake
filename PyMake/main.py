import argparse
import os
import sys
from pathlib import Path
from typing import Any

import yaml

from PyMake.console import list_target
from PyMake.console.inspect import inspect_target
from PyMake.console.run import run_target
from . import __version__

sys.tracebacklimit = 0


def register_command(
    subparser,
    name: str,
    help: str,
    description: str | None = None,
    epilog: str | None = None,
) -> argparse.ArgumentParser:
    # Format description
    if description is None:
        description = "description: " + help
    parser = subparser.add_parser(
        name, help=help, description=description, epilog=epilog
    )
    return parser


def read_pymake_file(path) -> dict[str, Any]:
    pymake_file = Path(path) / "PyMake.yaml"
    if not pymake_file.exists():
        raise FileNotFoundError("cannot find PyMake.yaml file in the current directory")
    with open(pymake_file, "r") as file:
        return yaml.safe_load(file)


def main(argv=None, path=None):
    if argv is None:
        argv = sys.argv[1:]
    if path is None:
        path = os.getcwd()

    main_parser = argparse.ArgumentParser(prog="pymake")
    main_parser.add_argument("--version", help="PyMake argument", action="store_true")
    subparser = main_parser.add_subparsers(dest="command")

    # Register all commands
    # List Command
    list_parser = register_command(
        subparser,
        "list",
        "list targets defined in PyMake.yaml file",
    )
    list_parser.add_argument(
        "--target",
        required=False,
        help="check whether target exists, similar usage to ls <target>",
    )

    # Run Command
    run_parser = register_command(
        subparser,
        "run",
        "run target commands with input arguments provided from command line",
        epilog="Use `pymake help` for an explanation on namespace and variables. "
        "Use `pymake inspect` to view the bound variable values",
    )
    run_parser.add_argument(
        "target",
        help="name of target defined in PyMake.yaml file",
    )

    run_parser.add_argument(
        "args",
        nargs=argparse.REMAINDER,
        help="values of variables declared in the var element under target",
    )

    # Inspect Command
    inspect_parser = register_command(
        subparser,
        "inspect",
        "inspect target's namespace with parsed values",
        epilog="Use `pymake help` for an explanation on namespace and variables. "
        "Use `pymake run <target> <args>` to run the target with the bound "
        "variables",
    )
    inspect_parser.add_argument(
        "target", help="name of target defined in PyMake.yaml file"
    )

    inspect_parser.add_argument(
        "-v",
        "--var",
        action="store_true",
        required=False,
        help="show namespace variables",
    )
    inspect_parser.add_argument(
        "-e",
        "--env",
        action="store_true",
        required=False,
        help="show environment variables",
    )
    inspect_parser.add_argument(
        "-c",
        "--cmd",
        action="store_true",
        required=False,
        help="show commands",
    )
    inspect_parser.add_argument(
        "args",
        nargs=argparse.REMAINDER,
        help="values of variables declared in the var element under target",
    )
    args = main_parser.parse_args(argv)
    # print(args)

    if args.version:
        print(__version__)
        return
    yaml_dict = read_pymake_file(path)
    # Parse commands:
    if args.command == "list":
        return list_target(yaml_dict, args)
    if args.command == "inspect":
        return inspect_target(yaml_dict, args)
    if args.command == "run":
        return run_target(yaml_dict, args)


if __name__ == "__main__":
    raise SystemExit(main())
