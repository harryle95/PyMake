from typing import Any

from PyMake.console import Builder, Parser


def parse_arg(builder: Builder, args: list[str]) -> Parser:
    parser = Parser(context=builder)
    parser.parse(args)
    return parser


def build_target(
    pymake_dict: dict[str, Any],
    target: str,
) -> Builder:
    try:
        recipe = pymake_dict[target]
    except KeyError:
        raise KeyError(f"Target {target} is not defined in PyMake.yaml file")
    builder = Builder(data=recipe)
    builder.build()
    return builder
