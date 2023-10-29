import re
from enum import Enum
from typing import Type, TypeVar


def _strip_name(text):
    """
    Strip special characters and convert text to lowercase.

    This function takes a text input, strips special characters and spaces, and converts the text to lowercase.

    :param text: The text to be processed.
    :type text: str
    :return: The processed text in lowercase without special characters.
    :rtype: str
    """
    return re.sub(r'[\W_]+', '', text).lower()


_Enum = TypeVar('_Enum', bound=Enum)


def load_from_enum(obj, enum_class: Type[_Enum]) -> _Enum:
    """
    Load an enum value from its text representation.

    This function allows you to load an enum value from either a matching enum instance, its text representation, or its integer representation.

    :param obj: The value to load from the enum.
    :type obj: Union[_Enum, str, int]
    :param enum_class: The enum class to load the value from.
    :type enum_class: Type[_Enum]
    :return: The enum value corresponding to the input.
    :rtype: _Enum
    :raises ValueError: If the input value does not match any enum values.
    :raises TypeError: If the input value is of an unknown type.
    """
    if isinstance(obj, enum_class):
        return obj
    elif isinstance(obj, (str, int)):
        for name, item in enum_class.__members__.items():
            if item.value == obj or (isinstance(obj, str) and _strip_name(obj) == _strip_name(item.name)):
                return item

        raise ValueError(f'Unknown value of {obj!r} from {enum_class!r}.')
    else:
        raise TypeError(f'Unknown enum value - {obj!r}.')


def load_text_from_enum(obj, enum_class: Type[_Enum]) -> str:
    """
    Load the text representation of an enum value.

    This function allows you to load the text representation of an enum value from its corresponding enum instance, text representation, or integer representation.

    :param obj: The value to load from the enum.
    :type obj: Union[_Enum, str, int]
    :param enum_class: The enum class to load the text from.
    :type enum_class: Type[_Enum]
    :return: The text representation of the enum value.
    :rtype: str
    :raises ValueError: If the input value does not match any enum values.
    :raises TypeError: If the input value is of an unknown type.
    """
    v = load_from_enum(obj, enum_class)
    return str(v.value)
