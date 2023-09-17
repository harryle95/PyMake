from typing import Any

from PyMake.exceptions import MissingTarget


def list_target(yaml_dict: dict[str, Any], args):
    if args.target:
        if args.target in yaml_dict:
            print(args.target)
        else:
            raise MissingTarget(
                f"target `({args.target})` does not exist in PyMake.yaml"
            )
    else:
        for key in yaml_dict:
            print(key)
