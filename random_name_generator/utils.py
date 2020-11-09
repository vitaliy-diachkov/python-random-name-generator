import random
from itertools import chain
from typing import List

from .constants import Descent, Sex, FIRST_NAMES, LAST_NAMES
from .errors import NameGenerationError


def get_first_names(
    descent: Descent = Descent.ENGLISH,
    sex: Sex = Sex.UNISEX
) -> List[str]:
    names_by_descent = FIRST_NAMES.get(descent)

    if not names_by_descent:
        raise NameGenerationError(
            f'We do not support {descent} descent at this moment'
        )

    sexes = get_sexes(sex)
    random_first_names = sorted(chain.from_iterable(
        names_by_descent.get(sex, [])
        for sex in sexes
    ))

    if not random_first_names:
        raise NameGenerationError(
            f'We can not generate {sex} {descent} names at this moment'
        )

    return random_first_names


def get_last_names(
    descent: Descent = Descent.ENGLISH,
    sex: Sex = Sex.UNISEX
) -> List[str]:
    names_by_descent = LAST_NAMES[descent]
    if isinstance(names_by_descent, list):
        return names_by_descent
    if isinstance(names_by_descent, dict):
        if sex is Sex.UNISEX:
            raise NameGenerationError(
                f'Unisex is not supported for {descent} descent. Please, '
                'specify this parameter manually.'
            )
        sexes = get_sexes(sex)
        return sorted(chain.from_iterable(
            names_by_descent.get(sex, [])
            for sex in sexes
        ))


def pick_random_name(names: List[str]) -> str:
    print('randomly picked =)')
    return random.choice(names)


def get_sexes(initial: Sex) -> List[Sex]:
    if initial in [Sex.MALE, Sex.FEMALE]:
        return [initial, Sex.UNISEX]
    if initial is Sex.UNISEX:
        return [Sex.UNISEX]
