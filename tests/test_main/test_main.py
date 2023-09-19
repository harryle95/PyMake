import os

import pytest

from PyMake.main import main


@pytest.fixture(scope="function")
def pymake_path():
    return os.getcwd()


@pytest.mark.parametrize(
    "input_str, output_str",
    [
        ("run missing_default_basic_0", "0"),
        ("run missing_default_basic_0 0", "0"),
        ("run missing_default_basic_0 1", "1"),
        ("run missing_default_basic_0 10", "10"),
        ("run missing_default_basic_0 --interactive", "-i 0"),
        ("run missing_default_basic_0 --interactive --bhp_class 0", "-i 0"),
        ("run missing_default_basic_0 --interactive --bhp_class 1", "-i 1"),
        ("run missing_default_basic_0 --interactive --bhp_class 10", "-i 10"),
    ],
)
def test_missing_default_basic_0(input_str, output_str, pymake_path, capfd):
    main(input_str.split(), pymake_path)
    out, err = capfd.readouterr()
    assert out.strip() == output_str
