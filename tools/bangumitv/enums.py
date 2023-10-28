from typing import Optional, Iterator, Tuple, List, Union

import requests
from hbutils.string import underscore

from .session import _get_bangumitv_session


def _get_full_dict(session: Optional[requests.Session] = None):
    session = session or _get_bangumitv_session()
    resp = session.get('https://bangumi.github.io/api/dist.json')
    resp.raise_for_status()
    return resp.json()


def _iter_all_items() -> Iterator[Tuple[str, List[Union[int, str]], List[str]]]:
    def _recursion(root):
        if isinstance(root, dict) and 'title' in root and 'enum' in root and 'x-enum-varnames' in root:
            yield root['title'], root['enum'], root['x-enum-varnames']

        if isinstance(root, dict):
            for key, value in root.items():
                yield from _recursion(value)
        elif isinstance(root, list):
            for item in root:
                yield from _recursion(item)
        else:
            pass

    yield from _recursion(_get_full_dict()['components'])


def _create_enum_source_file(source_file: str):
    need_simple_enum, need_int_enum = False, False
    enum_list = []
    for title, values, names in _iter_all_items():
        enum_names = [underscore(name).upper() for name in names]
        if all(isinstance(v, int) for v in values):
            need_int_enum = True
        else:
            need_simple_enum = True
        enum_list.append((title, values, enum_names))

    with open(source_file, 'w', encoding='utf-8') as f:
        print('from enum import unique', file=f, end='')
        if need_simple_enum:
            print(', Enum', file=f, end='')
        if need_int_enum:
            print(', IntEnum', file=f, end='')
        print('', file=f)
        print('', file=f)

        for title, values, names in enum_list:
            print('', file=f)
            print('@unique', file=f)
            if all(isinstance(v, int) for v in values):
                print(f'class {title}(IntEnum):', file=f)
            else:
                print(f'class {title}(Enum):', file=f)
            for v, n in zip(values, names):
                print(f'    {n} = {v!r}', file=f)
            print('', file=f)
