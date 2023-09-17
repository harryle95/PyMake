from typing import Any


def list_target(yaml_dict: dict[str, Any]):
    for key in yaml_dict:
        print(key)
