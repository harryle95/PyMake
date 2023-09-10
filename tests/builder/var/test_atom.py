import pytest
from pydantic_core import ValidationError

from PyMake.builder.var.atom import BasicAtom, FlagAtom, SequenceAtom


def test_basic_required():
    atom = BasicAtom(_name="var1", _default="REQUIRED")
    assert atom.default is None
    assert atom.required is True


def test_basic_name():
    atom = BasicAtom(_name="var1", _default=10)
    assert atom.name == "var1"


def test_basic_position_assignment():
    atom = BasicAtom(_name="var1", _default=10)
    atom.position = 10
    assert atom.position == 10


def test_basic_error_access_position_before_set():
    atom = BasicAtom(_name="var1", _default=10)
    with pytest.raises(ValueError):
        print(atom.position)


def test_basic_error_invalid_set_position():
    atom = BasicAtom(_name="var1", _default=10)
    with pytest.raises(ValueError):
        atom.position = -10


def test_flag_error_no_default():
    with pytest.raises(ValidationError):
        atom = FlagAtom(_name="var1")


def test_flag_valid():
    atom = FlagAtom(_name="var1", _default="-t")
    assert atom.default == "-t"
    assert atom.required is False


def test_sequence_error_default():
    with pytest.raises(ValidationError):
        atom = SequenceAtom(_name="var1", _default="required")


def test_sequence_required():
    atom = SequenceAtom(_name="var1", _default="REQUIRED")
    assert atom.default is None
    assert atom.required is True


def test_sequence_value():
    atom = SequenceAtom(_name="var1", _default=[1, 2, 3])
    assert atom.default == [1, 2, 3]
    assert atom.required is False
