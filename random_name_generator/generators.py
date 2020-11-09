import random

from .constants import Descent, Sex
from .errors import NameGenerationError
from .selectors import get_first_names, get_last_names


def generate(
    descent: Descent = Descent.ENGLISH,
    sex: Sex = Sex.UNISEX,
    *,
    limit: int
) -> list[str]:
    first_names = get_first_names(descent, sex)
    last_names = get_last_names(descent, sex)

    max_random_names = min(len(first_names), len(last_names))

    if max_random_names < limit:
        raise NameGenerationError(
            f'We can not generate {limit} {sex} {descent} '
            f'names (max. possible count: {max_random_names})'
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
    descent: Descent = Descent.ENGLISH,
    sex: Sex = Sex.UNISEX
):
    names = generate(descent, sex, limit=1)
    return names[0]
