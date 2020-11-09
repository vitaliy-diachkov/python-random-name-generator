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

    if not random_first_names: raise NameGenerationError(
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
    return random.choice(names)


def generate_one(
    descent: Descent = Descent.ENGLISH,
    sex: Sex = Sex.UNISEX
) -> str:
    return generate(descent, sex, limit=1)[0]


def generate(
    descent: Descent = Descent.ENGLISH,
    sex: Sex = Sex.UNISEX,
    *,
    limit: int
) -> List[str]:

    first_names = get_first_names(descent, sex)
    last_names = get_last_names(descent, sex)

    possible_combinations = len(first_names) * len(last_names)

    if possible_combinations < limit:
        raise NameGenerationError(
            f'We can not generate more then {possible_combinations} {sex} '
            f'names for {descent} descent'
        )

    result = []

    for _ in range(limit):
        name = __generate_one(first_names, last_names)

        while name in result:
            name = __generate_one(first_names, last_names)

        result.append(name)
    return result


def __generate_one(first_names, last_names):
    first_name = pick_random_name(first_names)
    last_name = pick_random_name(last_names)
    return f'{first_name} {last_name}'


def get_sexes(initial: Sex) -> List[Sex]:
    if initial in [Sex.MALE, Sex.FEMALE]:
        return [initial, Sex.UNISEX]
    if initial is Sex.UNISEX:
        return [Sex.UNISEX]
