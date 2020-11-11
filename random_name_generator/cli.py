from typing import Tuple, Union

import click

from .constants import Descent, Sex
from .errors import (
    LimitExceedError,
    UnsupportedDescentError,
    UnsupportedSexError
)
from .generators import generate


@click.command()
@click.option('-D', '--descent', type=str, default='English')
@click.option('-S', '--sex', type=str, default='unisex')
@click.option('-L', '--limit', type=int, required=True)
def generate_random_names(descent: str, sex: str, limit: int):
    try:
        descent_value = parse_descent(descent)
    except ValueError:
        click.echo(f'Invalid descent: {descent}.')
        return

    try:
        sex_value = Sex(sex.lower())
    except ValueError:
        click.echo(f'Invalid sex: {sex}.')
        return

    try:
        names = generate(descent=descent_value, sex=sex_value, limit=limit)
    except UnsupportedDescentError as e:
        click.echo(f'Unsupported descent: {descent}.')
        return
    except UnsupportedSexError:
        click.echo(f'{descent} descent does not support {sex} sex.')
        return
    except LimitExceedError as e:
        click.echo(str(e))
        return

    click.echo('\n'.join(names))


def parse_descent(descent: str) -> Union[Descent, Tuple[Descent, Descent]]:
    if '/' in descent:
        first_name_descent, last_name_descent = descent.split('/', 1)
        return (
            Descent(first_name_descent.capitalize()),
            Descent(last_name_descent.capitalize())
        )
    return Descent(descent.capitalize())
