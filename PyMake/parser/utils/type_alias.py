from typing import Literal, Union

OptionType = Literal["basic", "flag", "sequence"]
VariablesType = dict[str, OptionType]
PositionalType = dict[int, str]
DefaultType = dict[str, Union[int, float, str, list[int], list[float], list[str]]]

NameSpaceType = dict[str, str]
RequiredType = list[str]
