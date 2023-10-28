import os.path

import click
from huggingface_hub import HfFileSystem

from .responses import mock_responses_from_hf
from .responses.base import _REMOTE_REPOSITORY

GLOBAL_CONTEXT_SETTINGS = dict(
    help_option_names=['-h', '--help']
)

hf_fs = HfFileSystem()
_REPOSITORY = _REMOTE_REPOSITORY

C_RESPONSES_FILE = os.path.join(os.path.dirname(__file__), 'c_responses.py')


def list_responses():
    return [
        os.path.splitext(os.path.basename(item))[0]
        for item in hf_fs.glob(f'datasets/{_REPOSITORY}/responses/*.zip')
    ]


@click.group(context_settings={**GLOBAL_CONTEXT_SETTINGS}, help='Operate on test files')
def cli():
    pass  # pragma: no cover


@cli.command('responses', context_settings={**GLOBAL_CONTEXT_SETTINGS},
             help='Remake response files.')
def responses():
    with open(C_RESPONSES_FILE, 'w') as f:
        print(f'import pytest', file=f)
        print(f'', file=f)
        print(f'from .responses import {mock_responses_from_hf.__name__}', file=f)

        for ds_name in list_responses():
            print(f"", file=f)
            print(f"", file=f)
            print(f"@pytest.fixture()", file=f)
            print(f"def {ds_name}():", file=f)
            print(f"    with {mock_responses_from_hf.__name__}({ds_name!r}):", file=f)
            print(f"        yield", file=f)


if __name__ == '__main__':
    cli()
