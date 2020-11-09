from itertools import chain
from typing import Optional

from .errors import NameGenerationError
from .constants import Descent, Sex, FIRST_NAMES, LAST_NAMES


def get_first_names(
    descent: Descent = Descent.ENGLISH,
    sex: Sex = Sex.UNISEX
) -> list[str]:
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
    sex: Optional[Sex] = None
) -> list[str]:
    last_names = LAST_NAMES.get(descent)

    if isinstance(last_names, dict):
        if sex is None:
            raise NameGenerationError(
                'You need to explicitly set sex to get list of last names for '
                f'{descent} descent'
            )

        if sex not in [Sex.MALE, Sex.FEMALE]:
            raise NameGenerationError(
                f'{sex} is not supported for {descent} descent.'
            )

        last_names = last_names.get(sex)

    if not last_names:
        raise NameGenerationError(
            f'We can not get {sex} {descent} last names.'
        )

    return last_names


def get_sexes(initial: Sex) -> list[Sex]:
    if initial in [Sex.MALE, Sex.FEMALE]:
        return [initial, Sex.UNISEX]
    if initial is Sex.UNISEX:
        return [Sex.UNISEX]
