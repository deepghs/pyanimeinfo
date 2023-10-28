import re
from enum import Enum
from typing import Type, TypeVar


def _strip_name(text):
    return re.sub(r'[\W_]+', '', text).lower()


_Enum = TypeVar('_Enum', bound=Enum)


def load_from_enum(obj, enum_class: Type[_Enum]) -> _Enum:
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
    v = load_from_enum(obj, enum_class)
    return str(v.value)
