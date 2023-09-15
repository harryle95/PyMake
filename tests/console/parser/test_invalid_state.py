import pytest
import yaml

from PyMake.console.builder.builder import Builder
from PyMake.console.parser.parser import Context
from PyMake.exceptions import InvalidParserState


@pytest.fixture(scope="function")
def null_context():
    builder = Builder(data={"cmd": "echo Hello"})
    builder.build()
    return builder


@pytest.fixture(scope="function")
def context_target12(valid_yaml_target12_1):
    yaml_dict = yaml.safe_load(valid_yaml_target12_1)["target"]
    builder = Builder(data=yaml_dict)
    builder.build()
    return builder


@pytest.mark.parametrize(
    "reference, position, use_position",
    [
        ("var1", 0, True),
        (None, None, True),
        (None, 1, True),
        (None, -1, True),
    ],
)
def test_invalid_init(null_context, reference, position, use_position):
    with pytest.raises(InvalidParserState):
        Context(
            build_context=null_context,
            reference=reference,
            position=position,
            use_position=use_position,
        )


@pytest.mark.parametrize(
    "reference, position, use_position",
    [
        ("var1", 0, True),
        (None, None, True),
        (None, 4, True),
        (None, -1, True),
    ],
)
def test_valid_target(context_target12, reference, position, use_position):
    with pytest.raises(InvalidParserState):
        Context(
            build_context=context_target12,
            reference=reference,
            position=position,
            use_position=use_position,
        )
