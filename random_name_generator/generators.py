import random
from typing import Union

from .constants import Descent, Sex
from .errors import NameGenerationError
from .selectors import get_first_names, get_last_names


DescentPair = tuple[Descent, Descent]


def generate(
    descent: Union[Descent, DescentPair] = Descent.ENGLISH,
    sex: Sex = Sex.UNISEX,
    *,
    limit: int,
) -> list[str]:
    if isinstance(descent, Descent):
        first_name_descent, last_name_descent = descent, descent
    if isinstance(descent, tuple):
        first_name_descent, last_name_descent = descent

    first_names = get_first_names(first_name_descent, sex)
    last_names = get_last_names(last_name_descent, sex)

    max_random_names = min(len(first_names), len(last_names))

    if max_random_names < limit:
        raise NameGenerationError(
            f'We can not generate {limit} {sex} {first_name_descent}/'
            f'{last_name_descent} names (max. possible count: '
            f'{max_random_names}).'
        )

    random.shuffle(first_names)
    random.shuffle(last_names)

    name_pairs = list(zip(first_names, last_names))[:limit]

    return [
        f'{first_name} {last_name}'
        for first_name, last_name
        in name_pairs
    ]


def generate_one(
    descent: Union[Descent, DescentPair] = Descent.ENGLISH,
    sex: Sex = Sex.UNISEX,
):
    names = generate(descent, sex, limit=1)
    return names[0]
