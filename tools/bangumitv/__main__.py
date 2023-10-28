import os.path

import click

from .enums import _create_enum_source_file

GLOBAL_CONTEXT_SETTINGS = dict(
    help_option_names=['-h', '--help']
)


@click.group(context_settings={**GLOBAL_CONTEXT_SETTINGS}, help='Operate with bangumi TV code')
def cli():
    pass  # pragma: no cover


_ENUM_FILE = os.path.join('pyanimeinfo', 'bangumitv', 'enums.py')


@cli.command('create', context_settings={**GLOBAL_CONTEXT_SETTINGS},
             help='Remake enum file.')
@click.option('-o', '--output_file', 'output_file', type=str, default=_ENUM_FILE,
              help='Destination for creating the enum classes for bangumi.tv.')
def create(output_file):
    _create_enum_source_file(output_file)


if __name__ == '__main__':
    cli()
