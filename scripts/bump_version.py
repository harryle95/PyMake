import argparse
import sys
from pathlib import Path

import toml

sys.tracebacklimit = 1


def main():
    parser = argparse.ArgumentParser(
        "Version Sync Tool",
        description="Plugin to sync pyproject.toml version with package __version__ "
        "number. "
        "The pyproject.toml file must contain version number under "
        "tool.poetry "
        "tag. "
        "The package directory must contain a __version__.py file "
        "containing "
        "version number",
    )
    parser.add_argument(
        "--pyproject_path", help="Directory containing the pyproject.toml file"
    )
    parser.add_argument(
        "--package_path", help="Directory containing the __version__.py file"
    )
    args = parser.parse_args()
    pyproject_file = Path(args.pyproject_path) / "pyproject.toml"
    if not pyproject_file.exists():
        raise FileNotFoundError(
            "pyproject.toml file not found in the current directory"
        )

    version_file = Path(args.package_path) / "__version__.py"
    if not version_file.exists():
        raise FileNotFoundError("__version__.py not found in the current directory")

    # Read toml file
    with open(pyproject_file, "r") as file:
        data = toml.load(file)
    try:
        version = data["tool"]["poetry"]["version"]
    except KeyError:
        raise ValueError(
            "version is not defined under tool.poetry tag of pyproject.toml"
        )

    # Write version:
    with open(version_file, "w") as file:
        file.write(f'__version__= "{version}"')
    print(f"Update package version to {version} sucessfully")


if __name__ == "__main__":
    raise SystemExit(main())
